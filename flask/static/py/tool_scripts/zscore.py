# Performs Z-score.
#######################################################
########## 1. Libraries ###############################
#######################################################
import numpy as np

#######################################################
########## 2. Run #####################################
#######################################################

def analyze(dataset, log10=True):

	# Log-transform
	if log10:
		dataset['expression_dataframe'] = np.log10(dataset['expression_dataframe']+1)

	# Get gene variance
	# topGenes = dataset['expression_dataframe'].apply(np.var, 1).sort_values(ascending=False).index[:1000]

	# # Get subset
	# dataset['expression_dataframe'] = dataset['expression_dataframe'].loc[topGenes]

	# Z-score
	# dataset['expression_dataframe'] = ((dataset['expression_dataframe'] - dataset['expression_dataframe'].mean())/dataset['expression_dataframe'].std())
	# dataset['expression_dataframe'] = ((dataset['expression_dataframe'].T - dataset['expression_dataframe'].T.mean())/dataset['expression_dataframe'].T.std()).T
	# dataset['expression_dataframe'].fillna(0, inplace=True)
	return dataset
