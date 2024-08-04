from django import forms
from .models import Student, Parent, Faculty, Transaction

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['uid']  # Exclude uid field from the form

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        exclude = ['uid']  # Exclude uid field from the form

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        exclude = ['uid']  # Exclude uid field from the form

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['sender_uid', 'receiver_uid', 'amount']
