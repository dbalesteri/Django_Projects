from django.forms import ModelForm
from .models import Transaction
from .models import Account


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'