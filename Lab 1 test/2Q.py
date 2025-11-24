# Q2: Rectangle class with AI-generated docstrings
class Rectangle:
    def __init__(self, length, width):
        """length and width."""
        self.length = length
        self.width = width
    def area(self):
        """area (length × width)."""
        return self.length * self.width
    def perimeter(self):
        """perimeter (2 × (length + width))."""
        return 2 * (self.length + self.width)

# ---------- Testing the Rectangle class ----------
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())
