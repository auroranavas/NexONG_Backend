from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator, URLValidator
from django.utils import timezone 

# Create your models here.

ADMIN = 'ADMIN'
EDUCATOR = 'EDUCATOR'
VOLUNTEER = 'VOLUNTEER'
FAMILY = 'FAMILY'
PARTNER = 'PARTNER'
VOLUNTEER_PARTNER= 'VOLUNTEER_PARTNER'
ROLE = [
    (ADMIN, 'Administrador'),
    (VOLUNTEER, 'Voluntario'),
    (EDUCATOR, 'Educador'),
    (FAMILY, 'Familia'),
    (PARTNER, 'Socio'),
    (VOLUNTEER_PARTNER, 'Voluntario y socio'),
]
PENDING = 'PENDING'
ACCEPTED = 'ACCEPTED'
REJECTED = 'REJECTED'
STATUS = [
    (PENDING, 'Pendiente'),
    (ACCEPTED, 'Aceptado'),
    (REJECTED, 'Rechazado'),
]
ANNUAL = 'ANNUAL'
MENSUAL = 'MENSUAL'
QUARTERLY = 'QUARTERLY'
SIXMONTHLY = 'SIX-MONTHLY'
FRECUENCY = [
    (ANNUAL, 'Anual'),
    (MENSUAL, 'Mensual'),
    (QUARTERLY, 'Trimestral'),
    (SIXMONTHLY, ' Seis Meses'),
]
THREE_YEARS = 'THREE_YEARS'
FOUR_YEARS = 'FOUR_YEARS'
FIVE_YEARS = 'FIVE_YEARS'
FIRST_PRIMARY = 'FIRST_PRIMARY'
SECOND_PRIMARY = 'SECOND_PRIMARY'
THIRD_PRIMARY = 'THIRD_PRIMARY'
FOURTH_PRIMARY = 'FOURTH_PRIMARY'
FIFTH_PRIMARY = 'FIFTH_PRIMARY'
SIXTH_PRIMARY = 'SIXTH_PRIMARY'
FIRST_SECONDARY = 'FIRST_SECONDARY'
SECOND_SECONDARY = 'SECOND_SECONDARY'
THIRD_SECONDARY= 'THIRD_SECONDARY'
FOURTH_SECONDARY= 'FOURTH_SECONDARY'
CURRENT_EDUCATION_YEAR=[
    (THREE_YEARS, 'Tres años'),
    (FOUR_YEARS, 'Cuatro años'),
    (FIVE_YEARS, 'Cinco años'),
    (FIRST_PRIMARY, 'Primero de primaria'),
    (SECOND_PRIMARY, 'Segundo de primaria'),
    (THIRD_PRIMARY, 'Tercero de primaria'),
    (FOURTH_PRIMARY, 'Cuarto de primaria'),
    (FIFTH_PRIMARY, 'Quinto de primaria'),
    (SIXTH_PRIMARY, 'Sexto de primaria'),
    (FIRST_SECONDARY, 'Primero de secundaria'),
    (SECOND_SECONDARY, 'Segundo de secundaria'),
    (THIRD_SECONDARY, 'Tercero de secundaria'),
    (FOURTH_SECONDARY,'Cuarto de secundaria'), 
]

ZERO_TO_ONE = 'ZERO_TO_ONE'
ONE_TO_FIVE = 'ONE_TO_FIVE'
ZERO_TO_TEN = 'ZERO_TO_TEN'
GRADESYSTEM = [
    (ZERO_TO_ONE, '0-1'),
    (ONE_TO_FIVE, '1-5'),
    (ZERO_TO_TEN, '0-10'),
    
]
DIARY = 'DIARY'
ANNUAL = 'ANNUAL'
EVALUATION_TYPE = [
    (DIARY, 'Diario'),
    (ANNUAL, 'Anual'),
]
class Family(models.Model):
    name = models.CharField(max_length=255)
    documents = models.CharField(max_length=250)

