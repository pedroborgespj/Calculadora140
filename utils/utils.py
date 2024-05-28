import csv

def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            tabela = csv.reader(massa, delimiter=',')
            next(tabela)
            for linha in tabela:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo nao encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')