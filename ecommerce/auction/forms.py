from django import forms
from django.core.validators import MinValueValidator


class BidsForm(forms.Form):
    bid_amount = forms.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        fields = 'bid_amount'
