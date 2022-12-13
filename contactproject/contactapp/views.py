from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Profile, Category, QrCode
from .forms import ProfileForm
import csv, io

# Create your views here.


def contact_list(request):
   no_of_contacts= Profile.objects.count()
   no_male= Profile.objects.filter(gender='male').count()
   no_female= Profile.objects.filter(gender='female').count()
   no_favorites= Profile.objects.filter(favorites=True).count()
   contact_list= Profile.objects.all()
   categories=Category.objects.all()
   context={'contact_list': contact_list, 'category':categories, 'no_male': no_male, 
   'no_female': no_female, 'no_favorites': no_favorites, 'no_of_contacts': no_of_contacts}
   return render(request, 'contactapp/index.html', context)

def contact_profile(request, pk):
   profile= Profile.objects.get(pk=pk)
   return render(request, 'contactapp/contact-profile.html', {'profile': profile})


def edit_profile(request, pk):
   profile= Profile.objects.get(pk=pk)
   
   if request.method=="POST":
      profile.first_name= request.POST['first_name']
      profile.last_name= request.POST['last_name']
      profile.relationship= request.POST['relationship']
      profile.email= request.POST['email']
      profile.phone_number= request.POST['phone_number']
      profile.address= request.POST['address']
      profile.save() 
      return redirect('contact_list')

   context={'profile': profile}

   return render(request, 'contactapp/edit.html', context)

def add_contact(request):
   form= ProfileForm()

   if request.method=="POST":
      form= ProfileForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
      return redirect('/')
   else:
      form=ProfileForm()
      context={'form': form}
   return render(request, 'contactapp/contact_create.html', context)


def delete_list(request, pk):
   obj= Profile.objects.get(pk=pk)
   if request.method =="POST":
      obj.delete()
      return redirect('contact_list')

   context={'obj': obj}
   return render(request, 'contactapp/delete.html', context)

def categories(request, pk):
   category=Category.objects.filter(id=pk).first()
   # or category=Category.objects.get(id=pk)

   return render(request, 'contactapp/category.html', {'category': category})

def contact_upload(request):
   template="contactapp/contact_upload.html"

   prompt={
      'order': 'Order of csv should be first_name, last_name, phone_number, email', 
   }
   if request.method=="GET":
      return render(request, template, prompt)

   csv_file= request.FILES['file']
   if not csv_file.name.endswith('.csv'):
      messages.error(request, 'This is not a csv file')

   data_set= csv_file.read().decode('UTF-8')
   io_string=io.StringIO(data_set)
   next(io_string)
   for column in csv.reader(io_string, delimiter=',', quotechar="|"):
      created=Profile.objects.update_or_create(
         first_name=column[0],
         last_name=column[1],
         address=column[2],
         email=column[3],
         phone_number=column[4]
      )
   context= {}
   return render(request, template, context)


def contact_download(request):
   items = Profile.objects.all()

   response= HttpResponse(content_type='text/csv')
   response['Content-Disposition'] ='attachment; filename="contact.csv"'

   writer= csv.writer(response, delimiter=',')
   writer.writerow(['first_name', 'last_name', 'address', 'email', 'phone_number'])

   for obj in items:
      writer.writerow([obj.first_name, obj.last_name, obj.address, obj.email, obj.phone_number])

   return response


def qr_view(request):
   name= "Welcome to"

   obj= QrCode.objects.get(name='code1')
   context= {
      'name': name,
      'obj': obj,
   }
   return render(request, 'contactapp/qrcode.html', context)