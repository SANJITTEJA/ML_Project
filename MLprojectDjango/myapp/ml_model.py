import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def get_column_names():
    return X_test.columns

def generate_recommendations(employee_data, top_features):
    recommendations = []
    for feature_name in top_features.index:

        feature_idx = X.columns.get_loc(feature_name)
        feature_value = employee_data[feature_idx]

        feature_mean = X_train[feature_name].mean()
        feature_std = X_train[feature_name].std()

        lower_threshold = feature_mean - feature_std
        upper_threshold = feature_mean + feature_std
        
        if feature_value < lower_threshold:
            recommendations.append(f"Consider improving {feature_name}, as it is significantly lower than the average.")
        elif feature_value > upper_threshold:
            recommendations.append(f"Consider maintaining or optimizing {feature_name}, as it is significantly higher than the average.")
        else:
            recommendations.append(f"Consider enhancing {feature_name} for better satisfaction and performance.")
    
    return recommendations

data = pd.read_csv('/Users/sanjitteja/Desktop/MLproject/myapp/WA_Fn-UseC_-HR-Employee-Attrition.csv.xls')
df = pd.DataFrame(data)
data_types = df.dtypes
categorical_columns = data_types[data_types == 'object'].index.tolist()

for column in categorical_columns:
    unique_values = df[column].unique()
    num_unique_values = len(unique_values)
    # print(f"{column} has {num_unique_values} unique values.")

LE = LabelEncoder()
for feature in categorical_columns:
    df[feature] = LE.fit_transform(df[feature])
df.drop('Over18', axis = 1, inplace = True)


X = df.drop('Attrition', axis = 1)
y = df['Attrition']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle = True, random_state = 60)


rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

feature_importance_rf = pd.Series(rf_model.feature_importances_, index=X.columns)
feature_importance_rf = feature_importance_rf.drop(['Age', 'EmployeeNumber'])
top_features = feature_importance_rf.nlargest(5)
# print("\nTop 5 Features Contributing to Attrition (based on Random Forest):")
# print(top_features)

# data = X_test.iloc[0]
# print(generate_recommendations(data, top_features))
# print(X_test.shape)
