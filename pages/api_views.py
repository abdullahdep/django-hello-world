from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
import json
import logging
from .models import ShortQuestion, Subject, Chapter, TestResult
from .gemini_helper import init_gemini, check_answer
from django.contrib.auth.decorators import login_required

@csrf_protect
@require_POST
def check_answer_view(request):
    try:
        # Parse request data
        try:
            data = json.loads(request.body)
            question_id = data.get('question_id')
            student_answer = data.get('answer', '').strip()
            
            if not question_id:
                return JsonResponse({
                    'error': 'Question ID is required'
                }, status=400)
            
            # Get question and check answer
            question = ShortQuestion.objects.get(id=question_id)
            api_key = init_gemini()
            result = check_answer(api_key, question.question_text, question.answer, student_answer, question.marks or 2)
            
            return JsonResponse(json.loads(result))
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except ShortQuestion.DoesNotExist:
            return JsonResponse({'error': 'Question not found'}, status=404)
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
@csrf_protect
@require_POST
def save_test_results(request):
    try:
        data = json.loads(request.body)
        logger = logging.getLogger(__name__)
        logger.info(f"Received test results data: {data}")
        
        # Validate required fields
        required_fields = ['subject_id', 'chapter_id', 'total_marks', 'marks_obtained', 'percentage']
        for field in required_fields:
            if field not in data:
                logger.error(f"Missing required field: {field}")
                return JsonResponse({'error': f'{field} is required'}, status=400)
        
        # Get subject and chapter
        try:
            subject = Subject.objects.get(id=data['subject_id'])
            chapter = Chapter.objects.get(id=data['chapter_id'])
        except (Subject.DoesNotExist, Chapter.DoesNotExist) as e:
            logger.error(f"Subject or Chapter not found: {str(e)}")
            return JsonResponse({'error': 'Subject or Chapter not found'}, status=404)
        
        # Convert percentage to float, removing any % sign
        try:
            percentage_str = str(data['percentage']).strip().rstrip('%')
            percentage = float(percentage_str)
        except (ValueError, TypeError) as e:
            logger.error(f"Invalid percentage value '{data['percentage']}': {str(e)}")
            return JsonResponse({'error': f"Invalid percentage value: {str(e)}"}, status=400)

        # Convert marks to float
        try:
            total_marks = float(data['total_marks'])
            marks_obtained = float(data['marks_obtained'])
        except (ValueError, TypeError) as e:
            logger.error(f"Invalid marks value: {str(e)}")
            return JsonResponse({'error': f"Invalid marks value: {str(e)}"}, status=400)
            
        # Create test result
        test_result = TestResult.objects.create(
            user=request.user,
            subject=subject,
            chapter=chapter,
            total_marks=total_marks,
            marks_obtained=marks_obtained,
            percentage=percentage,
            is_completed=data.get('is_completed', True)
        )
        logger.info(f"Successfully created test result with ID: {test_result.id}")
        
        return JsonResponse({'success': True, 'test_result_id': test_result.id})
        
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON data: {str(e)}")
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        logger.error(f"Unexpected error saving test results: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)
