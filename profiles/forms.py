from django import forms
from .models import Profile
from django.core.exceptions import ValidationError


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone_number', 'address', 'age', 'profile_picture']


    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone:
            if not phone.isdigit():
                raise ValidationError('Phone number must contain only digits')
        return phone


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('Name is required')
        return name