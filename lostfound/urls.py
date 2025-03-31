from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lostfoundapp.urls')),  # Include your app URLs
]

if settings.DEBUG:  # Add Debug Toolbar URLs only when DEBUG is True
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))  # Debug toolbar path
    ]
