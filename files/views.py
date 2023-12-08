from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render, redirect
from .forms import FileUploadForm
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/upload/')  # Redirect to a success page
    else:
        form = FileUploadForm()
    return render(request, 'upload_file.html', {'form': form})
