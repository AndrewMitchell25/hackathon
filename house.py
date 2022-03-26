#!/usr/bin/env python3
from uszipcode import SearchEngine

class House:
    def __init__(self, zipcode, surface_area, angle = 30):
        self.zipcode = str(zipcode)
        self.county = ""
        self.surface_area = surface_area
        self.angle = angle

    def set_county(self):
        sr = SearchEngine(download_url="https://your-private-storage.sqlite")
        zipcode = sr.by_zipcode(self.zipcode)
        self.county = zipcode.values()[5]

    def power_estimate(self):
        if self.county == "":
            self.set_county()


class SolarPanels:
    def __init__(self, type)


if __name__ == '__main__':
    myhouse = House("89110", 10000, 30)
    myhouse.set_county()
    print(myhouse.county)i
