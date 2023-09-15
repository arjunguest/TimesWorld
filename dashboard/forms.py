from django import forms
from dashboard.models import Customer
from django.core.validators import RegexValidator

class SignUpForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name','email', 'password', 'role', 'country', 'nationality','mobile')
        extra_kwargs = {'password': {'write_only': True}}
        
        error_css_class = 'error_msg'
        required_css_class = "required"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'txt_field_input'}),
            'email': forms.TextInput(attrs={'class': 'txt_field_input'}),
            'country': forms.TextInput(attrs={'class': 'txt_field_input'}),
            'nationality': forms.TextInput(attrs={'class': 'txt_field_input'}),
            'mobile': forms.TextInput(attrs={'class': 'txt_field_input'}),
            'password': forms.PasswordInput(attrs={'class': 'txt_field_input'}),
            'role': forms.Select(attrs={'class': 'txt_field_select'}),
        }
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
       
        if commit:
            if self.cleaned_data['role'] == 'staff':
                user.is_staff = True
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'txt_field_input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'txt_field_input'}))
    error_css_class = 'error_msg'
    