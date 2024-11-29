# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
# from django.urls import reverse_lazy

# from .forms import IncomeForm
# from .models import Income


# @login_required
# def income_list(request):
#     incomes = get_list_or_404(Income, owner=request.user)
#     add_income_form = IncomeForm()
#     context = {
#         "incomes": incomes,
#         "add_income_form": add_income_form,
#     }
#     return render(request, "incomes/income_list.html", context)


# @login_required
# def add_income_view(request):
#     if request.method == "POST":
#         form = IncomeForm(request.POST)
#         if form.is_valid():
#             income = form.save(commit=False)
#             income.owner = request.user
#             income.save()
#             return redirect("income-list")
#     else:
#         form = IncomeForm()
#     # return redirect(reverse_lazy("detail", kwargs={"slug": complaint_slug}))
#     # return redirect(reverse_lazy("/"))


# def income_detail_view(request, slug):
#     income = get_object_or_404(Income, slug=slug)
#     context = {
#         "income": income,
#     }
#     return render(request, "incomes/income_detail.html", context)


# def income_update_view(request, slug):
#     income = get_object_or_404(Income, slug=slug)
#     form = IncomeForm(instance=income)
#     if request.method == "POST":
#         form = IncomeForm(request.POST, instance=income)
#         if form.is_valid():
#             form.save()
#             return redirect("income-detail", slug=income.slug)
#     context = {
#         "form": form,
#         'income': income,
#     }
#     return render(request, "incomes/income_update.html", context)