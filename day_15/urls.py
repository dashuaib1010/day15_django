"""
URL configuration for day_15 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from app_01.views import department_views,prettynum_views,user_views,admin_views, login, task_views, chart_views, upload_views


urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'media/(?P<path>.*)/$', serve, {'document_root': settings.MEDIA_ROOT},name='media'),
    path('depart/list/',department_views.department_list),
    path('depart/add/',department_views.department_add),
    path('depart/delete/',department_views.department_delete),
    path('depart/<int:id>/edit/',department_views.department_edit),
    path('depart/multi/',department_views.department_multi),
    path('user/list/',user_views.user_list),
    path('user/add/',user_views.user_add),
    path('user/<int:id>/delete/',user_views.user_delete),
    path('user/<int:id>/edit/',user_views.user_edit),
    path('prettynum/list/',prettynum_views.prettynum_list),
    path('prettynum/add/',prettynum_views.prettynum_add),
    path('prettynum/<int:id>/delete/', prettynum_views.prettynum_delete),
    path('prettynum/<int:id>/edit/', prettynum_views.prettynum_edit),

    path('admin/list/', admin_views.admin_list),
    path('admin/add/', admin_views.admin_add),
    path('admin/<int:id>/edit/', admin_views.admin_edit),
    path('admin/<int:id>/delete/', admin_views.admin_delete),
    path('admin/<int:id>/reset_pwd/', admin_views.admin_reset_pwd),



    path('login/', login.login),
    path('logout/', login.logout),
    path('image/code/', login.image_code),


    path('task/list/', task_views.task_list),
    path('task/add/', task_views.task_ajax_add),

    path('task/<int:id>/delete/', task_views.task_ajax_delete),
    path('task/<int:id>/edit/', task_views.task_ajax_edit),
    path('task/<int:id>/details/', task_views.task_ajax_details),





    path('chart/list/', chart_views.chart_list),
    path('chart/bar/', chart_views.chart_bar),
    path('chart/pie/', chart_views.chart_pie),
    path('chart/line/', chart_views.chart_line),



    path('upload/list/', upload_views.upload),
    path('upload_modelform/list/', upload_views.upload_modelform),




]
