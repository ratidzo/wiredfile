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
