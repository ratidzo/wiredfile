from django.contrib.auth.models import User
from .models import (School, Student,
                     Guardian, Account, Financials)
from .serializers import (
    UserSerializer,
    SchoolSerializer,
    StudentSerializer,
    AccountSerializer,
    GuardianSerializer,
    FinancialsSerializer
)
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user)


class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        user = self.request.user
        return School.objects.filter(owner=user)


class FinancialsViewSet(viewsets.ModelViewSet):
    serializer_class = FinancialsSerializer

    def get_queryset(self):
        user = self.request.user
        return Financials.objects.filter(school__owner=user)


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name']

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(school__owner=user)

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer

    def get_queryset(self):
        user = self.request.user
        return Account.objects.filter(
            student__school__owner=user
        )


class GuardianViewSet(viewsets.ModelViewSet):
    serializer_class = GuardianSerializer

    def get_queryset(self):
        user = self.request.user
        return Guardian.objects.filter(
            student__school__owner=user
        )
