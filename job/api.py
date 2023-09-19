from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer


@api_view(['GET'])
def jobListApi(request):
    jobs = Job.objects.all()
    jobSerializer = JobSerializer(jobs, many=True).data
    return Response({'data': jobSerializer})
