from django.contrib import admin
from .models import Patient, Queue, Hospital

# Register your models here.
admin.site.site_title = 'NoQ'
admin.site.site_header = 'NoQ Admin'

class PatientStacked(admin.TabularInline):
    model = Patient
    fields = ['token','number','name','q']
    show_change_link = True
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    exclude = ['token','time']
    list_display = ('token','number','q','time',)
    list_filter = ('q__name','time')
    search_fields = ['token','number']

@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    list_display = ('name','active')
    inlines = [PatientStacked,]
