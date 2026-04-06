# Feito por Pedro Ruan - 30/03

def pegar_numeros():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    return n1, n2

resp = "sim"

while resp.lower() in ["s", "sim", "com certeza"]:
    print("\n--- CALCULADORA INTELIGENTE ---")
    esc = int(input(
        "Qual o cálculo você deseja fazer?\n"
        "[1] Soma\n"
        "[2] Subtração\n"
        "[3] Multiplicação\n"
        "[4] Divisão\n"
        "Escolha: "
    ))

    if esc == 1:
        n1, n2 = pegar_numeros()
        print(f"RESPOSTA: {n1} + {n2} = {n1 + n2}")

    elif esc == 2:
        n1, n2 = pegar_numeros()
        print(f"RESPOSTA: {n1} - {n2} = {n1 - n2}")

    elif esc == 3:
        n1, n2 = pegar_numeros()
        print(f"RESPOSTA: {n1} x {n2} = {n1 * n2}")

    elif esc == 4:
        n1, n2 = pegar_numeros()
        if n2 != 0:
            print(f"RESPOSTA: {n1} / {n2} = {n1 / n2}")
        else:
            print("RESPOSTA: Erro! Não é possível dividir por zero.")

    else:
        print("RESPOSTA: Opção inválida!")

    resp = input("\nDeseja continuar? [Sim/Não]: ")

print("\nObrigado por usar a Calculadora Inteligente!")