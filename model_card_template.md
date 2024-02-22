# Model Card


## Model Details
  - Developer: the model is developed/updated by Gagandeep/WGU
  - Model-data : the model is developed/updated on 02/21/2024
  - Model-type : RandomForestClassifier type of classifier is used
## Intended Use
  - Primary Intended Use: Model is being trained and tested only for Educational purposes

## Training Data
  - Data Source: Public Census Data is used

## Evaluation Data
  - Data Source : 25 percent of data is used for evaluating the model.

## Metrics
  - Metrics:
     - Precision: 0.73
     - Recall: 0.6288
     - F1 Score: 0.6789


## Ethical Considerations
  - Bias Evaluation: after performing the metrics on different data slices, the data bias does exist in categories like workclass, education and maritual status. Further investigation of data is required if the model need to be used for real-life applications.

## Caveats and Recommendations
 - The model is intended for educational purpose only
