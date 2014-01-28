from django.contrib import admin

import autocomplete_light

from .models import *
from . import forms


admin.site.register(RelatedModel)


class ReadonlyFieldsModelAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return ['relation'] if obj is not None and obj.pk else []

    def get_form(self, request, obj=None, **kwargs):
        kwargs['formfield_callback'] = autocomplete_light.FormfieldCallback()
        return super(ReadonlyFieldsModelAdmin, self).get_form(request, obj, **kwargs)


for model in (TestFk, TestMtm, TestOto):
    ModelAdmin = type('%sModelAdmin' % model.__name__,
                      (ReadonlyFieldsModelAdmin,), attrs)

    admin.site.register(model, ModelAdmin)
