
def create_hash_table(size, chained = False):
    if(chained):
        return [[] for i in range(size)]
    else:
        return [None for i in range(size)]


def h1(name, size, p = 31):
    h_name = 0
    for letter in name:
        h_name = (p * h_name + ord(letter)) % size
    return h_name


def h2(name, size):
    h_name = 0
    for i in range(len(name)):
        h_name = (h_name + ord(name[i])**i) % size
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
    h_table[address].append(name)

def pesquisa_chained(h_table, name, address):
    for i in range(len(h_table[address])):
        if h_table[address][i] == name:
            return (i + 1)
    return (-1)

if __name__ == '__main__':
    size = 2
    h_table = create_hash_table(size, True)
    insere_chained(h_table, 'maria', h1('maria', size))
    insere_chained(h_table, 'lucio', h1('lucio', size))
    insere_chained(h_table, 'ricardo', h1('ricardo', size))
    insere_chained(h_table, 'luana', h1('luana', size))
    insere_chained(h_table, 'daives', h1('daives', size))
    insere_chained(h_table, 'valmir', h1('valmir', size))
    insere_chained(h_table, 'malaquias', h1('malaquias', size))
    insere_chained(h_table, 'jaime', h1('jaime', size))
    print(h_table)
    print(pesquisa_chained(h_table, 'maria', h1('maria', size)))
    print(pesquisa_chained(h_table, 'lucio', h1('lucio', size)))
    print(pesquisa_chained(h_table, 'ricardo', h1('ricardo', size)))
    print(pesquisa_chained(h_table, 'luana', h1('luana', size)))
    print(pesquisa_chained(h_table, 'daives', h1('daives', size)))
    print(pesquisa_chained(h_table, 'valmir', h1('valmir', size)))
    print(pesquisa_chained(h_table, 'laura', h1('laura', size)))
    print(pesquisa_chained(h_table, 'malaquias', h1('malaquias', size)))
    print(pesquisa_chained(h_table, 'joelma', h1('joelma', size)))
    print(pesquisa_chained(h_table, 'jaime', h1('jaime', size)))


