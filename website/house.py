#!/usr/bin/env python3
from uszipcode import SearchEngine
import requests
import json
import pandas as pd
import numpy as np


class County:
    def __init__(self, county):
        self.county = county
        self.solar_install_cost = 0
        self.average_electric_bill = 0
        self.average_number_solar_panels = 0
        self.average_residential_electricity_price = 0
        self.average_energy_produced_per_day = 0

    def set_info(self):
        fh = open("solarinfo.csv")
        df = pd.read_csv(fh)
        for i in range(len(df)):
            if df.loc[i, 'County'] == self.county:
                self.solar_install_cost = df.loc[i,
                                                 'Solar Installation Cost (of 5kW System)']
                self.average_electric_bill = df.loc[i,
                                                    'Average Electric Bill per County']
                self.average_number_solar_panels = df.loc[i,
                                                          'Average Number of Solar Panels per Household']
                self.average_residential_electricity_price = df.loc[i,
                                                                    'Average Residential Electricity Price per County (kWh)']
                self.average_energy_produced_per_day = df.loc[i,
                                                              'Average Energy Produced in each County Per Day']
                break


class House:
    def __init__(self, zipcode, num_panels):
        self.zipcode = str(zipcode)
        self.num_panels = num_panels
        self.county = None
        self.state = ""
        self.power_cost = 0

    def set_county(self, county):
        # sr = SearchEngine()
        # zipcode = sr.by_zipcode(self.zipcode)
        # county = zipcode.values()[5][:-7]
        county = county
        self.county = County(county)
        self.county.set_info()

    def set_state(self, state):
        # sr = SearchEngine()
        # zipcode = sr.by_zipcode(self.zipcode)
        # self.state = zipcode.values()[6]
        self.state = state

    def set_power_cost(self, cost):
        self.power_cost = cost

    def power_estimate_ten_year(self):
        return self.power_cost * 10 * 12


class SolarPanel:
    def __init__(self, length=1.6, width=1, power=300):
        self.length = length
        self.width = width
        self.power = power


class SolarSystem:
    def __init__(self, num_panels):
        self.output_peak = 0
        self.sqm = 0
        self.solar_panel_type = None
        self.num_panels = num_panels
        self.solar_system_ten_year = 0

    def set_solar_panel_type(self, length=1.6, width=1, power=300):
        solar_panel = SolarPanel(length, width, power)
        self.solar_panel_type = solar_panel

    def set_output_peak(self):
        if self.solar_panel_type is None:
            self.set_solar_panel_type()
        self.output_peak = self.num_panels * self.solar_panel_type.power

    def set_sqm(self, solar_panel):
        self.sqm = solar_panel.length*solar_panel.width * self.num_panels

    def estimate(self, num_panels, price_by_state):
        if self.output_peak == 0:
            self.set_output_peak()
        ratio = self.output_peak/5000
        estimate = ratio * price_by_state
        return estimate

    def set_solar_system_ten_year(self, house):
        if house.county is None:
            house.set_county()


def OnlyFunctionYouNeed(zipcode, num_panels, monthly_bill, county, state) -> float:
    myhouse = House(zipcode, num_panels)
    solar_system = SolarSystem(num_panels)
    solar_system.set_output_peak()
    myhouse.set_county(county)
    myhouse.set_state(state)
    myhouse.set_power_cost(monthly_bill)
    ten_year_estimate = myhouse.power_estimate_ten_year()
    solar_startup_cost = solar_system.estimate(
        num_panels, myhouse.county.solar_install_cost)

    sub_daily_energy = 3.25 * solar_system.output_peak

    total_energy_day = myhouse.county.average_energy_produced_per_day * \
        1000 - sub_daily_energy
    energy_cost_hour = (total_energy_day/24 * myhouse.county.average_residential_electricity_price /
                        100)/(myhouse.county.average_energy_produced_per_day*1000/24)
    energy_cost_day = energy_cost_hour * 24
    energy_cost_month = energy_cost_day * 31
    ten_year_new = energy_cost_month * 12 * 10

    price = -(ten_year_new - ten_year_estimate) - solar_startup_cost

    return f'{round(price,2)}'


def UpfrontCost(zipcode, num_panels, county, state):
    myhouse = House("46556", num_panels)
    solar_system = SolarSystem(num_panels)
    myhouse.set_county(county)
    myhouse.set_state(state)
    res = solar_system.estimate(num_panels, myhouse.county.solar_install_cost)
    return f'{round(res,2)}'


if __name__ == '__main__':
    num_panels = 15
    monthly_bill = 150
    zipcode = 46001
    county = "St. Joseph"
    state = "Indiana"
    print(OnlyFunctionYouNeed(zipcode, num_panels, monthly_bill, county, state))
    print(UpfrontCost(zipcode, num_panels, county, state))
