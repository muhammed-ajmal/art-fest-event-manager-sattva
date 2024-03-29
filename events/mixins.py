import csv
from django.http import HttpResponse

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) if field != 'branch' and field != 'semester' and field != 'slot'  else getattr(obj, 'get_branch_display')() if field != 'semester' and field != 'slot'  else getattr(obj, 'get_semester_display')() if field != 'slot' else getattr(obj, 'get_slot_display')() for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected"
