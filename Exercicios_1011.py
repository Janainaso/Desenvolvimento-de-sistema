
# 1. Números Primos em Intervalo
#Escreva uma função primos_no_intervalo(a, b) que retorna uma lista com todos os números primos entre a e b.
def primos_no_intervalo(a, b):
    primos = []
    for n in range(max(2, a), b + 1):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            primos.append(n)
    return primos


# 2. Ordena e Remove Duplicatas
#Implemente uma função ordenar_sem_repeticao(lista) que retorna uma lista ordenada sem elementos repetidos.
def ordenar_sem_repeticao(lista):
    return sorted(set(lista))


# 3. Soma dos Dígitos
#Crie uma função soma_digitos(n) que recebe um número inteiro e retorna a soma de seus dígitos.
def soma_digitos(n):
    return sum(int(d) for d in str(abs(n)))


# 4. Palíndromo
#Faça uma função eh_palindromo(texto) que verifica se uma string é palíndroma (ignorar maiúsculas/minúsculas e espaços).
def eh_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]


# 5. Frequência de Palavras
#Implemente uma função frequencia_palavras(texto) que recebe uma frase e retorna um dicionário com cada palavra e sua frequência.
def frequencia_palavras(texto):
    palavras = texto.lower().split()
    freq = {}
    for palavra in palavras:
        palavra = palavra.strip(".,!?;:")
        freq[palavra] = freq.get(palavra, 0) + 1
    return freq


# 6. Média dos Elementos
#Implemente uma função media_lista(lista) que retorna a média dos elementos de uma lista de números. Se a lista estiver vazia, retorne None.
def media_lista(lista):
    if not lista:
        return None
    return sum(lista) / len(lista)