from django import forms
from spisok_biletov.models import SpisokBiletov

class DefaultSearch(forms.Form):
    name_out = forms.CharField(widget=forms.TextInput(attrs={'id': 'Gorod_v', 'placeholder': 'Владивосток'}))
    name_in = forms.CharField(widget=forms.TextInput(attrs={'id': 'Gorod_p', 'placeholder': 'Анталия'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'id': 'data', 'placeholder': 'ГГГГ-ММ-ДД'}))

    class Meta:
        model = SpisokBiletov
        fields = ('date', 'name_out', 'name_in')

class DataSearch(forms.Form):
    date_2 = forms.DateField(widget=forms.DateInput(attrs={'id': 'vspliv_data', 'placeholder': 'ГГГГ-ММ-ДД'}))

    class Meta:
        model = SpisokBiletov
        fields = ('date', 'price')

class GorodSearch(forms.Form):
    name_out_2 = forms.CharField(widget=forms.TextInput(attrs={'id': 'inp_vspliv_gorod_v', 'placeholder': 'Владивосток'}))
    name_in_2 = forms.CharField(widget=forms.TextInput(attrs={'id': 'inp_vspliv_gorod_p', 'placeholder': 'Анталия'}))

    class Meta:
        model = SpisokBiletov
        fields = ('name_out', 'name_in')