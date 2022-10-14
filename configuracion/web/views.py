from django.shortcuts import render

# Create your views here.
#Quier que python cuando lea la función Home me cargue el index
#Renderizar es PINTAR
def Home(request):
    return render(request,'index.html')