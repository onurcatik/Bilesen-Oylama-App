from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Kullanıcı Adı', max_length=150, required=True)
    email = forms.EmailField(label='E-posta', required=True)
    password1 = forms.CharField(label='Parola', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Parolayı Onayla', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
