from distutils.command.clean import clean
from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class loginform(forms.Form):
    username = forms.CharField(
        max_length=12
        , label='사용자 이름'
        , error_messages={
            'required': '아이디를 입력해주세요'
        }
        )
    password = forms.CharField(
        widget = forms.PasswordInput
        , max_length=12
        , label="비밀번호"
        , error_messages={
            'required': '비밀번호를 기입해주세요'
        }
        )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try: 
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', '등록되지 않은 아이디입니다')
                return 

            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호가 틀렸습니다')
            else:
                self.user_id = fcuser.id