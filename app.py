def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def py3_13func(valor): #função que não funciona no python 3.10
    match valor:
        case [1, 2, *rest]:
            return f"começa com 1,2 e o resto é {rest}"
        case _:
            return "outro formato"
