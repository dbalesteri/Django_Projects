from django.db import models

# Create your models here.


class Account(models.Model):
    first_name = models.CharField(max_length=25, default="", blank=True)
    last_name = models.CharField(max_length=25, default="", blank=True)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    Accounts = models.Manager()

    def __str__(self):
        return self.first_name + " " + self.last_name


TransactionTypes = [('Deposit','Deposit'),('Withdrawal','Withdrawal')]


class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=60, choices=TransactionTypes)
    amount = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)

    Transactions = models.Manager()

    def __str__(self):
        return self.account

