#   https://edabit.com/challenge/8pDH2SRutPoaQghgc
#   Luke Skywalker has family and friends.
#   Help him remind them who is who.
#   Given a string with a name, return the relation of that person to Luke.
#   Person      Relation
#   Darth Vader father
#   Leia        sister
#   Han         brother-in-law
#   R2D2	    droid


def relation_to_luke(name: str) -> str:
    try:
        family_dict = {
            "Darth Vader": "father",
            "Leia": "sister",
            "Han": "brother-in-law",
            "R2D2": "droid"
        }

        if name not in family_dict:
            other_result = f"I am not related to you, {name}!"
            return other_result

        result = f"Luke, I am your {family_dict[name]}"
        return result
    except TypeError as err:
        print(f"Error: {err}")


print(relation_to_luke("Darth Vader"))
print(relation_to_luke("Leia"))
print(relation_to_luke("Han"))
print(relation_to_luke("R2D2"))
print(relation_to_luke("Palpatine"))
