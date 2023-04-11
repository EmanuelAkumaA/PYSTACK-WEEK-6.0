""" EM usuarios - templates - views.py

def validar_senha(senha):
    '''Valida a força da senha'''

#'''VARIÁVEIS DE CONTAGEM'''

    alfabeto_maiusculo = False
    alfabeto_minusculo = False
    numeros = False
    caracteres_especiais = False

#'''PARA CHECAR OS CARACTERES DA SENHA'''

    for caractere in senha:

        if caractere.isupper():
            alfabeto_maiusculo = True

        elif caractere.islower():
            alfabeto_minusculo = True

        elif caractere.isdigit():
            numeros = True

        else:
            caracteres_especiais = True
   #'''CHECAR SE A SENHA CONTEM TODOS OS CARACTERES'''

    if (len(senha) >= 8) and alfabeto_maiusculo and alfabeto_minusculo and numeros:
        print("Senha forte.")
    elif (len(senha) >= 8) and (alfabeto_maiusculo or alfabeto_minusculo) and numeros:
        print("Senha moderada.")
    else:
        print("Senha fraca.")"""