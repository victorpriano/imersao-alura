# 🧮 Calculadora em Python — Imersão Engenharia de Software com IA

> **Status:**
 - Desafio 1 Concluído ✅  
 - Desafio 2 Concluído ✅  
> **Curso / Evento:** Imersão de Engenharia de Software com IA — **Alura**  

> **Foco de Aprendizado:** Google AI Studio (Ambiente & Capacidades) / Antigravity

> **Linguagem Utilizada:** Python 3.8+

---

## 📌 Sobre o Projeto

Este repositório contém a entrega dos **desafios realizados** durante a **Imersão de Engenharia de Software com IA da Alura**.

O objetivo central da imersão foi mergulhar nas tecnologias e ferramentas avançadas do ecossistema do Google, com ênfase no Google AI Studio e no Antigravity. O desenvolvimento da calculadora serviu como laboratório prático para exercitar esse fluxo: entender como orquestrar modelos fundacionais, definir requisitos estritos de engenharia, refinar código iterativamente e construir soluções resilientes e profissionais com assistência de IA.
---

## 🧠 Conceitos e Aprendizados sobre o Google AI Studio

- Durante a primeira etapa da Imersão, a ênfase esteve em explorar o ecossistema e as ferramentas oferecidas pelo **Google AI Studio**. Os principais aprendizados consolidados foram:

| Conceito / Pilar do Google AI Studio | O Que Foi Aprendido e Aplicado na Prática |
| :--- | :--- |
| **Engenharia de Prompt para Código** | Formulação de instruções precisas, contexto delimitado e especificações claras de requisitos, permitindo que o modelo produza uma solução organizada, modular e sem alucinações. |
| **Refinamento Iterativo (*Chat-driven Iteration*)** | Utilização da janela de contexto contínua do AI Studio para solicitar melhorias incrementais, como tratamento defensivo de erros, validações e documentação estruturada. |
| **Arquitetura Assistida por IA** | Capacidade de instruir o AI Studio a estruturar código seguindo boas práticas de engenharia de software (separação de responsabilidades, modularidade e padrões PEP 8). |
| **Instruções de Sistema (*System Instructions*)** | Compreensão de como orientar o comportamento, tom, persona técnica e restrições do modelo antes da execução das tarefas. |
| **Exploração de Modelos Gemini** | Entendimento de como os modelos do ecossistema Google lidam com raciocínio lógico, depuração de erros em tempo real e geração de código executável. |
| **Prototipagem Acelerada de Software** | Transformação imediata de uma necessidade de negócio em um programa funcional, reduzindo drasticamente o ciclo de ideação, codificação e validação. |

---

## 🚀 Conceitos e Aprendizados sobre o Google Antigravity

- Na segunda etapa da Imersão, aprofundamos no **Antigravity**, a plataforma e assistente de desenvolvimento agêntico do Google. Os principais conceitos consolidados foram:

| Conceito / Recurso do Antigravity | Aplicação Prática no Ciclo de Desenvolvimento |
| :--- | :--- |
| **Assistência Agêntica Autônoma** | Capacidade do agente de ler o contexto do repositório, inspecionar código existente, propor planos e executar alterações pontuais sem perder a estrutura original. |
| **Execução Segura e Testes Automatizados** | Criação e execução de baterias de testes automatizados (unittest), simulando entradas de usuário e validando edge cases (divisão por zero, porcentagens e entradas inválidas). |
| **Ambiente Híbrido (Terminal / Sandbox)** | Compreensão do isolamento seguro de ferramentas e comandos locais, permitindo gerenciar dependências, ambiente de execução e ferramentas do sistema operacional. |
| **Governança de Código com Git e .gitignore** | Criação e manutenção de políticas de arquivos ignorados (.gitignore), garantindo um repositório limpo e sem artefatos temporários ou caches (__pycache__, .venv). |
| **Evolução Iterativa de Features** | Expansão incremental do software (como a implementação da operação de porcentagem %), respeitando a arquitetura modular e os padrões PEP 8 já estabelecidos. |

---

## ✨ O Software Desenvolvido: Calculadora em Python

Como resultado das instruções e refinamentos trabalhados no Google AI Studio, foi gerada uma calculadora funcional com:
- As 4 operações matemáticas fundamentais: Adição (`+`), Subtração (`-`), Multiplicação (`*`) e Divisão (`/`).
- Tratamento preventivo contra divisão por zero (`ZeroDivisionError`).
- Blindagem contra entradas inválidas de texto (`try...except ValueError`).
- Funções desacopladas com `def`, retorno via `return` e ponto de entrada seguro `if __name__ == "__main__":`.

---

## 💻 Como Executar o Projeto

### Pré-requisitos
- **Python 3.8+** instalado no ambiente ([python.org](https://www.python.org/downloads/)).
- **Git** configurado na máquina (opcional, para controle de versão).

### 1. Clonar o Repositório
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd imersao-alura
```

### 2. Executar a Calculadora
Execute o script interativo através do terminal:

```bash
# No Windows:
python src/calculadora.py
# ou:
py src/calculadora.py

# No Linux/macOS:
python3 src/calculadora.py
```

### 3. Executar os Testes Automatizados
O projeto conta com uma suíte de testes unitários (unittest) que valida todas as operações e fluxos de entrada da CLI:

```bash
# No Windows:
python -m unittest tests/test_calculadora.py

# No Linux/macOS:
python3 -m unittest tests/test_calculadora.py
```

---

## 📂 Código Gerado no Google AI Studio (`calculadora.py`)

```python
# ========================================================
# CALCULADORA BÁSICA EM PYTHON
# Gerada via Google AI Studio — Imersão Alura
# ========================================================

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
    """Retorna a divisão de a por b com validação defensiva."""
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

def main():
    print("=" * 36)
    print("       CALCULADORA EM PYTHON        ")
    print("=" * 36)
    print("Operações disponíveis:")
    print("  + : Adição")
    print("  - : Subtração")
    print("  * : Multiplicação")
    print("  / : Divisão")
    print("-" * 36)

    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Escolha a operação (+, -, *, /): ").strip()
        num2 = float(input("Digite o segundo número: "))

        if operacao == "+":
            resultado = somar(num1, num2)
        elif operacao == "-":
            resultado = subtrair(num1, num2)
        elif operacao == "*":
            resultado = multiplicar(num1, num2)
        elif operacao == "/":
            resultado = dividir(num1, num2)
        else:
            print("Operação inválida! Use apenas +, -, * ou /.")
            return

        print("-" * 36)
        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        print("=" * 36)

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos!")

if __name__ == "__main__":
    main()
