from django import forms
from django.contrib.auth.models import User
from auth_app.models import UserInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
class UserProfile(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
        widgets = {
            'nim': forms.TextInput(attrs={'class': 'form-control'}),
            'kelas': forms.TimeInput(attrs={'class': 'form-control'}),
            'jurusan': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'})
        }