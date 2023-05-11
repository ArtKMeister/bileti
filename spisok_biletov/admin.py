from django.contrib import admin

from spisok_biletov.models import SpisokBiletov
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#admin.site.register(SpisokBiletov)
# Register your models here.

class SpisokBiletovResource(resources.ModelResource):

    class Meta:
        model = SpisokBiletov


class SpisokBiletovAdmin(ImportExportModelAdmin):
    resource_classes = [SpisokBiletovResource]

admin.site.register(SpisokBiletov, SpisokBiletovAdmin)
