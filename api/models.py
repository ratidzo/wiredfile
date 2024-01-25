from django.db import models
from .lib import constants


# Create your models here.
class School(models.Model):
    owner = models.OneToOneField(
        'auth.User', related_name='school', on_delete=models.CASCADE,

    )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(
        max_length=100, blank=False, default=constants.DEFAULT_SCHOOL_NAME
    )
    school_type = models.CharField(null=False)

    def __str__(self):
        return f"{self.name}"


"""
    We'll try and manage each school's finances in a seperate model.
    The idea is to use this model as a source of truth for all our
    financial analyses. For the lack of a better name we'll just call
    it 'Financials' for now.
"""


class Financials(models.Model):
    school = models.OneToOneField(
        to="School", related_name='financials', on_delete=models.CASCADE
    )
    # We store amounts as integers in cents.
    term_fees_day = models.IntegerField(default=0)
    term_fees_boarding = models.IntegerField(default=0)

    def __str__(self):
        return "school financials"


"""
    Model to store student information. Each student has a one-to-one
    relationship to a Guardian and Account.
"""


class Student(models.Model):
    school = models.ForeignKey(
        to="School", related_name='students', on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(
        auto_now_add=True)  # date the account was created.
    date_enrolled = models.DateTimeField(
        null=True)  # date the student was enrolled
    first_name = models.CharField(
        max_length=100, null=False)
    middle_name = models.CharField(max_length=100, default='', blank=True)
    last_name = models.CharField(max_length=100, null=False)
    date_of_birth = models.DateField(null=False)
    sex = models.CharField(null=False, max_length=20)
    mode = models.CharField(max_length="20", null=False)
    address = models.CharField(max_length=100, null=False)
    grade_at_enrol = models.CharField(max_length=20, null=False)
    student_class = models.CharField(max_length=20, null=False)
    student_rank = models.CharField(
        max_length=20, default=constants.DEFAULT_STUDENT_RANK)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Model for representing a student's financial account
class Account(models.Model):
    student = models.OneToOneField(
        to='Student',
        related_name='account',
        on_delete=models.CASCADE
    )
    debit = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    account_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"account balance: {self.balance}"


# Model for representing a student's registered guardian
class Guardian(models.Model):
    student = models.OneToOneField(
        to='Student',
        related_name='guardian',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    relationship = models.CharField(null=False)
    phone = models.CharField(max_length=100)
    email = models.EmailField(default='example@email.com')

    def __str__(self):
        return f"{self.title}. {self.first_name} {self.last_name}"
