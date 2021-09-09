"""
Title: translation.py
Purpose: Load demographic data using parameters in mapping.py
"""

import pandas as pd

def data_extract(filename_import, mapping, col_zcta, zcta):
    """ Get data from Census data file and output dataframe. """

    # read in
    df = pd.read_csv(filename_import)
    zcta_data = {}
    # load data only for this ZCTA using Mapping columns
    for k in mapping.keys():
        df_key = mapping[k]
        [df_value] = df.loc[df[col_zcta] == zcta][df_key].values
        zcta_data[k] = df_value

    return zcta_data


def format_data(df):
    """ Set proportions using population counts. """

    # total population as integer
    df['pop_count'] = int(df['pop_count']) 

    # convert count to proportion of population 
    for k, v in df.items(): 
        if '_age_' in k or '_sex_' in k:
            df[k] = df[k] / df['pop_count']
        elif '_race_' in k:
            df[k] = df[k] / df['pop_count_race']
        else:
            df[k] = df[k]

    return df


def create_prob(df):
    """ Set probability value dictionary. """

    # open variables
    prob_dict = {}
    prob_age = []
    prob_sex = []
    prob_race = []

    # loop through
    for k, v in df.items():
        if '_age_' in k:
            prob_age.append(df[k])
        elif '_sex_' in k:
            prob_sex.append(df[k])
        elif '_race_' in k:
            prob_race.append(df[k])
        else:
            pass

    prob_dict['prob_age'] = prob_age
    prob_dict['prob_sex'] = prob_sex
    prob_dict['prob_race'] = prob_race

    return prob_dict
