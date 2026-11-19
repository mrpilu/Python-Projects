from django import forms
from django.forms import ModelForm

from .models import Account, Transaction


# Creates Account Form based on Account Model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# Creates Transaction Form based on Transaction Model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }


# Drop-down of existing accounts for the home page
class SelectAccountForm(forms.Form):
    account = forms.ModelChoiceField(
        queryset=Account.Accounts.all(),
        empty_label='-- Select an account --',
        label='Choose Account',
    )
