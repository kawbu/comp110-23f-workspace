class Pizza:
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, toppings_input: int, gf_input: bool):
        """Constructor"""
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf_input