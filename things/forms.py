"""Forms of the project."""

from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from things.models import Thing

class ThingForm(forms.Form):

    name = forms.CharField(max_length=35)
    description = forms.CharField(max_length=120, widget=forms.Textarea(attrs={'name':'body', 'style': 'height: 3em'}))
    quantity = forms.IntegerField(
        validators=[MinLengthValidator(0), MaxLengthValidator(50)]
    )

    class Meta:
        fields = (
            "name",
            "description",
            "quantity",
        )

    def save(self, commint=True):

        returnedUser = thing.objects.create_user(
            name = self.cleaned_data.get('name'),
            description = self.cleaned_data.get('description'),
            quantity = self.cleaned_data.get('quantity')
        )

        return returnedUser
