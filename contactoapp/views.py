from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
# Create your views here.

def home (request):
    return render (request,'static/home.html',{})


def contacto(request):
    if request.method =="POST":
        
        name=request.POST["name"]
        subject=request.POST["subject"]
        message=request.POST["message"] + " " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["oalonso222@gmail.com"]
        send_mail=(name, subject, message, email_from, recipient_list)

        email_from=EmailMessage('mensaje desde app django ',"el usuario con el nombre {}  con la direccion de correo {} te escribe este mensaje:\n \n{}" .format(name,email_from,subject),"",["oalonso222@gmail.com"],reply_to= [email_from])
        try:
            email_from.send()

            return redirect("section5/contacto/?enviado")#usamos e importamos  redirect para que envie la confirmacion de envio del formulario al url de contacto
        except:
              return redirect("section5/contacto/?noenviado")

    return render(request,"static/home.html/contacto")




