"""
Title: Base Population Attributes, attr_base.py
Purpose: Generate the base population using demographic probabilities from the Census.
The composition of the selected ZCTA creates distributions determine the likelihood 
of different person-level attributes in the generated population.
"""

import numpy as np
import pandas as pd
from shapely.geometry import Polygon, MultiPolygon, Point
import shapely
import sys
import random
import uuid

# local modules
from utility import *
from parameters import *


def set_id():
    # alphanumeric to identify an individual person
    resident_id = uuid.uuid4()

    return resident_id


def set_age(prob_age):

    # generate age group for each person based on Census distribution
    resident_age = np.random.choice(np.arange(1, len(prob_age) + 1), p=prob_age)

    return resident_age


def set_sex(prob_sex):

    # generate gender for each person based on Census distribution
    resident_sex = np.random.choice(np.arange(1, len(prob_sex) + 1), p=prob_sex)

    return resident_sex


def set_race(prob_race):

    # generate race for each person based on Census distribution
    resident_race = np.random.choice(np.arange(1, len(prob_race) + 1), p=prob_race)

    return resident_race


def find_zcta(filename_json):

    # ingest ZCTA geojson for determining locations for each person
    df = pd.read_json(filename_json, orient='records')
    df = pd.json_normalize(df['features'])
    df_zcta = df[df['properties.ZCTA5CE10'] == str(zcta)]
    zcta_coords = df_zcta.iloc[0]['geometry.coordinates']
    shape_type = df_zcta.iloc[0]['geometry.type']

    return zcta_coords, shape_type


def set_location(zcta_coords, shape_type):
    
    # for each person, assign a random coordinate pair within the ZCTA
    coords = []
    if shape_type == 'Polygon':
        for lists in zcta_coords:
            for l in lists:
                k = tuple((l[0],l[1]))
                coords.append(k)
        poly = Polygon(coords)
        minx, miny, maxx, maxy = poly.bounds
        while True:
            p = Point(random.uniform(minx,maxx), random.uniform(miny,maxy))
            if poly.contains(p):
                return p
        resident_location = p
    else:
        resident_location = 'ZCTA shape not available.'

    return resident_location


def gen_attr_base(pop_count, prob_dict, legend_attr_base, filename_json):
    
    print(prefix + '... generating base population attributes ...')

    data = []
    zcta_coords, shape_type = find_zcta(filename_json)
    for i in range(pop_count):
        sys.stdout.write('\rGenerating Resident #: %s' % str(i))
        data.append([ set_id()
                     ,set_age(prob_dict.get('prob_age'))
                     ,set_sex(prob_dict.get('prob_sex'))
                     ,set_race(prob_dict.get('prob_race'))
                     ,set_location(zcta_coords, shape_type)
                    ])
    population_base = pd.DataFrame(data, columns = list(legend_attr_base))
    print('\n' + prefix + '... added base population attributes.')

    return population_base