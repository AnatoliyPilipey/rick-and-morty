from django.db import models


class Character(models.Model):
    class StatusChoices(models.TextChoices):
        ALIVE = "Alive"
        DEAD = "Dead"
        UNKNOWN = "unknown"

    class GenderChoices(models.TextChoices):
        FEMALE = "Alive"
        MALE = "Dead"
        GENDERLESS = "Genderless"
        UNKNOWN = "unknown"

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=StatusChoices.choices,
        default=StatusChoices.UNKNOWN,
    )
    species = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=50,
        choices=GenderChoices.choices,
        default=GenderChoices.UNKNOWN,
    )
    image = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return self.name
