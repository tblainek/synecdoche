"""
Title: parameters.py
Purpose: Specify the geography for the template population, then set a series of 
probabilities to determine characteristics of the generated population.
"""


"""
COMMUNITY SELECTION
Choose a ZCTA code for the population serving as the template. Demographic
characteristics of the generated population will be extrapolated from the 
demographic distribution of this real population.
"""
zcta = 63117

"""
COMMUNITY SIZE
Choose True to scale the population to a new number of residents, or choose
False to generate the same number of residents reported in the Census.
"""
change_community = False # set to True or False
new_community = 1000 # generate a custom number of residents if change == True

def set_community(change_community, new_community, population_formatted):
    if change_community == True:
        community_size = int(new_community)
    else:
        community_size = int(population_formatted['pop_count'])

    return community_size

"""
ACQUIRED ATTRIBUTES: INCIDENCE
Adjust the probability of an acquired trait occurring based on person-level attributes.
Example: A risk probability of 0.01 means that 1 out of every 100 people in that category 
will acquire the trait if no other attributes are considered.
"""
age_risk_map = {
                1: 0.0001,  # <5yrs
                2: 0.00,    # 5-9yrs
                3: 0.00,    # 10-14 yrs
                4: 0.00,    # 15-19yrs
                5: 0.00,    # 20-24yrs
                6: 0.00,    # 25-29yrs
                7: 0.00,    # 30-34yrs
                8: 0.00,    # 35-39yrs
                9: 0.00,    # 40-44yrs
                10: 0.00,   # 45-49yrs 
                11: 0.00,   # 50-54yrs
                12: 0.03,   # 55-59yrs
                13: 0.047,  # 60-64yrs
                14: 0.072,  # 65-69yrs
                15: 0.109,  # 70-74yrs
                16: 0.155,  # 75-79yrs
                17: 0.239,  # 80-84yrs
                18: 0.245   # >85yrs
                }

sex_risk_map = {
                1: 0.096,   # male
                2: 0.065    # female
                }

race_risk_map = {
                1: 0.04,    # American Indian or Alaskan Native
                2: 0.02,    # Asian
                3: 0.06,    # Black or African American 
                4: 0.03,    # Hawaiian or Pacific Islander
                5: 0.03,    # Other Race
                6: 0.03     # White
                }

""" 
ACQUIRED ATTRIBUTES: OTHER CHARACTERISTICS
Adjust parameters for the probability of certain disease outcomes in the population. 
Lists can accept more/less values to reflect a different number of outcomes.
Note that total probability should == 1.
"""
prob_trait_dependent = [0.7, 0.2, 0.1] # outcome 1, outcome 2, outcome 3