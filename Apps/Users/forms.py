from django import forms
from .models import Cliente

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982','1983']
DOCUMENT_CHOICES = ['Document', 'PASSPORT']

class RawClienteForm(forms.Form):
    CliNom = forms.CharField(
        initial='name',
        max_length=100,
        label='Name',
    )
    CliEma = forms.EmailField(
        label='Email',
    )
    CliPas = forms.CharField(
        label='Password',
        max_length=100,
        widget=forms.PasswordInput(),
        )
    CliNumTel = forms.IntegerField(
        label='CellPhone',
        widget=forms.NumberInput(
        )
    )
    CliTipDoc = forms.CharField(
        label='Document Type',
    )
    CliNumDoc = forms.IntegerField(
        label='Document Num',
    )
    CliFecCum = forms.DateField(
        label='Date Birthday', 
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),
        )
    CliHueDig = forms.ImageField(
        label='Huella Digital',
    )
    CliMemCod = forms.IntegerField(
        label='Membresia Number',
    )
    CliMemIni = forms.DateField(
        label='Membresia Inicio',
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),
    )
    CliMemFin = forms.DateField(
        label='Menbresia Fin',
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),
    )

class RawInstructorForm(forms.Form):
    InsCod = forms.IntegerField()
    InsNom = forms.CharField(max_length=100)
    InsEma = forms.EmailField()
    InsPas = forms.CharField(max_length=100)
    InsTipDoc = forms.IntegerField()
    InsNumDoc = forms.IntegerField()
    InsNumTel = forms.IntegerField()
    InsFecCum = forms.DateField()
    InsHueDig = forms.ImageField()
    InsFecIni = forms.DateField()


