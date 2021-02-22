from django import forms


class CreateNewListForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    check = forms.BooleanField(required=False)
