from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import login, logout
from chat.views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index),
    path('accounts/login/', login),
    path('accounts/logout/', logout),
    path('admin/', admin.site.urls),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
