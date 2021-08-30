from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from hello.serializers import PessoaSerializer
from hello.models import Pessoa


@csrf_exempt
def pessoa_list(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = PessoaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def pessoa_details(request, pk):    
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PessoaSerializer(Pessoa)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PessoaSerializer(Pessoa, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Pessoa.delete()
        return HttpResponse(status=204)
@csrf_exempt
def hello(request):
    return HttpResponse('Hello World!',status=200)