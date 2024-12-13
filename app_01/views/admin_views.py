from django.shortcuts import render, redirect
from app_01.models import Admin

from app_01.utils.forms import AdminForm, AdminEditForm, AdminResetForm

from app_01.utils.pagination import Pagination



def admin_add(request):
    if request.method == "GET":
        content = {
            "target_module_label":"管理员账户",
            "form": AdminForm(),
        }
        return render(request, 'add_edit.html', content)

    form = AdminForm(request.POST)


    if form.is_valid():
        confirm_username = form.cleaned_data['username']
        if Admin.objects.filter(username=confirm_username).exists():

            return redirect('/admin/list')

        form.save()
        return redirect('/admin/list')


    content = {
        'form': form,
        "target_model_label": "管理员账户",
    }

    print(form.errors)
    return render(request, 'add_edit.html', content)


def admin_delete(request, id):
    Admin.objects.filter(id=id).first().delete()


    return redirect('/admin/list/')


def admin_edit(request, id):

    admin_obj = Admin.objects.filter(id=id).first()

    if not admin_obj:
        return redirect("admin/list")

    if request.method == "GET":
        content = {
            "target_module_label": "管理员账户",
            "form": AdminEditForm(instance=admin_obj),
        }
        return render(request, 'add_edit.html', content)

    form = AdminEditForm(request.POST, instance=admin_obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')

    content = {"form": form}

    return render(request, 'add_edit.html', content)


def admin_list(request):
    # for i in range(50):
    #
    #     Admin.objects.create(username='zyy'+str(i), password='pwdqweasd'+str(i))
    #

    query_param = request.GET.get('query','')


    query_dict = {
        'username__contains':query_param,
    }


    data_list = Admin.objects.filter(**query_dict)

    form_fields = AdminForm().fields.items()


    my_page = Pagination(request, data_list, page_size=10)
    content = {
        "query_param":query_param,
        "target_model_name":'admin',
        "target_model_label":'管理员用户',
        "form_fields":form_fields,

        'data_list': my_page.data_list,
        'page_param': my_page.page_param,
        'page_str': my_page.page_str(),

    }

    return render(request, 'list.html', content)



def admin_reset_pwd(request, id):
    obj = Admin.objects.filter(id=id).first()

    if not obj:
        return redirect("/admin/list")



    if request.method == "GET":
        content = {
            "target_model_label": '新密码',
            "form": AdminResetForm(instance=obj),
        }
        return render(request,'add_edit.html',content)


    form = AdminResetForm(request.POST, instance=obj)

    if form.is_valid():
        new_password = form.cleaned_data.get('new_password')

        print(new_password)

        Admin.objects.filter(id=id).update(password=new_password)
        return redirect('/admin/list')

    content  = {
        'form':form
    }

    return render(request, 'add_edit.html', content)







