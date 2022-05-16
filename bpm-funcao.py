#Escreva um programa que peça ao usuário sua idade em anos (y)
# e então estime seu batimento cardiaco maximo em batidas por minuto,
#usasndo a fórmula 208 - 0.7y.
def batimento(y):
    f = 208 -0.7 * y
    return f

def main():
    y = int(input("Entre com a sua idade: "))
    print("Batimento cardíaco máximo por minuto: ", batimento(y))

main()
