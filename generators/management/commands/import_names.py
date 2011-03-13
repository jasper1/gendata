import sys, os
import csv


from django.core.management.base import BaseCommand, CommandError
from generators.models import FirstName, Surname



class Command(BaseCommand):
    args = '<import_folder ...>'
    help = 'Import data from not normalized csv files'
    folder = 'raw_data'
    
    

    def handle(self, *args, **options):
        
        print "Process Firstnames"
        firstnames_db = os.path.abspath(os.path.join(self.folder,'firstnames.csv'))
        reader = csv.reader(open(firstnames_db,'rb'), dialect=csv.excel, delimiter=';', quotechar='"')
        for row in reader:
            name = row[0]
            gender = row[1]
            n = FirstName.objects.create(first_name=name, gender=gender)
            n.save()
        
        print "Process Surnames"
        surnames_db = os.path.abspath(os.path.join(self.folder,'surnames.csv'))
        reader = csv.reader(open(surnames_db,'rb'), dialect=csv.excel, delimiter=',', quotechar='"')
        for row in reader:
            surname = row[0]
            n = Surname.objects.create(surname=surname)
            n.save()
    