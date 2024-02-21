import csv



def limpa_dados():
# Nome do arquivo de entrada
    input_file = 'arquivo_bruto.txt'

    # Nome do arquivo CSV de saída
    output_file = 'dados.csv'



    # Abre o arquivo de entrada para leitura
    with open(input_file, 'r') as infile:
        # Lê as linhas do arquivo de entrada
        data = infile.readlines()

    # Abre o arquivo CSV de saída para escrita
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        # Escreve os cabeçalhos no arquivo CSV
        header = ["idlogs", "data","hora", "dados_recebidos"]
        writer.writerow(header)

        # Escreve os dados no arquivo CSV
        for line in data:
            # Remove os pipes "|" e divide os valores
            values = line.strip().replace('|', '').split()

            # Verifica se há pelo menos três valores na linha
            if len(values) >= 4:
                # Adiciona o número 1 ao final de cada valor em "dados_recebidos"
                values[3] += '1'

            writer.writerow(values)

