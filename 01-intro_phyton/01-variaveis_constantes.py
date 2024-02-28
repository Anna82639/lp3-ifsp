# Identificadores
# Letra, número e ...
# Não pode ser palavra reservada: if, nome, true, false
# case sensitive 
    nome = "Pedro"
    Nome = "Pedro"

# variaveis 
# tudo em minusculo
# separador _
# snake_case
    idade = 20
    pessoa_fisica = "Marcio"
    pessoa_juridica = "Paula LTDA"
    imposto_renda = 2200.45

# e o tipo?
# java 
# String nome = "Pedro"
# int idade - 20
# no pythin temos inferencia de tipo
# o tipo será definido com base no valor (literal)
    idade = 20 # int 
    nome = "Pedro" # string 

# constantes 

# nao existe constante em python 
# convenção: nome em maiusculo 
    PI = 3.14

# comentarios de única linha 

'''
comentario de 
multiplas linhas 
'''

# docstring (comentário de documentação)
# documentar classe, módulo, funções...

public static somar(double numero1, double numero2) {
    return numero1 + numero2
}

def somar(numero1, numero2):
    '''
    funçaõ que soma dois números

    :param número1: primeiro numero
    :param número2: segundo número
    :return: a soma dos números 

    '''
    return numero1 + numero2