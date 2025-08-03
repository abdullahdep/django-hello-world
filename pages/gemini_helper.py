import requests
import json
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

GEMINI_API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def init_gemini():
    """Initialize by validating API key"""
    if not hasattr(settings, 'GEMINI_API_KEY') or not settings.GEMINI_API_KEY:
        logger.error("GEMINI_API_KEY not found in settings")
        raise ValueError("GEMINI_API_KEY is not configured")
    return settings.GEMINI_API_KEY

def check_answer(api_key, question, correct_answer, student_answer, total_marks):
    """Check student answer using Gemini 2.0 Flash API"""
    # Handle empty or None answers immediately
    if not student_answer or student_answer.strip() == "":
        return json.dumps({
            'score': 0,
            'feedback': 'No answer provided. Please provide an answer to receive marks.',
            'key_points': ['Answer is required'],
            'total_marks': total_marks
        })

    try:
        headers = {
            'Content-Type': 'application/json',
            'X-goog-api-key': api_key
        }

        # Format prompt to get only numerical score
        prompt = f"""Compare answer, respond with ONLY a number between 0 and {total_marks}:
Q:{question}
Correct:{correct_answer}
Student:{student_answer}"""

        payload = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }],
            "generationConfig": {
                "temperature": 0.1,
                "topP": 0.95,
                "topK": 1,
                "maxOutputTokens": 8
            }
        }

        # Make API request with timeout
        response = requests.post(
            GEMINI_API_ENDPOINT,
            headers=headers,
            json=payload,
            timeout=15
        )
        
        if response.status_code == 200:
            data = response.json()
            if 'candidates' in data and data['candidates']:
                text = data['candidates'][0]['content']['parts'][0]['text'].strip()
                logger.debug(f"Raw AI response: {text}")
                
                # Extract score from response
                try:
                    # Remove any non-numeric characters except decimal point
                    score_text = ''.join(c for c in text if c.isdigit() or c == '.')
                    score = float(score_text) if score_text else 0
                    # Ensure score is between 0 and total_marks
                    score = min(max(0, score), total_marks)
                    
                    # Generate appropriate feedback based on score percentage
                    percentage = (score / total_marks) * 100
                    if percentage >= 80:
                        feedback = "Excellent answer! Demonstrates thorough understanding."
                        key_points = ["Complete and accurate", "Well explained"]
                    elif percentage >= 60:
                        feedback = "Good answer, but room for improvement."
                        key_points = ["Generally correct", "Could be more detailed"]
                    elif percentage >= 40:
                        feedback = "Fair attempt, but needs significant improvement."
                        key_points = ["Partially correct", "Missing key details"]
                    else:
                        feedback = "Answer needs substantial improvement."
                        key_points = ["Incomplete", "Major concepts missing"]
                    
                    result = {
                        'score': score,
                        'feedback': feedback,
                        'key_points': key_points,
                        'total_marks': total_marks
                    }
                    return json.dumps(result)
                except (ValueError, TypeError) as e:
                    logger.error(f"Error extracting score: {str(e)}")
                    raise ValueError(f"Failed to extract score from AI response: {str(e)}")
        else:
            error_msg = f"API request failed with status {response.status_code}"
            if response.text:
                try:
                    error_details = response.json()
                    error_msg += f": {json.dumps(error_details)}"
                except json.JSONDecodeError:
                    error_msg += f": {response.text}"
            logger.error(error_msg)
            raise ValueError(error_msg)
    except requests.RequestException as e:
        error_msg = f"Network error occurred: {str(e)}"
        logger.error(error_msg)
        raise ValueError(error_msg)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")

    # Return error response if any step fails
    return json.dumps({
        'score': 0,
        'feedback': 'System Error: Failed to evaluate answer. Please try again.',
        'key_points': ['Evaluation system temporarily unavailable'],
        'total_marks': total_marks
    })