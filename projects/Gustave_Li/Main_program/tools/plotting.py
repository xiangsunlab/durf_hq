from bokeh.plotting import figure, show
from bokeh.io import output_notebook

def dimreduct(Method, array):
    """
    Visualize the results from dimensionality reduction
    Only applicable for dimension reduced to 2D

    Parameters
    ----------
    Method : TYPE. String
        DESCRIPTION. Specify the algorithm for dimensionality reduction, used for the title of the plot
    array : TYPE. Numpy array, shape=(num of instances, 2)
        DESCRIPTION. The array generated by dimensionality reduction, set n_components=2

    Returns
    -------
    None. Prints the plot on the screen

    """
    # check for dimensionality
    if array.shape[-1]==2:        
        x = array[:, 0].reshape(len(array), )
        y = array[:, 1].reshape(len(array), )
        p = figure(title=Method, x_axis_label='dim1', y_axis_label='dim2')
        p.circle(x, y)
        output_notebook()
        show(p)
    else:
        print('Sorry, only dimension reduced to 2D accepted.')
