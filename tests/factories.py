from datetime import date, timedelta

import factory

from ads.models import Category
from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = factory.Faker('name')
    slug = factory.Faker('ean', length=8)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    birth_date = date.today() - timedelta(days=5000)