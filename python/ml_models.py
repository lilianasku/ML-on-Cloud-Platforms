#python scripts for running machine-learning models
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

#running different scikit machine learning models
def run_ml_model(xtrain,ytrain,xtest,ytest, model):
    inst={ 'knn': KNeighborsClassifier(),
           'xgboost': XGBClassifier()} [value]
    ml=inst[model]
    ml.fit(X_train, y_train)
    y_pred = ml.predict(X_test)
    acc_xg= ml.score(X_test, y_test)
    print('\n')
    print('*'*10, model,  '*'*10)
    print('predicted target values:', y_pred)
    print('accuracy:', acc_xg)
    print('*'*10)
    return(y_pred, acc)


if __name__=="__main__":
      run_ml_model(xtrain,ytrain,xtest,ytest, 'knn')
