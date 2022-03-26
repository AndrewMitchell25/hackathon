#!/usr/bin/env python3
from uszipcode import SearchEngine

class House:
    def __init__(self, zipcode, surface_area, angle = 30):
        self.zipcode = str(zipcode)
        self.county = ""
        self.state = ""
        self.surface_area = surface_area
        self.angle = angle

    def set_county(self):
        sr = SearchEngine(download_url="https://your-private-storage.sqlite")
        zipcode = sr.by_zipcode(self.zipcode)
        self.county = zipcode.values()[5]

    def set_state(self):
        sr = SearchEngine(download_url="https://your-private-storage.sqlite")
        zipcode = sr.by_zipcode(self.zipcode)
        self.state = zipcode.values()[6]

    def power_estimate(self):
        if self.county == "":
            self.set_county()


class SolarPanel:
    def __init__(self, length = 1.6, width = 1, power = 300):
        self.length = length
        self.width = width
        self.power = power


class SolarSystem:
    def __init__(self, output_peak = 5000, sqm = 17.2):
        self.output_peak = output_peak
        self.sqm = sqm
        self.solar_panel_type = None
        self.num_panels = 0
        self.estimate = 0

    def set_solar_panels(self, length = 1.6, width = 1, power = 300):
        solar_panel = SolarPanel(length, width, power)
        self.num_panels = int(self.output_peak / solar_panel.power)
        self.solar_panels = solar_panel


    def set_sqm(self, solar_panel):
        self.sqm = solar_panel.length*solar_panel.width * self.num_panels

    def set_estimate(self):
        if self.num_panels == 0:
            self.estimate = 0


if __name__ == '__main__':
    myhouse = House("89110", 10000, 30)
    myhouse.set_county()
    myhouse.set_state()
    print(myhouse.county, myhouse.state)
