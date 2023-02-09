from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('search', views.search, name="search"),
    path('about', views.about_us, name="about"),
    path('agents', views.navbar, name="agent"),
    path('pricing', views.pricing, name="pricing"),
    path('profile/<str:user>', views.profile, name="profile"),
    path('contact', views.contact, name="contact"),
    path('detail/<int:id>', views.property_detail, name="detail"),
    path('edit-profile/<str:id>', views.edit_profile, name="edit-profile"),
] 

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)