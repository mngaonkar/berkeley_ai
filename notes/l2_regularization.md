# L2 (Ridge) Regularization
L2 Regularization adds a penalty to the loss function proportional to the sum of the squares of the model's weights (coefficients).

$\text{Total Loss} = \text{Original Loss} + \lambda \sum_{i=1}^{n} w_i^2$

Where: \
$\lambda$  (lambda) = regularization strength (how harsh the penalty is) \
$w_i^2$  = square of each weight

Note:
$\text{C} = 1/\lambda$ in scikit-learn, so a smaller C means stronger regularization.
​

In scikit-learn, when you use L2 regularization (penalty='l2'), a solver is the optimization algorithm that minimizes the loss function during model training.

| Model | Supported Solvers for penalty='l2' | Recommended Solver | Notes |
|-------|-------------------------------------|-------------------|-------|
| LogisticRegression | liblinear, lbfgs, newton-cg, sag, saga | lbfgs (small-medium data)<br>saga (large data) | lbfgs is fast and stable for L2 |
| LinearSVC | liblinear | liblinear | Only liblinear supports L2 |
| SGDClassifier | sag, saga | sag (small-medium data)<br>saga (large data) | Supports L2 via penalty='l2' |

## Detailed Explanation of Main Solvers

### solver='liblinear' (Most Common for L2)
- Best for small to medium datasets.
- Very fast and stable when using L2 regularization.
- Uses a coordinate descent algorithm.
- Limitation: Does not support multinomial (multi-class) with L2 very well.

### solver='lbfgs'
- Best for small to medium datasets.
- Uses a quasi-Newton method.
- Very fast and stable for L2 regularization.
- Can handle multinomial (multi-class) problems.

### solver='sag' and solver='saga'
- Best for large datasets (thousands of samples or features).
- Uses Stochastic Average Gradient (SAG) or Stochastic Average Gradient with Adaptive learning rate (SAGA) algorithm.
- Can handle multi-class problems better than liblinear.
- Supports both L1 and L2 regularization (saga supports both, sag only supports L2).

### solver='newton-cg'
- Uses Newton’s method with conjugate gradient.
- More accurate but slower than lbfgs.
- Good when lbfgs fails to converge.

## Practical recommendations

| Situation | Recommended Solver |
|-----------|-------------------|
| General use / Default | lbfgs |
| Large dataset (> 50k samples) | saga |
| Very sparse data | saga |
| Small dataset + Binary classification | liblinear |
| Need highest accuracy (slow OK) | newton-cg |