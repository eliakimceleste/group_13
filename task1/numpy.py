from typing import List, Tuple, Union

class Array:
    def __init__(self, data: Union[List[Union[int, float]], List[List[Union[int, float]]]]):
        if isinstance(data, list):
            if all(isinstance(i, list) for i in data):  # 2D array
                self.data = data
                self.shape = (len(data), len(data[0]))
            elif all(isinstance(i, (int, float)) for i in data):  # 1D array
                self.data = data
                self.shape = (len(data),)
            else:
                raise ValueError("Array must be a list of lists or a list of integers or floats.")
        else:
            raise TypeError("Data must be a list.")

    def __repr__(self) -> str:
        return f"Array({self.data})"

    def __len__(self) -> int:
        return self.shape[0]

    def __getitem__(self, index: Union[int, Tuple[int, int]]) -> Union[int, float, List[Union[int, float]]]:
        if isinstance(index, tuple):
            return self.data[index[0]][index[1]]
        else:
            return self.data[index]

    def __add__(self, other: Union[int, float, 'Array']) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Shapes must be the same for element-wise operations.")
            if len(self.shape) == 1:
                return Array([self.data[i] + other.data[i] for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] + other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
        elif isinstance(other, (int, float)):
            if len(self.shape) == 1:
                return Array([x + other for x in self.data])
            else:
                return Array([[x + other for x in row] for row in self.data])
        else:
            raise TypeError("Operand must be an int, float, or Array.")

    def __sub__(self, other: Union[int, float, 'Array']) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Shapes must be the same for element-wise operations.")
            if len(self.shape) == 1:
                return Array([self.data[i] - other.data[i] for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] - other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
        elif isinstance(other, (int, float)):
            if len(self.shape) == 1:
                return Array([x - other for x in self.data])
            else:
                return Array([[x - other for x in row] for row in self.data])
        else:
            raise TypeError("Operand must be an int, float, or Array.")

    def __mul__(self, other: Union[int, float, 'Array']) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Shapes must be the same for element-wise operations.")
            if len(self.shape) == 1:
                return Array([self.data[i] * other.data[i] for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] * other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
        elif isinstance(other, (int, float)):
            if len(self.shape) == 1:
                return Array([x * other for x in self.data])
            else:
                return Array([[x * other for x in row] for row in self.data])
        else:
            raise TypeError("Operand must be an int, float, or Array.")

    def __truediv__(self, other: Union[int, float, 'Array']) -> 'Array':
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Shapes must be the same for element-wise operations.")
            if len(self.shape) == 1:
                return Array([self.data[i] / other.data[i] for i in range(len(self.data))])
            else:
                return Array([[self.data[i][j] / other.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
        elif isinstance(other, (int, float)):
            if len(self.shape) == 1:
                return Array([x / other for x in self.data])
            else:
                return Array([[x / other for x in row] for row in self.data])
        else:
            raise TypeError("Operand must be an int, float, or Array.")

    def __matmul__(self, other: 'Array') -> Union[int, float]:
        if len(self.shape) == len(other.shape) == 1:
            if len(self.data) != len(other.data):
                raise ValueError("Arrays must be of the same length for dot product.")
            return sum(self.data[i] * other.data[i] for i in range(len(self.data)))
        else:
            raise ValueError("Dot product is only supported for 1D arrays.")

    def __contains__(self, item: Union[int, float]) -> bool:
        if len(self.shape) == 1:
            return item in self.data
        else:
            return any(item in row for row in self.data)

if __name__ == "__main__":
    # Tests interactifs

    # Test de la création d'un tableau 1D
    arr1d = Array([1, 2, 3])
    print(f"arr1d: {arr1d}")
    print(f"Shape of arr1d: {arr1d.shape}")

    # Test de la création d'un tableau 2D
    arr2d = Array([[1, 2], [3, 4]])
    print(f"arr2d: {arr2d}")
    print(f"Shape of arr2d: {arr2d.shape}")

    # Test de l'opérateur 'in'
    print(f"2 in arr1d: {2 in arr1d}")
    print(f"5 in arr1d: {5 in arr1d}")

    print(f"3 in arr2d: {3 in arr2d}")
    print(f"5 in arr2d: {5 in arr2d}")

    # Test de l'addition
    result = arr1d + 1
    print(f"arr1d + 1: {result}")

    result = arr2d + 1
    print(f"arr2d + 1: {result}")

    arr1d_other = Array([4, 5, 6])
    result = arr1d + arr1d_other
    print(f"arr1d + arr1d_other: {result}")

    arr2d_other = Array([[5, 6], [7, 8]])
    result = arr2d + arr2d_other
    print(f"arr2d + arr2d_other: {result}")

    # Test de la soustraction
    result = arr1d - 1
    print(f"arr1d - 1: {result}")

    result = arr2d - 1
    print(f"arr2d - 1: {result}")

    result = arr1d - arr1d_other
    print(f"arr1d - arr1d_other: {result}")

    result = arr2d - arr2d_other
    print(f"arr2d - arr2d_other: {result}")

    # Test de la multiplication
    result = arr1d * 2
    print(f"arr1d * 2: {result}")

    result = arr2d * 2
    print(f"arr2d * 2: {result}")

    result = arr1d * arr1d_other
    print(f"arr1d * arr1d_other: {result}")

    result = arr2d * arr2d_other
    print(f"arr2d * arr2d_other: {result}")

    # Test de la division
    result = arr1d / 1
    print(f"arr1d / 1: {result}")

    result = arr2d / 1
    print(f"arr2d / 1: {result}")

    result = arr1d / arr1d_other
    print(f"arr1d / arr1d_other: {result}")

    result = arr2d / arr2d_other
    print(f"arr2d / arr2d_other: {result}")

    # Test du produit scalaire (dot product)
    result = arr1d @ arr1d_other
    print(f"arr1d @ arr1d_other: {result}")

    arr3d = Array([10, 12, 13])

    print(arr3d)
    print( 10 in arr3d)
    arr4d = Array([[1, 2], [3, 4]])
    print(f"arr2d: {arr3d}")
    print(f"Shape of arr2d: {arr3d.shape}")
