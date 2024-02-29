import random
import csv
import csv
import json
import os
import shutil

#1-)
def contar_vogais(string):
    count_vogais = 0
    string = string.lower()
    vogais = 'eiauo'
    for i in string:
        for j in vogais:
            if(i == j ):
                count_vogais += 1
    print(count_vogais)

#contar_vogais('aaavsdwooo')

#2-)
def substituir_letra(letra, letra_sub, string_original):
    string_original = string_original.replace(letra ,letra_sub)
    print(string_original)

#substituir_letra('a', 'o', 'carro')

#3-)
def return_numero_palavras(string_palavras):
    string_dividida = string_palavras.split()
    print(len(string_dividida))


#return_numero_palavras('asdad dwqj13j asdas')

#4-)
def count_words(string_words, word_check):
    string_words = string_words.split()
    count_words = 0
    for l in string_words:
        if(l == word_check):
            count_words += 1
    print(count_words)

#count_words('asd asd asd asd dsa', 'asd')

#5-)
def k_maiores_elementos(lista, k):
    maiores_elementos = []

    for i in range(k):
        max_valor = max(lista)
        maiores_elementos.append((lista.index(max_valor), max_valor))
        lista.remove(max_valor)

    return maiores_elementos

#k_maiores_elementos( [4, 8, 2, 6, 1, 9, 3, 7, 5], 3)

#6-)
def soma_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("As matrizes devem ter as mesmas dimensões para serem somadas.")

    resultado = [[0 for _ in range(len(matriz1[0]))] for _ in range(len(matriz1))]

    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]

    print("Matriz 1:")
    for linha in matriz1:
        print(linha)

    print("\nMatriz 2:")
    for linha in matriz2:
        print(linha)

    print("\nResultado da Soma:")
    for linha in resultado:
        print(linha)

#soma_matrizes([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]])

#7-)
def encontrar_intersecao(lista1, lista2):
    intersecao = []

    for elemento in lista1:
        if elemento in lista2 and elemento not in intersecao:
            intersecao.append(elemento)

    print(intersecao)

#encontrar_intersecao([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])

#8-)
def embaralhar_lista(lista):
    lista_embaralhada = lista.copy()
    random.shuffle(lista_embaralhada)
    print(lista_embaralhada)

#embaralhar_lista([1, 2, 3, 4, 5, 6, 7, 8, 9])

#9-)

def encontrar_par_com_soma(lista, alvo):
    visto = set()

    for elemento in lista:
        complemento = alvo - elemento
        if complemento in visto:
            print(complemento, elemento)
        visto.add(elemento)

    print()

#encontrar_par_com_soma([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)

#10-)
def calcular_frequencia(texto, palavra):
    texto = texto.lower()
    palavras = texto.split()
    ocorrencias = 0

    for palavra_texto in palavras:
        if palavra_texto == palavra.lower():
            ocorrencias += 1

    print(ocorrencias)


#calcular_frequencia("Este é um exemplo de texto Este texto contém a palavra exemplo várias vezes.","exemplo")

#11-)
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos_na_lista(lista):
    primos = [numero for numero in lista if eh_primo(numero)]
    print(primos)

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#numeros_primos_na_lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

#12-)
def encontrar_menor_string(lista_strings):
    if not lista_strings:
        return None  # Retorna None se a lista estiver vazia

    menor_string = lista_strings[0]

    for string in lista_strings:
        if len(string) < len(menor_string):
            menor_string = string

    print(menor_string)

#encontrar_menor_string(["banana", "maçã", "uva", "abacaxi", "pêra", "kiwi"])

#13-)
def ler_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print(f'O arquivo {caminho_arquivo} não foi encontrado.')
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

#ler_arquivo('arquivo.txt')

#14-)
def ler_arquivo_csv(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8', newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            cabecalho = next(leitor_csv, None)
            linhas = []
            
            for linha in leitor_csv:
                linhas.append(linha)
            
            print(cabecalho, linhas)
    except FileNotFoundError:
        print(f'O arquivo {caminho_arquivo} não foi encontrado.')
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")


#ler_arquivo_csv('arquivo.csv')

#15-)
def ler_arquivo_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)
            print(dados_json)
    except FileNotFoundError:
        print(f'O arquivo {caminho_arquivo} não foi encontrado.')
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo JSON: {e}")


