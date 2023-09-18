# Exercício 8: Faça um programa que solicita ao usuario inserir um email e retorna se ele é válido ou não.

def verificar_espaco(email):
    print(f"\tEtapa 2 verificar se contém espaços")
    espaco = email.split()
    if len(espaco) > 1:
        print(f"\tEtapa 2 reprovada.\n")
        print(f"\nContém {len(espaco)-1} espaços ")
        return True
    else:
        print(f"\tEtapa 2 aprovada.\n")
        return False
def verificar_arroba(email):
    print(f"\tEtapa 3 verificar se contém @")
    arroba = email.split("@")
    if len(arroba)< 2 or len(arroba) >2:
        print(f"\tEtapa 3 reprovado.\n")
        return False
    else:
        print(f"\tEtapa 3 aprovada.\n")
        return True

def verificar_email(email):
    carac_especial = ["_", "*", "@", "#", "$", "%", "&", "!", "?", "~"]
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    print(f"\n\tEtapa 1 verificar se pomeça com caracter especial ou numeros")
    if email[0] in carac_especial or email[0] in numeros:
        print(f"\tEtapa 1 reporvada. \n")
        return f"Email {email}. não contém um formato valido!\n"
    else:
        print(f"\tEtapa 1 aprovada.\n")
        if verificar_espaco(email):
            return f"Email {email}. não contém um formato valido!\n"
        else:
            if verificar_arroba(email):
                return f"Email utilizado contém um formato valido!\n"
            else:
                return f"Email {email}. não contém um formato valido!\n"

    





print(verificar_email(input("Digite seu email! ")))