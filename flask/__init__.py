# Modules
import json, sys
import pandas as pd
from flask import Flask, render_template, url_for, request
sys.path.append('static/py')
from AnalysisNotebook import generate_jupyter_notebook

# Configure
app = Flask(__name__)
entry_point = '/saturn'

@app.route(entry_point)
def index():

	dataset_dataframe = pd.read_table('static/datasets.txt')
	tool_dataframe = pd.read_table('static/tools.txt')
	return render_template('index.html', dataset_dataframe=dataset_dataframe, tool_dataframe=tool_dataframe)

@app.route(entry_point+'/analyze')
def analyze():
	return render_template('notebook.html')

@app.route(entry_point+'/api/analyze')
def analyze_api():
	# try:
	config = json.loads(request.args.get('config'))
	result = generate_jupyter_notebook(config)
	# except:
		# result = '<h1 style="text-align: center; margin-top: 100px;">Sorry, there has been an error.</h1>'
	return result

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')