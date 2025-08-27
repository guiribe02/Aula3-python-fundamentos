# ===============================
# Sistema de Cadastro de Alunos
# ===============================

# 1. Função de saudação
def saudacao():
    print("👋 Olá, bem-vindo ao Sistema de Cadastro de Alunos!")


# 2. Cadastro de alunos (lista de dicionários)
def cadastrar_alunos():
    alunos = []  # lista que vai guardar os dicionários de cada aluno

    while True: #lista de repetição-V,loop ate receber 'sair'
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":  #Lower metodo/string transforma,se 'sair' executa break
            break

        idade = int(input("Digite a idade do aluno: "))
        nota = float(input("Digite a nota do aluno: "))

        # Criando um dicionário para o aluno
        aluno = {"nome": nome, "idade": idade, "nota": nota}

        alunos.append(aluno)  # adiciona na lista alunos

    return alunos


# 3. Operações com os dados
def calcular_media(alunos): #(alunos) função rebece a lista como entrada
    if not alunos: #se não
        return 0
    soma = sum([aluno["nota"] for aluno in alunos]) #compreesão de listas/ sum funçao somar-[]percorre aluno/aluno,para/em e pega a variavel nota
    return soma / len(alunos) # len função conta a quantidade para media

def contar_acima_de_sete(alunos):
    return len([aluno for aluno in alunos if aluno["nota"] > 7]) #compreesão de listas,percorre aluno em alunoS,se V adiciona na lista

def listar_em_ordem(alunos):
    return sorted([aluno["nome"] for aluno in alunos]) #sorted funçao organiza (A-Z),variavel nome/dicionario aluno na lista alunoS.


# 4. Laços de repetição e condicionais
def verificar_situacao(alunos):
    for aluno in alunos:
        nota = aluno["nota"] #pega a variavel nota do dicionario aluno
        if nota >= 7: #se
            situacao = "Aprovado"
        elif nota >= 5: #senão,2ª condição
            situacao = "Recuperação"
        else: # SENÃO (em qualquer outro caso)
            situacao = "Reprovado"
        print(f"{aluno['nome']} - Nota: {nota} - {situacao}")


# 5. Manipulação de arquivos
def salvar_em_arquivo(alunos, nome_arquivo="alunos.txt"):  #cria funçao que adc lista alunos dentro do arquivo alunos.txt
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:#formatação do arquivo,w=write,encoding=utf-8 = grava o arquivo em formato utf-8
        for aluno in alunos:
            linha = f"{aluno['nome']},{aluno['idade']},{aluno['nota']}\n"
            arquivo.write(linha) #grava a linha no arquivo

def ler_arquivo(nome_arquivo="alunos.txt"):
    print("\n📂 Conteúdo do arquivo salvo:")
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:#abre o arquivo para leitura
        conteudo = arquivo.read() #conteudo variavel recebe o conteudo do arquivo, .read lê
        print(conteudo)


# 6. Programação Orientada a Objetos
class Aluno: #classe que representa um aluno
    def __init__(self, nome, idade, nota): #construtor,roda quando constroe o objeto
        self.nome = nome #self referencia o objeto que está sendo criado
        self.idade = idade
        self.nota = nota

    def exibir_informacoes(self): #método(dentro da classe) para exibir informações do aluno
        print(f"Aluno: {self.nome}, Idade: {self.idade}, Nota: {self.nota}")


# ===============================
# PROGRAMA PRINCIPAL
# ===============================
def main(): #identifica o inicio do programa
    saudacao()

    alunos = cadastrar_alunos()

    print("\n📊 Operações com os dados:")
    print(f"Média das notas: {calcular_media(alunos):.2f}")
    print(f"Alunos com nota acima de 7: {contar_acima_de_sete(alunos)}")
    print(f"Nomes em ordem alfabética: {listar_em_ordem(alunos)}")

    print("\n📌 Situação dos alunos:")
    verificar_situacao(alunos)

    salvar_em_arquivo(alunos)
    ler_arquivo()


if __name__ == "__main__":
    main()
