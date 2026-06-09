''' 
Contexto

Pedro é um estudante universitário entusiasta do uso do GitHub e pos-
sui grande preocupação com organização. Para gerenciar seus materiais aca-
dêmicos, ele criou um repositório privado chamado “coisas-da-universidade”.

Após isso, realizou o clone do repositório em sua máquina local, onde pretende
armazenar e versionar conteúdos relacionados à sua vida acadêmica.

Inicialmente, Pedro criou diversos diretórios para organizar suas ativi-
dades, como:

• Estágios;
• Monitorias;
• Iniciação Científica;
• entre outros ...

No entanto, ao tentar versionar esses diretórios utilizando o Git, ele per-
cebeu um comportamento importante:

O Git não versiona diretórios vazios.

Por convenção, para contornar essa limitação, utiliza-se um arquivo cha-
mado .gitkeep dentro de diretórios vazios, permitindo que esses diretórios se-
jam versionados. Além disso, essa convenção estabelece que o arquivo .gitkeep
deve existir apenas em diretórios vazios.

Objetivo

Desenvolver um programa em Python que automatize esse processo den-
tro de um repositório local.
'''


# importando as bibliotecas necessárias
import json
import os
from datetime import datetime

class GerenciadorLog: # classe que vai gerenciar a criação e a atualização dos arquivos de log
    def __init__(self, log_dir: str = "logs", log_file: str = "log.json"):
    # construtor da classe. definiu o nome da pasta onde os logs ficarão e o nome do arquivo de log (histórico)
        self.log_dir = log_dir
        self.log_file = log_file
        self.log_path = os.path.join(self.log_dir, self.log_file) # define o caminho do arquivo de log no computador
        # pega a pasta "logs" e "log.json" e junta os dois para formar o endereço único logs/log.json, sem problemas com as diferenças entre sistemas operacionais

    def garantia_diretorio(self): # garante que o diretótio de logs existe!
        if not os.path.exists(self.log_dir): # se a pasta de logs não existir
            os.makedirs(self.log_dir) # cria a pasta de logs

    def salvar_execucao(self, criados: list, removidos: list): # salva a execução do programa, tanto o que foi criado quanto o que foi removido
        # registro atual:
        novo_registro = { # dict
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # data e hora da execução do programa
            "arquivos_criados": criados, # lista de arquivos criados
            "arquivos_removidos": removidos # lista de arquivos removidos
        }

        historico = [] # lista vazia para armazenar o histórico de execuções

        # se o arquivo já existir, vai ler o histórico para não sobreescrever o que já tiver
        if os.path.exists(self.log_path): # se o arquivo de log já existir
            with open(self.log_path, "r", encoding = "utf-8") as f: # abre o arquivo de log para leitura
                try:
                    historico = json.load(f) # tenta carregar o histórico do arquivo de log
                except json.JSONDecodeError: # se o arquivo de log estiver vazio ou com formato inválido
                    historico = [] # mantém o histórico como uma lista vazia

        historico.append(novo_registro) # adiciona o novo registro ao histórico

        # salva no formato json 
        with open(self.log_path, "w", encoding = "utf-8") as f: # abre o arquivo de log para escrita
            json.dump(historico, f, indent = 4, ensure_ascii=False) # salva o histórico no arquivo de log com indentação para melhor leitura


