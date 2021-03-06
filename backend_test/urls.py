from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

app_name = "adminUrls"

urlpatterns = [
    path('', include('how_to.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('keyval/', include('key_val_api.urls')),
    path('dogs/', include('dogs_api.urls')),
    path('schema/', get_schema_view(title='API Schema'), name='openapi-schema'),
    path('docs/', include_docs_urls(title='API Docs'), name='docs'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
