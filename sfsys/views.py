from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import deathForm

installed_apps = ['sfsys']

def Homepage(request): 
	return render(request,'swfever.html')

def Tablelist(request):
	data = UserInfo.objects.all()
	data1 = DeathRecords.objects.all()

	return render(request, 'swfrecords.html',{'data':data, 'data1':data1})

    
def Swfrecordslist(request):
	if request.method == "POST":
		surname = request.POST['surname']
		firstname= request.POST['firstname']
		middleInitial= request.POST['middleInitial']
		email = request.POST['email']
		date = request.POST['date']
		region = request.POST['region']
		death = request.POST['death']
		data = UserInfo.objects.create(surname = surname,
		firstname = firstname,
		middleInitial = middleInitial,
		email= email,
		date= date,
		region = region,)
		data1 = DeathRecords.objects.create(Region = region, Date = date, Num_Deaths = death,)
		data1.save()
		data.save()

		return redirect('/Tablelist')


def updates1(request, id):
	death = DeathRecords.objects.get(id=id)
	form = deathForm(instance=death)
	if request.method == 'POST':
		form = deathForm(request.POST, instance = death)
		if form.is_valid():
			form.save()
			return redirect('/Tablelist')

	return render(request, 'swfupdate.html', {'form':form})
		
def delete(request, id):
    a = UserInfo.objects.get(id=id)
    for x in UserInfo.objects.only('id'):

        print(x)
        if a == x:
            d = "a"
            print(d)
            x = UserInfo.objects.get(id=id).delete()
            break
    return redirect('/Tablelist')

def delete1(request, id):
    a = DeathRecords.objects.get(id=id)
    for x in DeathRecords.objects.only('id'):

        print(x)
        if a == x:
            d = "a"
            print(d)
            x = DeathRecords.objects.get(id=id).delete()
            break
    return redirect('/Tablelist')






