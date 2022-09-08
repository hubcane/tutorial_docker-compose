from django.shortcuts import render, redirect
from .models import Fcuser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .forms import loginform

# Create your views here.

def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
    return render(request, 'home.html')

def logout(request):
    if request.session['user']:
        del(request.session['user'])
    return redirect('/')

def login(request):
    form = loginform()

    if request.method == "POST":
        form = loginform(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = loginform()
    return render(request, 'login.html', {'form': form})

# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)

#         res_data = {}
#         if not(username and password): 
#             res_data['error'] = '모든 값을 기입해야합니다'
#         else:
#             try:
#                 fcuser = Fcuser.objects.get(username=username)
#                 if check_password(password, fcuser.password):
#                     # session
#                     request.session['user'] = fcuser.id
#                     return redirect('/')
#                     pass
#                 else: 
#                     res_data['error'] = '비밀번호가 틀렸습니다.'
#             except Exception as e:
#                 # res_data['error'] = '등록되지 않은 User 입니다'
#                 res_data['error'] = str(e)

#         return render(request, 'login.html', res_data)


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        useremail = request.POST.get('useremail', None)
        
        res_data = {}
        if not (username and password and re_password) and useremail:
            res_data['error'] = '모든 값을 기입하셔야합니다'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다'
        else:
            fcuser = Fcuser(
                username=username
                , password = make_password(password)
                , useremail=useremail
                )
        
            fcuser.save()

        return render(request, 'register.html', res_data)