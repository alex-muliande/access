from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from .models import InitialForm


class InitialformCreateView(CreateView):
    model = InitialForm
    template_name = 'initial.html'  
    fields = ['cert_image', 'name']

    




















# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})


# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from .forms import ModelFormWithFileField

# def upload_file(request):
#     if request.method == 'POST':
#         form = ModelFormWithFileField(request.POST, request.FILES)
#         if form.is_valid():
#             # file is saved
#             form.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = ModelFormWithFileField()
#     return render(request, 'upload.html', {'form': form})