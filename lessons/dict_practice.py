"""Practice with Dictionary Syntax"""

ice_cream: dict[str, int] = {"vanilla": 10, "strawberry": 8, "chocolate": 5, "chocolate": 6}

if "vanilla" in ice_cream:
    print(ice_cream["vanilla"])
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no mint")

for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")