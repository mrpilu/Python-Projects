from django.shortcuts import get_object_or_404, redirect, render

from .forms import AccountForm, SelectAccountForm, TransactionForm
from .models import Account


def home(request):
    if request.method == 'POST':
        form = SelectAccountForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            return redirect('balance', pk=account.pk)
    else:
        form = SelectAccountForm()
    return render(request, 'checkbook/index.html', {'form': form})


def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save()
            return redirect('balance', pk=account.pk)
    else:
        form = AccountForm()
    return render(request, 'checkbook/CreateNewAccount.html', {'form': form})


def balance(request, pk=None):
    # /balance/ with no account renders an empty sheet; /balance/<pk>/ shows one account.
    if pk is None:
        return render(request, 'checkbook/BalanceSheet.html', {'account': None, 'rows': []})

    account = get_object_or_404(Account, pk=pk)

    # Build the rows with a running balance, oldest transaction first.
    running = account.initial_deposit
    rows = []
    for t in account.transaction_set.all():
        if t.type == 'Deposit':
            running += t.amount
        else:
            running -= t.amount
        rows.append({'transaction': t, 'balance': running})

    context = {
        'account': account,
        'rows': rows,
        'balance': account.balance,
    }
    return render(request, 'checkbook/BalanceSheet.html', context)


def transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            new_transaction = form.save()
            return redirect('balance', pk=new_transaction.account.pk)
    else:
        # The balance sheet's "Add Transaction+" button passes ?account=<pk>
        form = TransactionForm(initial={'account': request.GET.get('account')})
    return render(request, 'checkbook/AddTransaction.html', {'form': form})
