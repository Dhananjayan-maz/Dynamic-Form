from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if dictionary:
        return dictionary.get(key, "")
    return ""

@register.filter(name="add_class")
def add_class(field, css):
    return field.as_widget(attrs={"class": css})

@register.filter
def class_name(value):
    return value.__class__.__name__ 