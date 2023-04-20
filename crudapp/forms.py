from django import forms
from crudapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['firstname', 'lastname', 'email']