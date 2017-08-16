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
########## 2. Analysis Notebook Class ###########################
#################################################################
#################################################################

def generate_jupyter_notebook(config):

	# Add notebook
	notebook = nbf.v4.new_notebook()

	# Add description
	notebook['cells'].append(nbf.v4.new_markdown_cell('# Analysis Notebook\n## 1. Load Modules'))

	# Setup code
	notebook['cells'].append(nbf.v4.new_code_cell('\n'.join([
		'import sys', 'import plotly', 'plotly.offline.init_notebook_mode()', 'sys.path.append("static/py")', 'from data_scripts import *', 'from tool_scripts import *'])))

	# Fetch dataset
	notebook['cells'].append(nbf.v4.new_markdown_cell('## 2. Get Dataset'))
	notebook['cells'].append(nbf.v4.new_code_cell('\n'.join(['# Get data', 'dataset = {script}.fetch_dataset("{accession}")'.format(**config['dataset'])])))
	notebook['cells'].append(nbf.v4.new_code_cell('{script}.display_dataset(dataset)'.format(**config['dataset'])))

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

#######################################################
########## 1. Initialize ##############################
#######################################################

class AnalysisNotebook:

	def __init__(self, config_dict):

		# Add notebook
		self.notebook = nbf.v4.new_notebook()

		# Add description
		self.notebook['cells'].append(nbf.v4.new_markdown_cell('# Analysis Notebook\n## 1. Load Modules'))

		# Setup code
		self.notebook['cells'].append(nbf.v4.new_code_cell('\n'.join(['import sys', 'import plotly', 'plotly.offline.init_notebook_mode()', 'sys.path.append("report_generator")', 'from data_scripts import *', 'from tool_scripts import *'])))

		# Fetch dataset
		self.notebook['cells'].append(nbf.v4.new_markdown_cell('## 2. Get Dataset'))
		self.notebook['cells'].append(nbf.v4.new_code_cell('\n'.join([
			'# Get data',
			'dataset = d2t.Dataset(dataset_id="{dataset_id}", dataset_source="{dataset_source}")'.format(**config_dict['dataset']),
			'dataset.data["rawcount_dataframe"].head()'
		])))
		self.notebook['cells'].append(nbf.v4.new_code_cell('dataset.data["sample_metadata_dataframe"].head()'))

		# # Add analyses
		# for tool in config_dict['tools']:
			
		# 	# Get parameter string
		# 	# tool['parameter_str'] = ', '.join(['='.join([key, '"'+value+'"']) for key, value in tool['params'].iteritems()])

		# 	# Add cell
		# 	self.notebook['cells'].append(nbf.v4.new_code_cell('\n'.join([
		# 		'# Run analysis\ndataset.analyze(tool_name="{tool_name}")'.format(**tool)
		# 	])))

		# 	# Add cell
		# 	self.notebook['cells'].append(nbf.v4.new_code_cell('\n'.join([
		# 		'# Display results\ndataset.display_results(tool_name="{tool_name}")'.format(**tool)
		# 	])))

	#######################################################
	########## 2. Export to HTML ##########################
	#######################################################

	def export_to_html(self):

		# Add preprocessor
		ep = ExecutePreprocessor(timeout=600)

		# Process
		ep.preprocess(self.notebook, {'metadata': {'path': '.'}})

		# create a configuration object that changes the preprocessors
		from traitlets.config import Config
		c = Config()
		c.HTMLExporter.preprocessors = ['nbconvert.preprocessors.ExtractOutputPreprocessor']

		# create the new exporter using the custom config
		html_exporter_with_figs = HTMLExporter(config=c)
		html_exporter_with_figs.preprocessors
		resources_with_fig = html_exporter_with_figs.from_notebook_node(self.notebook)[0]

		# Return
		return resources_with_fig

