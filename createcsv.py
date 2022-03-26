import numpy as np
import pandas as pd
import random


def csvcreate():
    db = pd.DataFrame(columns = ["County","State","Solar Installation Cost (of 5kW System)","Average Electric Bill per County", "Average Number of Solar Panels per Household"])

    county = ['Ohio', 'Dearborn', 'Allen', 'Hendricks', 'Marion', 'Hamilton', 'Boone', 'Crawford', 'Kosciusko', 'Vanderburgh', 'Daviess', 'Clay', 'Warrick', 'Delaware', 'Tipton', 'Wells', 'LaPorte', 'Shelby', 'Adams', 'Elkhart', 'Cass', 'Clark', 'Lawrence', 'Hancock', 'DeKalb', 'Monroe', 'Porter', 'Vigo', 'Starke', 'Steuben', 'Pike', 'Decatur', 'Johnson', 'Bartholomew', 'Floyd', 'Grant', 'Tippecanoe', 'Wabash', 'Fountain', 'Clinton', 'St. Joseph', 'Pulaski', 'Lake', 'LaGrange', 'Spencer', 'Washington', 'Madison', 'Dubois', 'Jefferson', 'Knox', 'Franklin']
    size = len(county)

    state = ['IN'] * size
    solarcost = [9916.00] * size
    electric = round(random.uniform(108.04,148.04),2)
    solarcnt = np.random.normal(17,2,size)
    solarcnt = [round(solarcnt[i]) for i in range(size)]

    db["County"] = county
    db["State"] = state
    db["Solar Installation Cost (of 5kW System)"] = solarcost
    db["Average Electric Bill per County"] = electric
    db["Average Number of Solar Panels per Household"] = solarcnt

    db.to_csv("solarinfo.csv", index=False)










