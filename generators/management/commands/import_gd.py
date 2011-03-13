import sys, os
import csv


from django.core.management.base import BaseCommand, CommandError
from generators.models import Country, City, Region



class Command(BaseCommand):
    args = '<import_folder ...>'
    help = 'Import data from not normalized csv files'
    folder = 'raw_data'
    
    

    def handle(self, *args, **options):
        countries = {}
        regions = {}
        
        print "Process countries"
        countries_db = os.path.abspath(os.path.join(self.folder,'countries.csv'))
        reader = csv.reader(open(countries_db,'rb'), dialect=csv.excel, delimiter=',', quotechar='"')
        for country in reader:
            c = Country.objects.get (country=country[1], country_code=country[0])
#            c.save()
            countries[country[0]] = c
        
#        print "Process regions"
#        regions_db = os.path.abspath(os.path.join(self.folder,'regions.csv'))
#        reader = csv.reader(open(regions_db,'rb'), dialect=csv.excel, delimiter=',', quotechar='"')
#        for region in reader:
#            c = countries[region[0].upper()]
#            r = Region.objects.create(country=c, region=region[2], region_code=region[1])
#            r.save()

        
        print "Process cities"
        cities_db = os.path.abspath(os.path.join(self.folder,'worldcitiespop_utf.txt'))
        fh = open(cities_db,'rb') 
        reader = csv.reader(fh, dialect=csv.excel, delimiter=',', quotechar='"')
        
#        print countries
        
        # Total 2 700 000
        counter = 0 
        total_counter = 0
        for city in reader:
            counter += 1
            if counter == 100:
                total_counter += counter
                counter = 0
                print total_counter
                
            if total_counter<2013100:
                continue
            
            city_ascii = city[1][:79]
            city_name  = city[2][:79]
            population = int(city[4] if not len(city[4])==0 else 0)
            latitude = float(city[5])
            longitude = float(city[6])

            try:
                c = countries[city[0].upper()]
#                c = Country.objects.get(country_code=city[0])
                region = None
                try:
                    region = Region.objects.get(country=c, region_code=city[3])
                except:
                    pass
                
                city_obj = City.objects.create(country=c,
                                               region=region,
                                               ASCIIcity=city_ascii,
                                               city=city_name,
                                               population=population,
                                               latitude=latitude,
                                               longitude=longitude)
                city_obj.save()
            except:
                print "Pass %s" % city_ascii
                print sys.exc_info()
                sys.exit()

                    
            
            
        
    