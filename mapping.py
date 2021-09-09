"""
Title: Feature Map, mapping.py
Purpose: Normalize column names from a data file granular to ZCTA.
"""

# map column names to variables
# begin column names for age groupings with 'pop_age_'
# begin column names for sex groupings with 'pop_sex_'
# begin column names for race groupings with 'pop_race_'
col_mapping = {
    'pop_count': 'Total Population'
    ,'pop_sex_m': 'Pop. Male'
    ,'pop_sex_f': 'Pop. Female'
    ,'pop_age_1': 'Pop. Under 5 Years'
    ,'pop_age_2': 'Pop. 5-9 Years'
    ,'pop_age_3': 'Pop. 10-14 Years'
    ,'pop_age_4': 'Pop. 15-19 Years'
    ,'pop_age_5': 'Pop. 20-24 Years'
    ,'pop_age_6': 'Pop. 25-29 Years'
    ,'pop_age_7': 'Pop. 30-34 Years'
    ,'pop_age_8': 'Pop. 35-39 Years'
    ,'pop_age_9': 'Pop. 40-44 Years'
    ,'pop_age_10': 'Pop. 45-49 Years'
    ,'pop_age_11': 'Pop. 50-54 Years'
    ,'pop_age_12': 'Pop. 55-59 Years'
    ,'pop_age_13': 'Pop. 60-64 Years'
    ,'pop_age_14': 'Pop. 65-69 Years'
    ,'pop_age_15': 'Pop. 70-74 Years'
    ,'pop_age_16': 'Pop. 75-79 Years'
    ,'pop_age_17': 'Pop. 80-84 Years'
    ,'pop_age_18': 'Pop. Over 85 Years'
    ,'pop_count_race': 'Pop. Race'
    ,'pop_race_amerind': 'Pop. AmInd or Alaska Alone'
    ,'pop_race_asian': 'Pop. Asian Alone'
    ,'pop_race_black': 'Pop. Black or AfrAm Alone'
    ,'pop_race_hawpacisl': 'Pop. Hawaiian or PacIsl Alone'
    ,'pop_race_other': 'Pop. Other Race Alone'
    ,'pop_race_white': 'Pop. White Alone'
}

# base population attributes
legend_attr_base = {
    'id': 'Unique ID value assigned, random string'
    ,'age': 'Resident Age: 1 = <5yrs, 2 = 5-9yrs, 3 = 10-14 yrs, 4 = 15-19yrs, 5 = 20-24yrs, 6 = 25-29yrs, 7 = 30-34yrs, 8 = 35-39yrs, 9 = 40-44yrs, 10 = 45-49yrs, 11 = 50-54yrs, 12 = 55-59yrs, 13 = 60-64yrs, 14 = 65-69yrs, 15 = 70-74yrs, 16 = 75-79yrs, 17 = 80-84yrs, 18 = >85yrs'
    ,'sex': 'Resident Sex: 1 = Male, 2 = Female'
    ,'race': 'Resident Race: 1 = American Indian or Alaska Alone; 2 = Asian Alone; 3. Black or AfrAm Alone; 4. Hawaiian or PacIsl Alone; 5. Other Race Alone; 6. White Alone'
    ,'location': 'Resident Location: Latitude and Longitude of that resident within the geography specified'
}

# acquired attributes
legend_attr_acquired = {
    'trait': 'Trait did or did not occur. 1 = Trait not present, 2 = Trait present'
    ,'trait_dependent': 'If trait occurs, likelihood of some other detail about the trait. 1 = Variant 1, 2 = Variant 2'
    ,'trait_event_time': 'Date and time of trait occurring within this year'
}
