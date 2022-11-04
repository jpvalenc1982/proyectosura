from django import forms
class FormularioMedico(forms.Form):

    ESPECIALIDADES=(
        (1,'Cardiología'),
        (2,'Medicina Interna'),
        (3,'Medico General'),
        (4, 'Ortopedia'),
        (5, 'Pediatria')
    )
    JORNADAS=(
        (1,'6:00 AM - 2:00 PM'),
        (2, '2:00 PM - 10:00 PM'),
        (3, '10:00 PM - 6:00 AM')
    )
    SEDES=(
        (1,'Almacentro'),
        (2,'Punto Clave'),
        (3,'Molinos')


        
    )
    nombre=forms.CharField(
        widget=forms.TextInput(attrs={"":"form-control mb-3"}),
        required=True,
        max_length=15
    )    
    apellidos=forms.CharField(
        widget=forms.TextInput(attrs={"":"form-control mb-3"}),
        required=True,
        max_length=35
    )
    cedula=forms.CharField(
        widget=forms.TextInput(attrs={"":"form-control mb-3"}),
        required=True,
        max_length=10
    )
    tarjetaProfesional=forms.CharField(
        widget=forms.TextInput(attrs={"":"form-control mb-3"}),
        required=True,
        max_length=20
    )
    especialidad=forms.ChoiceField(
        widget=forms.Select(attrs={"":"form-select mb-3"}),
        required=True,
        choices=ESPECIALIDADES
    )
    jornada=forms.ChoiceField(
        widget=forms.Select(attrs={"":"form-select mb-3"}),
        required=True,
        choices=JORNADAS

    )
    contacto=forms.CharField(
        widget=forms.NumberInput(attrs={"":"form-control mb-3"}),
        required=True,
        max_length=20
    )
    sede =forms.ChoiceField(
        widget=forms.Select(attrs={"":"form-select mb-3"}),
        required=True,
        choices=SEDES
    )