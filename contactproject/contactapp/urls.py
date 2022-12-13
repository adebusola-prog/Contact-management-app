from django.urls import path
from . import views

urlpatterns=[
   path('', views.contact_list, name="contact_list"),
   path('add-contact', views.add_contact, name="add_contact"),
   path('delete-list/<int:pk>', views.delete_list, name="delete_contact"),
   path('contact-profile/<int:pk>', views.contact_profile, name="contact_profile"),
   path('edit-profile/<int:pk>', views.edit_profile, name="edit_profile"),
   path('category/<int:pk>', views.categories, name="categories"),
   path('upload-csv', views.contact_upload, name="contact_upload"),
   path('download-csv', views.contact_download, name='contact_download'), 
   path('qr-view', views.qr_view, name='qr_code')
]

