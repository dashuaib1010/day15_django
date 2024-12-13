from operator import contains
from webbrowser import register

from Tools.scripts.generate_opcode_h import internal_footer
from django.core.mail import forbid_multi_line_headers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from io import BytesIO

from app_01.models import Admin
from app_01.utils.encrypt import md5
from app_01.utils.captcha import CaptchaGenerator
from app_01.utils.forms import LoginForm

def login(request):
    if request.method == "GET":
        content={
            'form':LoginForm()
        }

        return render(request,'login.html',content)

    form = LoginForm(request.POST)
    if form.is_valid():


        input_img_code = form.cleaned_data.pop('img_code')      # 使用pop以防止增添的代码影响之前写的查询逻辑

        session_img_code = request.session.get('img_code','')
        if input_img_code.upper() != session_img_code.upper():
            form.add_error('img_code', '验证码输入错误')
            return render(request,"login.html",{'form':form})

        request.session.delete('img_code')

        print(form.cleaned_data)

        obj = Admin.objects.filter(**form.cleaned_data).first()
        if not obj:
            form.add_error('username','用户名或密码不正确')
            return render(request,"login.html",{'form':form})


        request.session['info'] = {
            'id':obj.pk,
            'username':obj.username

        }
        request.session.set_expiry(3600*24*3)   # 设置三天的登录session有效时间
        return redirect('/admin/list/')


    content = {
        'form':form,
    }

    return render(request, 'login.html',content)


def logout(request):
    request.session.clear()
    return redirect('/login/')



def image_code(request):
    cgr = CaptchaGenerator()
    img,img_code = cgr.generate_captcha()

    print(img_code)
    stream = BytesIO()
    img.save(stream,'png')

    request.session['img_code'] = img_code
    request.session.set_expiry(60)

    return HttpResponse(stream.getvalue())


