from django import forms


class SearchForm(forms.Form):
    Destination = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'half', 'placeholder': 'City'}))
    Date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'departure', 'placeholder': 'From...'}))
    Date2 = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'departure', 'placeholder': 'To..'}), label='')
    duration_in_days = forms.CharField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'From...'}))
    duration_in_days2 = forms.CharField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'To..'}), label='')
    price = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'From...'}))
    price2 = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'To..'}), label='')
    meals = forms.ChoiceField(required=False, choices=[('meals...', 'meals...'),('halfboard', 'halfboard'), ('fullboard', 'fullboard')], widget=forms.Select(attrs={'class': 'half'}))
    agency = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'half', 'placeholder': 'Agnecy Name...'}))

