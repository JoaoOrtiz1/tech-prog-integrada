import string

def validar_senha(senha):
    # Verifica se a senha tem pelo menos uma letra maiúscula, uma letra minúscula e um número
    if any(c.isupper() for c in senha) and any(c.islower() for c in senha) and any(c.isdigit() for c in senha):
        # Verifica se a senha não contém caracteres de pontuação, acentuação ou espaço
        if all(c.isalnum() for c in senha):
            # Verifica se a senha tem de 6 a 32 caracteres
            if 6 <= len(senha) <= 32:
                return "Senha valida."
    
    return "Senha invalida."

# Processa as senhas até o final do arquivo
while True:
    try:
        senha = input()
        resultado = validar_senha(senha)
        print(resultado)
    except EOFError:
        break