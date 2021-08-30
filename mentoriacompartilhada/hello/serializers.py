from rest_framework import serializers
from hello.models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id','nome','email','password']