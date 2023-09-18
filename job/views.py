from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Job, Apply
from django.core.paginator import Paginator
from .form import ApplyForm, AddJob
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

# Create your views here.


def jobList(request):
    job_list = Job.objects.all()

    job_filter = JobFilter(request.GET, queryset=job_list)
    job_list = job_filter.qs
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    context = {'job_list': page_obj, 'job_filter': job_filter}
    return render(request, 'job/job_list.html', context)


def jobDetails(request, slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_detail
            my_form.save()

    else:
        form = ApplyForm()
    context = {'job': job_detail, 'form': form}
    return render(request, 'job/job_detail.html', context)


@login_required
def addJob(request):
    if request.method == "POST":
        form = AddJob(request.POST, request.FILES)
        if (form.is_valid()):
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = AddJob()
    context = {'form': form}
    return render(request, 'job/add_job.html', context)
