from django import forms

class Signup(forms.Form):
    username=forms.CharField(min_length=3,label="Username")
    password=forms.CharField(min_length=3,label="Password",widget=forms.PasswordInput)
    confirm=forms.CharField(min_length=3,label="Conf pass",widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")

        if password and confirm and password !=confirm:
            raise forms.ValidationError("Wrong passwords")

        values={
            "username" :username,
            "password": password,
            }
        return values

class LoginF(forms.Form):
    username= forms.CharField(label="Username")
    password= forms.CharField(label="Password",widget=forms.PasswordInput)
