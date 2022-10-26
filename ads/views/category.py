import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category



@method_decorator(csrf_exempt, name='dispatch')
class CategoryListCreateView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = []
        for cat in categories:
            response.append({'id': cat.pk, 'name': cat.name})
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        cat = Category.objects.create(**data)
        return JsonResponse({'id': cat.pk,
                             'name': cat.name
                             }, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({'id': cat.pk, 'name': cat.name}, safe=False)

