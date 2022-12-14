from django.shortcuts import render

from web.formularios.formularioMedico import FormularioMedico
from web.formularios.formularioPaciente import FormularioPaciente

from web.models import Medicos
from web.models import Pacientes

# Create your views here.
# Quier que python cuando lea la función Home me cargue el index
# Renderizar es PINTAR


def Home(request):
    return render(request, 'index.html')


def consultorioMedico(request):
    medicosConsultados=Medicos.objects.all()


    datosMedicos={
        "medicos":medicosConsultados

    }
    
    return render(request, 'consultoriomedico.html',datosMedicos)


def consultorioPaciente(request):
    pacientesConsultados=Pacientes.objects.all()


    datosPacientes={
        "pacientes":pacientesConsultados

    }
    
    return render(request,'consultoriopaciente.html',datosPacientes)


def MedicosVista(request):

    #Creamos una variable para controlar la ejecución de la alerta

    lanzandoAlerta = False

    # Debo utilizar la clase formularioMedico
    # Creamos entonces un objeto
    formulario = FormularioMedico()
    diccionario = {
        "formulario": formulario,
        "bandera":lanzandoAlerta
    }

    # Activar la recepción de datos

    if request.method == 'POST':
        # Validar si los datos son correctos
        datosRecibidos = FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            # Capturar los datos
            datos = datosRecibidos.cleaned_data
            # print(datos)
            # Llevar mis datos hacia la BD
            medicoNuevo = Medicos(
                nombre=datos["nombre"],
                apellido=datos["apellidos"],
                cedula=datos["cedula"],
                tarjetaprofesional=datos["tarjetaProfesional"],
                especialidad=datos["especialidad"],
                jornada=datos["jornada"],
                contacto=datos["contacto"],
                sede=datos["sede"],
            )
            medicoNuevo.save()
            diccionario["bandera"]=True
            #print("exito en la operación")

    return render(request, 'vistaprueba.html', diccionario)

def PacienteVista(request):
    # Debo utilizar la clase formularioMedico
    # Creamos entonces un objeto
    lanzandoAlertaP = False
    formularioP = FormularioPaciente()
    diccionarioP = {
        "formularioP": formularioP,
        "banderaP":lanzandoAlertaP
    }

    # Activar la recepción de datos

    if request.method == 'POST':
        # Validar si los datos son correctos
        datosRecibidosP = FormularioPaciente(request.POST)
        if datosRecibidosP.is_valid():
            # Capturar los datos
            datos = datosRecibidosP.cleaned_data
            # print(datos)
            # Llevar mis datos hacia la BD
            pacienteNuevo = Pacientes(
                nombre=datos["nombre"],
                apellido=datos["apellidos"],
                cedula=datos["cedula"],
                regimen=datos["regimen"],
                grupoingreso=datos["grupoingreso"],
                cuotamoderadora=datos["cuotaModeradora"],
                contacto=datos["contacto"],
                correo=datos["correo"],
            )
            pacienteNuevo.save()
            diccionarioP["banderaP"]=True
            #print("exito en la operación")

    return render(request, 'pacientes.html', diccionarioP)