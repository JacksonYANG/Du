from django import forms

from Du.models import Comment


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名')
    username.widget.attrs.update({'class': 'form-control'})
    password = forms.CharField(label='密码', widget= forms.PasswordInput)
    password.widget.attrs.update({'class': 'form-control'})

class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名')
    username.widget.attrs.update({'class': 'form-control'})
    email = forms.CharField(label='电子邮箱', required=False, widget=forms.EmailInput)
    email.widget.attrs.update({'class': 'form-control'})
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
    password.widget.attrs.update({'class': 'form-control'})
    confirm = forms.CharField(label='确认密码', widget=forms.PasswordInput)
    confirm.widget.attrs.update({'class': 'form-control'})

    def clean_confirm(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm']
        if password == confirm_password:
            return password
        else:
            raise forms.ValidationError('两次输入的密码不一致')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']


