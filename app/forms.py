from django import forms


class po(forms.Form):
    your_name = forms.CharField(
        label='名前',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )