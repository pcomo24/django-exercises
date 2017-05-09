from django.template.response import TemplateResponse
def homepage (request):
  return TemplateResponse(request, 'homepage.html', {})

def american (request):
  return TemplateResponse(request, 'american.html', {})
