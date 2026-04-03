import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = "Загружает данные из phones.csv в модель Phone"

    def handle(self, *args, **options):
        file_path = "phones.csv"
        try:
            with open(file_path, encoding="utf-8") as file:
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
            self.stdout.write(self.style.SUCCESS(f"Данные успешно загружены из {file_path}"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Файл {file_path} не найден!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка: {e}"))