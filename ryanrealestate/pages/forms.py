from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Your Name',
        max_length=120,
        required=True
    )
    company = forms.CharField(
        label='Company/Organization',
        max_length=120,
        required=False,
    )
    email = forms.EmailField(
        label='Your Email',
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea,
        label='Message',
        required=True
    )