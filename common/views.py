from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from common.forms import UserForm

def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자인증:사용자명과 비밀번호가 정확한지 검증
            login(request, user) # 로그인: 사용자 세션 생성
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})



