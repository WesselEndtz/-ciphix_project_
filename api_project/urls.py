from django.urls import path
from django.contrib import admin
from core import views as core_views
from rest_framework import routers
from django.conf.urls.static import static
from api_project import settings


router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('txt_sentiment/', core_views.SentimentAPIView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
