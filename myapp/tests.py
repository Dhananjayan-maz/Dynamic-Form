from django.test import TestCase

# Create your tests here.
    # <nav class="navbar navbar-expand-lg px-4">
    #     <a class="navbar-brand fw-bold" href="{% url 'home' %}">DynamicForms</a>

    #     <div class="collapse navbar-collapse">
    #         <ul class="navbar-nav me-auto ms-3">
    #             <li class="nav-item">
    #                 <a class="nav-link" href="{% url 'home' %}">Home</a>
    #             </li>
    #             <li class="nav-item">
    #                 <a class="nav-link" href="{% url 'create_form' %}">Make Form</a>
    #             </li>
    #         </ul>

    #         <div class="d-flex align-items-center">
    #             {% if request.user.is_authenticated %}
    #             <span class="me-3">Hi, {{ request.user.username }}</span>
    #             <a href="{% url 'logout' %}" class="btn btn-outline-light btn-sm">Logout</a>
    #             {% else %}
    #             <a href="{% url 'login' %}" class="btn btn-outline-light btn-sm me-2">Login</a>
    #             <a href="{% url 'signup' %}" class="btn btn-light btn-sm">Signup</a>
    #             {% endif %}
    #         </div>
    #     </div>
    # </nav>