from typing import List, Tuple, Union

class Array:
    def __init__(self, data: Union[List[int], List[List[int]]]):
        # Initialise l'objet Array avec les données et définit sa forme (shape)
        self.data = data
        if all(isinstance(i, list) for i in data):
            self.shape = (len(data), len(data[0]))
        else:
            self.shape = (len(data),)

    def _broadcast(self, other: 'Array') -> Tuple[List[List[int]], Tuple[int, int]]:
        # Diffuse les données de l'autre tableau pour rendre les dimensions compatibles
        if self.shape == other.shape:
            return other.data, other.shape
        if len(self.shape) == 1:
            broadcasted_data = [other.data] * self.shape[0]
            return broadcasted_data, (self.shape[0], len(other.data))
        elif len(other.shape) == 1:
            broadcasted_data = [[other.data[i]] * self.shape[1] for i in range(len(other.data))]
            return broadcasted_data, (len(other.data), self.shape[1])
        else:
            raise ValueError("Broadcasting is only supported for 1D to 2D array operations and vice versa.")

    def __add__(self, other: Union[int, 'Array']) -> 'Array':
        # Ajoute un nombre ou un autre tableau élément par élément
        if isinstance(other, Array):
            other_data, other_shape = self._broadcast(other)
            if self.shape != other_shape:
                raise ValueError("Shapes must be the same for element-wise operations.")
            if len(self.shape) == 1:
                return Array([self.data[i] + other_data[i] for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] + other_data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
        else:
            if len(self.shape) == 1:
                return Array([x + other for x in self.data])
            else:
                return Array([[x + other for x in row] for row in self.data])

    def __sub__(self, other: Union[int, 'Array']) -> 'Array':
        # Soustrait un nombre ou un autre tableau élément par élément
        if isinstance(other, Array):
            other_data, other_shape = self._broadcast(other)
            if self.shape != other_shape:
                raise ValueError("Shapes must be the same for element-wise operations.")
            if len(self.shape) == 1:
                return Array([self.data[i] - other_data[i] for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] - other_data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
        else:
            if len(self.shape) == 1:
                return Array([x - other for x in self.data])
            else:
                return Array([[x - other for x in row] for row in self.data])

    def __mul__(self, other: Union[int, 'Array']) -> 'Array':
        # Multiplie un nombre ou un autre tableau élément par élément
        if isinstance(other, Array):
            other_data, other_shape = self._broadcast(other)
            if self.shape != other_shape:
                raise ValueError("Shapes must be the same for element-wise operations.")
            if len(self.shape) == 1:
                return Array([self.data[i] * other_data[i] for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] * other_data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
        else:
            if len(self.shape) == 1:
                return Array([x * other for x in self.data])
            else:
                return Array([[x * other for x in row] for row in self.data])

    def __truediv__(self, other: Union[int, 'Array']) -> 'Array':
        # Divise par un nombre ou un autre tableau élément par élément
        if isinstance(other, Array):
            other_data, other_shape = self._broadcast(other)
            if self.shape != other_shape:
                raise ValueError("Shapes must be the same for element-wise operations.")
            if len(self.shape) == 1:
                return Array([self.data[i] / other_data[i] for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] / other_data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
        else:
            if len(self.shape) == 1:
                return Array([x / other for x in self.data])
            else:
                return Array([[x / other for x in row] for row in self.data])

    def __matmul__(self, other: 'Array') -> Union[int, 'Array']:
        # Effectue la multiplication matricielle entre deux tableaux
        if len(self.shape) == 1 and len(other.shape) == 1:
            if self.shape[0] != other.shape[0]:
                raise ValueError("Shapes must be the same for matrix multiplication.")
            return sum(self.data[i] * other.data[i] for i in range(len(self.data)))
        elif len(self.shape) == 2 and len(other.shape) == 2:
            if self.shape[1] != other.shape[0]:
                raise ValueError("Inner dimensions must match for matrix multiplication.")
            result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.shape[1])) for j in range(other.shape[1])] for i in range(self.shape[0])]
            return Array(result)
        else:
            raise ValueError("Matrix multiplication is only supported for 1D and 2D arrays.")

    def __contains__(self, item: int) -> bool:
        # Vérifie si un élément est contenu dans le tableau
        if len(self.shape) == 1:
            return item in self.data
        else:
            return any(item in row for row in self.data)

    def __getitem__(self, index: Union[int, Tuple[int, int]]) -> Union[int, List[int]]:
        # Accède à un élément ou à une sous-partie du tableau
        if isinstance(index, int):
            return self.data[index]
        elif isinstance(index, tuple):
            if len(self.shape) == 1:
                raise IndexError("Too many indices for 1D array")
            return self.data[index[0]][index[1]]
        else:
            raise TypeError("Invalid index type")

    def __len__(self) -> int:
        # Retourne la taille du tableau
        return self.shape[0]

    def __repr__(self) -> str:
        # Représente le tableau sous forme de chaîne de caractères
        return f"Array({self.data})"

# Exemples d'utilisation
# x = Array([1, 2, 3])
# y = Array([4, 5, 6])
# print(x + y)  # Array([5, 7, 9])
# print(x - y)  # Array([-3, -3, -3])
# print(x * 2)  # Array([2, 4, 6])
# print(x @ y)  # 32
# print(x * y)  # Array([4, 10, 18])
# print(x / y)  # Array([0.25, 0.4, 0.5])
# print(1 in y)  # True

# z = Array([[1, 2], [3, 4]])
# w = Array([[5, 6], [7, 8]])
# print(z + w)  # Array([[6, 8], [10, 12]])
# print(z * 2)  # Array([[2, 4], [6, 8]])
# print(2 in x)  # True
# print(z[1, 1])  # 4
# print(len(z))  # 2
# print(z @ w)  # Array([[19, 22], [43, 50]]) - multiplication matricielle correcte
# print(z * w)  # Array([[5, 12], [21, 32]])
# print(w / z)  # Array([[5.0, 3.0], [2.3333333333333335, 2.0]])
# print(1 in z)  # True
