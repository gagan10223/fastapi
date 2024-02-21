import ml.model as tm
import pytest
import pandas as pd
import os
import pickle
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
file_name = os.path.join(os.path.dirname(__file__),'model','model.pkl')
def test_if_model_exist():
    """
    checking if our model exists
    """
    assert os.path.exists(file_name), 'model does not exist'


# TODO: implement the second test. Change the function name and input as needed
def test_metrics():
    y_true = [1,0,1]
    y_actual = [1,0,0]

    pre,rec,f1= tm.compute_model_metrics(y_true,y_actual)
    assert pre is not None, 'metrics function failed'
    """
    making sure precision is returned
    """
    # Your code here



# TODO: implement the third test. Change the function name and input as needed
def test_data():
    file = os.path.join(os.path.dirname(__file__),'data','census.csv') 
    df = pd.read_csv(file)
    assert df.shape[1] == 15, 'data specifications failed'
    # testing the number of features
    