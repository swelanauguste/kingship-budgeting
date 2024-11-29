from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import AccountForm
from .models import Account


@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)  # Changed from get_list_or_404

    add_account_form = AccountForm()
    context = {
        "accounts": accounts,
        "add_account_form": add_account_form,
    }
    return render(request, "accounts/account_list.html", context)


@login_required
def add_account_view(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.owner = request.user
            account.save()
            return redirect("account-list")
    else:
        form = AccountForm()
    # return redirect(reverse_lazy("detail", kwargs={"slug": complaint_slug}))
    # return redirect(reverse_lazy("/"))


def account_detail_view(request, slug):
    account = get_object_or_404(Account, slug=slug)
    context = {
        "account": account,
    }
    return render(request, "accounts/account_detail.html", context)


def account_update_view(request, slug):
    account = get_object_or_404(Account, slug=slug)
    form = AccountForm(instance=account)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect("account-detail", slug=account.slug)
    context = {
        "form": form,
        "account": account,
    }
    return render(request, "accounts/account_update.html", context)
