import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from ads.models import Ad, Category
from users.models import User


def root(request):
    return JsonResponse({'status': 'ok'})


class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        ads = self.object_list.all()
        response = []
        for ad in ads:
            response.append({'id': ad.pk, 'name': ad.name, 'author': ad.author.username, 'price': ad.price,
                             'category': ad.category.name})
        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['name']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        author = get_object_or_404(User, username=data['author'])
        category = get_object_or_404(Category, name=data['category'])

        ad = Ad.objects.create(name=data['name'],
                               author=author,
                               category=category,
                               price=data['price'],
                               description=data['description'],
                               is_published=data['is_published'])
        return JsonResponse({'id': ad.pk,
                             'name': ad.name,
                             'author': ad.author.username,
                             'price': ad.price,
                             'description': ad.description,
                             'address': ad.category.name,
                             'is_published': ad.is_published
                             }, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({'id': ad.pk,
                             'name': ad.name,
                             'author': ad.author.username,
                             'category': ad.category.name,
                             'price': ad.price,
                             'description': ad.description,
                             'is_published': ad.is_published
                             }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)
        # author = get_object_or_404(User, data['author'])
        # category = get_object_or_404(Category, data['category'])
        if 'name' in data:
            self.object.name = data['name']
        if 'price' in data:
            self.object.name = data['price']
        if 'description' in data:
            self.object.name = data['description']
        if 'is_published' in data:
            self.object.name = data['is_published']
        self.object.save()
        return JsonResponse({'id': self.object.pk,
                             'name': self.object.name,
                             'author': self.object.author,
                             'price': self.object.price,
                             'description': self.object.description,
                             'address': self.object.address,
                             'is_published': self.object.is_published
                             }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, status=204)