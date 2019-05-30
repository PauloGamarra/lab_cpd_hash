import sys
import numpy as np

def create_hash_table(size, chained = False):
    if(chained):
        return [[] for i in range(size)]
    else:
        return [None for i in range(size)]


def h1(name, size, p = 127):
    h_name = 0
    for letter in name:
        h_name = (p * h_name + ord(letter)) % size
    return h_name


def h2(name, size):
    h_name = 0
    for i in range(len(name)):
        h_name = (h_name + ord(name[i]))**(i + 1) % size
    return h_name

#função de inserção na tabela usando quadratic probing para resolver colisões
#os valores de c1 e c2 escolhidos são adequados para size igual a uma potencia de 2
#None significa que o endereço está livre e nunca foi usado enquanto False significa que apenas está livre
def insere_quadratic(h_table, name, address, size, c1 = 1/2, c2 = 1/2):
    if(h_table[address] == None or h_table[address] == False):
        h_table[address] = name
        return (1)
    else:
        i = 1
        while(h_table[address] != None and h_table[address] != False):
            address = (address + int(c1 * i + c2 * i**2)) % size
            i += 1
        h_table[address] = name
        return(i)

#função de pesquisa em tabela utilizando quadratic probing
#os valores de c1 e c2 escolhidos são adequados para size igual a uma potencia de 2
#None significa que o endereço está livre e nunca foi usado enquanto False significa que apenas está livre
def pesquisa_quadratic(h_table, name, initial_address, size, c1 = 1/2, c2 = 1/2):
    address = initial_address
    if(h_table[address] == name):
        return(1)
    else:
        if(h_table[address] == None):
            return (-1)
        else:
            i = 1
            while (h_table[address] != None):
                address = (address + int(c1 * i + c2 * i ** 2)) % size
                i += 1
                if(address == initial_address):
                    return(-1)
                if (h_table[address] == name):
                    return (i)
            return (-1)

#função de inserção em tabela utilizando encadeamento
def insere_chained(h_table, name, address):
    if(h_table[address] != []):
        colision = 1
    else:
        colision = 0
    h_table[address].append(name)
    return colision

def pesquisa_chained(h_table, name, address):
    for i in range(len(h_table[address])):
        if h_table[address][i] == name:
            return (i + 1)
    return (-1)

def combinacao1(arq_nomes, arq_consultas, tamanho = 16384):

    h_table = create_hash_table(tamanho, False)

    with open(arq_nomes) as file:
        names = file.read().splitlines()

    colisions = 0
    for name in names:
        colisions += (insere_quadratic(h_table, name, h1(name, tamanho), tamanho) - 1)

    print('1.2')
    print('taxa de ocupação: {}%'.format(100 * (len(names) / tamanho)))
    print('número de colisões: {}'.format(colisions))

    with open(arq_consultas) as file:
        names = file.read().splitlines()

    results = []
    encontrados = []
    nao_encontrados = []
    for name in names:
        results.append(pesquisa_quadratic(h_table, name, h1(name, tamanho), tamanho))
        if results[-1] == -1:
            nao_encontrados.append(name)
        else:
            encontrados.append(name)

    print('\n1.3')
    print("encontrados ({}): \n{}".format(len(encontrados), encontrados))
    print("\nnao encontrados ({}): \n{}".format(len(nao_encontrados), nao_encontrados))
    print("\nmedia do numero de verificacoes: {}".format(np.sum(results) / len(results)))

    results = dict(zip(names, results))
    results = sorted(results.items(), key=lambda kv: kv[1])
    results = results[len(nao_encontrados):]
    print("\nnomes que geraram o menor numero de berificações: {}".format((results[:10])))
    print("\nnomes que geraram o menor numero de berificações: {}".format((results[-10:])))

