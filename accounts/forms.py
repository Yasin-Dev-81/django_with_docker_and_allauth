from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from allauth.account.forms import SignupForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'age', )
        # or: fields = UserCreationForm.Meta.fields + ('age', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'age', )
        # or: fields = UserChangeForm.Meta.fields + ('age', )


class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        first_name = forms.CharField(max_length=30, label='First Name')
        last_name = forms.CharField(max_length=30, label='Last Name')
        age = forms.CharField(max_length=30, label='Age')
        # phone = forms.CharField(max_length=30, label='Phone Number')
        # address = forms.CharField(max_length=30, label='Address')
        # gender = forms.CharField(max_length=30,label = 'Gender')

    # Put in custom signup logic
    def custom_signup(self, request, user):
        # Set the user's type from the form response
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.age = self.cleaned_data['age']
        # user.phone = self.cleaned_data['phone']
        # user.address = self.cleaned_data['address']
        # user.gender = self.cleaned_data['gender']

        # Save the user's type to their database record
        user.save()
