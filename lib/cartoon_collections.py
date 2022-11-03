def roll_call_dwarves(dwarves_names):
    for index, name in enumerate(dwarves_names):
        print(f"{index + 1}. {name}")


def capitalize_call(call):
    # return call[0].upper() + call[1:] + "!"
    return call.title() + "!"


def summon_captain_planet(planeteer_calls):
    return [capitalize_call(call) for call in planeteer_calls]


def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True

    return False


def find_the_cheese(foods):
    cheeses = [
        "cheddar",
        "gouda",
        "camembert"
    ]

    for cheese in cheeses:
        if cheese in foods:
            return cheese

    return None
