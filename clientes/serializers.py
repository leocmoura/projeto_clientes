from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua dígitos nesse campo"})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF inválido"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG não deve ser menor que 6 dígitos e maior que 9 dígitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve seguir este modelo: 11 91234-1234"})
        return data