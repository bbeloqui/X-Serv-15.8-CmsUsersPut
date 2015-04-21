
from django.shortcuts import render
from models import Table
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def login(request):
	if request.user.is_autehticated ():
		return	 ("<br>You're: " + request.user.username +"<br><a href='/admin/logout/'>Logout</a>")	
	else:		
		return ("<br>You aren't registred\n<a href='/admin/'>Login</a>")
	
def todo(request):
	list= Table.objects.all()
	out = "<ul>\n"
	for i in list:
		out += "<li><a href=agenda/" + i.name + ">" + i.name + "</a></li>\n"
	out += "</ul>\n"
	out += login(request)
	return HttpResponse(out)

@csrf_exempt

def numero(request, recuerso):
	if request.method == "GET":
		list = Table.objects.filter(name = recurso)
		if not list:
			return notfound(request, recuerso)
		out = " "
		for i in list:
			out += i.name + ": " + str(i.numero)
	if request.method == "PUT":
		if request.user.is_authenticated():
			new = Table(name=recuerso, numero=request.body)
			new.save()
			out = ("Se guardo la pagina, haz un check")
		else:
			out = ("Tienes queregistrarte")
	out += login(request)
	return HttpResponse(out)
