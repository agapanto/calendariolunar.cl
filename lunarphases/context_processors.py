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
