from django.http import JsonResponse
from django.shortcuts import render, redirect
from Register2.models import Person, NumberPhone


def mains(request):
    numberPhone = NumberPhone.objects.all()
    return render(request, 'Register\mains.html', {'numberPhones':numberPhone})

def deleteId(request):
    Person.objects.filter(id=request.POST['idHidden']).delete()
    return redirect(mains)

def update(request, id):
    numberPhone = NumberPhone.objects.get(person_id=id)
    person = Person.objects.get(id=id)
    if(request.GET['lastName']):
        person.lastName = request.GET['lastName']

    if(request.GET['firstName']):
        person.firstName = request.GET['firstName']

    person.save()
    #numberPhone.person = person

    if(request.GET['number']):
        numberPhone.number = request.GET['number']
    numberPhone.save()
    return redirect(mains)

def insert(request):
    return render(request, 'Register\insert.html')

def personId(request, id):
    numberPhone=NumberPhone.objects.get(person_id=id)
    return render(request, 'Register\personId.html', {'numberPhone': numberPhone})


def redirects(request):
    if request.POST['lastName']!="":
        person = Person()
        person.lastName = request.POST['lastName']
        person.firstName = request.POST['firstName']
        person.save()
        numberPhone = NumberPhone()
        numberPhone.number = request.POST['number']
        numberPhone.person = person
        numberPhone.save()

    return redirect(mains)