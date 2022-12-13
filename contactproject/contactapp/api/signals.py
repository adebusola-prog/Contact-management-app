from ..models import Profile
from django.db.models.signals import post_save, post_delete, pre_save 
from django.dispatch import receiver
import inspect
from django_elasticsearch_dsl.registries import registry


@receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
   app_label= sender._meta.app_label
   model_name= sender._meta.model_name
   instance= kwargs['instance']

   if app_label == 'contactapp':
      if model_name == 'category':
         instances= instance.profile_set.all()
         for _instance in instances:
            registry.update(_instance)


@receiver(post_delete)
def delete_document(sender, **kwargs):
   app_label = sender._meta.app_label
   model_name= sender._meta.model_name
   instance= kwargs['instance']

   if app_label == 'contactapp':
      if model_name == 'category':
         instances= instance.profile_set.all()
         for _instance in instances:
            registry.update(_instance)