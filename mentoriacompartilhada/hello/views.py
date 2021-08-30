import re
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from hello.serializers import PessoaSerializer
from hello.models import Pessoa


@csrf_exempt
@api_view(['GET','POST'])
def pessoa_list(request):
    if request.method == 'GET':
        
        pagina = int(request.GET['page']) if 'page' in request.GET else 0
        tamanho = int(request.GET['size']) if 'size' in request.GET else 10
        offset = pagina * tamanho

        pessoas = Pessoa.objects.all()[offset:offset+tamanho]
        serializer = PessoaSerializer(pessoas,many=True)
        pagina = {
            'page': int(pagina),
            'size': pessoas.count(),
            'total': Pessoa.objects.count(),
            'items':serializer.data
        }
        return JsonResponse(pagina,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(stream=request,media_type='application/json')
        serializer = PessoaSerializer(data=data)
        if serializer.is_valid():
            pessoa = serializer.save()
            response = HttpResponse(status=201)
            response['Location'] = '/api/pessoas/' + str(pessoa.id)
            return response
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def pessoa_details(request, pk):    
    try:
        pessoa = Pessoa.objects.get(pk=pk)
    except Pessoa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PessoaSerializer(pessoa)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(stream=request,media_type='application/json')
        serializer = PessoaSerializer(pessoa, data=data)
        if serializer.is_valid():
            pessoa = serializer.save()
            return HttpResponse(status=202)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Pessoa.delete()
        return HttpResponse(status=204)
@csrf_exempt
def hello(request):
    return HttpResponse('Hello World!',status=200)