"""Module containing the Square Class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square Class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """updates a value to each attribute internely."""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates the values of attributes"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}

    def __str__(self):
        """String Representation of Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
