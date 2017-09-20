from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views

import salas.views
import salas.urls

urlpatterns = [
    url(r'', include(salas.urls)),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', salas.views.usuarios_lista),
]
