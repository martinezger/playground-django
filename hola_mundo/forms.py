from django import forms


class BuscarPersonasForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=20)