"""
Name: utility.py
Purpose: Control input files, their origin, and the destination of output files.
"""

# requirements
import datetime as dt

# local modules
from parameters import * 

# record date/time for file
now = dt.datetime.now()
dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")

# package name
prefix = 'CENSUS SIM: '

# set directories for input and output files
filepath_input = './input'
filepath_output = './output'

# name of Census dataset
filename_census = filepath_input + '/acs_zcta_2018.csv'

# location of Census ZCTA JSON
filename_json = filepath_input + '/zcta.json'

# name of the zcta column in import file
col_zcta = 'zip code tabulation area'

# export location
filename_export = filepath_output + '/results_zcta_' + str(zcta) + '__' + dt_string + '.csv'