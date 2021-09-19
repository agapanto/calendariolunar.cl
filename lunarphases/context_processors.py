from django.urls import resolve


def social_networks(request):
    social_networks = {
        'facebook': {
            'url': 'https://www.facebook.com/calendariolunarchile'
        },
        'instagram': {
            'url': 'https://www.instagram.com/calendario_lunar_chile/'
        },
        'github': {
            'url': 'https://github.com/mcueto/calendariolunar.cl'
        },
    }
    return {
        'SOCIAL_NETWORKS': social_networks
    }


def current_url_name(request):
    current_url_name = ''
    
    try:
        current_url_name = resolve(request.path_info).url_name
    except:
        pass

    return {
        'CURRENT_URL_NAME': current_url_name
    }
