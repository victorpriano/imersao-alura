# ========================================================
# CALCULADORA BÁSICA EM PYTHON
# Demonstração das 4 operações matemáticas fundamentais
# ========================================================

# 1. Definição das Funções Matemáticas
def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a diferença entre dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna o produto de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão do primeiro número pelo segundo.
    Verifica se o divisor é zero para evitar erro crítico.
    """
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

def porcentagem(a, b):
    """Retorna b por cento de a (a * b / 100)."""
    return (a * b) / 100

# 2. Função Principal do Programa
def main():
    print("=" * 36)
    print("       CALCULADORA EM PYTHON        ")
    print("=" * 36)
    print("Operações disponíveis:")
    print("  + : Adição")
    print("  - : Subtração")
    print("  * : Multiplicação")
    print("  / : Divisão")
    print("  % : Porcentagem")
    print("-" * 36)

    try:
        # Entrada do primeiro número
        num1 = float(input("Digite o primeiro número: "))
        
        # Escolha da operação
        operacao = input("Escolha a operação (+, -, *, /, %): ").strip()
        
        # Entrada do segundo número
        num2 = float(input("Digite o segundo número: "))

        # Tomada de decisão baseada na operação escolhida
        if operacao == "+":
            resultado = somar(num1, num2)
        elif operacao == "-":
            resultado = subtrair(num1, num2)
        elif operacao == "*":
            resultado = multiplicar(num1, num2)
        elif operacao == "/":
            resultado = dividir(num1, num2)
        elif operacao == "%":
            resultado = porcentagem(num1, num2)
        else:
            print("Operação inválida! Use apenas +, -, *, / ou %.")
            return

        # Exibição do resultado usando f-strings
        print("-" * 36)
        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        print("=" * 36)

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos!")

# 3. Ponto de entrada do script
if __name__ == "__main__":
    main()