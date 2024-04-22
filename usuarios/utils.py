from re import match

def validar_campo(campo):
    # Define a expressão regular para permitir apenas letras, espaços e caracteres especiais comuns
    padrao = r'^[a-zA-ZáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ\s\-\.]+$'
    
    # Verifica se o campo corresponde ao padrão
    if match(padrao, campo):
        return True
    else:
        return False