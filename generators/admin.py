from django.contrib import admin
from generators.models import Country, City, Region
from generators.models import FirstName, Surname

from utils.exporters import export_as_json, export_as_xml, export_as_yaml


# Admin classes for geo information
class CountryAdmin(admin.ModelAdmin):
#    fields = ('country',) # Visible control in edit form
    list_display = ['country', 'country_lang_key', 'zip_format'] # Visible in table list

#    prepopulated_fields = {"country": ("zip_format",)} # ???
#    list_filter = ['country',] # Set right side filters
#    list_editable = ['country','zip_format'] # in table editor
#    list_display_links = list_display # Links settings
#    actions = [export_as_json, export_as_yaml, export_as_xml] # Local commands for current model 
    
#    Settings for global override widget by fieldtype
#    formfield_overrides = {
#        models.CharField: {'widget':CheckboxInput},
#     }
    
#    save_on_top = True # ??
#    list_filter = ['country', 'zip_format']
#    search_fields = ['id', 'country', 'country_lang_key', 'zip_format']
    
#    fieldsets = (
#        (None, {
#            'classes': ('wide',),
#            'description':'Main <b>country</b> definitions',
#            'fields': ('country',)
#        }),
#        ('Advanced options', {
#            'classes': ('wide',),
#            'fields': ('country_lang_key','zip_format',)
#        }),
#    )

#    actions_on_bottom = True # Enable toolbar for table in bottom side
#    actions_selection_counter = True # Enable or disable selections counter

#    def get_actions(self, request):
#        actions = super(CountryAdmin, self).get_actions(request)
#        print request
#        if request.user.username[0].upper() != 'J':
#            del actions['delete_selected']
#        return actions


#from django.conf.urls.defaults import patterns
#from django.http import HttpResponse

class CityAdmin(admin.ModelAdmin):
#    actions = None # for disable all actions in model
    list_display = ['city', 'country', 'region','get_links']
#    raw_id_fields = ("country",) # For FK or M2M - set widget to ID selector
#    save_as = False # Change "Save and add anouther" to "Save New" button 
#    save_on_top = True # Allow save bar to top side
#    search_fields = ['country__country']
    
    
    
#    def get_urls(self):
#        print "GET URLS"
#        urls = super(CityAdmin, self).get_urls()
#        my_urls = patterns('',
#            (r'^my_view/$', self.my_view)
#        )
#        return my_urls + urls
#
#    def my_view(self, request):
#        return HttpResponse("ZAEBAL!!!!")
    

class RegionAdmin(admin.ModelAdmin):
    pass

class FirstNameAdmin(admin.ModelAdmin):
    pass

class SurnameAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Region, RegionAdmin)

admin.site.register(FirstName, FirstNameAdmin)
admin.site.register(Surname, SurnameAdmin)

# Global commands 
admin.site.add_action(export_as_json, 'Export as JSON')
admin.site.add_action(export_as_yaml, 'Export as YAML')
admin.site.add_action(export_as_xml,  'Export as XML')