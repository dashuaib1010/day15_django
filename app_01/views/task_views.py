import json
from socket import fromfd
from tarfile import data_filter

from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app_01.models import TaskInfo, Admin
from app_01.utils.forms import TaskAddForm, TaskShowListForm
from app_01.utils.pagination import Pagination


def task_list(request):

    query_param = request.GET.get('query', '')
    query_dict = {
        'title__contains': query_param,
    }


    data_list = TaskInfo.objects.filter(**query_dict).order_by('-id')

    form = TaskAddForm()

    form_fields = TaskShowListForm().fields.items()

    my_page = Pagination(request, data_list, page_size=10)

    content = {
        'form': form,
        'target_model_label': '任务',
        'form_fields': form_fields,

        'data_list': my_page.data_list,
        'page_param': my_page.page_param,
        'page_str': my_page.page_str(),
    }

    return render(request, 'task_list.html', content)


@csrf_exempt
def task_ajax_add(request):
    form = TaskAddForm(request.POST)
    if form.is_valid():
        user_id = request.session['info']['id']
        print(user_id)
        obj = Admin.objects.filter(id=user_id).first()
        # 要写注意层级关系 是设置instance的user_id
        form.instance.user = obj
        print(form.cleaned_data)
        form.save()

        data_dict = {
            'status': True,

        }
        return HttpResponse(json.dumps(data_dict))

    data_dict = {
        'status': False,
        'errors': form.errors,
    }
    return HttpResponse(json.dumps(data_dict))


def task_ajax_delete(request, id):
    if not TaskInfo.objects.filter(id=id).exists():
        return JsonResponse({"status": False, "error": "数据不存在，删除失败。"})

    TaskInfo.objects.filter(id=id).delete()

    return JsonResponse({
        "status": True,
    })

@csrf_exempt
def task_ajax_edit(request, id):
    if not TaskInfo.objects.filter(id=id).exists():
        return JsonResponse({"status": False, "error": "数据不存在，编辑失败。"})
    obj = TaskInfo.objects.filter(id=id).first()
    form = TaskAddForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True,})

    return JsonResponse({
        "status": False,
        'errors':form.errors,
    })

def task_ajax_details(request, id):
    if not TaskInfo.objects.filter(id=id).exists():
        return JsonResponse({"status": False, "error": "数据不存在，编辑失败。"})

    data_list = TaskInfo.objects.filter(id=id).values('level', 'title', 'detail').first()

    return JsonResponse({
        "status": True,
        "data": data_list
    })
