from django import forms


class FormularioPaciente(forms.Form):

    REGIMEN = (
        (1, 'Contributivo'),
        (2, 'Subsidiado')
    )
    GRUPOINGRESO = (
        (1, 'A'),
        (2, 'B'),
        (3, 'C')
    )

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
        required=True,
        max_length=15
    )
    apellidos = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
        required=True,
        max_length=35
    )
    cedula = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mb-3"}),
        required=True,
        max_length=10
    )
    regimen = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-select mb-3"}),
        required=True,
        choices=REGIMEN
    )
    grupoingreso = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-select mb-3"}),
        required=True,
        choices=GRUPOINGRESO
    )
    cuotaModeradora = forms.CharField(
        widget=forms.NumberInput(attrs={"class": "form-control mb-3"}),
        required=True,
        max_length=20
    )
    contacto = forms.CharField(
        widget=forms.NumberInput(attrs={"class": "form-control mb-3"}),
        required=True,
        max_length=20
    )
    correo = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "form-control mb-3"}),
        required=True,
        max_length=30
    )