from django import forms
from django.core.validators import RegexValidator
from decimal import Decimal
from datetime import date, datetime

def build_dynamic_form(form_definition):

    class DynamicRegistrationForm(forms.Form):
        pass

    for ff in form_definition.fields.all():

        field_kwargs = {
            "label": ff.label,
            "required": ff.required,
            "help_text": ff.help_text or "",
        }

        # ---------- TEXT ----------
        if ff.field_type == "text":
            field = forms.CharField(
                max_length=ff.max_length or 255,
                widget=forms.TextInput(attrs={
                    "placeholder": ff.placeholder
                }),
                **field_kwargs
            )

        # ---------- EMAIL ----------
        elif ff.field_type == "email":
            field = forms.EmailField(
                widget=forms.EmailInput(attrs={
                    "placeholder": ff.placeholder
                }),
                **field_kwargs
            )

        # ---------- NUMBER ----------
        elif ff.field_type == "number":
            field = forms.IntegerField(
                widget=forms.NumberInput(attrs={
                    "placeholder": ff.placeholder,
                    "inputmode": "numeric"
                }),
                **field_kwargs
            )

        # ---------- DATE ----------
        elif ff.field_type == "date":
            field = forms.DateField(
                widget=forms.DateInput(attrs={
                    "type": "date"
                }),
                **field_kwargs
            )

        # ---------- TELEPHONE ----------
        elif ff.field_type == "tel":
            field = forms.CharField(
                max_length=10,
                validators=[
                    RegexValidator(
                        regex=r'^[6-9][0-9]{9}$',
                        message="Enter a valid 10-digit mobile number"
                    )
                ],
                widget=forms.TextInput(attrs={
                    "type": "tel",
                    "inputmode": "numeric",
                    "placeholder": ff.placeholder,
                    "pattern": "[6-9][0-9]{9}",
                    "maxlength": "10",
                    "title": "Enter a valid 10-digit mobile number",
                    "oninput": "this.value = this.value.replace(/[^0-9]/g, '')"
                }),
                **field_kwargs
                )

        # ---------- TEXTAREA ----------
        elif ff.field_type == "textarea":
            field = forms.CharField(
                widget=forms.Textarea(attrs={
                    "placeholder": ff.placeholder
                }),
                **field_kwargs
            )

        # ---------- SELECT / RADIO ----------
        elif ff.field_type in ["select", "radio"]:
            choices = [
                (c.strip(), c.strip())
                for c in ff.choices.split(",")
                if c.strip()
            ]

            widget = forms.Select() if ff.field_type == "select" else forms.RadioSelect()

            field = forms.ChoiceField(
                choices=choices,
                widget=widget,
                **field_kwargs
            )

        # ---------- CHECKBOX ----------
        elif ff.field_type == "checkbox":
            field = forms.BooleanField(required=False, label=ff.label, help_text=ff.help_text or "")

        # ---------- FALLBACK ----------
        else:
            field = forms.CharField(alert="Unsupported field type", required=False) 

        # ✅ CRITICAL FIX (USE ff.key)
        DynamicRegistrationForm.base_fields[ff.key] = field

    return DynamicRegistrationForm
