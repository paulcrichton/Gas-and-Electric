import datetime
import pandas as pd

def calculate_cost_E1(unit_rate_day, unit_rate_night, next_meter_reading, last_meter_reading):
    KWH_used = next_meter_reading - last_meter_reading
    cost = (KWH_used * unit_rate_night)/100
    return cost

def calculate_cost_E2(unit_rate_day, unit_rate_night, unit_rate_single, next_meter_reading_day, next_meter_reading_night, last_meter_reading_day, last_meter_reading_night):
    KWH_used_day = next_meter_reading_day - last_meter_reading_day
    cost_day = (KWH_used_day * unit_rate_day)/100
    
    KWH_used_night = next_meter_reading_night - last_meter_reading_night
    cost_night = (KWH_used_night * unit_rate_night)/100

    single_rate_cost = ((KWH_used_day + KWH_used_night)*unit_rate_single)/100

    return cost_day, cost_night, single_rate_cost

def calculate_cost_G1(unit_rate_gas, next_meter_reading, last_meter_reading):
    KWH_used = next_meter_reading - last_meter_reading
    
    cost_gas = (KWH_used * unit_rate_gas)/100

    return cost_gas

def total_cost(cost_day, cost_night, single_rate_cost, cost_gas):
    total = cost_day + cost_night + cost_gas
    cost_single = single_rate_cost + cost_gas
    return total, cost_single

def cost_record(cost_total, cost_day, cost_night, cost_single, cost_gas):
    date = str(datetime.datetime.now())
    with open("gas_and_electric_cost_record.txt", "a") as file:
        file.write("Total: £{}, Electric Day: £{}, Electric Night: £{}, Cost Single Rate: £{}, Cost Gas: £{}\n".format(cost_total, cost_day, cost_night, cost_single, cost_gas))

def get_last_readings():
    df = pd.read_csv('meter_readings.csv')
    row = df.iloc[-1]
    print(row.to_string())
    return row

def add_meter_readings(E1, E2_day, E2_night, G1):
    date = str(datetime.datetime.today())
    df = pd.read_csv('meter_readings.csv')
    readings_dict = {"E1": E1, "E2_day":E2_day, "E2_night":E2_night, "G1":G1, "Date":date}
    df_dict = pd.DataFrame([readings_dict])
    df = pd.concat([df, df_dict], ignore_index=True)
    df.to_csv('meter_readings.csv')


def main():
    unit_rate_day = 30.61
    unit_rate_night = 20.28
    unit_rate_gas = 7.34
    unit_rate_single = 27.8376

    last_readings = get_last_readings()
    
    next_meter_reading_E1 = 166204
    last_meter_reading_E1 = last_readings["E1"]
    E1_cost = calculate_cost_E1(unit_rate_day, unit_rate_night, next_meter_reading_E1, last_meter_reading_E1)
    print(E1_cost)

    last_meter_reading_night_E2 = last_readings["E2_night"]
    next_meter_reading_night_E2 = 299510
    last_meter_reading_day_E2 = last_readings["E2_day"]
    next_meter_reading_day_E2 = 85263

    E2_cost_day, E2_cost_night, E2_single_rate_cost = calculate_cost_E2(unit_rate_day, unit_rate_night, unit_rate_single, next_meter_reading_day_E2, next_meter_reading_night_E2, last_meter_reading_day_E2, last_meter_reading_night_E2)
    print(E2_cost_day, E2_cost_night, E2_single_rate_cost)
    
    next_meter_reading_G1 = 8786
    last_meter_reading_G1 = last_readings["G1"]

    G1_cost = calculate_cost_G1(unit_rate_gas, next_meter_reading_G1, last_meter_reading_G1)
    add_meter_readings(next_meter_reading_E1, next_meter_reading_day_E2, next_meter_reading_night_E2, next_meter_reading_G1)
    print(G1_cost)





main()