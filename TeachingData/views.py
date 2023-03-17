from django.shortcuts import render

# Create your views here.


def catalog(request):
    return render(request, 'TeachingDataCatalog.html')
    # return render(request, 'component/back.html')
