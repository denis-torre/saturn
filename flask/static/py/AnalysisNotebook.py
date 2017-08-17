#################################################################
#################################################################
########## 1. Libraries #########################################
#################################################################
#################################################################
import nbformat as nbf
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter

#################################################################
#################################################################
########## 2. Analysis Notebook Generator #######################
#################################################################
#################################################################

def generate_jupyter_notebook(config):

	# Add notebook
	notebook = nbf.v4.new_notebook()

	# Add description
	notebook['cells'].append(nbf.v4.new_markdown_cell('# On-the-fly Jupyter Analysis\n## 1. Load Modules'))

	# Setup code
	notebook['cells'].append(nbf.v4.new_code_cell('\n'.join(['# Setup', '%run static/py/init.ipy'])))

	# Add datasets label
	notebook['cells'].append(nbf.v4.new_markdown_cell('## 2. Get Datasets'))

	# Loop through datasets
	for dataset in config['datasets']:

		# Get data
		notebook['cells'].append(nbf.v4.new_code_cell('\n'.join(['# Get data', 'AnalysisData.fetch_dataset(dataset_accession="{accession}", download_script="{script}")'.format(**dataset)])))

		# Check if normalization is specified
		if 'normalization' in dataset.keys():

			# Loop through normalization methods
			for normalization_method in dataset['normalization']:

				# Normalize
				notebook['cells'].append(nbf.v4.new_code_cell('\n'.join(['# Normalize data', 'AnalysisData.normalize_dataset(normalization_script="{normalization_script}")'.format(**normalization_method)])))


	# Add analysis label
	notebook['cells'].append(nbf.v4.new_markdown_cell('## 3. Analyze'))

	# Add analyses
	for index, tool in enumerate(config['tools']):

		# Title
		notebook['cells'].append(nbf.v4.new_markdown_cell('### 3.'+str(index+1)+' '+tool['tool_title'].title()))
		
		# Get parameter string
		# tool['parameter_str'] = ', '.join(['='.join([key, '"'+value+'"']) for key, value in tool['params'].iteritems()])

		# Run analysis
		notebook['cells'].append(nbf.v4.new_code_cell('\n'.join(['# Run analysis', 'AnalysisData.analyze_dataset(tool_name="{tool_name}")'.format(**tool)])))

	# Add preprocessor
	ep = ExecutePreprocessor(timeout=600)

	# Process
	ep.preprocess(notebook, {'metadata': {'path': '.'}})

	# create a configuration object that changes the preprocessors
	from traitlets.config import Config
	c = Config()
	c.HTMLExporter.preprocessors = ['nbconvert.preprocessors.ExtractOutputPreprocessor']

	# create the new exporter using the custom config
	html_exporter_with_figs = HTMLExporter(config=c)
	html_exporter_with_figs.preprocessors
	jupyter_notebook_html = html_exporter_with_figs.from_notebook_node(notebook)[0]

	# Return
	return jupyter_notebook_html
