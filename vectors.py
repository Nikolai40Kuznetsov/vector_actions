class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other): #скалярное произведение
        return (self.x * other.x + self.y * other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __matmul__(self, other): #векторное произведение (знак @)
        return Vector3D(self.y * other.z - other.y * self.z, 
                        other.x * self.z - self.x * other.z,
                        self.x * other.y - other.x * self.y)
    
    def __mul__(self, other): #скалярное произведение (знак *)
        q = (self.x * other.x + self.y * other.y + self.z * other.z)
        return (q * q / ((self.x * self.x + self.y * self.y + self.z * self.z) * (other.x * other.x + other.y * other.y + other.z * other.z)) ** 0.5)
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
class Matrix4:
    def __init__(self, row1, row2, row3, row4):
        self.rows = [row1, row2, row3, row4]

    def determinant2(a11, a12, a21, a22):
        return a11 * a22 - a12 * a21
    
    def column_pairs():
        column_pairs = []
        for i in range(1, 4):
            if i <= 3:
                column_pairs.append([i, i+1])
            if i <= 2:
                column_pairs.append([i, i+2])
            if i <= 1:
                column_pairs.append([i, i+3])
        return column_pairs
    
    def minor2(self, row_index_1, row_index_2):
        row_list = [1, 2, 3, 4]
        row_list.remove(row_index_1)
        row_list.remove(row_index_2)
        items = []
        column_pair = Matrix4.column_pairs()
        for i in range(0, len(column_pair)):
            col_list = [1, 2, 3, 4]
            col_list.remove(column_pair[i][0])
            col_list.remove(column_pair[i][1])
            items.append((-1)**(row_index_1+row_index_2+column_pair[i][0]+column_pair[i][1]) * 
                         self.determinant2(self.rows[row_list[0]][col_list[0]], 
                                           self.rows[row_list[0]][col_list[1]], 
                                           self.rows[row_list[1]][col_list[0]],
                                           self.rows[row_list[1]][col_list[1]]))
            determinant4 = sum(items)
            return determinant4

    
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
print(v1 * v2)
print(v1 @ v2)
mtr = Matrix4([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4])
mtr.minor2(1, 2)
                    