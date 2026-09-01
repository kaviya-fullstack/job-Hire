from django.shortcuts import render, redirect, get_object_or_404
from .models import Job

# CREATE
def create_job(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Job.objects.create(
            name=name, 
            email=email, 
            phone=phone)
        return redirect('list')
    return render(request, 'create.html')

# READ
def list_jobs(request):
    jobs = Job.objects.all() # select * from tablename
    return render(request, 'list.html', {'jobs': jobs})

# UPDATE
def update_job(request, id):
    job = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        job.name = request.POST['name']
        job.email = request.POST['email']
        job.phone = request.POST['phone']
        job.save()
        return redirect('list')
    return render(request, 'update.html', {'jobs': job})


# DELETE
def delete_job(request, id):
    job = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        job.delete()
        return redirect('list')
    return render(request, 'delete.html', {'jobs': job})

#APPLY
def apply_job(request,id):
    job=get_object_or_404(Job,id=id)
    if request.method == 'POST':
        job.save()
        return redirect('list')
    return render(request,'apply.html',{'jobs':job})








