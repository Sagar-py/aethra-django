from django.shortcuts import render
from .forms import ProgressForm

# Home page view
def home(request):
    return render(request, 'life_tracker/home.html')

# Tracker page view
def tracker(request):
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            # Save the data or process it
            print(form.cleaned_data)  # For debugging
            # Redirect to another page or stay on the same page with success message
    else:
        form = ProgressForm()

    return render(request, 'life_tracker/tracker.html', {'form': form})

# Review page view
def review(request):
    progress_data = Progress.objects.all().order_by('-date_created')[:1]  # Fetch the latest entry
    return render(request, 'life_tracker/review.html', {'progress_data': progress_data})
