"""
Name: main.py
Purpose: Controller function. Run this file to generate a population.
"""

# requirements
import numpy as np
import pandas as pd
import datetime as dt
import random

# local modules
from parameters import *
from utility import *
from mapping import *
from translation import *
from attr_base import *
from attr_acquired import *


if __name__ == '__main__':

    """
    from: translation.py
    - Load population data from the Census extract
    - Assert dictionary of probabilities for assigning attributes based on demography
    """
    population_extracted = data_extract(filename_census, col_mapping, col_zcta, zcta)
    print(prefix + '... data loaded from: ' + filename_census)
    population_formatted = format_data(population_extracted)
    prob_dict = create_prob(population_formatted)

    """
    from: attr_base.py
    Generate the resident population and their basic characteristics
    """
    community_size = set_community(change_community, new_community, population_formatted)
    base = gen_attr_base(community_size, prob_dict, legend_attr_base, filename_json)

    """
    from: attr_acquired.py
    Generate characteristics acquired in part due to basic characteristics
    """
    acquired = gen_attr_acquired(legend_attr_acquired, base)

    """
    send results to CSV 
    """
    acquired['zcta'] = zcta
    acquired.to_csv(filename_export)
    print(prefix + '... data saved to: ' + filename_export)
