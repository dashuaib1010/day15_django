
from django.shortcuts import render, redirect
from app_01.models import PrettyNum
from app_01.utils.pagination import Pagination

from app_01.utils.forms import PrettyNumForm,PrettyEditNumForm




def prettynum_list(request):
        query_param = request.GET.get('query', '')
        print(query_param)

        query_dict = {
            'mobile__contains': query_param
        }

        all_data_list = PrettyNum.objects.filter(**query_dict).order_by('-level')

        my_page = Pagination(request,all_data_list,)

        # total_count_obj = len(all_data_list)
        # page_size = 10
        # x, y = divmod(total_count_obj, page_size)
        # if y != 0:
        #     total_count_page = x + 1
        # else:
        #     total_count_page = x
        #
        #
        # page_param = int(request.GET.get('page',1,))
        #
        # import copy
        # full_params = copy.deepcopy(request.GET)
        # full_params._mutable = True
        #
        #
        #
        #
        # if page_param >total_count_page:
        #     page_param=total_count_page
        # elif page_param<1:
        #     page_param=1
        #
        # start = (page_param-1)*10
        # if start<0:
        #     start=0
        # end = page_param*10
        #
        # data_list = PrettyNum.objects.filter(**query_dict)[start:end]
        #
        #
        #
        #
        #
        #
        #
        # page_str_list = []
        #
        #
        # # 添加首页
        # full_params.setlist('page', [1,])
        # print(full_params.urlencode())
        # ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(full_params.urlencode(), "首页")
        # page_str_list.append(ele)
        #
        # # 添加上一页
        # if page_param-1>0:
        #     full_params.setlist('page', [page_param-1,])
        #     ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(full_params.urlencode(), "上一页")
        #     page_str_list.append(ele)
        # else:
        #     full_params.setlist('page', [1,])
        #     ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(full_params.urlencode() ,"上一页")
        #     page_str_list.append(ele)
        #
        # # 添加非首尾页
        # for i in range(page_param-5, page_param+6):
        #         if i <= 0 or i > total_count_page:
        #             continue
        #
        #         if i == page_param:
        #             full_params.setlist('page', [i,])
        #             ele = """<li class="page-item active"><a class="page-link" href="?{0}">{1}</a></li>""".format(full_params.urlencode(),i)
        #             page_str_list.append(ele)
        #             continue
        #
        #
        #         full_params.setlist('page', [i,])
        #         ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(full_params.urlencode(),i)
        #         page_str_list.append(ele)
        #
        # # 添加下一页
        # if page_param + 1 < total_count_page:
        #     full_params.setlist('page', [page_param+1,])
        #
        #     ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(full_params.urlencode(),
        #                                                                                                 "下一页")
        #     page_str_list.append(ele)
        # else:
        #     full_params.setlist('page', [total_count_page,])
        #
        #     ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(full_params.urlencode(), "下一页")
        #     page_str_list.append(ele)
        #
        #
        # # 添加尾页
        # full_params.setlist('page', [total_count_page,])
        #
        # ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(full_params.urlencode(), "尾页")
        # page_str_list.append(ele)
        #
        #
        #
        #
        #
        #
        # page_str = mark_safe(''.join(page_str_list))

        return render(request,'prettynum_list.html',{"data_list":my_page.data_list, 'query_param':query_param,'page_param':my_page.page_param, 'page_str':my_page.page_str})


def prettynum_add(request):
    if request.method == 'GET':
        form = PrettyNumForm()
        return render(request,'prettynum_add.html',{"form":form})

    form = PrettyNumForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/prettynum/list')

    print(form.errors)
    return render(request, 'prettynum_add.html', {"form": form})


def prettynum_edit(request, id):

    prettynum_obj = PrettyNum.objects.filter(id=id).first()

    if request.method == "GET":
        form = PrettyEditNumForm(instance=prettynum_obj)

        return render(request, 'prettynum_edit.html', {'form':form})

    form = PrettyEditNumForm(request.POST, instance=prettynum_obj)

    content = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/prettynum/list/')

    print(form.errors)

    return render(request,'prettynum_edit.html',content)


def prettynum_delete(request, id):
    PrettyNum.objects.filter(id=id).first().delete()
    return redirect('/prettynum/list/')