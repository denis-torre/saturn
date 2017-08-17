# Performs VST.
#######################################################
########## 1. Libraries ###############################
#######################################################
from rpy2.robjects import r, pandas2ri
from IPython.display import display, HTML
pandas2ri.activate()
r.source('static/R/tool_scripts/vst.R')

#######################################################
########## 2. Run #####################################
#######################################################

def analyze(dataset):

	# Get rawcount dataframe
	rawcount_dataframe = pandas2ri.py2ri(dataset['expression_dataframe'])

	# Run
	vst_dataframe = pandas2ri.ri2py(r.run_vst(rawcount_dataframe))

	# Add
	dataset['expression_dataframe'] = vst_dataframe

	# Display
	display(HTML('<h5>Variance Stabilized Transformation (VST)</h5><p>The rawcount dataframe has been normalized using VST, part of the DESeq2 package (<a href="https://rdrr.io/bioc/DESeq2/man/varianceStabilizingTransformation.html">link</a>).</p>'))
	display(dataset['expression_dataframe'].head())

	return dataset
