from django import forms

from .models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["name","amount", "description"]
        widgets = {
            # "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": "3"}),
        }
