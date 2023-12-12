from apps.accounts.models import User, Course, UserCourse
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_staff",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        get_password = validated_data.get("password")
        instance = super().create(validated_data)
        instance.set_password(get_password)
        instance.save()
        return instance
    

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = [
            "id",
            "course",
            "mentor",
            "title",
            "user"
        ]

class DataCourseSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="user.id")
    username = serializers.CharField(source="user.username")

    class Meta:
        model = Course
        fields = [
            "id",
            "username",
            "course",
            "mentor",
            "title",
        ]


class TotalPesertaCourseSerializer(serializers.ModelSerializer):
    jumlah_peserta = serializers.SerializerMethodField()


    def get_jumlah_peserta(self, obj):
        return Course.objects.filter(course=obj.course).count()

    class Meta:
        model = Course
        fields = [
            "course",
            "mentor",
            "title",
            "jumlah_peserta"
        ]