# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Productor, ProductoCorrida, ProductoCampo, Huerto, Empleado, Producto, Usuario, Calibre

admin.site.register(Productor)
admin.site.register(ProductoCampo)
admin.site.register(Huerto)
admin.site.register(Empleado)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Calibre)
admin.site.register(ProductoCorrida)

# Register your models here.
