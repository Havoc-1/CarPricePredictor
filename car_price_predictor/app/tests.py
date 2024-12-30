from django.test import TestCase
from .models import Car

class CarModelTest(TestCase):

    def setUp(self):
        Car.objects.create(make="Toyota", model="Camry", year=2020, price=24000)
        Car.objects.create(make="Honda", model="Accord", year=2021, price=26000)

    def test_car_creation(self):
        toyota = Car.objects.get(make="Toyota")
        honda = Car.objects.get(make="Honda")
        self.assertEqual(toyota.model, "Camry")
        self.assertEqual(honda.price, 26000)

    def test_car_string_representation(self):
        car = Car(make="Ford", model="Mustang", year=2022, price=30000)
        self.assertEqual(str(car), "Ford Mustang")  # Assuming __str__ method is defined in the model

    def test_car_price_range(self):
        cars = Car.objects.all()
        prices = [car.price for car in cars]
        self.assertTrue(all(price > 0 for price in prices))  # Ensure all prices are positive