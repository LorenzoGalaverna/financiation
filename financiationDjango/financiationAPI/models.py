from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class Agreement(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class CityDepartment(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class MinistryDepartment(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Address(models.Model):
    street = models.CharField(max_length=70)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.street} {self.number}"


class UserStatus(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class VisitStatus(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Faq(models.Model):
    name = models.TextField()
    ministry_department = models.ManyToManyField(MinistryDepartment)

    def __str__(self):
        return f"{self.name}"


class Mayor(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Location(models.Model):
    name = models.CharField(max_length=70)
    department = models.ForeignKey(CityDepartment, models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}"


class Logo(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class VehicleBrand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class VehicleModel(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(VehicleBrand, models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}"


class PoliticParty(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class VehiclePlate(models.Model):
    plate = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.plate}"


class Role(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class ContactedReferrer(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class UserAccountManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, ssn, phone_number, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, ssn=ssn,
                          phone_number=phone_number)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, first_name, last_name, ssn, phone_number, profile_picture,
                         password=None, is_staff=True, is_superuser=True):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, ssn=ssn,
                          is_staff=is_staff, phone_number=phone_number, is_superuser=is_superuser,
                          profile_picture=profile_picture)

        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    ssn = models.BigIntegerField(unique=True)
    email = models.EmailField(max_length=2550, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.BigIntegerField()
    profile_picture = models.ImageField(default=None)
    role = models.ForeignKey(Role, models.DO_NOTHING, null=True)
    user_status = models.ForeignKey(UserStatus, models.DO_NOTHING, null=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'ssn'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone_number', 'profile_picture']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_last_name(self):
        return self.last_name

    def __str__(self):
        return f"{self.ssn}"


class Group(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.name}"


class Vehicles(models.Model):
    plate = models.ForeignKey(VehiclePlate, models.DO_NOTHING)
    brand = models.ForeignKey(VehicleBrand, models.DO_NOTHING)
    model = models.ForeignKey(VehicleModel, models.DO_NOTHING)

    def __str__(self):
        return f"{self.brand} {self.model} {self.plate}"


class Visit(models.Model):
    flyer = models.IntegerField()
    distance = models.IntegerField()
    travel_time = models.IntegerField()
    visit_date = models.DateField()
    civil_registration = models.BooleanField()
    accommodation = models.BooleanField()
    modernization_fund = models.BooleanField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    place_name = models.CharField(max_length=70)
    location = models.ForeignKey(Location, models.DO_NOTHING)
    group = models.ForeignKey(Group, models.DO_NOTHING)
    visit_status = models.ForeignKey(VisitStatus, models.DO_NOTHING)
    agreement = models.ManyToManyField(Agreement)
    contacted_referrer = models.ForeignKey(ContactedReferrer, models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    logo = models.ManyToManyField(Logo)

    def __str__(self):
        return f"Visit to {self.location}"


class RequestStatus(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Coordinator(models.Model):
    user = models.ForeignKey(UserAccount, models.DO_NOTHING)
    group = models.ForeignKey(Group, models.DO_NOTHING)

    def __str__(self):
        return f"{self.user} {self.group}"


class Advisor(models.Model):
    user = models.ForeignKey(UserAccount, models.DO_NOTHING)
    group = models.ForeignKey(Group, models.DO_NOTHING)

    unique_together = (('user', 'group'),)

    def __str__(self):
        return f"{self.user} {self.group}"


class Request(models.Model):
    visit = models.ForeignKey(Visit, models.DO_NOTHING)
    advisor = models.ForeignKey(Advisor, models.DO_NOTHING)
    ministry_department = models.ForeignKey(MinistryDepartment, models.DO_NOTHING)
    faq = models.ForeignKey(Faq, models.DO_NOTHING)
    status = models.ForeignKey(RequestStatus, models.DO_NOTHING)

    def __str__(self):
        return f"Request {self.id}"


class ContactedReferrerEmail(models.Model):
    mail = models.CharField(max_length=100)
    contacted_referrer = models.ForeignKey(ContactedReferrer, models.DO_NOTHING)

    def __str__(self):
        return f"Request {self.mail}"


class MayorPhone(models.Model):
    phone = models.BigIntegerField()
    mayor = models.ForeignKey(Mayor, models.DO_NOTHING)

    def __str__(self):
        return f"Request {self.phone}"


class MayorEmail(models.Model):
    mail = models.CharField(max_length=100)
    mayor = models.ForeignKey(Mayor, models.DO_NOTHING)

    def __str__(self):
        return f"Request {self.mail}"


class ContactedReferrerPhone(models.Model):
    phone = models.BigIntegerField()
    contacted_referrer = models.ForeignKey(ContactedReferrer, models.DO_NOTHING)

    def __str__(self):
        return f"Request {self.phone}"
