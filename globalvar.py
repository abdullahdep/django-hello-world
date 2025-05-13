from django.shortcuts import render

def global_variables(request):
    return {
        'site_name': 'Safar Academy',
        'site_description': 'This is my site',
        'site_keywords': 'site, my site, example',
        'site_author': 'John Doe',
        'site_url': 'https://www.example.com',
        'site_email': '',
        'site_phone': '+1 234 567 890',
        'site_address': '123 Main St, Anytown, USA',
        'site_facebook': 'https://www.facebook.com/example',
        'site_twitter': 'https://www.twitter.com/example',
        'site_instagram': 'https://www.instagram.com/example',
        'site_linkedin': 'https://www.linkedin.com/in/example',
        'site_youtube': 'https://www.youtube.com/example',
        'site_pinterest': 'https://www.pinterest.com/example',
        'site_tiktok': 'https://www.tiktok.com/@example',
        'site_snapchat': 'https://www.snapchat.com/add/example',
        'site_whatsapp': 'https://wa.me/1234567890',
        'site_telegram': 'https://t.me/example',
        'site_discord': 'https://discord.gg/example',
        'site_reddit': 'https://www.reddit.com/user/example',
        'site_quora': 'https://www.quora.com/profile/example',
        'site_github':  '',
        
        'logo': 'https://example.com/logo.png',
    }