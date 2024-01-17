from features_trans_back import features_trans_back_shortened as ftbs
from features_trans_back import question_short as qs
import matplotlib.pyplot as plt


class MakeFeaturePlots:
    def __init__(self, df, feature):
        self.df = df 
        self.feature = feature       


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
            q_name = ftbs(conditional_prob.index.name)
            ax.set_xticks(range(len(q_name)))
            ax.set_xticklabels(list(q_name.values()))
            ax.legend(list(feature_name.values()))

            counter+=1
        plt.tight_layout()  # Adjust layout for better visualization
        plt.show()    
        