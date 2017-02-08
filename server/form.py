# -*- coding:utf-8 -*-
__author__ = 'abc'
from django import forms
from django.forms import ModelForm
from models import Servers,User
from django.contrib.auth.admin import User



class ServerForm(ModelForm):
    ip = forms.GenericIPAddressField(max_length=30,  protocol='ipv4',
                                     help_text=u'必填', error_messages={'required': u'请输入ip'})

    class Meta:
        model = Servers
        #fields = ['name', 'ip','cpu' 'purpose', 'status',  'remark']
        exclude = ['id']

class UserRegister(forms.Form):
    username = forms.CharField(
                        widget=forms.TextInput(
                        attrs={'placeholder': u"用户名",}),
                        error_messages={'required':u'必填'},
                        label=u'用户名')
    password = forms.CharField(
                        widget=forms.PasswordInput(attrs={'placeholder': u"密码",}),
                        help_text='不少于6位',
                        label='密 码',
                        error_messages={'required':u'密码不能为空', 'min_length': u'至少六位'},
                        min_length=6)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': u"重复密码",}),
                         help_text='再次确认密码',
                         label='密 码',
                         error_messages={'required':u'必填', 'min_length': u'至少六位'},
                         min_length=6)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': u"电子邮箱",}),
                        error_messages={'required': u'不能为空', 'invalid': u'邮箱格式不正确'},
                        label='电子邮箱')

#   custom email validation error
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(u'邮箱已注册')
        return email

# custom username validation error
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(u"用户名已存在")
        return username

# custom password validation error
    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError(u'密码不一致')
        return password2

class Admins(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']



