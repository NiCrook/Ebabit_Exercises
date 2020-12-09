#   https://edabit.com/challenge/vAS4Hp4wzSEnQs3tZ
#   Write a function that takes in a name and returns a name tag, that should read:
#   "Hi! I'm [name], and I'm from [country]."
#   If the name is not in the dictionary, return:
#   "Hi! I'm a guest."
#   GUEST_LIST = {
#   "Randy": "Germany",
#   "Karla": "France",
#   "Wendy": "Japan",
#   "Norman": "England",
#   "Sam": "Argentina"
#   }


GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
    }


def greeting(name: str) -> str:
    if name in GUEST_LIST:
        return f"Hi! I'm {name}, and I'm from {GUEST_LIST[name]}."
    else:
        return "Hi! I'm a guest."


print(greeting("Randy"))
print(greeting("Sam"))
print(greeting("Monti"))
