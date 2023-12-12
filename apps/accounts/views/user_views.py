
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.accounts.models import User, Course
from apps.accounts.serializers.user_serializers import DataCourseSerializer, TotalPesertaCourseSerializer, UserSerializer, CourseSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            queryset = User.objects.all()
        else:
            queryset = User.objects.filter(id=user.id)

        return queryset


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"


class CourseListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = "id"


class DataCourseSarjanaListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DataCourseSerializer
    queryset = Course.objects.filter(title__icontains="S.")

class DataCourseNonSarjanaListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DataCourseSerializer
    queryset = Course.objects.exclude(title__icontains="S.")

class DataCourseTotalPesertaListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TotalPesertaCourseSerializer
    queryset = Course.objects.all().distinct("course")