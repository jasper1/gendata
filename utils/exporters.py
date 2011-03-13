from django.http import HttpResponse
from django.core import serializers


#admin functions
def export_as_json(modeladmin, request, queryset):
    return export_as(modeladmin, request, queryset, 'json')
    
def export_as_yaml(modeladmin, request, queryset):
    return export_as(modeladmin, request, queryset, 'yaml')

def export_as_xml(modeladmin, request, queryset):
    return export_as(modeladmin, request, queryset, 'xml')

def export_as(modeladmin, request, queryset, export_type):
    response = HttpResponse(mimetype="text/javascript")
    serializers.serialize(export_type, queryset, stream=response)
    return response