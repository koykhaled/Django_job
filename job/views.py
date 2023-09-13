from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator

# Create your views here.


def jobList(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    context = {'job_list': page_obj}
    return render(request, 'job/job_list.html', context)


def jobDetails(request, id):
    job_detail = Job.objects.get(id=id)
    context = {'job': job_detail}
    return render(request, 'job/job_detail.html', context)
