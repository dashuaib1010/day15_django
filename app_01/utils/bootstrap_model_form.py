from calendar import firstweekday

from django.forms import ModelForm, Form


class BootStrapFrom(Form):
    exclude_fields = []

    def __init__(self, *args, **kwargs):
        super(BootStrapFrom, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.exclude_fields:
                continue
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class BootStrapModuleFrom(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootStrapModuleFrom, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
