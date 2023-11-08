from django import forms

class SearchForm(forms.Form):
    search_lab = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search...'})
    )