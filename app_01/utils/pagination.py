from django.utils.safestring import mark_safe
import copy




class Pagination(object):


    def __init__(self,request,all_data_list, page_param='page',page_size=10):
        self.request = request
        self.all_data_list=all_data_list
        self.page_param = page_param
        self.page_size = page_size

        total_count_obj = len(self.all_data_list)
        x, y = divmod(total_count_obj, self.page_size)
        if y != 0:
            self.total_count_page = x + 1
        else:
            self.total_count_page = x


        param = request.GET.get(self.page_param, '1', )
        if param.isdecimal():
            self.page_param=int(param)
        else:
            self.page_param=1

        if self.page_param >self.total_count_page:
            self.page_param=self.total_count_page
        elif self.page_param<1:
            self.page_param=1



        self.start = (self.page_param-1)*page_size
        if self.start<0:
            self.start=0
        self.end = self.page_param*page_size

        self.data_list = all_data_list[self.start:self.end]

        # 得到完整的请求参数
        self.full_params = copy.deepcopy(request.GET)
        self.full_params._mutable = True


    def page_str(self):

        page_str_list = []

        # 添加首页
        self.full_params.setlist('page', [1, ])


        ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(self.full_params.urlencode(),
                                                                                               "首页")
        page_str_list.append(ele)

        # 添加上一页
        if self.page_param - 1 > 0:
            self.full_params.setlist('page', [self.page_param - 1, ])
            ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(
                self.full_params.urlencode(), "上一页")
            page_str_list.append(ele)
        else:
            self.full_params.setlist('page', [1, ])
            ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(
                self.full_params.urlencode(), "上一页")
            page_str_list.append(ele)

        # 添加非首尾页
        for i in range(self.page_param - 5, self.page_param + 6):
            if i <= 0 or i > self.total_count_page:
                continue

            if i == self.page_param:
                self.full_params.setlist('page', [i, ])
                ele = """<li class="page-item active"><a class="page-link" href="?{0}">{1}</a></li>""".format(
                    self.full_params.urlencode(), i)
                page_str_list.append(ele)
                continue

            self.full_params.setlist('page', [i, ])
            ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(
                self.full_params.urlencode(), i)
            page_str_list.append(ele)

        # 添加下一页
        if self.page_param + 1 < self.total_count_page:
            self.full_params.setlist('page', [self.page_param + 1, ])

            ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(
                self.full_params.urlencode(),
                "下一页")
            page_str_list.append(ele)
        else:
            self.full_params.setlist('page', [self.total_count_page, ])

            ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(
                self.full_params.urlencode(), "下一页")
            page_str_list.append(ele)

        # 添加尾页
        self.full_params.setlist('page', [self.total_count_page, ])

        ele = """<li class="page-item"><a class="page-link" href="?{0}">{1}</a></li>""".format(self.full_params.urlencode(),
                                                                                               "尾页")
        page_str_list.append(ele)

        page_str = mark_safe(''.join(page_str_list))

        return page_str