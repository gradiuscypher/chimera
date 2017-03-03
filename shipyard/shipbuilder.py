chassis_list = range(0, 5)
engine_list = range(0, 5)
radiator_list = range(0, 5)
ship_list = []

for chassis in chassis_list:
    for engine in engine_list:
        for radiator in radiator_list:
            ship = {"chassis": chassis, "engine": engine, "radiator": radiator}
            ship_list.append(ship)
            print(ship)

