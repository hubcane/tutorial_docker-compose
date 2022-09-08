
from django import forms

class Boardform(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요'
        }, max_length=128
        , label = '제목'
        )
    contents = forms.CharField(
        widget = forms.Textarea
        , label="내용"
        , error_messages={
            'required': '비밀번호를 기입해주세요'
        }
        )
    tags = forms.CharField(
        label="태그"
        , required=False
        )