import datetime
<<<<<<< Updated upstream


unit_rate_day = 30.61
unit_rate_night = 20.28
unit_rate_gas = 7.34
unit_rate_single = 27.8376


def calculate_cost_E1(unit_rate_day, unit_rate_night):
    last_meter_reading = 166204
    next_meter_reading = 166236
=======
import pandas as pd
import os

def calculate_cost_E1(unit_rate_day, unit_rate_night, next_meter_reading, last_meter_reading):
    """Calculate cost of electric meter 1"""
>>>>>>> Stashed changes
    KWH_used = next_meter_reading - last_meter_reading
    cost = (KWH_used * unit_rate_night)/100
    return cost

<<<<<<< Updated upstream
def calculate_cost_E2(unit_rate_day, unit_rate_night, unit_rate_single):
    last_meter_reading_night = 299723
    next_meter_reading_night = 299510
    last_meter_reading_day = 84394
    next_meter_reading_day = 85262

=======
def calculate_cost_E2(unit_rate_day, unit_rate_night, unit_rate_single, next_meter_reading_day, next_meter_reading_night, last_meter_reading_day, last_meter_reading_night):
    """Calculate cost of electric meter 2"""
>>>>>>> Stashed changes
    KWH_used_day = next_meter_reading_day - last_meter_reading_day
    cost_day = (KWH_used_day * unit_rate_day)/100
    
    KWH_used_night = next_meter_reading_night - last_meter_reading_night
    cost_night = (KWH_used_night * unit_rate_night)/100

    single_rate_cost = ((KWH_used_day + KWH_used_night)*unit_rate_single)/100

    return cost_day, cost_night, single_rate_cost

<<<<<<< Updated upstream
def calculate_cost_G1(unit_rate_gas):
    last_meter_reading = int(input("Please Enter Last Gas Reading: "))
    next_meter_reading = int(input("Please Enter Next Gas Reading: "))
=======
def calculate_cost_G1(unit_rate_gas, next_meter_reading, last_meter_reading):
    """Caculate cost of gas"""
>>>>>>> Stashed changes
    KWH_used = next_meter_reading - last_meter_reading
    
    cost_gas = (KWH_used * unit_rate_gas)/100

    return cost_gas

def total_cost(cost_day, cost_night, single_rate_cost, cost_gas):
    """calculate cost of day rate, night rate and gas combined and single tarrif rate and gas combined """
    total = cost_day + cost_night + cost_gas
    cost_single = single_rate_cost + cost_gas
    return total, cost_single

<<<<<<< Updated upstream
def record(cost_total, cost_day, cost_night, cost_single, cost_gas):
    date = str(datetime.datetime.now())
=======
def cost_record(cost_total, cost_day, cost_night, cost_single, cost_gas):
    """Write monthly cost to cost records"""
    date = datetime.date()
>>>>>>> Stashed changes
    with open("gas_and_electric_cost_record.txt", "a") as file:
        file.write("Total: £{}, Electric Day: £{}, Electric Night: £{}, Cost Single Rate: £{}, Cost Gas: £{}\n".format(cost_total, cost_day, cost_night, cost_single, cost_gas, date))

<<<<<<< Updated upstream
=======
def get_last_readings():
    """Get last meter reading for calculation of next months cost"""
    df = pd.read_csv('meter_readings.csv')
    row = df.iloc[-1]
    return row

def add_meter_readings(E1, E2_day, E2_night, G1):
    
    """Add inputted meter readings to records"""

    date = datetime.datetime.now().date()

    if os.stat('meter_readings.csv').st_size == 0:
        readings_dict = {"E1": E1, "E2_day":E2_day, "E2_night":E2_night, "G1":G1, "Date":date}
        df = pd.DataFrame([readings_dict])
        df.to_csv('meter_readings.csv', index=False)
    else:
        df = pd.read_csv('meter_readings.csv')
        readings_dict = {"E1": E1, "E2_day":E2_day, "E2_night":E2_night, "G1":G1, "Date":date}
        df_dict = pd.DataFrame([readings_dict])
        df = pd.concat([df, df_dict], ignore_index=True)
        df.to_csv('meter_readings.csv', index=False)


def main():

    date = datetime.datetime.now().date()
    unit_rate_day = 30.61
    unit_rate_night = 20.28
    unit_rate_gas = 7.34
    unit_rate_single = 27.8376

    if os.stat('meter_readings.csv').st_size == 0:
        names = ["E1", "E2_day", "E2_night", "G1", "Date"]
        df_dict = {}
        for name in names:
            df_dict[name] = input("Please enter the previous reading for " + name + ":")
        last_readings = pd.DataFrame.from_dict([df_dict])
    else:
        last_readings = get_last_readings()
    
    next_meter_reading_E1 = 166204
    last_meter_reading_E1 = int(last_readings["E1"].item())
    E1_cost = calculate_cost_E1(unit_rate_day, unit_rate_night, next_meter_reading_E1, last_meter_reading_E1)


    last_meter_reading_night_E2 = int(last_readings["E2_night"].item())
    next_meter_reading_night_E2 = 299510
    last_meter_reading_day_E2 = int(last_readings["E2_day"].item())
    print(last_meter_reading_day_E2)
    next_meter_reading_day_E2 = 85263

    E2_cost_day, E2_cost_night, E2_single_rate_cost = calculate_cost_E2(unit_rate_day, unit_rate_night, unit_rate_single, next_meter_reading_day_E2, next_meter_reading_night_E2, last_meter_reading_day_E2, last_meter_reading_night_E2)
    print(E2_cost_day, E2_cost_night, E2_single_rate_cost)
    
    next_meter_reading_G1 = 8786
    last_meter_reading_G1 = int(last_readings["G1"].item())

    G1_cost = calculate_cost_G1(unit_rate_gas, next_meter_reading_G1, last_meter_reading_G1)
    add_meter_readings(next_meter_reading_E1, next_meter_reading_day_E2, next_meter_reading_night_E2, next_meter_reading_G1)
    print(G1_cost)


>>>>>>> Stashed changes

cost_gas = calculate_cost_G1(unit_rate_gas)
cost_day, cost_night, single_rate_cost = calculate_cost_E2(unit_rate_day, unit_rate_night, unit_rate_single)

cost_total, cost_single = total_cost(cost_day, cost_night, single_rate_cost, cost_gas)

print("Total: £{}, Electric Day: £{}, Electric Night: £{}, Cost Single Rate: £{}, Cost Gas: £{}".format(cost_total, cost_day, cost_night, cost_single, cost_gas))
record(cost_total, cost_day, cost_night, cost_single, cost_gas)