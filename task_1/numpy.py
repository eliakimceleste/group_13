class Array:
    def __init__(self, x = list):
        self.x = x
        if all(isinstance(i, list) for i in x):
            self.shape = (len(x), len(x[0]))
        else:
            self.shape = (len(x), )

    # Afficher le tableau  
    def __repr__(self):
        return "array({})".format(self.x)
    
    # Faire l'addition d'une matrice à 1D et d'un nombre d'une part et de deux matrices d'autre part 
    def __add__(self, other):
        if isinstance(other, int):
            if all(isinstance(i, list) for i in self.x):
                return Array([[j + other for j in i] for i in self.x])
            else:
                return Array([i + other for i in self.x])
        if isinstance(other, Array):
            if all(isinstance(x, list) for x in self.x) and all(isinstance(y, list) for y in other.x):
                return Array([[i+j for i, j in zip(l1, l2)] for l1, l2 in zip(self.x, other.x)])
        return Array([i+j for i, j in zip(self.x, other.x)])
    
    # Faire la soustraction d'une matrice à 1D et d'un nombre d'une part et de deux matrices d'autre part 
    def __sub__(self, other):
        if isinstance(other, int):
            if all(isinstance(i, list) for i in self.x):
                return Array([[j - other for j in i] for i in self.x])
            else:
                return Array([i - other for i in self.x])
        if isinstance(other, Array):
            if all(isinstance(x, list) for x in self.x) and all(isinstance(y, list) for y in other.x):
                return Array([[i-j for i, j in zip(l1, l2)] for l1, l2 in zip(self.x, other.x)])
        return Array([i-j for i, j in zip(self.x, other.x)])
    
    # Faire la multiplication d'une matrice à 1D et d'un nombre d'une part et de deux matrices d'autre part 
    def __mul__(self, other):
        if isinstance(other, int):
            if all(isinstance(i, list) for i in self.x):
                return Array([[j * other for j in i] for i in self.x])
            else:
                return Array([i * other for i in self.x])
        if isinstance(other, Array):
            if all(isinstance(x, list) for x in self.x) and all(isinstance(y, list) for y in other.x):
                return Array([[i * j for i, j in zip(l1, l2)] for l1, l2 in zip(self.x, other.x)])
        return Array([i * j for i, j in zip(self.x, other.x)])
    
    # Faire la division d'une matrice à 1D et d'un nombre d'une part et de deux matrices d'autre part 
    def __truediv__(self, other):
        if isinstance(other, int):
            if all(isinstance(i, list) for i in self.x):
                return Array([[j / other for j in i] for i in self.x])
            else:
                return Array([i / other for i in self.x])
        if isinstance(other, Array):
            if all(isinstance(x, list) for x in self.x) and all(isinstance(y, list) for y in other.x):
                return Array([[i / j for i, j in zip(l1, l2)] for l1, l2 in zip(self.x, other.x)])
        return Array([i / j for i, j in zip(self.x, other.x)])
    
    # Afficher la taille de la matrice
    def __len__(self):
        return len(self.x)
    
    # Vérifier si un élément est dans une liste ou pas avec l'opérateur "in"
    def __contains__(self, el):
        if all(isinstance(x, list) for x in self.x):
            for x in self.x:
                return el in x
        else:
            return el in self.x
        
    # Slicing et indexing
    def __getitem__(self, index):
        if isinstance(index, tuple):
            rows, col = index
            if isinstance(rows, slice):
                start, stop, step = rows.indices(len(self.x))
                return [self.x[i][col] for i in range(start, stop, step)]
            else:
                return self.x[rows][col]
        else:
            return self.x[index]
        
    # Calculer le produit scalaire
    
                
                    
    
        
tab = Array([[1, 2], [1, 1]])
tab1 = Array([[3, 4], [1, 1]])
tab2 = Array([1, 2])
tab3 = Array([3, 5])
tab4 = Array([1, 2, 3, 4, 5, 6])
print(tab[0][1])