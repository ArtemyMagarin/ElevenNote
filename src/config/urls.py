
from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
	path('', RedirectView.as_view(url='notes/')),
    path('api/', include('api.urls', namespace='api')),
    path('admin/', admin.site.urls),

    # TODO: remove it later
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
