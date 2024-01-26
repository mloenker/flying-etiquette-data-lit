def features_trans_back(feature, number=None):
    '''
    This function turns the transformed answers back to the original one.
    Args: 
        - Feature: The Feature (Question) you refer to
        - number: The corresponding answer you need. 
                  Default is None.
                  If None is given whole transform of the feature will be given.
    '''

    if feature == 'On a 6 hour flight from NYC to LA, how many times is it acceptable to get up if you\'re not in an aisle seat?':
        times_map = {
            'More than five times': 0,
            'Four times': 1,
            'Three times': 2,
            'Twice': 3,
            'Once': 4,
            'It is not okay to get up during a flight': 5
            }
        return return_feature(times_map, number)


    if feature == 'Who should have control over the window shade?':
        shade_control_map = {
            'The person in the window seat should have exclusive control': 0,
            'Everyone in the row should have some say': 1
        }
        return return_feature(shade_control_map, number)
    
    if feature == 'Under normal circumstances, does a person who reclines their seat during a flight have any obligation to the person sitting behind them?':
        recline_obligation_map = {
            'Yes, they should not recline their chair if the person behind them asks them not to': 1,
            'No, the person on the flight has no obligation to the person behind them': 0
        }
        return return_feature(recline_obligation_map, number)
    
    if feature=='Gender':
        gender_map = {'Male': 0, 'Female': 1}
        return return_feature(gender_map, number)
    
    if feature == 'Age':
        age_map = {'18-29': 0, '30-44': 1, '45-60': 2, '> 60': 3}
        return return_feature(age_map, number)
    
    if feature=='Do you have any children under 18?':
        binary_map = {'Yes': 1, 'No': 0}
        return return_feature(binary_map, number)
    
    if feature=='Have you ever used personal electronics during take off or landing in violation of a flight attendant\'s direction?':
        binary_map = {'Yes': 1, 'No': 0}
        return return_feature(binary_map, number)
    
    if feature=='Have you ever smoked a cigarette in an airplane bathroom when it was against the rules?':
        binary_map = {'Yes': 1, 'No': 0}
        return return_feature(binary_map, number)
 
    if feature== 'Given the opportunity, would you eliminate the possibility of reclining seats on planes entirely?':
        binary_map = {'Yes': 1, 'No': 0}
        return return_feature(binary_map, number)
    
    if feature == 'Household Income':
        income_map = {'$0 - $24,999': 0, '$25,000 - $49,999': 1, '$50,000 - $99,999': 2, '$100,000 - $149,999': 3, '150000': 4}
        return return_feature(income_map, number)
    
    if feature=='Education':
        education_map = {'Less than high school degree': 0, 'High school degree': 1, 'Some college or Associate degree': 2, 
                     'Bachelor degree': 3, 'Graduate degree': 4}
        return return_feature(education_map, number)

    if feature=='Location (Census Region)':
        location_map = {'Pacific': 0, 'East North Central': 1, 'New England': 2, 'Mountain': 3, 'South Atlantic': 4, 
                    'East South Central': 5, 'Middle Atlantic': 6, 'West North Central': 7, 'West South Central': 8}
        return return_feature(location_map, number)
    
    if feature=='How often do you travel by plane?':
        travel_frequency_map = {
            'Every day': 5,
            'A few times per week': 4,
            'A few times per month': 3,
            'Once a month or less': 2,
            'Once a year or less': 1,
            'Never': 0
        }
        return return_feature(travel_frequency_map, number)
    
    if feature=='Do you ever recline your seat when you fly?':
        recline_seat_map = {
            'Always': 0,
            'Usually': 1,
            'About half the time': 2,
            'Once in a while': 3,
            'Never': 4
        }
        return return_feature(recline_seat_map, number)
        
    
    rudeness_questions = [
        'Generally speaking, is it rude to say more than a few words tothe stranger sitting next to you on a plane?',
        'Is it rude to ask someone to switch seats with you in order to be closer to friends?',
        'Is itrude to ask someone to switch seats with you in order to be closer to family?',
        'Is it rude to wake a passenger up if you are trying to go to the bathroom?',
        'Is itrude to wake a passenger up if you are trying to walk around?',
        'In general, is itrude to bring a baby on a plane?',
        'In general, is it rude to knowingly bring unruly children on a plane?'
    ]

    rudeness_map = {
        'No, not at all rude': 0,
        'Yes, somewhat rude': 1,
        'Yes, very rude': 2
    }
    for q in rudeness_questions:
        if feature==q:
            return return_feature(rudeness_map, number)
    
    rudeness_questions2 = ['Is itrude to move to an unsold seat on a plane?',
                            'Is itrude to recline your seat on a plane?'
                            ]
    rudeness_map2 = {
        'No, not rude at all': 0,
        'Yes, somewhat rude': 1,
        'Yes, very rude': 2
    }

    for q in rudeness_questions2:
        if feature==q:
            return return_feature(rudeness_map2, number)
    
    if feature=='In a row of two seats, who should get to use the middle arm rest?':
        armrest_two_map = {
            'The person in aisle':5,
            'The arm rests should be shared':4,
            'Other (please specify)':3,
            'Whoever puts their arm on the arm rest first':2,
            'The person by the window':1    
        }
        return return_feature(armrest_two_map, number)
    
    if feature=='In a row of three seats, who should get to use the two arm rests?':
        armrest_three_map = {
            'The person in the middle seat gets both arm rests':5,
            'The arm rests should be shared':4,
            'Other (please specify)':3,
            'Whoever puts their arm on the arm rest first':2,
            'The people in the aisle and window seats get both arm rests':1    
        }
        return return_feature(armrest_three_map, number)
    
    
