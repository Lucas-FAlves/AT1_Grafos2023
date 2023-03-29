import numpy as np

#Le um arquivo e cria uma matriz a partir dos dados lidos
def criaMatriz(inst):
    print("Abrindo o arquivo: " + inst +  ".txt")
    caminho = 'C:/Users/Lucas/OneDrive/Documentos/Grafos/AT1/' + inst + ".txt" #Caminho do arquivo no meu sistema operacional
    with open(caminho, "rb") as f:
        matriz = np.genfromtxt(f, dtype='int64')#Le os dados do arquivo .txt e armazena como matriz
    print("O arquivo " + inst +  ".txt " + "foi aberto")
    return matriz #Retorna a matriz que foi encontrada no arquivo aberto

#salva o resultado de uma operação no arquivo "Resultado.txt"
def salvaResultado (resultado):
    caminho = "C:/Users/Lucas/OneDrive/Documentos/Grafos/AT1/Resultado/Resultado.txt"
    with open(caminho, "w") as arquivo:
        arquivo.write(resultado)#Salvando os resultados no Arquivo

#Descobre o tamanho da matriz
def descubraLinhasEColunas (matriz):
    linhas = matriz.shape[0]
    colunas = matriz.shape[1]
    return (linhas, colunas)

if __name__ == "__main__":
    inst = input("Digite o nome do arquivo: ")#Recebe qual o arquivo que deve ser acessado
    matriz = criaMatriz(inst) #Le o arquivo que foi passado e armazena seus dados
    tamMatriz = descubraLinhasEColunas(matriz) #Pega os dados de uma matriz
    resultado = "A matriz do arquivo " + inst + ".txt possui:" +"\nLinhas:  " + str(tamMatriz[0]) +"\nColunas:  "+ str(tamMatriz[1])
    salvaResultado(resultado)#Salva os dados recebidos