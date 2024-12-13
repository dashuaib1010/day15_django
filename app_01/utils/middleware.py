from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        exclude_path = ['/login/', '/image/code/']

        if request.path_info in exclude_path:
            return

        if request.session.get('info'):
            return

        return redirect("/login/")