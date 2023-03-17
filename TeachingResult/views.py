from django.shortcuts import render

# Create your views here.


def analyse(request):
    message = {"key1": {
        "key2": "value"
    }}
    return render(request, 'TeachingResult.html', message)
