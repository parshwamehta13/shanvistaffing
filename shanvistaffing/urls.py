"""shanvistaffing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings 
from recruitment.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name='index'),
    url(r'^joblist/$',joblist,name='joblist'),
    url(r'^joblist/(?P<job_id>[0-9]+)$',jobpage,name='jobpage'),
    url(r'^login/$',login_view,name='login'),
    url(r'^update/$',update_information,name='update_information'),
    url(r'^signup/$',signup,name='signup'),
    url(r'^requirement/$',requirement,name='requirement'),
    url(r'^logout/$',logout_view,name='logout'),
    url(r'^apply/(?P<job_id>[0-9]+)$',apply_job,name='apply_job'),
    url(r'^changepass/$',change_password,name='change_password'),
    url(r'^applcation_tracking_system/$',app_tracking_sys,name='app_tracking_sys'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
