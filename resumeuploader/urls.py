from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = " ProbeQ "
admin.site.site_title = "ProbeQ Administrator "
admin.site.index_title = "Welcome to ProbeQ Adminstrator"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>', views.CandidateView.as_view(), name='candidate')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)