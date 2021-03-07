from django import forms
from .models import User
from .models import Profile
from django.core import validators


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', ]


class ProfileView(forms.ModelForm):
    first_name = forms.CharField(validators=[validators.MinLengthValidator(3)])
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "optional"}))

    YEARS = [x for x in range(1940, 2003)]
    birthdate = forms.DateField(initial="1994-06-21", widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "gender", "birthdate"]


class ProfileView2(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "optional"}))

    class Meta:
        model = Profile
        fields = ["profile_image", "bio"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'gender',
                  'profile_image', 'bio', 'account_type', 'birthdate']
