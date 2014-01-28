from django.contrib import admin

import autocomplete_light

from .models import *
from . import forms


admin.site.register(RelatedModel)


class ReadonlyFieldsMixin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return ['relation'] if obj is not None and obj.pk else []

    def get_form(self, request, obj=None, **kwargs):
        kwargs['formfield_callback'] = autocomplete_light.FormfieldCallback()
        return super(ReadonlyFieldsMixin, self).get_form(request, obj, **kwargs)


for model in (TestFk, TestMtm, TestOto):
    attrs = {
        'readonly_fields': ['relation'],
    }

    ModelAdmin = type('%sModelAdmin' % model.__name__,
                      (ReadonlyFieldsMixin,), attrs)

    admin.site.register(model, ModelAdmin)
