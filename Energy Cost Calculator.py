unit_rate_day = 30.61
unit_rate_night = 20.28
unit_rate_gas = 7.34
unit_rate_single = 27.8376


def calculate_cost_E1(unit_rate_day, unit_rate_night):
    last_meter_reading = 166204
    next_meter_reading = 166236
    KWH_used = next_meter_reading - last_meter_reading
    cost = (KWH_used * unit_rate_night)/100
    return cost

def calculate_cost_E2(unit_rate_day, unit_rate_night, unit_rate_single):
    last_meter_reading_night = 299723
    next_meter_reading_night = 299510
    last_meter_reading_day = 84394
    next_meter_reading_day = 85262

    KWH_used_day = next_meter_reading_day - last_meter_reading_day
    cost_day = (KWH_used_day * unit_rate_day)/100
    
    KWH_used_night = next_meter_reading_night - last_meter_reading_night
    cost_night = (KWH_used_night * unit_rate_night)/100

    single_rate_cost = ((KWH_used_day + KWH_used_night)*unit_rate_single)/100

    return cost_day, cost_night, single_rate_cost

def calculate_cost_G1(unit_rate_gas):
    last_meter_reading = 8802
    next_meter_reading = 8789
    KWH_used = next_meter_reading - last_meter_reading
    
    cost_gas = (KWH_used * unit_rate_gas)/100

    return cost_gas

def total_cost(cost_day, cost_night, single_rate_cost, cost_gas):
    total = cost_day + cost_night + cost_gas
    cost_single = single_rate_cost + cost_gas
    return total, cost_single


cost_gas = calculate_cost_G1(unit_rate_gas)
cost_day, cost_night, single_rate_cost = calculate_cost_E2(unit_rate_day, unit_rate_night, unit_rate_single)

cost_total, cost_single = total_cost(cost_day, cost_night, single_rate_cost, cost_gas)

print("Total: {}, Electric Day: {}, Electric Night: {}, Cost Single Rate: {}".format(cost_total, cost_day, cost_night, cost_single))