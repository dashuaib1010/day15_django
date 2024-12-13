from django.shortcuts import render, redirect
from app_01.models import UserInfo
from app_01.utils.forms import UserInfoForm

from app_01.utils.pagination import Pagination

def user_add(request):
    if request.method == "GET":
        content = {
            "form":UserInfoForm(),
        }
        return render(request, 'user_add.html', content)

    form = UserInfoForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/user/list')


    print(form.errors)
    return render(request, 'user_add.html', {'form': form})

def user_delete(request,id):
    UserInfo.objects.filter(id=id).first().delete()
    return redirect('/user/list/')

def user_edit(request, id):
    user_obj = UserInfo.objects.filter(id=id).first()

    if request.method == "GET":
        content = {
            "form":UserInfoForm(instance=user_obj),
        }
        return render(request, 'user_edit.html', content)

    form = UserInfoForm(request.POST, instance=user_obj)
    if form.is_valid():
        form.save()
        return redirect('/user/list')

    print(form.errors)
    return render(request,'user_edit.html',{"form":form})

def user_list(request):
    data_list = UserInfo.objects.all()


    my_page = Pagination(request,data_list,page_size=2)

    return render(request, 'user_list.html', {'data_list': my_page.data_list,'page_param':my_page.page_param,'page_str':my_page.page_str()})