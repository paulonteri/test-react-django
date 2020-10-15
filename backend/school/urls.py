from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path('', TemplateView.as_view(template_name='index.html')),
    path('', include('frontend.urls')),
    path('', include('accounts.urls')),
    path('', include('library.urls')),
    path('', include('students.urls')),
    path('', include('academics.urls')),
    path('', include('examinations.urls')),
    path('', include('assignments.urls')),
    path('', include('mail.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