def combinacao2(arq_nomes, arq_consultas, tamanho = 16384):

    h_table = create_hash_table(tamanho, False)

    with open(arq_nomes) as file:
        names = file.read().splitlines()

    colisions = 0
    for name in names:
        colisions += (insere_quadratic(h_table, name, h2(name, tamanho), tamanho))

    print('1.2')
    print('taxa de ocupação: {}%'.format(100 * (len(names) / tamanho)))
    print('número de colisões: {}'.format(colisions))

    with open(arq_consultas) as file:
        names = file.read().splitlines()

    results = []
    encontrados = []
    nao_encontrados = []
    for name in names:
        results.append(pesquisa_quadratic(h_table, name, h2(name, tamanho), tamanho))
        if results[-1] == -1:
            nao_encontrados.append(name)
        else:
            encontrados.append(name)

    print('\n1.3')
    print("encontrados ({}): \n{}".format(len(encontrados), encontrados))
    print("\nnao encontrados ({}): \n{}".format(len(nao_encontrados), nao_encontrados))
    print("\nmedia do numero de verificacoes: {}".format(np.sum(results) / len(results)))

    results = dict(zip(names, results))
    results = sorted(results.items(), key=lambda kv: kv[1])
    results = results[len(nao_encontrados):]
    print("\nnomes que geraram o menor numero de berificações: {}".format((results[:10])))
    print("\nnomes que geraram o menor numero de berificações: {}".format((results[-10:])))

def combinacao3(arq_nomes, arq_consultas, tamanho = 2003):

    h_table = create_hash_table(tamanho, True)

    with open(arq_nomes) as file:
        names = file.read().splitlines()

    colisions = 0
    for name in names:
        colisions += (insere_chained(h_table, name, h1(name, tamanho)))

    print('1.2')
    print('número de colisões: {}'.format(colisions))

    with open(arq_consultas) as file:
        names = file.read().splitlines()

    results = []
    encontrados = []
    nao_encontrados = []
    for name in names:
        results.append(pesquisa_chained(h_table, name, h1(name, tamanho)))
        if results[-1] == -1:
            nao_encontrados.append(name)
        else:
            encontrados.append(name)

    print('\n1.3')
    print("encontrados ({}): \n{}".format(len(encontrados), encontrados))
    print("\nnao encontrados ({}): \n{}".format(len(nao_encontrados), nao_encontrados))
    print("\nmedia do numero de verificacoes: {}".format(np.sum(results) / len(results)))

    results = dict(zip(names, results))
    results = sorted(results.items(), key=lambda kv: kv[1])
    results = results[len(nao_encontrados):]
    print("\nnomes que geraram o menor numero de berificações: {}".format((results[:10])))
    print("\nnomes que geraram o menor numero de berificações: {}".format((results[-10:])))

def combinacao4(arq_nomes, arq_consultas, tamanho = 2003):

    h_table = create_hash_table(tamanho, True)

    with open(arq_nomes) as file:
        names = file.read().splitlines()

    colisions = 0
    for name in names:
        colisions += (insere_chained(h_table, name, h2(name, tamanho)))

    print('1.2')
    print('número de colisões: {}'.format(colisions))

    with open(arq_consultas) as file:
        names = file.read().splitlines()

    results = []
    encontrados = []
    nao_encontrados = []
    for name in names:
        results.append(pesquisa_chained(h_table, name, h2(name, tamanho)))
        if results[-1] == -1:
            nao_encontrados.append(name)
        else:
            encontrados.append(name)

    print('\n1.3')
    print("encontrados ({}): \n{}".format(len(encontrados), encontrados))
    print("\nnao encontrados ({}): \n{}".format(len(nao_encontrados), nao_encontrados))
    print("\nmedia do numero de verificacoes: {}".format(np.sum(results) / len(results)))

    results = dict(zip(names, results))
    results = sorted(results.items(), key=lambda kv: kv[1])
    results = results[len(nao_encontrados):]
    print("\nnomes que geraram o menor numero de berificações: {}".format((results[:10])))
    print("\nnomes que geraram o menor numero de berificações: {}".format((results[-10:])))


if __name__ == '__main__':
    print("combinacao 1 ----------------------------------------------------------------------------------------------")
    combinacao1(sys.argv[1], sys.argv[2], 16384)
    #print("combinacao 2 ----------------------------------------------------------------------------------------------")
    #combinacao2(sys.argv[1], sys.argv[2], 16384)
    #print("combinacao 3 ----------------------------------------------------------------------------------------------")
    #combinacao3(sys.argv[1], sys.argv[2], 2003)
    #print("combinacao 4 ----------------------------------------------------------------------------------------------")
    #combinacao4(sys.argv[1], sys.argv[2], 2003)