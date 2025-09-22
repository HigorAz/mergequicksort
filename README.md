<p align="center">
    <img loading="lazy" src="https://files.engaged.com.br/5db0810e95b4f900077e887e/account/5db0810e95b4f900077e887e/xMCS8NFKTMqwhefy8WLd_catolica-horizontal.png" width="300">
</p>

## Situação do Projeto
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue)

# Comparativo de Merge Sort vs Quick Sort

Este repositório contém uma implementação em **Python** dos algoritmos de ordenação **Merge Sort** e **Quick Sort** com coleta de métricas de desempenho e **relatório automatizado** em CSV + **gráficos** gerados com Matplotlib. O projeto atende ao pedido da atividade (abaixo) e já está pronto para rodar sobre três arquivos de entrada (`entrada_20000.txt`, `entrada_40000.txt`, `entrada_160000.txt`).

> **Objetivo da atividade**  
> Implementar MergeSort e QuickSort, medir e comparar o tempo de execução, registrar resultados para 20k, 40k e 160k elementos. O tempo medido **não** deve considerar a leitura do arquivo de entrada.

---

## Estrutura esperada do projeto

```
.
├── main.py                      # Script com os algoritmos e geração de relatório/gráficos
├── entrada_20000.txt            # Inteiros (um por linha)
├── entrada_40000.txt            # Inteiros (um por linha)
├── entrada_160000.txt           # Inteiros (um por linha)
└── (gerados) resultados_ordenacao.csv, grafico_tempo.png, grafico_comparacoes.png, grafico_trocas_mov.png
```

> **Observação:** O código fornecido no `main.py` já vem configurado para ler os três arquivos acima e gerar os relatórios automaticamente.

---

## Código

- Lê arquivos texto contendo **um inteiro por linha**.
- Executa:
  - **Merge Sort** (divide‑e‑conquista, estável, `O(n log n)`).
  - **Quick Sort** em duas variações:
    - **Pivô fixo**: último elemento do subarray.
    - **Pivô aleatório**: índice aleatório por partição.
- Mede **tempo de execução** (apenas a fase de ordenação), **número de comparações** e **número de trocas/movimentações**.
- Salva um **CSV** consolidando as métricas por tamanho de entrada e algoritmo.
- Gera **gráficos de barras** comparando: Tempo, Comparações e Trocas/Movimentações.

As funções principais são:
- `merge_sort(arr)` / `quick_sort(arr, tipo_pivo='ultimo'|'aleatorio')`: executam o algoritmo e retornam um dicionário de estatísticas.
- `salvar_resultados_csv(resultados, 'resultados_ordenacao.csv')`: gera o relatório em CSV.
- `gerar_graficos(resultados)`: cria três arquivos PNG com comparações visuais.

---

## Métricas coletadas

- `tempo` — segundos de CPU/relogio da fase de ordenação.
- `comparacoes` — contagem de comparações realizadas entre elementos.
- `trocas` *(Quick Sort)* ou `movimentacoes` *(Merge Sort)* — operações de troca/escrita registradas.

O arquivo **`resultados_ordenacao.csv`** terá o formato:

| Tamanho_Entrada | Algoritmo                 | Tempo_Execucao_s | Comparacoes | Trocas_ou_Movimentacoes |
|----------------:|---------------------------|------------------:|------------:|------------------------:|
| 20000           | Merge Sort                | 0.123456          | 300000      | 400000                  |
| 20000           | Quick Sort (Pivô Fixo)    | 0.234567          | 350000      | 250000                  |
| 20000           | Quick Sort (Pivô Aleatório)| 0.210000         | 320000      | 240000                  |
| ...             | ...                       | ...               | ...         | ...                     |

Os gráficos gerados:
- `grafico_tempo.png`
- `grafico_comparacoes.png`
- `grafico_trocas_mov.png`

---

## Como executar

### 1) Pré-requisitos
- **Python 3.10+**
- Pacotes: `matplotlib`, `numpy`

Instale as dependências (recomendado usar um ambiente virtual):

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install matplotlib numpy
```

### 2) Posicione os arquivos de entrada
Garanta que `entrada_20000.txt`, `entrada_40000.txt` e `entrada_160000.txt` estão na **mesma pasta** do `main.py`.  
Cada arquivo deve conter **um inteiro por linha**.

### 3) Execute o script
```bash
python main.py
```

Saídas esperadas no diretório:
- `resultados_ordenacao.csv`
- `grafico_tempo.png`
- `grafico_comparacoes.png`
- `grafico_trocas_mov.png`

> Se algum arquivo de entrada não for encontrado ou tiver valores inválidos, o script emitirá mensagens de erro e **pulará** aquele conjunto, seguindo para os demais.

---

## Contribuidores
A equipe envolvida nesta atividade é constituída por alunos da 7ª Fase (20252) do curso de Engenharia de Software do Centro Universitário Católica SC de Jaraguá do Sul.

<div align="center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/HigorAz"><img loading="lazy" src="https://avatars.githubusercontent.com/u/141787745?v=4" width="115"><br><sub>Higor Azevedo</sub></a></td>
    <td align="center"><a href="https://github.com/AoiteFoca"><img loading="lazy" src="https://avatars.githubusercontent.com/u/141975272?v=4" width="115"><br><sub>Nathan Cielusinski</sub></a></td>
    <td align="center"><a href="https://github.com/MrNicolass"><img loading="lazy" src="https://avatars.githubusercontent.com/u/80847876?v=4" width="115"><br><sub>Nicolas Gustavo 
  </tr>
</div>
