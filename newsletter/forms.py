from django import forms 
from .models import Subscribe


class EmailSubscribeForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Enter your email",
    }), label="")

    class Meta:
        model = Subscribe
        fields = ('email', )
