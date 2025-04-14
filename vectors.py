class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other): #скалярное произведение
        return (self.x * other.x + self.y * other.y)
    
    def __str__(self):
        return f"({self.x},{self.y})"

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
        return f"({self.x},{self.y},{self.z})"
    
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
print(v1 * v2)
                    