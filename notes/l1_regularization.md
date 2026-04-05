# L1 (Lasso) Regularization
L1 Regularization adds a penalty to the loss function proportional to the sum of the absolute values of the model's weights (coefficients).

$\text{Total Loss} = \text{Original Loss} + \lambda \sum_{i=1}^{n} |w_i|$

Where:

$\lambda$  (lambda) = regularization strength (how harsh the penalty is) \
$|w_i|$  = absolute value of each weight

In scikit-learn, when you use L1 regularization (penalty='l1'), the solver is the optimization algorithm that solves the underlying mathematical problem.

| Model | Supported Solvers for penalty='l1' | Recommended Solver | Notes |
|-------|-------------------------------------|-------------------|-------|
| LogisticRegression | liblinear, saga | liblinear (small-medium data)<br>saga (large data) | liblinear is fastest for L1 |
| LinearSVC | liblinear | liblinear | Only liblinear supports L1 |
| SGDClassifier | saga | saga | Supports L1 via penalty='l1' |

## Detailed Explanation of Main Solvers

### solver='liblinear' (Most Common for L1)
- Best for small to medium datasets.
- Very fast and stable when using L1 regularization.
- Uses a coordinate descent algorithm.
- Limitation: Does not support multinomial (multi-class) with L1 very well.

### solver='saga'
- Best for large datasets (thousands of samples or features).
- Supports both L1 and L2 regularization.
- Uses Stochastic Average Gradient (SAGA) algorithm.
- Can handle multi-class problems better than liblinear.

### Why L1 Regularization Can Set Weights to Zero
L1 regularization can shrink some weights to exactly zero, effectively performing feature selection. This happens because the penalty is based on the absolute value of the weights, which creates a "sparse" solution. In contrast, L2 regularization (Ridge) shrinks weights but rarely makes them exactly zero, as it penalizes the square of the weights. This is why L1 is often preferred when you want to identify important features in your dataset.

## Practical recommendations

| Your Dataset Size | Recommended Solver for L1 |
|-------------------|---------------------------|
| Small / Medium (< 10k samples) | liblinear |
| Large dataset (> 10k–100k) | saga |
| Very large / sparse data | saga |