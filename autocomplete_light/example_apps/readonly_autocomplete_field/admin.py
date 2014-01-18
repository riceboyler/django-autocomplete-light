from django.contrib import admin

import autocomplete_light

from .models import *


admin.site.register(RelatedModel)


for model in (TestFk, TestMtm, TestOto):
    ModelAdmin = type('%sModelAdmin' % model.__class__.__name__,
                      (admin.ModelAdmin,),
                      {'form': autocomplete_light.modelform_factory(model),
                       'readonly_fields': ['relation']})

    admin.site.register(model, ModelAdmin)
