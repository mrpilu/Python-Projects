from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum


# Creates the Account Model
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(
        max_digits=15, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
    )

    # Defines the Model Manager for Accounts
    Accounts = models.Manager()

    class Meta:
        ordering = ['last_name', 'first_name']

    # Allows references to a specific account to be returned as the owner's name not the primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def balance(self):
        """Initial deposit + all deposits - all withdrawals."""
        totals = self.transaction_set.values('type').annotate(total=Sum('amount'))
        sums = {row['type']: row['total'] for row in totals}
        return (
            self.initial_deposit
            + sums.get('Deposit', Decimal('0.00'))
            - sums.get('Withdrawal', Decimal('0.00'))
        )


# Choices for a transaction
TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]


# Creates the Transaction Model
class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(
        max_digits=15, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
    )
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # Defines the Model Manager for Transactions
    Transactions = models.Manager()

    class Meta:
        ordering = ['date', 'id']

    def __str__(self):
        return f'{self.date} {self.type} {self.amount} ({self.account})'
