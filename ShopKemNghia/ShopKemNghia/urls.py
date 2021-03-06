"""ShopKemNghia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include

from contact import views as contact_views
from profiles import views as profiles_views
from checkout import views as checkout_views
from products import views as products_views
from cart import views as cart_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profiles_views.home, name='home'),
    url(r'^about/$', profiles_views.about, name='about'),
    url(r'^profile/$', profiles_views.user_profile, name='profile'),
    url(r'^checkout/$', checkout_views.checkout, name='checkout'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^products/$', products_views.products, name='products'),
    url(r'^cart/$', cart_views.cart, name='cart'),
    # url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    # url(r'^auth/', include('django.contrib.auth.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns == static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns == static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
