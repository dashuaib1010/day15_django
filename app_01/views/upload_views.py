import os

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from day_15 import settings

from django.views.decorators.csrf import csrf_exempt

from app_01.utils.forms import UploadForm, UploadModelForm
from app_01.models import Boss


@csrf_exempt
def upload(request):
    if request.method == 'GET':
        content = {
            'form_title': '头像上传',
            'form': UploadForm(),
        }

        return render(request, 'upload.html', content)




    form = UploadForm(data=request.POST,files=request.FILES)


    if form.is_valid():
        print(form.cleaned_data)

        name = form.cleaned_data.get('name')
        age = form.cleaned_data.get('age')

        img = form.cleaned_data.get('img')

        # media_path = os.path.join(settings.MEDIA_ROOT,img.name)
        media_path = os.path.join('media',img.name)

        with open(media_path,'wb') as file:
            for chunk in img.chunks():
                file.write(chunk)

        Boss.objects.create(name=name,age=age,img=media_path)
        return HttpResponse('uploaded')

    content = {
        'form_title': '头像上传',
        'form': form,
    }


    return render(request, 'upload.html', content)



@csrf_exempt
def upload_modelform(request):
    if request.method == 'GET':
        content = {
            'form_title': '城市logo上传',
            'form': UploadModelForm(),
        }

        return render(request, 'upload.html', content)




    form = UploadModelForm(data=request.POST,files=request.FILES)


    if form.is_valid():
        form.save()
        return HttpResponse('uploaded')

    content = {
        'form_title': '城市logo上传',
        'form': form,
    }


    return render(request, 'upload.html', content)




