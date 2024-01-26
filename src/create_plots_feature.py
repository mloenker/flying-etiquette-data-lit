from features_trans_back import features_trans_back_shortened as ftbs
from features_trans_back import question_short as qs
import os
import matplotlib.pyplot as plt
from tueplots import bundles


# this provides the color palette of Uni Tuebingen
from tueplots.constants.color import rgb 
# e.g. as rgb.tue_blue, rgb.tue_red, etc.

class MakeFeaturePlots:
    def __init__(self, df, feature):
        self.df = df 
        self.feature = feature       

    def list_features(self, get_f = None):
        '''
        this returns a list of all features. If number is giving it returns the value (feature) for giving index number
        params:
            get_f (int, optional): gets the feature for the given index number

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
        """
        Calculates conditional probabilities based on the specified condition and event columns.

        This function takes a DataFrame, groups it by a specified condition column, and calculates
        the conditional probabilities for each level of the event column. The result is a DataFrame
        where each row represents a level of the condition column, and each column represents a level
        of the event column.

        Parameters:
        - self: The instance of the class containing the dataset and necessary methods.
        - changed_df (pd.DataFrame): The DataFrame containing the data for calculation.
        - condition_column (str): The column used for conditioning the probabilities.
        - event_column (str): The column for which conditional probabilities are calculated.

        Returns:
        - pd.DataFrame: A DataFrame representing conditional probabilities for each combination of
        levels in the condition and event columns.
        """

        # Group by the condition column and calculate the conditional probabilities
        probabilities = changed_df.groupby(condition_column)[event_column].value_counts(normalize=True).unstack()

        # Fill NaN values with 0 (when the condition is not present for a specific event)
        probabilities = probabilities.fillna(0)

        return probabilities


    def plot_single_conditional_probabilities(self, target_feature, title=None, color=None, save_plot=None):
        """
        Plots the conditional probability distribution of one feature given a specific target feature.

        This function generates a bar plot representing the conditional probability distribution
        of pne feature given a specified target feature. The target feature is conditioned upon,
        and the resulting plot shows the probabilities for each level of the target feature.

        Parameters:
        - self: The instance of the class containing the dataset and necessary methods.
        - target_feature (str): The feature for which conditional probabilities are calculated and plotted.
        - title (str, optional): The title for the plot. If not provided, it is derived from the target feature.
        - color (list, optional): A list of colors for the bars in the plot. If not provided, default colors are used.
        - save_plot (str, optional): If provided, the plot is saved in the doc/AnalysisPassengerBehaviour/fig folder with the specified name.

        Returns:
        - None
        """

        # set plotting stylesheet
        plt.rcParams.update(bundles.icml2022(column='half', usetex=False))
        plt.rcParams.update({
            'text.usetex': False,
            'font.family': 'serif',
            'text.latex.preamble': '\\usepackage{times} ',
            'figure.figsize': (3.25*2.77, 2.0086104634371584*1.4),
            'figure.constrained_layout.use': True,
            'figure.autolayout': False,
            'savefig.bbox': 'tight',
            'savefig.pad_inches': 0.015,
            'font.size': 11+5,
            'axes.labelsize': 8+3,
            'legend.fontsize': 8+3,
            'xtick.labelsize': 8+3,
            'ytick.labelsize': 8+3,
            'axes.titlesize': 11+5
        })

        conditional_prob = self.calculate_conditional_probability(self.df, self.feature, target_feature)

         # Use a specific color from tueplots.constants.color
        if color==None:
            color = [rgb.tue_red, rgb.tue_green, rgb.tue_blue, rgb.tue_orange]  # Replace tue_blue with the desired color constant

        conditional_prob.plot(kind='bar', stacked=False, color=color)
       
        if title==None:
            title = qs(conditional_prob.columns.name)
        
        plt.title(title)
        plt.xlabel(conditional_prob.index.name)
        plt.ylabel('Percentage')
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

        plt.xticks(range(len(q_name_list)), answer_change, rotation=0)
        plt.legend(columns_list, loc='upper right')
        if save_plot != None:
            path_fig = '../../doc/AnalysisPassengerBehaviour/fig'
            plt.savefig(os.path.join(path_fig, save_plot))
        plt.show()
        


    def plot_conditional_probabilities(self):
        """
        Plots conditional probabilities for each question in the dataset, given a specified feature.

        This function generates a set of bar plots, each representing the conditional probability distribution
        of a question given a specified feature. The plots are arranged in a 4x6 grid for better visualization.

        Parameters:
        - self: The instance of the class containing the dataset and necessary methods.
        
        Returns:
        - None

        Note:
        - The 'feature' attribute of the class instance is used as the conditioning feature.
        - The function skips plotting the conditional probability if the question is the same as the feature or
        if the question is 'How tall are you?'.
        """

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