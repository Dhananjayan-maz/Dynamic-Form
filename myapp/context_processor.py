from .models import FormDefinition

def user_forms_processor(request):
    if not request.user.is_authenticated:
        return {"user_forms": []}

    user_forms = (
        FormDefinition.objects
        .filter(created_by=request.user)
        .only("id", "title", "slug")
        .order_by("-created_at")
    )

    return {
        "user_forms": user_forms
    }
