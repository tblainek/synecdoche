"""
Title: Acquired Population Attributes, attr_acquired.py
Purpose: Generate attributes for each person that are acquired after 
base attributes, based on probability distributions in parameters.py. 
"""

import numpy as np
import pandas as pd
import datetime as dt
import random
import sys

# local modules
from utility import *
from parameters import *


def set_trait(age, age_risk_map, sex, sex_risk_map, race, race_risk_map):

    """ A trait occurs based on some mix of """
    if age in age_risk_map:
        risk_from_age = age_risk_map[age]
    else:
        risk_from_age = 0

    if sex in sex_risk_map:
        risk_from_sex = sex_risk_map[sex]
    else:
        risk_from_sex = 0

    if race in race_risk_map:
        risk_from_race = race_risk_map[race]
    else:
        risk_from_race = 0

    # probability of trait
    prob_trait = 1 - (1 - risk_from_age) * (1 - risk_from_sex) * (1 - risk_from_race)
    prob_not_trait = 1 - prob_trait
    resident_trait = np.random.choice(np.arange(1,3), p=[prob_not_trait,prob_trait])

    return resident_trait


def set_trait_dependent(prob_trait_dependent):
    
    # assign trait_dependent outcome using probability distribution
    resident_trait_dependent = np.random.choice(np.arange(1, len(prob_trait_dependent) + 1), p=prob_trait_dependent)

    return resident_trait_dependent
    

def set_trait_event_time():

    # set a random value within a range for the time Last Known Well
    year_start = 2020
    year_end = 2021
    start = dt.datetime(year_start, 1, 1, 0, 0, 0)
    years = year_end - year_start + 1
    end = start + dt.timedelta(days = 365 * years)
    date_random = start + (end - start) * random.random()
    resident_trait_event_time = date_random

    return resident_trait_event_time


def gen_attr_acquired(legend_attr_acquired, df):

    print(prefix + '... generating acquired attributes ...')

    population_acquired = pd.concat([df, pd.DataFrame(columns = list(legend_attr_acquired))], sort=False)

    trait = []
    for index, row in population_acquired.iterrows():
        trait.append(set_trait(row['age'], age_risk_map, row['sex'], sex_risk_map, row['race'], race_risk_map))
    population_acquired['trait'] = trait

    trait_dependent = []
    for i in population_acquired['trait']:
        if i == 2:
            trait_dependent.append(set_trait_dependent(prob_trait_dependent))
        else:
            trait_dependent.append('N/a')
    population_acquired['trait_dependent'] = trait_dependent

    trait_event_time = []
    for i in population_acquired['trait']:
        if i == 2:
            trait_event_time.append(set_trait_event_time())
        else:
            trait_event_time.append('N/a')
    population_acquired['trait_event_time'] = trait_event_time

    print(prefix + '... added acquired attributes.')

    return population_acquired
