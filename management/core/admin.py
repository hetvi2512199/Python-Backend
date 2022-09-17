from django.contrib import admin
from core import models as core_models
# Register your models here.

admin.site.register(core_models.School)
admin.site.register(core_models.Collages)
admin.site.register(core_models.Student)
admin.site.register(core_models.Subject)
admin.site.register(core_models.Standard)
admin.site.register(core_models.Course)
admin.site.register(core_models.StudentDetails)


