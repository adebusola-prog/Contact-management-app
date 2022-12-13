from django.urls import path
from contactapp.api import views
from rest_framework import routers


router = routers.SimpleRouter(trailing_slash=False)


router.register('profile-search', views.ProfileDocumentView,
   basename= 'profile-search'
)

urlpatterns=[ 
   path('api/list', views.ProfileListCreate.as_view(), name='list_create'),
   path('api/detail/<int:pk>', views.ProfileRetrieveUpdateDestroy.as_view(), name='detail_update'),
   path('api/category', views.CategoryList.as_view(), name='category_list'),

]

   


urlpatterns += router.urls