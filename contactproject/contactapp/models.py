from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.
class Category(models.Model):
   name=models.CharField(max_length=100)

   class Meta:
      verbose_name_plural= "Categories"

   def __str__(self):
      return self.name

GENDER=(
   ('female', 'female'),
   ('male', 'male'),
)
class Profile(models.Model):
   first_name=models.CharField(max_length=200, null=False, blank=False)
   last_name= models.CharField(max_length=200, null=False, blank=False)
   profile_pics=models.ImageField(upload_to='images', blank=True, null=True)
   contact_image=models.ImageField(upload_to='images', blank=True, null=True)
   phone_number=PhoneNumberField(blank=True, unique=True)
   gender=models.CharField(max_length=20, choices=GENDER, default='female')
   email=models.EmailField()
   favorites=models.BooleanField(default=False)
   relationship=models.CharField(max_length=200)
   address=models.TextField(blank=True, null=True)
   category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) 

   def __str__(self):
      return self.first_name + " " + self.last_name

   @property
   def image_URL(self):
      try:
         url= self.profile_pics.url
      except:
         url= ''
      return url
   
   class Meta:
      ordering=['favorites']


   
class QrCode(models.Model):
   name= models.CharField(max_length=200, blank=False, null=True)
   qr_id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   qr_code= models.ImageField(upload_to='qr_codes', blank=True, null=True)


   def __str__(self):
      return str(self.qr_id)


   def save(self, *args, **kwargs):
      qrcode_img= qrcode.make(self.name)
      canvas= Image.new('RGB', (290, 290), 'white')
      draw= ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      fname= f'qr_code-{self.name}.png'
      buffer= BytesIO()
      canvas.save(buffer, 'PNG')
      self.qr_code.save(fname, File(buffer), save=False)
      canvas.close()
      super().save(*args, **kwargs)
      

