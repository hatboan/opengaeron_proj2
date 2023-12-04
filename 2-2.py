import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR


def sort_dataset(dataset_df):
    cur_sorted_df = dataset_df.sort_values(by='year')
    return cur_sorted_df


def split_dataset(dataset_df):
    dataset_df['salary'] *= 0.001
    x = dataset_df.drop(columns='salary',axis=1)
    y = dataset_df['salary']
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.1015,shuffle=False)
    return x_train, x_test, y_train, y_test


def extract_numerical_cols(dataset_df):
    chg_df=dataset_df[['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR','RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP',
                       'fly', 'war']]
    return chg_df


def train_predict_decision_tree(X_train, Y_train, X_test):
    dt_rg=DecisionTreeRegressor()
    dt_rg.fit(X_train,Y_train)
    return(dt_rg.predict(X_test))


def train_predict_random_forest(X_train, Y_train, X_test):
    rf_rg = RandomForestRegressor()
    rf_rg.fit(X_train,Y_train)
    return rf_rg.predict(X_test)


def train_predict_svm(X_train, Y_train, X_test):
    svm_rg=SVR()
    svm_rg.fit(X_train,Y_train)
    return(svm_rg.predict(X_test))


def calculate_RMSE(labels, predictions):
    return np.sqrt(np.mean((predictions-labels)**2))



if __name__ == '__main__':
    # DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
    data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

    sorted_df = sort_dataset(data_df)
    X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)

    X_train = extract_numerical_cols(X_train)
    X_test = extract_numerical_cols(X_test)

    dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
    rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
    svm_predictions = train_predict_svm(X_train, Y_train, X_test)

    print("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))
    print("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))
    print("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))