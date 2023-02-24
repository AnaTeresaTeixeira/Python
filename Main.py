from datetime import datetime
from datetime import date

print("-----------------------------------------------------") 

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("\n\nHora atual:", current_time)

today = date.today()
print("\nData:", today)
today = str(today)

#-----------------------------------------------------------------------------------------------------
def ola():
    print("\n\n-----------------------------------------------------"
    + "\n----------------Registos do Ano 2023-----------------\n"
    + "-----------------------------------------------------\n")
    global nome
    nome = input("\nIntroduz o teu nome: ")
    print(f"\nOlá, {nome}")



def trimestre(num):
    # dicionario 
    dic_trimestres = {1 : "Janeiro, Fevereiro, Março",
                      2 : "Abril, Maio, Junho",
                      3 : "Julho, Agosto, Setembro",
                      4 : "Outubro, Novembro, Dezembro"}
    
    if(num>=1 and num<=4):
        for i in dic_trimestres:
            if(num==i):
                print("\n" + dic_trimestres[i])
        
        # guardar notas diarias
        f = open("Notas.txt", 'a')     
        print("\n-----------------------------------------------------") 
        print("---------------Mensagens da turma--------------------")  
        print("-----------------------------------------------------\n") 
        print("\nImportante: Não inserir acentos, apenas virgulas")  
        print("\n-----------------------------------------------------\n")
        inserir = input("\nEscreve a tua mensagem:\n\n")
        if(inserir != ""): 
            f.write("\n" + today + " " + inserir + " - " + current_time) 
        f.close()

        # abrir Notas e mostrar conteudo
        f = open("Notas.txt", 'r')
        print("\n-----------------------------------------------------\n")
        print(f.read())
        print("\n-----------------------------------------------------\n")
        f.close()

    else:
        erro = int(input("\nErro! Insere novamente: "))      
        if(erro<1 or erro>4):
            print("\nAi! Ai! Estás a portar-te mal! :)")
        else:
            trimestre(erro)   
     


def adeus():  
    resposta = input("\n-----------------------------------------------------"
    + "\n-----------------------------------------------------\n"
    + "\nQueres ir embora?\n\n** Para --Não--, faz o favor de escrever --N--"
    + "\n\n** Para --Sim, quero ir-- (fico chateado, mas ok :| ) \nfaz o favor de escrever --S--\n\n")

    if(resposta=="N" or resposta=="n"):
        print("\nBoa :) , vamos fazer outra coisa.\n")
        dois()
    else:
        print("\nOk, adeus. Vou ficar amuado! :| \n")



def dois():
    # abir arquivo
    f = open("File.txt", 'r')
    print(f"{nome}, vamos ver o que o teu nome significa.\n")
    print("Abrindo os nossos arquivos...\n\n\n")
    for linha in f:
        nomesLista = linha.split()
        for i in nomesLista:
            if(i==nome):
                while i!=" ":
                    print("\n-----------------------------------------------------")
                    print(linha)
                    print("-----------------------------------------------------\n")
                    break
            else:
                reclamar()
                break
        break
    f.close()



def reclamar():
    res = input("\nQueres adicionar o teu nome e um texto sobre ti à lista?"
    + "\n\nSim? --- escreve S\n\nNão? --- escreve N\n\n")
    if(res=="S" or res=="s"):
        f = open("File.txt", 'a')
        print("\n-----------------------------------------------------\n")
        print("\n\nImportante: Não inserir acentos, apenas virgulas")  
        print("\n-----------------------------------------------------\n")
        ad = input("\n\nEscreve abaixo o que queres adicionar ao ficheiro:\n\n")
        f.write("\n" + ad)
        f.close()

        #abrir ficheiro e ler 
        f = open("File.txt", "r")
        print("\n-----------------------------------------------------\n")
        print(f.read())
        print("\n-----------------------------------------------------\n")
        f.close()
    else:
        print("\n\nOk, adeus :|")

# -------------------------------------- main ---------------------------------------
def main():

    # boas-vindas
    ola()

    # pedir Trimestre
    num_trimestre = int(input("\nIntroduz o número referente ao trimestre: "))
    trimestre(num_trimestre)

    # dar adeus (ou não)
    adeus()


if __name__ == '__main__':
        main()
