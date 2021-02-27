from django import forms

from .models import Person, PhoneNumber


class CreatePersonForm(forms.ModelForm):
    phones = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Person
        fields = [
            'name',
            'phones'
        ]
class UpdatePersonForm(forms.ModelForm):
    phones = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Person
        fields = [
            'name'
        ]