#ler_arquivo_json('arquivo.json')

#16-)
def consolidar_arquivos_texto(diretorio, arquivo_destino):
    try:
        # Lista todos os arquivos no diretório
        arquivos = [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
        
        with open(arquivo_destino, 'w', encoding='utf-8') as arquivo_consolidado:
            for nome_arquivo in arquivos:
                caminho_arquivo = os.path.join(diretorio, nome_arquivo)
                
                with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_atual:
                    conteudo = arquivo_atual.read()
                    arquivo_consolidado.write(f'--- Conteúdo de {nome_arquivo} ---\n')
                    arquivo_consolidado.write(conteudo)
                    arquivo_consolidado.write('\n\n')

        print(arquivo_consolidado)
    except Exception as e:
        print(f"Ocorreu um erro ao consolidar os arquivos: {e}")

#consolidar_arquivos_texto('dir-textos', 'arquivo.txt')

#17-)
def encontrar_mes_maior_venda(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8', newline='') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            mes_maior_venda = None
            maior_valor_venda = 0
            
            for linha in leitor_csv:
                mes = linha['Mês']
                valor_venda = float(linha['Valor de Venda'])
                
                if valor_venda > maior_valor_venda:
                    mes_maior_venda = mes
                    maior_valor_venda = valor_venda

            print(mes_maior_venda)
    except FileNotFoundError:
        print(f'O arquivo {caminho_arquivo} não foi encontrado.')
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")


#encontrar_mes_maior_venda('arquivo-vendas.csv')

#18-)
def encontrar_mes_menos_venda(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8', newline='') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            mes_menos_venda = None
            menor_valor_venda = float('inf')
            
            for linha in leitor_csv:
                mes = linha['Mês']
                valor_venda = float(linha['Valor de Venda'])
                
                if valor_venda < menor_valor_venda:
                    mes_menos_venda = mes
                    menor_valor_venda = valor_venda

            print(mes_menos_venda)
    except FileNotFoundError:
        print(f'O arquivo {caminho_arquivo} não foi encontrado.')
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")

#encontrar_mes_menos_venda('arquivo-vendas.csv')

#19-)
def calcular_soma_vendas_por_vendedor(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8', newline='') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            
            # Dicionário para armazenar a soma de vendas por vendedor
            soma_vendas_por_vendedor = {}
            
            # Itera sobre as linhas do arquivo CSV
            for linha in leitor_csv:
                vendedor = linha['Vendedor']
                valor_venda = float(linha['Valor de Venda'])
                
                # Atualiza a soma de vendas do vendedor
                soma_vendas_por_vendedor[vendedor] = soma_vendas_por_vendedor.get(vendedor, 0) + valor_venda

            print(soma_vendas_por_vendedor)
    except FileNotFoundError:
        print(f'O arquivo {caminho_arquivo} não foi encontrado.')
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")

#calcular_soma_vendas_por_vendedor('arquivo-vendas.csv')

#20-)
def encontrar_vendedores_mais_menos_vendas(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8', newline='') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            
            soma_vendas_por_vendedor = {}
            
            for linha in leitor_csv:
                vendedor = linha['Vendedor']
                valor_venda = float(linha['Valor de Venda'])
                
                soma_vendas_por_vendedor[vendedor] = soma_vendas_por_vendedor.get(vendedor, 0) + valor_venda

            vendedor_mais_vendeu = max(soma_vendas_por_vendedor, key=soma_vendas_por_vendedor.get)
            vendedor_menos_vendeu = min(soma_vendas_por_vendedor, key=soma_vendas_por_vendedor.get)

            print(vendedor_mais_vendeu, vendedor_menos_vendeu)
    except FileNotFoundError:
        print(f'O arquivo {caminho_arquivo} não foi encontrado.')
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")


encontrar_vendedores_mais_menos_vendas('arquivo-vendas.csv')
