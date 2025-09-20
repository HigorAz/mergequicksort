import time
import sys
import random
import csv
import matplotlib.pyplot as plt
import numpy as np

sys.setrecursionlimit(200000)

def ler_arquivo(nome_arquivo):
    """Lê números de um arquivo, um por linha, e retorna uma lista de inteiros."""
    try:
        with open(nome_arquivo, 'r') as f:
            return [int(line.strip()) for line in f]
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado. Certifique-se de que ele está na mesma pasta que o script.")
        return None
    except ValueError:
        print(f"Erro: O arquivo '{nome_arquivo}' contém linhas que não são números inteiros.")
        return None

# --- Implementação do Merge Sort ---

def merge(arr, p, q, r, stats):
    """Intercala duas sub-listas ordenadas."""
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[p + i]
    for j in range(n2):
        R[j] = arr[q + 1 + j]

    i, j, k = 0, 0, p
    while i < n1 and j < n2:
        stats['comparacoes'] += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        stats['movimentacoes'] += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        stats['movimentacoes'] += 1
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        stats['movimentacoes'] += 1
        j += 1
        k += 1

def merge_sort_recursivo(arr, p, r, stats):
    """Função recursiva principal do Merge Sort."""
    if p < r:
        q = (p + r) // 2
        merge_sort_recursivo(arr, p, q, stats)
        merge_sort_recursivo(arr, q + 1, r, stats)
        merge(arr, p, q, r, stats)

def merge_sort(arr):
    """Prepara e inicia o Merge Sort, retornando as estatísticas."""
    stats = {'comparacoes': 0, 'movimentacoes': 0}
    arr_copy = arr[:] # Cria uma cópia para não alterar o array original
    start_time = time.time()
    merge_sort_recursivo(arr_copy, 0, len(arr_copy) - 1, stats)
    end_time = time.time()
    stats['tempo'] = end_time - start_time
    return stats

# --- Implementação do Quick Sort ---
# Baseado nos slides 68 e 70 do material de aula

def partition(arr, p, r, stats):
    """Particiona o array usando o último elemento como pivô."""
    pivo = arr[r]
    i = p - 1
    for j in range(p, r):
        stats['comparacoes'] += 1
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            stats['trocas'] += 1
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    stats['trocas'] += 1
    return i + 1

def quick_sort_recursivo(arr, p, r, stats, tipo_pivo):
    """Função recursiva principal do Quick Sort."""
    if p < r:
        if tipo_pivo == 'aleatorio':
            rand_idx = random.randint(p, r)
            arr[rand_idx], arr[r] = arr[r], arr[rand_idx]
            # Esta troca é parte da estratégia, não do algoritmo de ordenação em si.
            # Podemos optar por contar ou não. Aqui, contamos para refletir todo o trabalho.
            stats['trocas'] += 1
            
        q = partition(arr, p, r, stats)
        quick_sort_recursivo(arr, p, q - 1, stats, tipo_pivo)
        quick_sort_recursivo(arr, q + 1, r, stats, tipo_pivo)

def quick_sort(arr, tipo_pivo='ultimo'):
    """Prepara e inicia o Quick Sort, retornando as estatísticas."""
    stats = {'comparacoes': 0, 'trocas': 0}
    arr_copy = arr[:] # Cria uma cópia para não alterar o array original
    start_time = time.time()
    quick_sort_recursivo(arr_copy, 0, len(arr_copy) - 1, stats, tipo_pivo)
    end_time = time.time()
    stats['tempo'] = end_time - start_time
    return stats

# --- Funções para Relatório ---

def salvar_resultados_csv(resultados, nome_arquivo):
    """Salva o dicionário de resultados em um arquivo CSV."""
    print(f"\nSalvando resultados em '{nome_arquivo}'...")
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Tamanho_Entrada', 'Algoritmo', 'Tempo_Execucao_s', 'Comparacoes', 'Trocas_ou_Movimentacoes'])

        for tamanho, algos in resultados.items():
            for nome_algo, stats in algos.items():
                trocas_ou_mov = stats.get('trocas', stats.get('movimentacoes', 0))
                writer.writerow([
                    tamanho,
                    nome_algo,
                    f"{stats['tempo']:.6f}",
                    stats['comparacoes'],
                    trocas_ou_mov
                ])
    print("Resultados salvos com sucesso.")

