from django.urls import path,include
from.import views
urlpatterns=[
    path('new',views.Testfn,name="new"),
    path('html1',views.html1)
]