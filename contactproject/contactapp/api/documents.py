from django_elasticsearch_dsl import Document, Index,  fields
from django_elasticsearch_dsl.registries import registry
from phonenumber_field.modelfields import PhoneNumberField
from ..models import Profile 

@registry.register_document
class ProfileDocument(Document):
   id= fields.IntegerField()
   first_name= fields.TextField(
      attr='first_name',
      fields={
         'raw': fields.TextField(),
         'suggest': fields.CompletionField(),

      }
   )

   last_name= fields.TextField(
      attr='last_name',
      fields={
         'raw': fields.TextField(),
         'suggest': fields.CompletionField(),
         
      }
   )

   profile_pics= fields.FileField()
   contact_image=fields.FileField()

   gender= fields.TextField(
      attr='gender',
      fields={
         'raw': fields.TextField(),
         'suggest': fields.CompletionField(),
         
      }
   )  

   # email= fields.EmailField()
   
   relationship= fields.TextField(
      attr='relationship',
      fields={
         'raw': fields.TextField(),
         'suggest': fields.CompletionField(),
         
      }
   )


   address= fields.TextField(
      attr='address',
      fields={
         'raw': fields.TextField(),
         'suggest': fields.CompletionField(),
         
      }
   )
   phone_number=PhoneNumberField()
   category= fields.ObjectField(
      attr= 'category',
      properties={
               'id': fields.IntegerField(),
               'name': fields.TextField(
                  attr='name',
                  fields={
                     'raw': fields.KeywordField(),
                  }
               )
         }
      )

   class Index:
      name= 'contactapp'

   class Django:
      model= Profile
      # fields= [ 
      #    'first_name',
      #    'last_name',
      #    'profile_pics',
      #    'contact_image',
      #    'gender',
         
      #    'favorites',
      #    'address'
      # ]

      def indexing(self):
         obj= ProfileDocument( 
            meta={'id': self.id},
            # first_name=self.first_name,
            last_name= self.last_name,
            gender=self.gender,
            profile_pics= self.profilepics,
            contact_image= self.contact_image,
            relationship=self.relationship,
            address= self.address,
            favorites=self.favorites,
            
         )

         obj.save()
         return obj.to_dict(include_meta=True)