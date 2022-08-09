# Insertion sort in Python

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compara a chave com cada elemento à esquerda dela até que um elemento menor do que seja encontrado
        # Para ordem decrescente, altere key<array[j] para key>array[j].       
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            
        # Coloque a chave em após o elemento um pouco menor que ele.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Matriz classificada em ordem crescente:')
print(data)