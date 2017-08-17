# Performs PCA.
#######################################################
########## 1. Libraries ###############################
#######################################################
from sklearn.decomposition import PCA
import plotly.graph_objs as go
from plotly.offline import iplot
import numpy as np
import pandas as pd
from IPython.display import display

#######################################################
########## 2. Run #####################################
#######################################################

def analyze(dataset, n_components=3):

    # Perform PCA
    pca = PCA(n_components=n_components)
    pca.fit(np.log10(dataset['rawcount_dataframe']+1))

    # Get PC labels
    pc_labels = ['PC1 ({:0.2f}% var.)'.format(pca.explained_variance_ratio_[i]*100) for i in range(len(pca.components_))]

    # Get sample labels
    sample_labels = [dataset['sample_title_dict'][x] for x in dataset['rawcount_dataframe'].columns.tolist()]

    # Get PCA dataframe
    pca_dataframe = pd.DataFrame(pca.components_, index=pc_labels, columns=sample_labels).T

    # Print
    print 'Successfully ran PCA.'

    # Return result
    return pca_dataframe

#######################################################
########## 2. Display Results #########################
#######################################################

def display_results(pca_dataframe, title='PCA'):

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
    return iplot(fig)


