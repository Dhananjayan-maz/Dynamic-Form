from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import build_dynamic_form
import json
from django.http import JsonResponse
from datetime import date, datetime
from decimal import Decimal
from django.shortcuts import redirect

def home_view(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def registration_view(request, slug):

    # Safely fetch form (only user's form)
    form_def = FormDefinition.objects.filter(
        slug=slug,
        created_by=request.user
    ).first()

    if not form_def:
        return redirect("entries_list")

    DynamicForm = build_dynamic_form(form_def)

    if request.method == "POST":
        form = DynamicForm(request.POST)

        if form.is_valid():

            cleaned_data = {}

            # Track email & phone keys and values
            email_key = None
            phone_key = None
            email_value = None
            phone_value = None

            # -------- Collect cleaned data --------
            for field in form_def.fields.all():
                key = field.key
                value = form.cleaned_data.get(key)

                # Store email
                if field.field_type == "email":
                    email_key = key
                    email_value = value

                # Store phone
                if field.field_type == "tel":
                    phone_key = key
                    phone_value = value

                # Normalize data
                if isinstance(value, (date, datetime)):
                    cleaned_data[key] = value.isoformat()

                elif isinstance(value, Decimal):
                    cleaned_data[key] = float(value)

                else:
                    cleaned_data[key] = value

            # -------- Duplicate check PER FORM --------
            existing_entries = FormEntry.objects.filter(form=form_def)

            for entry in existing_entries:
                entry_data = entry.data or {}

                #  Duplicate Email
                if email_key and email_value:
                    if entry_data.get(email_key) == email_value:
                        messages.error(
                            request,
                            "This email ID is already registered for this form."
                        )
                        return render(request, "register.html", {
                            "form_def": form_def,
                            "form": form
                        })

                #  Duplicate Phone
                if phone_key and phone_value:
                    if entry_data.get(phone_key) == phone_value:
                        messages.error(
                            request,
                            "This mobile number is already registered for this form."
                        )   
                        return render(request, "register.html", {
                            "form_def": form_def,
                            "form": form
                        })

            # -------- Save entry --------
            FormEntry.objects.create(
                form=form_def,
                data=cleaned_data
            ) 

            return redirect("view_entries", slug=form_def.slug)

    else:
        form = DynamicForm()

    return render(request, "register.html", {
        "form_def": form_def,
        "form": form
    })


@login_required(login_url='login')
def create_form(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        fields_json = request.POST.get("fields_json", "").strip()
        
        if fields_json == "[]":
            messages.error(request, "You must add at least one field to the form.")
            return redirect("create_form") 

        # Save main form
        form_def = FormDefinition.objects.create(
            title=title,
            description=description,
            created_by=request.user
        )

        # Save fields
        fields = json.loads(fields_json)
        for index, f in enumerate(fields):
            FormField.objects.create(
                form=form_def,
                label=f["label"],
                field_type=f["field_type"],
                placeholder=f.get("placeholder", ""),
                choices=f.get("choices", ""),
                required=f.get("required", True),
                order=index
            )

        # Redirect to registration page
        return redirect("register_form", slug=form_def.slug)

    return render(request, "create_form.html")


@login_required(login_url="login")
def entries_list(request):
    user_forms = FormDefinition.objects.filter(created_by=request.user).order_by("-created_at")
    return render(request, "entries_list.html", {"user_forms": user_forms})


@login_required(login_url='login')
def view_entries(request, slug):

    # SAFELY fetch the form
    form_def = FormDefinition.objects.filter(
        slug=slug,
        created_by=request.user
    ).first()

    # If form is deleted or does not exist → redirect
    if not form_def:
        return redirect("entries_list")  # or 'home'

    # Normal flow
    entries = FormEntry.objects.filter(form=form_def).order_by("submitted_at")
    fields = form_def.fields.all()
    user_forms = FormDefinition.objects.filter(created_by=request.user)
    
    return render(request, "entries.html", {
        "form_def": form_def,
        "entries": entries,
        "fields": fields,
        "user_forms": user_forms
    })

    
@login_required(login_url='login')
def update_register(request, slug, entry_id):
    form_def = get_object_or_404(FormDefinition, slug=slug, created_by=request.user)
    
     # If form is deleted or does not exist → redirect
    if not form_def:
        return redirect("entries_list")
    
    entry = get_object_or_404(FormEntry, id=entry_id, form=form_def)

    if request.method == "POST":
        updated_data = {}
        for field in form_def.fields.all():
            updated_data[field.key] = request.POST.get(f"field_{field.id}", "")
        entry.data = updated_data
        entry.save()
        return redirect("view_entries", slug=slug)

    fields = []
    for field in form_def.fields.all():
        fields.append({
            "id": field.id,
            "label": field.label,
            "field_type": field.field_type,
            "value": entry.data.get(field.key, ""),
            "choices": [c.strip() for c in field.choices.split(",")] if field.choices else []
        })
        
    return render(request, "update_register.html", {
        "form_def": form_def,
        "fields": fields,
        "entry": entry
    })

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'signup.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('create_form')  
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def delete_form(request, id):
    if request.method == "POST":
        form = get_object_or_404(
            FormDefinition,
            id=id,
            created_by=request.user
        )
        form.delete()
        return JsonResponse({"success": True})

    return JsonResponse({"success": False}, status=400)