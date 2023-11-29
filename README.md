# Water Potability Classification Project 💧

[Webapps Deployment](https://huggingface.co/spaces/achmaddhani/water_potability)

## Objective 🎯
Water is essential for life, yet its quality varies greatly. This project aims to distinguish between potable and non-potable water using a classification model. Focusing on the Recall metric, aiming to ensure the safety and potability of water for consumption.

## Project Overview 📖
This project leverages machine learning to predict water potability. We use various classification models to analyze water quality based on chemical composition, aiming to safeguard public health by identifying safe drinking water.

## Dataset and Exploratory Data Analysis (EDA) 🔍
- The dataset contains essential chemical properties of water samples, with some missing values.
- EDA reveals a pH range of 5-9 and a high presence of chemicals like sulfate and chloramines.
- No significant difference in chemical composition between potable and non-potable samples suggests challenging water conditions.

## Model and Performance 💻
- Best performing model: RandomForest Classifier with a Recall of 65%.
- Models tested include RandomForest, AdaBoost, SVC, KNeighborsClassifier, and DecisionTreeClassifier.

## Libraries and Tools Used 🛠️

```python
# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
# libraries for preprocessing
from sklearn.impute import KNNImputer
from feature_engine.outliers import Winsorizer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
# pipeline
from imblearn.pipeline import make_pipeline as make_pipeline_imb
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
#models
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# evaluation
from sklearn.metrics import classification_report, ConfusionMatrixDisplay, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
# others
import time
from joblib import dump
```

## Suggestions for Future Work 🚀
- Gather more data to balance the dataset
- Future work includes improving the SVC model and acquiring more balanced datasets.
- Verification of dataset criteria and further exploration of chemical relationships.

## Conclusion 📌
This project underscores the critical need for accurate water quality assessment. The promising results pave the way for more comprehensive models and datasets to ensure safe drinking water.

## Dataset
[Water Quality Dataset](https://www.kaggle.com/link-to-your-dataset)