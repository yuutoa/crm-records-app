from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name=""),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_user, name="logout"),
    #     CRUD
    path("create-record/", views.create_record, name="create-record"),
    path("record/<int:pk>", views.singular_record, name="view-record"),
    path("update-record/<int:pk>", views.update_record, name="update-record"),
    path("delete-record/<int:pk>", views.delete_record, name="delete-record"),
]
