import re
from validate_docbr import CPF

def nome_valido(nome):
    return nome.isalpha()
def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)
def rg_valido(rg):
    return len(rg) >= 6 and len(rg) <= 9
def celular_valido(celular):
    """Verifica se o  celular é valido (11 91234-1234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta