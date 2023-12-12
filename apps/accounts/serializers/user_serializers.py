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