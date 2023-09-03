def water_jug_problem():
    jug_4 = 4  # Capacity of the 4-gallon jug
    jug_3 = 3  # Capacity of the 3-gallon jug

    # Initial states of the jugs
    state_4 = 0
    state_3 = 0

    while state_4 != 2:
        # Fill the 4-gallon jug if it's empty
        if state_4 == 0:
            state_4 = jug_4
            print(f"Fill the {jug_4}-gallon jug")

        # Pour water from the 4-gallon jug into the 3-gallon jug
        elif state_4 > 0 and state_3 < jug_3:
            transfer = min(state_4, jug_3 - state_3)
            state_4 -= transfer
            state_3 += transfer
            print(f"Pour {transfer} gallons from the {jug_4}-gallon jug to the {jug_3}-gallon jug")

        # Empty the 3-gallon jug
        elif state_3 == jug_3:
            state_3 = 0
            print(f"Empty the {jug_3}-gallon jug")

        # Pour water from the 4-gallon jug into the 3-gallon jug (when the 3-gallon jug is full)
        elif state_3 == jug_3:
            state_4 = jug_4 - jug_3
            state_3 = jug_3
            print(f"Pour {jug_4 - jug_3} gallons from the {jug_4}-gallon jug to the {jug_3}-gallon jug")

    print("You have successfully measured 2 gallons in the 4-gallon jug!")

if __name__ == "__main__":
    water_jug_problem()
