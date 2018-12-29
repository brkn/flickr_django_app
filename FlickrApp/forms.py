from django import forms


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=95, widget=forms.TextInput(attrs={'placeholder': 'kittens and puppies'}))
