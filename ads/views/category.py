import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import CreateAPIView

from ads.models import Ad, Category
from ads.serializers import CategorySerializer
from avito.settings import TOTAL_ON_PAGE


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('-name')
        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page = request.GET.get('page')
        obj = paginator.get_page(page)
        response = {}
        items_list = [{'id': cat.pk,
                       'name': cat.name,
                       } for cat in obj]
        response['items'] = items_list
        response['total'] = self.object_list.count()
        response['num_pages'] = paginator.num_pages

        return JsonResponse(response, safe=False)


# @method_decorator(csrf_exempt, name='dispatch')
# class CategoryCreateView(CreateView):
#     model = Category
#     fields = ['name']
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body)
#         cat = Category.objects.create(name=data['name'])
#         return JsonResponse({'id': cat.pk,
#                              'name': cat.name
#                              }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListCreateView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = []
        for cat in categories:
            response.append({'id': cat.pk, 'name': cat.name, 'slug': cat.slug})
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        cat = Category.objects.create(**data)
        return JsonResponse({'id': cat.pk,
                             'name': cat.name,
                             'slug': cat.slug}, safe=False)




class CategoryDetailView(DetailView):
    queryset = Category.objects.all()
    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({'id': cat.pk,
                             'name': cat.name
                             }, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)

        if 'name' in data:
            self.object.name = data['name']

        self.object.save()
        return JsonResponse({'id': self.object.pk,
                             'name': self.object.name
                             }, safe=False)


# @method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, status=204)