def features_trans_back_shortened(feature, number=None):
    '''
    This function turns the transformed answers shortened back to the original one.
    Args: 
        - Feature: The Feature (Question) you refer to
        - number: The corresponding answer you need. 
                  Default is None.
                  If None is given whole transform of the feature will be given.
    '''

    if feature == 'On a 6 hour flight from NYC to LA, how many times is it acceptable to get up if you\'re not in an aisle seat?':
        times_map = {
            '>5': 0,
            '4': 1,
            '3': 2,
            '2': 3,
            '1': 4,
            '0': 5
            }
        return return_feature(times_map, number)


    if feature == 'Who should have control over the window shade?':
        shade_control_map = {
            'Person in window seat': 0,
            'Everyone in row': 1
        }
        return return_feature(shade_control_map, number)
    
    if feature == 'Under normal circumstances, does a person who reclines their seat during a flight have any obligation to the person sitting behind them?':
        recline_obligation_map = {
            'Yes': 1,
            'No': 0
        }
        return return_feature(recline_obligation_map, number)
    
    if feature=='Gender':
        gender_map = {'Male': 0, 'Female': 1}
        return return_feature(gender_map, number)
    
    if feature == 'Age':
        age_map = {'18-29': 0, '30-44': 1, '45-60': 2, '> 60': 3}
        return return_feature(age_map, number)
    
    if feature=='Do you have any children under 18?':
        binary_map = {'Yes': 1, 'No': 0}
        return return_feature(binary_map, number)
    
    if feature=='Have you ever used personal electronics during take off or landing in violation of a flight attendant\'s direction?':
        binary_map = {'Yes': 1, 'No': 0}
        return return_feature(binary_map, number)
    
    if feature=='Have you ever smoked a cigarette in an airplane bathroom when it was against the rules?':
        binary_map = {'Yes': 1, 'No': 0}
        return return_feature(binary_map, number)
 
    if feature== 'Given the opportunity, would you eliminate the possibility of reclining seats on planes entirely?':
        binary_map = {'Yes': 1, 'No': 0}
        return return_feature(binary_map, number)
    
    if feature == 'Household Income':
        income_map = {'$0 - $25k': 0, '$25k - $50k': 1, '$50k - $100k': 2, '$100k - $150k': 3, '>$150k': 4}
        return return_feature(income_map, number)
    
    if feature=='Education':
        education_map = {'No high school': 0, 'High school': 1, 'College or similar': 2, 
                     'Bachelor': 3, 'Graduate': 4}
        return return_feature(education_map, number)

    if feature=='Location (Census Region)':
        location_map = {'PC': 0, 'ENC': 1, 'NE': 2, 'MT': 3, 'SA': 4, 
                    'ESC': 5, 'MA': 6, 'WNC': 7, 'WSC': 8}
        return return_feature(location_map, number)
    
    if feature=='How often do you travel by plane?':
        travel_frequency_map = {
            'Daily': 5,
            'Bi-weekly': 4,
            'Weekly': 3,
            'Monthly': 2,
            'Yearly': 1,
            'Never': 0
        }
        return return_feature(travel_frequency_map, number)
    
    if feature=='Do you ever recline your seat when you fly?':
        recline_seat_map = {
            'Always': 0,
            'Usually': 1,
            'Alternating': 2,
            'Sometimes': 3,
            'Never': 4
        }
        return return_feature(recline_seat_map, number)
        
    
    rudeness_questions = [
        'Generally speaking, is it rude to say more than a few words tothe stranger sitting next to you on a plane?',
        'Is it rude to ask someone to switch seats with you in order to be closer to friends?',
        'Is itrude to ask someone to switch seats with you in order to be closer to family?',
        'Is it rude to wake a passenger up if you are trying to go to the bathroom?',
        'Is itrude to wake a passenger up if you are trying to walk around?',
        'In general, is itrude to bring a baby on a plane?',
        'In general, is it rude to knowingly bring unruly children on a plane?'
    ]

    rudeness_map = {
        'No': 0,
        'Somewhat' : 1,
        'Yes': 2
    }
    for q in rudeness_questions:
        if feature==q:
            return return_feature(rudeness_map, number)
    
    rudeness_questions2 = ['Is itrude to move to an unsold seat on a plane?',
                            'Is itrude to recline your seat on a plane?'
                            ]
    rudeness_map2 = {
        'No': 0,
        'Somewhat' : 1,
        'Yes': 2
    }

    for q in rudeness_questions2:
        if feature==q:
            return return_feature(rudeness_map2, number)
    
    if feature=='In a row of two seats, who should get to use the middle arm rest?':
        armrest_two_map = {
            'Aisle':5,
            'Share':4,
            'Other': 3,
            'First-comer': 2,
            'Win': 1    
        }
        return return_feature(armrest_two_map, number)
    
    if feature=='In a row of three seats, who should get to use the two arm rests?':
        armrest_three_map = {
            'Middle':5,
            'Share':4,
            'Other': 3,
            'First-comer':2,
            'Edges':1    
        }
        return return_feature(armrest_three_map, number)
    

