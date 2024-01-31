from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout

from dashboard.forms import SignUpForm,LoginForm

# Create your views here.

class RegistrationView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'dashboard/signup.html', {'form': form})
    
    def post(self, request):
        try:
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('dashboard:login')
            return render(request, 'dashboard/signup.html', {'form': form, 'error_message': 'invaild data'})
        except Exception as e:
            return render(request, 'dashboard/signup.html', {'form': form, 'error_message': str(e)})

class LoginView(View):
    def get(self, request):
        try:
            form = LoginForm()
            return render(request, 'dashboard/login.html', {'form': form})
        except Exception as e:
            return render(request, 'dashboard/login.html', {'form': form, 'error_message': str(e)})
    
    def post(self, request):
        
        try:
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(email=email, password=password)
                if user is not None :
                    login(request, user)
                    return redirect('dashboard:dashboard')
                else:
                    error_message = "Invalid username or password."
                    return render(request, 'dashboard/login.html', {'form': form, 'error_message':error_message})
            else:
                return render(request, 'dashboard/login.html', {'form': form, 'error_message': 'invaild data'})
        except Exception as e:
            return render(request, 'dashboard/login.html', {'form': form, 'error_message': str(e)})

@method_decorator(login_required, name='dispatch')  
class DashboardView(View):
    
    def get(self, request):
        try:
            print("user",request.user.role)
            if request.user.role == 'student':           
                data = {
                    'name' : request.user.name,
                    'email' : request.user.email,
                    'country' : request.user.country,
                    'nationality' : request.user.nationality,
                    'mobile' : request.user.mobile,
                }
                return render(request, 'dashboard/dashboard_student.html', {'data':data})
            elif request.user.role == 'staff':           
                data = {
                    'name' : request.user.name,
                    'email' : request.user.email,
                    'country' : request.user.country,
                    'nationality' : request.user.nationality,
                    'mobile' : request.user.mobile,
                }
                return render(request, 'dashboard/dashboard_staff.html', {'data':data})
            elif request.user.role == 'editor':           
                data = {
                    'name' : request.user.name,
                    'email' : request.user.email,
                    'country' : request.user.country,
                    'nationality' : request.user.nationality,
                    'mobile' : request.user.mobile,
                }
                return render(request, 'dashboard/dashboard_editor_.html', {'data':data})
            elif request.user.role == 'admin':           
                data = {
                    'name' : request.user.name,
                    'email' : request.user.email,
                    'country' : request.user.country,
                    'nationality' : request.user.nationality,
                    'mobile' : request.user.mobile,
                }
                return render(request, 'dashboard/dashboard_admin.html', {'data':data})
            else:
                return render(request, 'dashboard/error.html', { 'error_message': "user not found"})
        except Exception as e:
            return render(request, 'dashboard/error.html', { 'error_message': str(e)})

# sample

