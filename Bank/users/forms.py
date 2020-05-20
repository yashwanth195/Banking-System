from django import forms
from django.contrib.auth.models import User
from .models import Customer

class NewTransactionForm(forms.Form):
    username=forms.CharField(label='User Name')
    amount=forms.IntegerField(label='Transaction Amout')
    
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()


    class Meta:
        model=User
        fields=['email']


# class CustomerUpdateForm(forms.ModelForm):
#     class Meta:
#         model=Customer