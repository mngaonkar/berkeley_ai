from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
import numpy as np
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

X, y = make_classification(n_samples=1000, 
                           n_features=50, 
                           n_informative=15, 
                           n_redundant=5, 
                           random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

logger.info("Training Logistic Regression model with L1 regularization...")
model = LogisticRegression(penalty='l1', 
                           C=0.1, # Regularization strength (smaller C = stronger regularization)
                           solver='liblinear', 
                           max_iter=1000, 
                           random_state=42)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
logger.info(f'Accuracy: {accuracy:.4f}')

logger.info("Evaluating model performance with grid search for hyperparameter tuning...")
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'penalty': ['l1']
}
grid_search = GridSearchCV(LogisticRegression(solver='liblinear', max_iter=1000, random_state=42), 
                           param_grid, 
                           cv=5, # 5-fold cross-validation
                           scoring='accuracy')

grid_search.fit(X_train, y_train)
logger.info(f"Best parameters: {grid_search.best_params_}")
logger.info(f"Best cross-validation accuracy: {grid_search.best_score_:.4f}")




