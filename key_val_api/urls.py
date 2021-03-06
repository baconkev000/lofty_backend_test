from django.urls import path
from . import views
from rest_framework.documentation import include_docs_urls

app_name='keyval'

urlpatterns = [
    path('list/', views.KeyValueList.as_view(), name='list'),
    path('create/', views.CreateKeyVal.as_view(), name='create-keyval'),
    path('view/<keyName>/', views.GetKeyVal.as_view(), name='kv-detail'),
    path('inc/<keyName>/', views.IncrementKeyVal.as_view(), name='inc-key'),
    path('delete/<keyName>/', views.KeyValDeleteByKeyName.as_view(), name='deletekey'),
    path('docs/', include_docs_urls(title='API Docs'), name='docs'),
]
