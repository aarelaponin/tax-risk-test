from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

# Create your views here.
from taxrisk.models import Person, BzEntity
from taxrisk.serializers import BzEntitySerializer


def post_list(request):
    return render(request, 'taxrisk/post_list.html')


@csrf_exempt
def person_list(request):
    if request.method == 'GET':
        entities = BzEntity.objects.all()
        serializer = BzEntitySerializer(entities, many=True)
        return JsonResponse(serializer.data, safe=False)