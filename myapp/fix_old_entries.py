from myapp.models import FormEntry

def run():
    for entry in FormEntry.objects.all():
        form = entry.form
        new_data = {}

        for field in form.fields.all():
            possible_keys = [
                field.key,
                field.label.lower().replace(" ", "_"),
                field.label.lower().replace("-", "_").replace(" ", "_")
            ]

            for k in possible_keys:
                if k in entry.data:
                    new_data[field.key] = entry.data[k]
                    break
            else:
                new_data[field.key] = ""

        entry.data = new_data
        entry.save()