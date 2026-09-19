def NULL_not_found(object: any) -> int:
    object_type = type(object)

    if object is None:
        print(f"Nothing: {object} {object_type}")
    elif object_type is float and object != object:
        print(f"Chesse: {object} {object_type}")
    elif object_type is int and object == 0:
        print(f"Zero: {object} {object_type}")
    elif object_type is str and object == "":
        print(f"Empty: {object_type}")
    elif object_type is bool and object is False:
        print(f"Fake: {object} {object_type}")
    else:
        print("Type not found")
        return 1

    return 0

# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ""
# Fake = False
# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))
