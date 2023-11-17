from classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 3, False)

print(my_pizza.size)

sals_pizza: Pizza = Pizza("medium", 5, False)

print(sals_pizza.size, sals_pizza.toppings, sals_pizza.gluten_free)

def price(input_pizza: Pizza) -> float:
    if input_pizza.size == "large:":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += .75 * input_pizza.toppings
    return cost