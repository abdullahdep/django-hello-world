from django.shortcuts import render

def global_variables(request):
    return {
        # Site Info
        'site_name': 'Safar Academy',
        'site_description': 'This is a site dedicated to educational resources.',
        'site_keywords': 'education, academy, learning, subjects, courses',
        'site_author': 'John Doe',
        'site_url': 'https://www.safaracademy.com',
        'site_email': 'contact@safaracademy.com',
        'site_phone': '+1 234 567 890',
        'site_address': '123 Main St, Anytown, USA',
        
        # Social Links
        'site_facebook': 'https://www.facebook.com/safaracademy',
        'site_twitter': 'https://www.twitter.com/safaracademy',
        'site_instagram': 'https://www.instagram.com/safaracademy',
        'site_linkedin': 'https://www.linkedin.com/company/safaracademy',
        'site_youtube': 'https://www.youtube.com/c/safaracademy',
        'site_pinterest': 'https://www.pinterest.com/safaracademy',
        'site_tiktok': 'https://www.tiktok.com/@safaracademy',
        'site_snapchat': 'https://www.snapchat.com/add/safaracademy',
        'site_whatsapp': 'https://wa.me/1234567890',
        'site_telegram': 'https://t.me/safaracademy',
        'site_discord': 'https://discord.gg/safaracademy',
        'site_reddit': 'https://www.reddit.com/r/safaracademy',
        'site_quora': 'https://www.quora.com/profile/safaracademy',
        'site_github': 'https://github.com/safaracademy',
        
        # Logo
        'logo': 'https://www.safaracademy.com/static/logo.png',

        # Subjects Data (Now a dictionary of subjects with descriptions and links)
        'subjects': {
            'English': {
                'description': 'Learn the fundamentals of English language and literature.',
                'anchor': 'login'
            },
            'Mathematics': {
                'description': 'Study algebra, calculus, and more to excel in Mathematics.',
                'anchor': 'https://www.safaracademy.com/subjects/mathematics'
            },
            'Physics': {
                'description': 'Explore the world of Physics, from mechanics to thermodynamics.',
                'anchor': 'https://www.safaracademy.com/subjects/physics'
            },
            'Chemistry': {
                'description': 'Understand the basics of Chemistry, reactions, and lab techniques.',
                'anchor': 'https://www.safaracademy.com/subjects/chemistry'
            },
            'Biology': {
                'description': 'Dive into the world of life sciences, anatomy, and ecology.',
                'anchor': 'https://www.safaracademy.com/subjects/biology'
            },
            'History': {
                'description': 'Explore the events that shaped the world throughout history.',
                'anchor': 'https://www.safaracademy.com/subjects/history'
            },
            'Geography': {
                'description': 'Learn about the world’s geography, maps, and earth sciences.',
                'anchor': 'https://www.safaracademy.com/subjects/geography'
            },
            'Computer Science': {
                'description': 'Master programming, algorithms, and everything related to computers.',
                'anchor': 'https://www.safaracademy.com/subjects/computer-science'
            },
        },
    }
