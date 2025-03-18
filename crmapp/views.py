from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginUserForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Record


# Home Page View
def home(request):

    return render(request, "crmapp/home.html")


# Register User View
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")
            return redirect("dashboard")
    context = {"form": form}

    return render(request, "crmapp/register.html", context=context)


# Login User View
def login(request):
    form = LoginUserForm()

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                messages.success(request, "Logged in successfully!")

                return redirect("dashboard")

    context = {"form": form}

    return render(request, "crmapp/login.html", context=context)


# Dashboard View
@login_required(login_url="login")
def dashboard(request):

    my_records = Record.objects.all()

    context = {"records": my_records}

    return render(request, "crmapp/dashboard.html", context=context)


# Crate a Record
@login_required(login_url="login")
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Record created successfully!")

            return redirect("dashboard")

    context = {"form": form}

    return render(request, "crmapp/create-record.html", context=context)


# Update a Record
@login_required(login_url="login")
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Record was updated successfully!")

            return redirect("dashboard")

    context = {"form": form}

    return render(request, "crmapp/update-record.html", context=context)


# View a singular Record
@login_required(login_url="login")
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {"record": all_records}

    return render(request, "crmapp/view-record.html", context=context)


# Delete a Record
@login_required(login_url="login")
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Record deleted successfully!")

    return redirect("dashboard")


# - User logout
def logout_user(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("login")