class GerenciadorGitKeep: # classe que vai gerenciar a criação e remoção dos arquivos .gitkeep
    def __init__(self, root_path: str = "."): # construtor da classe. define o caminho raiz onde o programa vai procurar por diretórios vazios
        self.root_path = root_path # salva ponto de partida onde vai começar a procurar por diretórios vazios
        self.gerenciador_log = GerenciadorLog() # instancia a classe de gerenciamento de logs

        # lisras temporárias que vão armazenar as ações da execução atual
        self.criados = [] # lista para armazenar os arquivos .gitkeep criados
        self.removidos = [] # lista para armazenar os arquivos .gitkeep removidos

    def percorrer_diretorios(self): # percorre os diretórios e aplica regras do .gitkeep
        self.criados.clear() # limpa a lista de arquivos criados para a execução atual
        self.removidos.clear() # limpa a lista de arquivos removidos para a execução atual
        # os.walk percorre a árvore de cima a baixo, visitando cada diretório e seus subdiretórios
        for dirpath, dirnames, filenames in os.walk(self.root_path): # percorre os diretórios a partir do caminho raiz
            # tem que ignorar o diretório de logs para não criar arquivos .gitkeep lá
            if self.gerenciador_log.log_dir in dirpath.split(os.sep): # dirpath guarda o caminho do diretório atual. split(os.sep) divide o caminho em partes usando o separador de diretórios do sistema operacional
                continue  # se "logs" estiver em qualquer parte do caminho do diretório atual, ignora para não criar arquivos .gitkeep lá
            if self.gerenciador_log.log_dir in dirnames: # se "logs" estiver na lista de nomes de diretórios
                dirnames.remove(self.gerenciador_log.log_dir) # remove o diretório de logs da lista de diretórios a serem percorridos, ou seja, não entra
            if dirpath == self.root_path: # se a pasta atual que tá percorrendo for a pasta raiz,
                continue # ignora o diretório raiz para não criar um arquivo .gitkeep lá -> evitar que crie o .gitkeep por não ter arquivo solto na raiz!
            gitkeep_path = os.path.join(dirpath, ".gitkeep") # define o caminho do arquivo .gitkeep no diretório atual
            conteudo_diretorio_sem_gitkeep = [f for f in filenames if f != ".gitkeep"] + dirnames # lista com os nome dos arquivos e subpastas no diretório, excluindo o .gitkeep
            if not conteudo_diretorio_sem_gitkeep: # se o diretório estiver vazio
                if not os.path.exists(gitkeep_path): # se não tiver arquivo .gitkeep
                    with open(gitkeep_path, "w", encoding = "utf-8") as f: # cria o arquivo .gitkeep
                        pass # cria arquivo vazio
                    self.criados.append(gitkeep_path) # adiciona o caminho do arquivo .gitkeep criado à lista de criados
            else: # se o diretório não estiver vazio
                if os.path.exists(gitkeep_path): # se tiver arquivo .gitkeep em diretório não vazio (não pode)
                    os.remove(gitkeep_path) # remove o arquivo .gitkeep
                    self.removidos.append(gitkeep_path) # adiciona o caminho do arquivo .gitkeep removido à lista de removidos

        # depois de acabar, tem que salvar o que fez no log
        self.gerenciador_log.salvar_execucao(self.criados, self.removidos) # salva a execução atual no log, passando as listas de arquivos criados e removidos
        self.exibir_resultados() # exibe os resultados da execução atual

    def exibir_resultados(self): # exibe os resultados da execução atual
        print("== AUTOMAÇÃO CONCLUÍDA ==") 
        print(f"Arquivos .gitkeep criados: {len(self.criados)}") # exibe a quantidade de arquivos .gitkeep criados
        print(f"Arquivos .gitkeep removidos: {len(self.removidos)}") # exibe a quantidade de arquivos .gitkeep removidos
        print(f"Log salvo em: {self.gerenciador_log.log_path}\n") # exibe o caminho do arquivo de log atualizado


# execução principal:
if __name__ == "__main__": # verifica se o script está sendo executado diretamente (e não importado como módulo)
    gerenciador = GerenciadorGitKeep(root_path=".") # instancia a classe de gerenciamento de arquivos .gitkeep
    gerenciador.gerenciador_log.garantia_diretorio() # garante que o diretório de logs existe
    gerenciador.percorrer_diretorios() # percorre os diretórios e aplica as regras do .gitkeep, além de salvar o log e exibir os resultados