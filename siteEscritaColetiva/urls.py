from django.conf.urls import url, include, handler400, handler403, handler404, handler500
from django.contrib import admin
import django.contrib.auth.views

import salas.views
import salas.urls

''' handler400 = 'salas.views.bad_request'
handler403 = 'salas.views.permission_denied'
handler404 = 'salas.views.page_not_found'
handler500 = 'salas.views.server_error' '''

urlpatterns = [
    url(r'', include(salas.urls)),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', salas.views.usuarios_lista),
]