def gerar_graficos(resultados):
    """Gera e salva gráficos de barra comparando as métricas dos algoritmos."""
    print("\nGerando gráficos comparativos...")
    tamanhos = sorted(resultados.keys())
    # Garante uma ordem consistente dos algoritmos no gráfico
    algoritmos = sorted(list(resultados[tamanhos[0]].keys()))
    
    metricas = {
        'tempo': 'Tempo de Execução (s)',
        'comparacoes': 'Número de Comparações',
        'trocas_mov': 'Número de Trocas/Movimentações'
    }
    
    for metrica_key, metrica_titulo in metricas.items():
        plt.figure(figsize=(12, 7))
        
        dados_grafico = {algo: [] for algo in algoritmos}
        for tamanho in tamanhos:
            for algo in algoritmos:
                if metrica_key == 'trocas_mov':
                    valor = resultados[tamanho][algo].get('trocas', resultados[tamanho][algo].get('movimentacoes', 0))
                else:
                    valor = resultados[tamanho][algo][metrica_key]
                dados_grafico[algo].append(valor)
        
        x = np.arange(len(tamanhos))
        width = 0.25
        
        for i, algo in enumerate(algoritmos):
            pos = x - width + (i * width)
            bars = plt.bar(pos, dados_grafico[algo], width, label=algo)
            plt.bar_label(bars, fmt='{:,.0f}', fontsize=9, rotation=45, padding=3)

        plt.ylabel(metrica_titulo)
        plt.title(f'Comparativo de Desempenho: {metrica_titulo}')
        plt.xticks(x, [f'{t:,} elementos'.replace(',', '.') for t in tamanhos])
        plt.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        nome_arquivo_grafico = f"grafico_{metrica_key}.png"
        plt.savefig(nome_arquivo_grafico)
        print(f"Gráfico '{nome_arquivo_grafico}' salvo com sucesso.")
    plt.close('all')

# --- Bloco Principal de Execução ---
if __name__ == '__main__':
    arquivos_entrada = ['entrada_20000.txt', 'entrada_40000.txt', 'entrada_160000.txt']
    resultados = {}

    for arquivo in arquivos_entrada:
        print(f"--- Processando arquivo: {arquivo} ---")
        numeros = ler_arquivo(arquivo)
        if numeros is None:
            continue
        
        tamanho = len(numeros)
        resultados[tamanho] = {}

        # Merge Sort
        stats_mergesort = merge_sort(numeros)
        resultados[tamanho]['Merge Sort'] = stats_mergesort
        print(f"Merge Sort - Tempo: {stats_mergesort['tempo']:.4f}s, Comparações: {stats_mergesort['comparacoes']:,}, Movimentações: {stats_mergesort['movimentacoes']:,}")

        # Quick Sort (Pivô Fixo no último elemento)
        stats_quicksort_fixo = quick_sort(numeros, tipo_pivo='ultimo')
        resultados[tamanho]['Quick Sort (Pivô Fixo)'] = stats_quicksort_fixo
        print(f"Quick Sort (Pivô Fixo) - Tempo: {stats_quicksort_fixo['tempo']:.4f}s, Comparações: {stats_quicksort_fixo['comparacoes']:,}, Trocas: {stats_quicksort_fixo['trocas']:,}")
        
        # Quick Sort (Pivô Aleatório)
        stats_quicksort_aleatorio = quick_sort(numeros, tipo_pivo='aleatorio')
        resultados[tamanho]['Quick Sort (Pivô Aleatório)'] = stats_quicksort_aleatorio
        print(f"Quick Sort (Pivô Aleatório) - Tempo: {stats_quicksort_aleatorio['tempo']:.4f}s, Comparações: {stats_quicksort_aleatorio['comparacoes']:,}, Trocas: {stats_quicksort_aleatorio['trocas']:,}")
        print("-" * 40 + "\n")

    if resultados:
        salvar_resultados_csv(resultados, 'resultados_ordenacao.csv')
        gerar_graficos(resultados)
    else:
        print("\nNenhum resultado foi gerado. Verifique se os arquivos de entrada existem e estão corretos.")