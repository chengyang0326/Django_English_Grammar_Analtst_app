from django.urls import path,include

from . import views
from django.views.generic.base import TemplateView
from accounts import views as v
from . views import register
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
   
    path("create", TemplateView.as_view(template_name="create.html"), name="create"),
    path("<int:id>",views.index, name = "index"),
    path("create/", views.create, name="index"),
    path("signup/", register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include("django.contrib.auth.urls")),
    path("upload/",views.model_form_upload,name="upload")
]


if settings.DEBUG:
    urlpatterns+= static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)