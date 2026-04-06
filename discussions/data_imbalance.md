# Data Imbalance
When handling class imbalance, oversampling the minority class is one of my primary strategies. 

## Random Oversampling
Randomly duplicate samples from the minority class until the desired balance ratio is reached. Extremely simple and fast; no assumptions about data distribution. However, it can lead to overfitting since it duplicates existing samples without adding new information.

## SMOTE (Synthetic Minority Over-sampling Technique)
For each minority sample $x_i$, find its $k$ nearest neighbors (usually $k=5$). Then generate a synthetic sample on the line segment between $x_i$ and a randomly chosen neighbor:
$$x_{\text{new}} = x_i + \lambda \cdot (x_{nn} - x_i), \quad \lambda \sim U(0,1)$$

Creates realistic synthetic points; widely used and effective in low-to-medium dimensions. Doesn’t work well with high-dimensional data or time-series (ignores temporal order); can generate noisy samples.

## Generative AI-based Oversampling
Use GANs, VAEs, diffusion models, or even LLMs to generate entirely new synthetic minority samples that follow the true data distribution.

## Time-Series Specific Oversampling
SMOTE applied only along the time axis while preserving sequence order. 
