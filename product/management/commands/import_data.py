from django.core.management.base import BaseCommand
import pandas as pd
from product.models import Product

class Command(BaseCommand):
    help = 'Import data from Excel file to Django model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        
        df = pd.read_excel(file_path)
        df = df[df.Country == 'France']
        df['Description'] = df['Description'].str.strip()
        df = df[df.Quantity >0]
        df = df.drop_duplicates(subset='StockCode', keep='first')

        
        for index, row in df.iterrows():
            Product.objects.create(
                  title=row['Description'],
                  stock_code=row['StockCode'],
                  price=row['UnitPrice']
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))
