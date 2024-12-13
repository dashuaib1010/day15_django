from fileinput import FileInput
from sys import orig_argv

from django import forms

from django.core.exceptions import ValidationError
from django.forms import PasswordInput, TextInput

from app_01.models import UserInfo, PrettyNum, TaskInfo, City

from app_01.utils.bootstrap_model_form import BootStrapModuleFrom, BootStrapFrom

from app_01.models import Admin
from app_01.utils.encrypt import md5
from app_01.views.chart_views import chart_bar


class UserInfoForm(BootStrapModuleFrom):
    name = forms.CharField(min_length=3, label='姓名')

    class Meta:
        model = UserInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'create_time':
                field.widget.attrs['id'] = 'dt_picker'


class PrettyNumForm(BootStrapModuleFrom):
    # # 验证方式1
    # mobile = forms.CharField(
    #     label='手机号码',
    #     validators=[RegexValidator(r"^1[3-9]\d{9}$", '手机号码格式错误',),]
    # )

    class Meta:
        model = PrettyNum
        fields = "__all__"

    # 验证方式2
    def clean_mobile(self):
        mobile_txt = self.cleaned_data['mobile']
        if len(mobile_txt) != 11:
            raise ValidationError('格式不正确')

        if PrettyNum.objects.filter(mobile=mobile_txt).exists():
            raise ValidationError('手机号已存在')

        return mobile_txt


class PrettyEditNumForm(BootStrapModuleFrom):
    mobile = forms.CharField(label='手机号码', disabled=True)

    class Meta:
        model = PrettyNum
        fields = "__all__"


class AdminForm(BootStrapModuleFrom):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=PasswordInput(render_value=True)
    )

    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {
            'password': PasswordInput(render_value=True)
        }

    def clean_password(self):
        password = self.cleaned_data.get("password")

        return md5(password)

    def clean_confirm_password(self):
        confirm_password = md5(self.cleaned_data.get('confirm_password'))
        password = self.cleaned_data.get('password')
        if confirm_password != password:
            raise ValidationError("密码不一致")

        return confirm_password


class AdminEditForm(BootStrapModuleFrom):
    class Meta:
        model = Admin
        fields = ["username", ]


class AdminResetForm(BootStrapModuleFrom):
    username = forms.CharField(label='账户名', disabled=True)

    confirm_password = forms.CharField(
        label='确认新密码',
        widget=PasswordInput(render_value=True)
    )
    new_password = forms.CharField(
        label='输入新密码',
        widget=PasswordInput(render_value=True),

    )

    class Meta:
        model = Admin
        fields = ['username', 'new_password', "confirm_password"]
        # exclude = ['password']

    def clean_new_password(self):
        new_password = self.cleaned_data.get("new_password")

        return md5(new_password)

    def clean_confirm_password(self):
        confirm_password = md5(self.cleaned_data.get('confirm_password'))
        new_password = self.cleaned_data.get('new_password')

        if confirm_password != new_password:
            raise ValidationError("密码不一致")

        if Admin.objects.filter(id=self.instance.pk, password=confirm_password).exists():
            raise ValidationError("新密码不得与原密码相同")

        return confirm_password


class LoginForm(BootStrapModuleFrom):
    username = forms.CharField(label='用户名', required=True, )
    password = forms.CharField(label='密码', required=True, widget=PasswordInput(render_value=True))
    img_code = forms.CharField(label='图片验证码', required=True, widget=PasswordInput())

    class Meta:
        model = Admin
        fields = ['username', 'password']

    def clean_password(self):
        password = md5(self.cleaned_data.get('password'))
        return password


class TaskShowListForm(BootStrapModuleFrom):
    class Meta:
        model = TaskInfo
        fields = '__all__'


class TaskAddForm(BootStrapModuleFrom):
    class Meta:
        model = TaskInfo
        # 使用户只能新建发布于自己的任务
        fields = ['level', 'title', 'detail', ]
        # fields = '__all__'
        widgets = {
            "detail": TextInput()
        }


class UploadForm(BootStrapFrom):
    exclude_fields = ['img', ]

    name = forms.CharField(label='名字')
    age = forms.IntegerField(label='年龄')
    img = forms.FileField(label='头像', widget=forms.FileInput(attrs={
        'style': 'width:200px;'
    }))


class UploadModelForm(BootStrapModuleFrom):
    img = forms.FileField(label='logo', widget=forms.FileInput(attrs={
        'style': 'width:200px;'
    }))

    class Meta:
        model = City
        fields = '__all__'

