from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os
import time

def index(request):
    context = {}
    context["verdict"] = "Problem Statement/ Verdict Goes here"
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['document']
        except:
            messages.error(request, 'no file found')
        if not uploaded_file.name.endswith(".cpp"):
            messages.error(request, 'file should be cpp')
        else:
            code_path = os.path.join(settings.MEDIA_ROOT, "user-runner/usercode.cpp")
            runner_path = os.path.join(settings.MEDIA_ROOT, "user-runner/")
            fs = FileSystemStorage()
            fs.save(code_path, uploaded_file)
            os.chdir(runner_path)
            os.system("./run.sh")
            os.remove("usercode.cpp")
            #here
            with open("test.txt", encoding = 'utf-8') as f:
                verdict = f.read() 
                context["verdict"] = verdict
            os.chdir("..")
    return render(request, "OJ/index.html", context)

