Gerador de Gráficos a partir de Dados do ChatBot
Este programa em Python é projetado para criar gráficos com base nos dados extraídos do banco de dados do ChatBot.

Pré-requisitos
Antes de executar o programa, certifique-se de ter instalado as seguintes bibliotecas Python listadas no arquivo requirements.txt. Você pode instalá-las usando o comando:

pip install -r requirements.txt

Atualização dos Dados
O programa não possui conexão direta com o banco de dados. Para atualizar o gráfico com novos dados, siga estes passos:

Substitua o arquivo "arquivo_bruto.txt" por uma nova extração do banco de dados.
Renomeie o novo arquivo para que tenha o mesmo nome que o arquivo original.
Execução
Após atualizar o arquivo manualmente, execute o arquivo grafico_geral.exe
(Nesta primeira versão os executaveis não estão funcionando e foram removidos temporariamente, então será necessario executar o arquivo "grafico_geral.py" por meio do terminal). 
Isso abrirá uma janela onde você poderá:

Selecionar o mês e o ano desejados para gerar o gráfico.
Clicar em "Gerar Gráfico Mensal" para visualizar o gráfico de acessos por dia do mês selecionado.
Clicar em "Gerar Gráfico Anual" para visualizar o gráfico de acessos mensais do ano selecionado.
O programa gera automaticamente gráficos em HTML toda vez que é executado. Os gráficos em HTML são salvos na pasta do programa.

Observações
Certifique-se de que os dados no arquivo "arquivo_bruto.txt" estejam no formato esperado pelo programa para garantir resultados precisos.
A legenda para o gráfico se encontra na pasta do programa