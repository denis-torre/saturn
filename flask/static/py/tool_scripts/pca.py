# Performs PCA.
#######################################################
########## 1. Libraries ###############################
#######################################################
from sklearn.decomposition import PCA
import plotly.graph_objs as go
from plotly.offline import iplot
import numpy as np
import pandas as pd
from IPython.display import display, HTML

#######################################################
########## 2. Run #####################################
#######################################################

def analyze(dataset, n_components=3, title='PCA'):

    # Filter
    dataset['expression_dataframe'] = np.log10(dataset['expression_dataframe']+1)
    topGenes = dataset['expression_dataframe'].apply(np.var, 1).sort_values(ascending=False).index[:5000]
    dataset['expression_dataframe'] = dataset['expression_dataframe'].loc[topGenes]

    # Perform PCA
    pca = PCA(n_components=n_components)
    pca.fit(dataset['expression_dataframe'])

    # Get PC labels
    pc_labels = ['PC'+str(i+1)+' ({:0.2f}% var.)'.format(pca.explained_variance_ratio_[i]*100) for i in range(len(pca.components_))]

    # Get sample labels
    sample_labels = [dataset['sample_title_dict'][x] for x in dataset['expression_dataframe'].columns.tolist()]

    # Get PCA dataframe
    pca_dataframe = pd.DataFrame(pca.components_, index=pc_labels, columns=sample_labels).T

    # Plot it
    trace = go.Scatter3d(
        x=pca_dataframe.iloc[:,0],
        y=pca_dataframe.iloc[:,1],
        z=pca_dataframe.iloc[:,2],
        mode='markers',
        hoverinfo='text',
        text=pca_dataframe.index.tolist(),
        marker=dict(
            size=12,
            opacity=0.8
        )
    )

    data = [trace]
    go.layout = go.Layout(
        title=title,
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
        ),
        scene = dict(
            xaxis = dict(
                title = pca_dataframe.columns.tolist()[0]
            ),
            yaxis = dict(
                title = pca_dataframe.columns.tolist()[1]
            ),
            zaxis = dict(
                title = pca_dataframe.columns.tolist()[2]
            )
        )
    )
    fig = go.Figure(data=data, layout=go.layout)
    iplot(fig)
    display(HTML('<p><b>PCA Analysis.</b>  The figure displays the results of a Principal Components Analysis (PCA) of the dataset.</p>'))