class Partner(models.Model):
    holder = models.CharField(max_length=50, unique=True)
    iban = models.CharField(max_length=34, unique=True)
    quantity = models.IntegerField(default=0 ,validators=[
        MinValueValidator(0)])
    frecuency = models.CharField(max_length=11,choices=FRECUENCY, default=MENSUAL)
    total = models.FloatField(default = 0.0, validators=[
        MinValueValidator(0)])
    documents = models.CharField(max_length=250)
    
class Volunteer(models.Model):
    academic_formation=models.CharField(max_length=1000)
    motivation=models.CharField(max_length=1000)
    verify=models.BooleanField(default=False)
    status=models.CharField(
        max_length=10, 
        choices=STATUS,
        default=PENDING)
    documents = models.CharField(max_length=100)
    


class Meeting(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateField(blank = True)
    start_date = models.DateTimeField(blank = True)

class Class(models.Model):
    name = models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    capacity=models.IntegerField(validators=[
        MinValueValidator(0)], blank=True)

class Event(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    place=models.CharField(max_length=1000)
    capacity=models.IntegerField(default= 0, validators=[MinValueValidator(0)])
    max_volunteers=models.IntegerField(validators=[MinValueValidator(0)])
    start_date=models.DateTimeField(blank=True)
    end_date=models.DateTimeField(blank=True)
    lesson = models.ForeignKey(Class, on_delete=models.CASCADE, null = True, blank = True) 

class Evaluation(models.Model):
    name = models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    gradeSystem = models.CharField(
        max_length=20, 
        choices=GRADESYSTEM,
        default=ZERO_TO_TEN)
    
class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    national_ID = models.CharField(max_length=9, unique=True)
    nationality = models.CharField(max_length=50)
    educative_centre = models.CharField(max_length=100)
    educative_centre_tutor = models.CharField(max_length=50)
    current_education_year = models.CharField(
        max_length=25,
        choices=CURRENT_EDUCATION_YEAR,
        default=THREE_YEARS,
    )
    birthdate = models.DateField(null=True)
    phone = models.IntegerField( default = 600000000, validators = [MaxValueValidator(999999999), MinValueValidator(600000000)]) 
    email = models.EmailField(unique=True) 
    role = models.CharField(
        max_length=25,
        choices=ROLE,
        default=FAMILY,
    )
    password = models.CharField(max_length=500, null = False)
    avatar=models.URLField(validators=[URLValidator()]) 
    address = models.CharField(max_length=255)
    postal_code= models.IntegerField(validators=[
        MinValueValidator(10000), 
        MaxValueValidator(90000)], default = 10000)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, blank=True, null = True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, blank=True, null = True)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, blank=True, null = True)
    last_login = None
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
    
class Comment(models.Model):
    title=models.CharField(max_length=25)
    text=models.CharField(max_length=800)
    date_time=models.DateTimeField()
    user_commented = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_commented')
    user_who_comment = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_who_comment')

class Centre_Exit(models.Model):
    authorization = models.CharField(max_length=100)
    responsible=models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class User_Has_Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    
class User_Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class User_Has_Class(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Class, on_delete=models.CASCADE)

class Class_Has_Evaluation(models.Model):
    grade = models.FloatField(validators=[
        MinValueValidator(0.0),
        MaxValueValidator(10.0)])
    date = models.DateField()
    evaluation_type = models.CharField( 
        max_length=25,
        choices=EVALUATION_TYPE,
        default=DIARY,
    )
    lesson = models.ForeignKey(Class, on_delete=models.CASCADE) 
    user_family = models.ForeignKey(User, on_delete=models.CASCADE)
    evaluation =  models.ForeignKey(Evaluation, on_delete=models.CASCADE)
  
   
class User_Has_Evaluation(models.Model):
    grade = models.FloatField(validators=[
        MinValueValidator(0.0),
        MaxValueValidator(10.0)])
    date = models.DateField()
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    user_educator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_evaluator')
    user_evaluated = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_evaluated')
    lesson = models.ForeignKey(Class, on_delete=models.CASCADE)