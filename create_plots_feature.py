from features_trans_back import features_trans_back_shortened as ftbs
from features_trans_back import question_short as qs
import matplotlib.pyplot as plt


class MakeFeaturePlots:
    def __init__(self, df, feature):
        self.df = df 
        self.feature = feature       

    def list_features(self, get_f = None):
        '''
        this returns a list of all features. If number is giving it returns the value (feature) for giving index number
        params:
            get_f (int): default is None

        '''

        f_list = ['How often do you travel by plane?',
                'Do you ever recline your seat when you fly?', 'How tall are you?',
                'Do you have any children under 18?',
                'In a row of three seats, who should get to use the two arm rests?',
                'In a row of two seats, who should get to use the middle arm rest?',
                'Who should have control over the window shade?',
                'Is itrude to move to an unsold seat on a plane?',
                'Generally speaking, is it rude to say more than a few words tothe stranger sitting next to you on a plane?',
                'On a 6 hour flight from NYC to LA, how many times is it acceptable to get up if you\'re not in an aisle seat?',
                'Under normal circumstances, does a person who reclines their seat during a flight have any obligation to the person sitting behind them?',
                'Is itrude to recline your seat on a plane?',
                'Given the opportunity, would you eliminate the possibility of reclining seats on planes entirely?',
                'Is it rude to ask someone to switch seats with you in order to be closer to friends?',
                'Is itrude to ask someone to switch seats with you in order to be closer to family?',
                'Is it rude to wake a passenger up if you are trying to go to the bathroom?',
                'Is itrude to wake a passenger up if you are trying to walk around?',
                'In general, is itrude to bring a baby on a plane?',
                'In general, is it rude to knowingly bring unruly children on a plane?',
                'Have you ever used personal electronics during take off or landing in violation of a flight attendant\'s direction?',
                'Have you ever smoked a cigarette in an airplane bathroom when it was against the rules?',
                'Gender', 
                'Age', 
                'Household Income', 
                'Education',
                'Location (Census Region)'
                ]
        
        if get_f is None:
            return f_list
        else:
            return f_list[get_f]

    def calculate_conditional_probability(self, changed_df, condition_column, event_column):
        # Group by the condition column and calculate the conditional probabilities
        probabilities = changed_df.groupby(condition_column)[event_column].value_counts(normalize=True).unstack()

        # Fill NaN values with 0 (when the condition is not present for a specific event)
        probabilities = probabilities.fillna(0)

        return probabilities

    def many_plots(self):
        questions = list(self.df.columns)[1:]
        counter = 0 
        fig, ax = plt.subplots(4, 6, figsize=(45,35))
        ax_flat = ax.flatten()
        for q in questions:
            if q == self.feature:
                continue
            if q == 'How tall are you?':
                continue
            conditional_prob = self.calculate_conditional_probability(self.df, self.feature, q)

            ax = ax_flat[counter]
            
            conditional_prob.plot(kind='bar', stacked=False, width=0.7,ax=ax)

            ax.set_title(qs(conditional_prob.columns.name))
            ax.set_xlabel(conditional_prob.index.name)
            ax.set_ylabel('Percentage')
            feature_name = ftbs(conditional_prob.columns.name)
            q_name = conditional_prob.index.name
            q_name_list = conditional_prob.index.tolist()
            
            answer_change = []
            for i in q_name_list:
                i = float(i)
                answer_change.append(ftbs(q_name, i))

            columns_list = []
            for i in conditional_prob.columns.tolist():
                i = float(i)
                columns_list.append(ftbs(conditional_prob.columns.name, i))

            ax.set_xticks(range(len(q_name_list)))
            ax.set_xticklabels(answer_change)
            ax.legend(columns_list)

            counter+=1
        
        plt.tight_layout()  # Adjust layout for better visualization
        plt.show()         
            