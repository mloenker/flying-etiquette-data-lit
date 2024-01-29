# flying-etiquette-data-lit
Original Survey: [flying-etiquette-survey](https://github.com/fivethirtyeight/data/blob/master/flying-etiquette-survey/flying-etiquette.csv)\
This repository contains a dataset and code for the analysis of a survey on airplane etiquette. The dataset includes responses from individuals regarding their travel habits, seat preferences, and opinions on various in-flight behaviors. The purpose of this analysis is to uncover interesting insights and patterns within the dataset.

We used Python 3.8.5, with the libraries numpy 1.23.2, matplotlib 3.7.4, prince 0.13.0, tueplots 0.0.12, scipy 1.10.1, scikit-learn 1.3.2, pandas 1.4.3.


## Hypotheses
1.  "Age" affects "electronics use during taking off"

    Chi² test p-value: 4.54e-10
    - [x] Significant Result

2.  "Having children" affects "finding it rude to bring unruly children on planes"

    Chi² test p-value: 2.29e-09
    - [x] Significant Result

3. "Body height" affects ones' attitude toward seat reclining

    "Height" and "Given the opportunity, would you eliminate the possibility of reclining seats on planes entirely?" Anova p-value: 0.017
    - [x] Significant Result
