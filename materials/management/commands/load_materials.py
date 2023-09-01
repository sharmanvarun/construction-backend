
import json
from django.core.management.base import BaseCommand
from materials.models import Material

class Command(BaseCommand):
    help = 'Load materials data from a JSON file'

    def handle(self, *args, **kwargs):
        with open('/Users/varunsharman/construction-materials-backend/material_backend/materials/management/commands/material_list.json', 'r') as json_file:
            materials_data = json.load(json_file)

        for material_data in materials_data:
            Material.objects.create(
                name=material_data['name'],
                description=material_data['description'],
                amount=material_data['amount']
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded materials data'))
