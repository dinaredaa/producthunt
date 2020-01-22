from django.urls import path, include
from django.contrib import admin
from products import views

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls'))
]
