from django.shortcuts import render

from web.formularios.formularioMedico import FormularioMedico

# Create your views here.
#Quier que python cuando lea la función Home me cargue el index
#Renderizar es PINTAR
def Home(request):
    return render(request,'index.html')

def Medicos(request):
    #Debo utilizar la clase formularioMedico
    #Creamos entonces un objeto
    formulario = FormularioMedico()
    diccionario={
        "formulario": formulario
    }

    #Activar la recepción de datos

    if request.method =='POST':
        #Validar si los datos son correctos
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #Capturar los datos
            datos=datosRecibidos.cleaned_data
            print(datos)

    return render(request,'vistaprueba.html',diccionario)