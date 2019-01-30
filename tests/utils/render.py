from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import boto3


# want to link it to my own lib
def download_file(bucket: str, prefix: str):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    bucket.download_file(prefix + '/VIS_21.png', 'tests/static/tests/VIS_21.png')


def file_list(bucket: str, prefix: str):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    listf = [item.key for item in bucket.objects.filter(Prefix=prefix)]
    return listf


class Render:

    Bucket_name = 'newbucketforfootshot'

    @staticmethod
    def render(path: str, params: dict):
        flist = file_list(Render.Bucket_name, 'proctest')
        download_file(Render.Bucket_name, 'proctest')

        template = get_template(path)
        html = template.render({'list': flist})
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error rendering PDF", status=400)