def change_dict(dict):
    dict_changed = {}
    for k, v in dict.items():
        dict_changed[v] = k
    return dict_changed


def return_feature(map, number):
    map = change_dict(map)
    if number is None:
        return map
    else:
        return map[number]
    
    
def question_short(feature):
    q_short = [
                'Get up ',
                'Control over Window',
                'Obligation',
                'Children under 18',
                'Personal Electronics in Beginning/End',
                'Smoked Cigarettes in bathroom',
                'Elimininate reclining seats',
                'Travel Frequency',
                'Recline Seat',
                'Rude to talk Stranger',
                'Rude ask switch seats for friends',
                'Rude ask switch seats for family',
                'Rude wake up bathroom',
                'Rude wake up walking',
                'Rude to bring baby',
                'Rude to bring bad children',
                'Rude recline seat',
                'Rude move unsold seat',
                'Row two seats, who middle arm rest',
                'Row three seats, who two arm rests',
                'Location',
                'Education',
                'Age',
                'Gender'
                ]
    
    if feature == 'On a 6 hour flight from NYC to LA, how many times is it acceptable to get up if you\'re not in an aisle seat?':
        return 'Get up'

    if feature == 'Who should have control over the window shade?':
        return 'Control over Window'
    
    if feature == 'Under normal circumstances, does a person who reclines their seat during a flight have any obligation to the person sitting behind them?':
        return 'Obligation'
    
    if feature=='Gender':
        return 'Gender'
    
    if feature == 'Age':
        return 'Age'
    
    if feature=='Do you have any children under 18?':
        return 'Children under 18'
    
    if feature=='Have you ever used personal electronics during take off or landing in violation of a flight attendant\'s direction?':
        return 'Personal Electronics in Beginning/End'
    
    if feature=='Have you ever smoked a cigarette in an airplane bathroom when it was against the rules?':
        return 'Smoked Cigarettes in bathroom'
 
    if feature== 'Given the opportunity, would you eliminate the possibility of reclining seats on planes entirely?':
        return 'Elimininate reclining seat'
    
    if feature == 'Household Income':
        return 'Household Income'
    
    if feature=='Education':
        return 'Education'

    if feature=='Location (Census Region)':
        return 'Location'
    
    if feature=='How often do you travel by plane?':
        return 'Flying Frequency'
    
    if feature=='Do you ever recline your seat when you fly?':
        return 'Recline Seat'

    if feature=='Generally speaking, is it rude to say more than a few words tothe stranger sitting next to you on a plane?':
        return 'Rude to talk Stranger'
    
    if feature=='Is itrude to recline your seat on a plane?':
        return 'Rude recline seat'
    
    if feature=='Is it rude to ask someone to switch seats with you in order to be closer to friends?':
        return 'Rude ask switch seats for friends'
    
    if feature=='Is itrude to ask someone to switch seats with you in order to be closer to family?':
        return 'Rude ask switch seats for family'

    if feature=='Is it rude to wake a passenger up if you are trying to go to the bathroom?':
        return 'Rude wake up bathroom'
    
    if feature=='Is itrude to wake a passenger up if you are trying to walk around?':
        return 'Rude wake up walking'
    
    if feature=='In general, is itrude to bring a baby on a plane?':
        return 'Rude to bring baby'
    
    if feature=='In general, is it rude to knowingly bring unruly children on a plane?':
        return 'Rude to bring unruly children'

    if feature=='In a row of two seats, who should get to use the middle arm rest?':
        return 'Row two seats, who middle arm rest'
    
    if feature=='In a row of three seats, who should get to use the two arm rests?':
        return 'Row three seats, who two arm rests'

    if feature=='Is itrude to move to an unsold seat on a plane?':
        return 'Move unsold seat'