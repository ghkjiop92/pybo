from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

import os

#def download_csv(request):
    # Update the path to reflect the correct directory structure
    #file_path = os.path.join('C:\\projects', 'inventory.csv')

    #with open(file_path, 'rb') as file:
        #response = HttpResponse(file.read(), content_type='text/csv')
        #response['Content-Disposition'] = 'attachment; filename="inventory.csv"'
        #return response
    
def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")




