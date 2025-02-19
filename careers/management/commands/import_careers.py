from django.core.management.base import BaseCommand
import csv
from careers.models import CareerPath, CareerDetail

class Command(BaseCommand):
    help = 'Import careers from a CSV file'

    def handle(self, *args, **options):
        file_path = 'careers.csv'

        with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            print("CSV Headers:", reader.fieldnames)

            for row in reader:
                print("Row Data:", row)
                if "name" not in row:
                    print("Error: 'name' column is missing!")
                    return
                
                career_name = row["name"].strip()
                career, created = CareerPath.objects.get_or_create(
                    name=career_name,
                    defaults={'category': row["category"].strip()}
                )
                if created:
                    CareerDetail.objects.create(
                        career=career,
                        category=row["category"].strip(),
                        description=row["description"].strip(),
                        required_courses=row["required_courses"].strip(),
                        salary_range=row["salary_range"].strip(),
                        top_colleges=row["top_colleges"].strip(),
                    )
                    self.stdout.write(self.style.SUCCESS(f"Added: {career_name}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Skipped (Already Exists): {career_name}"))

        self.stdout.write(self.style.SUCCESS("Career Import Completed!"))
