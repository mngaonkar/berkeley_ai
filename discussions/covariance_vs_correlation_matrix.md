# Covariance vs Correlation Matrix
## Covariance Matrix
The covariance matrix (often denoted as Σ) measures how two variables change together (linear relationship).
For a dataset with $  n  $ features, the covariance matrix is an $  n \times n  $ symmetric matrix where each element is:
$$\Sigma_{ij} = \text{Cov}(X_i, X_j) = \mathbb{E}\left[(X_i - \mu_i)(X_j - \mu_j)\right]$$

Positive value → variables move in the same direction
Negative value → variables move in opposite directions
Zero → no linear relationship

### Key characteristics:

- Scale-dependent (affected by the units and magnitude of the variables)
- Diagonal elements = variance of each feature
- Off-diagonal elements = covariance between pairs of features

## Correlation Matrix
The correlation matrix is the standardized version of the covariance matrix. It normalizes covariance by the standard deviations of the two variables:
$$\rho_{ij} = \frac{\text{Cov}(X_i, X_j)}{\sigma_i \cdot \sigma_j}$$

- Values are always between -1 and +1
- +1 → perfect positive linear relationship
- -1 → perfect negative linear relationship
- 0 → no linear relationship

### Key characteristics:

- Scale-invariant (unitless)
- Much easier to interpret and compare across features
- Diagonal elements are always 1

### Quick Comparison

| Aspect | Covariance Matrix | Correlation Matrix |
|--------|-------------------|-------------------|
| Scale | Scale-dependent | Scale-invariant |
| Range | $(-\infty, +\infty)$ | $[-1, +1]$ |
| Interpretation | Hard (depends on units) | Easy (strength & direction) |
| Use in ML | PCA, Mahalanobis distance | Feature correlation analysis |
| When features have different units/scales | Not ideal | Preferred |