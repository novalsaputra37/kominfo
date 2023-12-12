from django.urls import include, path

from apps.accounts.views import auth_views, user_views

app_name = "accounts"
urlpatterns = [
    path(
        "auth/",
        include(
            [
                path(
                    "login/",
                    auth_views.LoginGenericAPIView.as_view(),
                    name="auth-login",
                ),
                path(
                    "refresh/",
                    auth_views.RefreshGenericAPIView.as_view(),
                    name="auth-refresh",
                ),
                path(
                    "logout/",
                    auth_views.LogoutGenericAPIView.as_view(),
                    name="auth-logout",
                ),
            ]
        ),
    ),
    path(
        "user/",
        include([
            path("", user_views.UserListCreateAPIView.as_view(), name="user-list"),
            path("<str:id>", user_views.UserRetrieveUpdateDestroyAPIView.as_view(), name="user-retrieve-update-delete"),
        ])
    ),
    path(
        "course/",
        include([
            path("", user_views.CourseListCreateAPIView.as_view(), name="course-list"),
            path("<str:id>", user_views.CourseRetrieveUpdateDestroyAPIView.as_view(), name="course-retrieve-update-delete"),
        ])
    ),
    path(
        "data/",
        include([
            path("course-sarjana/", user_views.DataCourseSarjanaListAPIView.as_view(), name="course-data-mentor-sarjana"),
            path("course-non-sarjana/", user_views.DataCourseNonSarjanaListAPIView.as_view(), name="course-mentor-non-sarjana"),
            path("course-total-peserta/", user_views.DataCourseTotalPesertaListAPIView.as_view(), name="course-mentor-non-sarjana"),
        ])
    )
]