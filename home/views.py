from django.shortcuts import render


def home(request):
    packages = [
	{'name':'haikunator', 'url': 'https://pypi.org/project/haikunator/2.1.0/'},
	{'name':'black', 'url': 'https://pypi.org/project/black/22.1.0/'},
	{'name':'django-allauth', 'url': 'https://pypi.org/project/django-allauth/0.38.0/'},
	{'name':'django-bootstrap4', 'url': 'https://pypi.org/project/django-bootstrap4/0.0.7/'},
	{'name':'djangorestframework', 'url': 'https://pypi.org/project/djangorestframework/3.9.0/'},
    ]
    context = {
        'packages': packages
    }
    return render(request, 'home/index.html', context)
