from django.db import models
#from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

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


# class CustomUserManager(BaseUserManager):
#     def _create_user(self, email, password, first_name, last_name, phone_num, **extra_fields):
#         if not email:
#             raise ValueError("Email must be provided")
#         if not password:
#             raise ValueError('Password is not provided')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             first_name=first_name,
#             last_name=last_name,
#             mobile=phone_num,
#             **extra_fields
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)
#
#     def create_superuser(self, email, password, first_name, last_name, mobile, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)
#
#
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(db_index=True, unique=True, max_length=100)
#     first_name = models.CharField(max_length=100, blank=True, default='')
#     last_name = models.CharField(max_length=100, blank=True, default='')
#     phone_num = models.CharField(max_length=20)
#
#     is_staff = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['phone_num']
#
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
