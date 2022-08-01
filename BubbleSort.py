def bubble_sort(lista):
        #declaro uma lista
        n = len(lista)
        #percorro essa lista de i até n-1
        for j in range(n-1):
         for i in range(n-1):
            if lista[i] > lista[i+1]:
                #troca dos elementos nas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]
        
    
    
lista = [54,26,93,17,77,31,44,55,20]
bubble_sort(lista)
print(lista)
