import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open("phones.csv", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                Phone.objects.update_or_create(
                    id=row["id"],
                    defaults={
                        "name": row["name"],
                        "image": row["image"],
                        "price": int(row["price"]),
                        "release_date": row["release_date"],
                        "lte_exists": row["lte_exists"] == "True",
                    }
                )