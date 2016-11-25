from django.http import HttpResponse
import boto3

def home(request):
    s3 = boto3.resource('s3')
    keys = []
    for bucket in s3.buckets.all():
        for key in bucket.objects.all():
            keys.append(key.key)

    return HttpResponse("<html><body><ul><li>%s</li></ul></body></html>" % "</li><li>".join(keys))
