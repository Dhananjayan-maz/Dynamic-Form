from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import uuid

User = get_user_model()

FIELD_TYPE_CHOICES = [
    ('text', 'Text'),
    ('email', 'Email'),
    ('number', 'Number'),
    ('date', 'Date'),
    ('tel', 'Phone'),
    ('textarea', 'Textarea'),
    ('select', 'Select'),
    ('checkbox', 'Checkbox'),
    ('radio', 'Radio'),
]

class FormDefinition(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, blank=True) 
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='forms', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or "form"
            self.slug = f"{base}-{uuid.uuid4().hex[:6]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class FormField(models.Model):
    form = models.ForeignKey(FormDefinition, related_name='fields', on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    name = models.CharField(max_length=200, blank=True)  # if blank we can auto-generate from label
    field_type = models.CharField(max_length=20, choices=FIELD_TYPE_CHOICES)
    required = models.BooleanField(default=True)
    placeholder = models.CharField(max_length=200, blank=True)
    help_text = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    # for select/radio/checkbox we store choices as comma separated values
    choices = models.TextField(blank=True, help_text="Comma-separated choices for select/radio/checkbox.")
    max_length = models.PositiveIntegerField(null=True, blank=True)
    
    key = models.SlugField(max_length=255, blank=True)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.name:
            # generate a safe field name from label
            self.key = slugify(self.label).replace('-', '_')[:50]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.form.title} - {self.label}"

class FormEntry(models.Model):
    form = models.ForeignKey(FormDefinition, related_name='entries', on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()
    # optionally store IP or user if needed:
    submitted_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Entry {self.id} for {self.form.title} at {self.submitted_at}"

    