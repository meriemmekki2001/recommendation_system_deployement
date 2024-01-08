from django.core.management.base import BaseCommand
import pandas as pd
from product.models import AprioriResults

class Command(BaseCommand):
    help = 'Import data from Excel file to Django model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        
        df = pd.read_excel(file_path)
        df = df.replace({'frozenset': ''}, regex=True)
        df = df.applymap(lambda x: str(x).replace('({', ''))
        df = df.applymap(lambda x: str(x).replace('})', ''))
        df = df.applymap(lambda x: str(x).replace('\'', ''))
        

        
        for index, row in df.iterrows():
            AprioriResults.objects.create(
                  antecedents=row['antecedents'],
                  consequents=row['consequents'],
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))
