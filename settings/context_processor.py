from .models import Company

def get_info(request):
    context = Company.objects.last()
    return {'info' : context}