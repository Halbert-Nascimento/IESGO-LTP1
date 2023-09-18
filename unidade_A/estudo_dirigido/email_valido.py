# Exercício 8: Faça um programa que solicita ao usuario inserir um email e retorna se ele é válido ou não.

def verificar_email(email):
    espaco = email.split()
    if len(espaco) > 1:
        print(f"\nEmail invalido contém {len(espaco)-1} espaços ")
    else:
        if email.find('@') != -1:
            return "Email Valido!" 
        else:
            return "Email Invalido!" 



print(verificar_email(input("Digite um email! ")))