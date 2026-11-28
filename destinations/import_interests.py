
import os
import sys
import django
import pandas as pd

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from destinations.models import Place, Interest

file_path = r"C:\Users\HP_OS 11\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\sessions\C84DE90C3CD7464527E15EF96761A2EA3ECD4018\transfers\2026-48\attraction.csv"

df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()

for _, row in df.iterrows():

    place, created = Place.objects.update_or_create(
        id=int(row['attraction_id']),
        defaults={
            'name': row['attraction_name'],
            'country': row['attraction_country'],
            'address': row['attraction_address'],
            'region': row['attraction_region'],
            'city': row['attraction_city'],
            'continent': row['attraction_continent'],
            'rating': float(row['attraction_rating']),
        }
    )

    interest = Interest.objects.get(
        id=int(row['attracion_type'])
    )

    place.interests.add(interest)

print("Attractions imported successfully!")
