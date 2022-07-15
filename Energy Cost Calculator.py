import datetime
import pandas as pd
import os

class energy_calculator:
    """Calculates energy bills for Economy 7 Gas and electric meters"""
    
    date = datetime.datetime.now().date()
    unit_rate_day = 30.61
    unit_rate_night = 20.28
    unit_rate_gas = 7.34
    unit_rate_single = 27.8376
    
    names = ["E1", "E2_day", "E2_night", "G1", "Date"]
    
    last_readings = pd.DataFrame()
    
    E1_cost = 0
    E2_cost_day = 0
    E2_cost_night = 0 
    E2_single_rate_cost = 0
    G1_cost = 0
    total = 0
    single_rate_total = 0

    next_readings = {}
    last_readings = {}

    def __init__(self):

        self.get_next_readings()
        self.get_last_readings()

        self.E1_cost = self.calculate_cost_E1(self.next_readings["E1"], self.last_readings["E1"])

        self.E2_cost_day, self.E2_cost_night, self.E2_single_rate_cost = self.calculate_cost_E2(self.next_readings["E2_day"], self.last_readings["E2_day"], self.next_readings["E2_night"], self.last_readings["E2_night"])

        self.G1_cost = self.calculate_cost_G1(self.next_readings["G1"], self.last_readings["G1"])

        self.add_meter_readings(self.next_readings["E1"], self.next_readings["E2_day"], self.next_readings["E2_night"], self.next_readings["G1"])

        self.calculate_total_cost()
        
        self.cost_record()


    def get_next_readings(self):
        """Get next readings from user"""

        self.next_readings["E1"] = int(input("Input next reading for E1:"))
        self.next_readings["E2_day"] = int(input("Input next meter reading E2_day:"))
        self.next_readings["E2_night"] = int(input("Input next reading for E2_night:"))
        self.next_readings["G1"] = int(input("Input next reading for G1:"))

    def get_last_readings(self):
        """Get last meter reading for calculation of next months cost"""

        if os.stat('meter_readings.csv').st_size == 0:
            df_dict = {}
            for name in self.names:
                if name == "Date":
                    self.last_readings[name] = self.date
                else:
                    self.last_readings[name] = int(input("Please enter the previous reading for " + name + ":"))
        else:
            df = pd.read_csv('meter_readings.csv')
            last_row = df.iloc[-1]
            self.last_readings = last_row.to_dict()

        return self.last_readings

    def calculate_cost_E1(self, next_meter_reading, last_meter_reading):
        """Calculate cost of electric meter 1"""

        KWH_used = next_meter_reading - last_meter_reading
        cost = (KWH_used * self.unit_rate_night)/100
        return cost
    
    def calculate_cost_E2(self, next_meter_reading_day, last_meter_reading_day, next_meter_reading_night, last_meter_reading_night):
        """Calculate cost of electric meter 2"""

        KWH_used_day = next_meter_reading_day - last_meter_reading_day
        cost_day = (KWH_used_day * self.unit_rate_day)/100
        
        KWH_used_night = next_meter_reading_night - last_meter_reading_night
        cost_night = (KWH_used_night * self.unit_rate_night)/100

        single_rate_cost = ((KWH_used_day + KWH_used_night)*self.unit_rate_single)/100

        return cost_day, cost_night, single_rate_cost
    
    def calculate_cost_G1(self, next_meter_reading, last_meter_reading):
        """Caculate cost of gas"""

        KWH = 11.25
        KWH_used = (next_meter_reading - last_meter_reading)*KWH
        
        cost_gas = (KWH_used * self.unit_rate_gas)/100

        return cost_gas
    
    def calculate_total_cost(self):
        """calculate cost of day rate, night rate and gas combined and single tarrif rate and gas combined """

        self.total = self.E1_cost + self.E2_cost_day + self.E2_cost_night + self.G1_cost
        self.single_rate_total = self.E2_single_rate_cost + self.G1_cost

 
    def add_meter_readings(self, E1, E2_day, E2_night, G1):
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

    def cost_record(self):
        """Write monthly cost to cost records"""

        with open("gas_and_electric_cost_record.txt", "a") as file:
            file.write("Total: £{}, Electric Day: £{}, Electric Night: £{}, Cost Single Rate: £{}, Cost Gas: £{}\n".format(self.total, self.E2_cost_day, self.E2_cost_night, self.G1_cost, self.single_rate_total, self.date))
            print("Total: £{}, Electric Day: £{}, Electric Night: £{}, Cost Gas: £{}, Cost Single Rate: £{}\n".format(self.total, self.E2_cost_day, self.E2_cost_night, self.G1_cost, self.single_rate_total, self.date))



if __name__ == '__main__':
    calculator = energy_calculator()
    