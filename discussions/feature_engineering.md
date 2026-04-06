# Feature Engineering
## Steps

1. Domain understanding – Start with business or technical context (e.g., what does each sensor value really mean?).
2. Exploratory analysis – Use Pandas, NumPy, and visualizations to spot distributions, correlations, and anomalies.
3. Core techniques I apply:
   - Numerical features: Scaling/normalization, binning, log/power transforms, polynomial features, rolling statistics (mean, std, min/max over windows).
   - Categorical features: One-hot, target encoding, frequency encoding, embeddings.
   - Time-series / sequential data: Lag features, rolling windows, Fourier transforms, trend/seasonality decomposition.
4. Interactions: Cross-features (e.g., CPU × temperature), domain-specific ratios (e.g., battery drain rate). Correlation analysis and feature importance can help identify promising interactions. Covariance analysis can also help identify redundant features that can be removed or combined.
5. Dimensionality reduction: PCA, feature selection (mutual information, recursive elimination).
6. Handling missing data & outliers: Imputation strategies or specialized flags.

7. Use Feature Store (Vertex AI or SageMaker) so the exact same transformations are used for both training and real-time inference, preventing training-serving skew.


