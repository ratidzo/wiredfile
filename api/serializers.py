from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    School, Financials, Student, Guardian, Account
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    school = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='school-detail'
    )

    class Meta:
        model = User
        fields = [
            'id', 'username',
            'first_name', 'last_name', 'email', 'school']


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    financials = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='financials-detail'
    )

    class Meta:
        model = School
        fields = [
            'name',
            'schoo_type',
            'financials',
            'date_created'
        ]


class FinancialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Financials
        fields = [
            'term_fees_day',
            'term_fees_boarding'
        ]


# serializers for the student and related models.
class StudentSerializers(serializers.HyperlinkedModelSerializer):
    account = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='account-detail'
    )
    guardian = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='guardian-detail'
    )

    class Meta:
        model = Student
        fields = [
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'mode',
            'address',
            'grade_at_enrol',
            'student_class',
            'student_rank',
            'account',
            'guardian'
        ]


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'debit',
            'credit',
            'balance',
            'account_paid'
        ]


class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = [
            'id',
            'title',
            'first_name',
            'last_name',
            'relationship',
            'phone',
            'email'
        ]
