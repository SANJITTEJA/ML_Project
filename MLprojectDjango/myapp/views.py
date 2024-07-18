from django.shortcuts import render
from .forms import EmployeeForm
from .ml_model import generate_recommendations, top_features

def home(request):
    recommendations = None
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee_data = []
            for key in form.cleaned_data:
                employee_data.append(form.cleaned_data[key])
            recommendations = generate_recommendations(employee_data, top_features)
    else:
        form = EmployeeForm()

    return render(request, 'myapp/home.html', {'form': form, 'recommendations': recommendations})
