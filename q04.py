def leitura(a, b):
    text = a+','+b
    return text

def print_tela():
    a = input("Digite a priemira entrada: ")
    b = input("Digite a segunda entrada: ")
    print(leitura(a, b))
    
print_tela()