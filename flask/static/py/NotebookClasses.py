#################################################################
#################################################################
########## 1. Libraries #########################################
#################################################################
#################################################################
import sys
sys.path.append("static/py/data_scripts")
sys.path.append("static/py/tool_scripts")

#################################################################
#################################################################
########## 2. Data ##############################################
#################################################################
#################################################################

#######################################################
########## 1. Initialize ##############################
#######################################################

class AnalysisData:

	def __init__(self):

		# Initialize dictionary with stored data and signatures
		self.stored_datasets = {}
		self.signatures = {}
		self.analysis_results = []

#######################################################
########## 2. Fetch ###################################
#######################################################

	def fetch_dataset(self, dataset_accession, download_script, **kwargs):

		# Import script to download dataset
		dataset_downloader = __import__(download_script)

		# Add key
		if dataset_accession not in self.stored_datasets.keys():
			self.stored_datasets[dataset_accession] = {download_script: {}}

		# Get data
		self.stored_datasets[dataset_accession][download_script]['rawdata'] = dataset_downloader.fetch_dataset(dataset_accession, **kwargs)

		# Select it
		self.select_dataset(dataset_accession, download_script)

#######################################################
########## 3. Select Data #############################
#######################################################

	def select_dataset(self, dataset_accession, download_script, normalization_script='rawdata'):

		# Save arguments
		self.selected_data_info = locals()
		self.selected_data_info.pop('self')

		# Select dataset
		self.selected_data = self.stored_datasets[dataset_accession][download_script][normalization_script]

#######################################################
########## 4. Select Signature ########################
#######################################################

	def select_signature(self, signature_name=None):

		# Select signature
		self.selected_data = self.signatures[signature_name]

#######################################################
########## 4. Normalize ###############################
#######################################################

	def normalize_dataset(self, normalization_script, **kwargs):

		# Import normalization module
		dataset_normalizer = __import__(normalization_script)

		# Run
		self.stored_datasets[self.selected_data_info['dataset_accession']][self.selected_data_info['download_script']][normalization_script] = dataset_normalizer.analyze(self.selected_data, **kwargs)

		# Select dataset
		self.select_dataset(self.selected_data_info['dataset_accession'], self.selected_data_info['download_script'], normalization_script)

#######################################################
########## 5. Compute Signature #######################
#######################################################

	def compute_signature(self, signature_script, signature_name, **kwargs):

		# Import signature module
		signature_computer = __import__(signature_script)

		# Add signature
		self.signatures[signature_name] = signature_computer.analyze(self.selected_data, **kwargs)

#######################################################
########## 6. Analyze #################################
#######################################################

	def analyze_dataset(self, tool_name, **kwargs):

		# Import analysis module
		data_analyzer = __import__(tool_name)

		# Add analysis results
		self.analysis_results = data_analyzer.analyze(self.selected_data, **kwargs)

#################################################################
#################################################################
########## 2. Results ###########################################
#################################################################
#################################################################

