from django.test import TestCase
from .models import productReceipe
from datetime import timedelta

class productReceipeTestCase(TestCase):
    def test_units_per_minute_and_units_per_hour_calculation(self):
        # Create a productReceipe instance with target_per_unit set to 1 minute
        recipe = productReceipe(
            product_Name="Example Product",
            stages=3,
            target_per_unit=timedelta(minutes=1),  # Use timedelta to represent 1 minute
            skill_matrix="Example Skills"
        )

        # Check if the units_per_minute and units_per_hour properties are correctly calculated
        self.assertEqual(recipe.units_per_minute, 60)  # 60 units per minute
        self.assertEqual(recipe.units_per_hour, 3600)  # 3600 units per hour