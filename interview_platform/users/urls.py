from django.urls import path
from . import views

urlpatterns = [

    # Authentication
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),

    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),

    # Profile
    path("profile/", views.profile, name="profile"),

    # Resume
    path("resume/upload/", views.upload_resume, name="upload_resume"),

    # Interview
    path("interview/start/", views.start_interview, name="start_interview"),

    # Quiz
    path("quiz/start/", views.start_quiz, name="start_quiz"),

]