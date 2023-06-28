from django.db import models

INSTITUTE_CATEGORY = (('Детский сад', 'Детский сад'),
                      ('Школа', 'Школа'),
                      ('Колледж', 'Колледж'),
                      ('ВУЗ', 'ВУЗ'),)

INSTITUTE_POSSESSIVENESS = (('Государственный', 'Государственный'),
                           ('Частный', 'Частный'))

REGIONS = (('Иссык-Кульская', 'Иссык-Кульская'),
           ('Нарынская', 'Нарынская'),
           ('Чуйская', 'Чуйская'),
           ('Таласская', 'Таласская'),
           ('Джалал-Абадская', 'Джалал-Абадская'),
           ('Ошская', 'Ошская'),
           ('Баткенская', 'Баткенская'),)


class Institute(models.Model):
    category = models.CharField(choices=INSTITUTE_CATEGORY, max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    possessiveness = models.CharField(choices=INSTITUTE_POSSESSIVENESS, max_length=100, null=True)
    region = models.CharField(choices=REGIONS, max_length=100, null=True)
    city_or_reg = models.CharField(max_length=100, default=True, null=True)

    def __str__(self):
        return self.title


class InstituteEvent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    organizer = models.ForeignKey('Institute', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


RATING = ((1, 1),
          (2, 2),
          (3, 3),
          (4, 4),
          (5, 5),)


class Review(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    rating = models.IntegerField(choices=RATING)
    related_to = models.ForeignKey('Institute', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

