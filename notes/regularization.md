# Regularization

Regularization is a penalty added to the model's loss function that discourages the model from becoming too complex. In machine learning, a model with very large weights is often a model that is "trying too hard." It is memorizing every tiny jitter, outlier, and bit of noise in your training data rather than finding the broad, underlying pattern. Regularization helps to prevent overfitting by adding a penalty for larger weights, which encourages the model to find simpler patterns in the data.

```
Total loss = Original loss + Regularization penalty
```

| Type | Also Called | What it Penalizes | Common Use Cases | Effect |
|------|-------------|-------------------|------------------|--------|
| L1 Regularization | Lasso | Sum of absolute values of weights | Feature selection | Can make some weights exactly zero |
| L2 Regularization | Ridge | Sum of squares of weights | Most common, stable | Shrinks weights but rarely makes them zero |
| Elastic Net | - | Combination of L1 + L2 | When you have many correlated features | Good balance |
| Dropout | - | Randomly drops neurons during training | Deep Neural Networks | Prevents co-adaptation of neurons |
| Early Stopping | - | Stops training when validation loss rises | All neural networks | Simple and effective |
| Weight Decay | L2 in neural nets | Same as L2 regularization | Neural Networks | Very common |
| Batch Normalization | - | Stabilizes training | Deep Learning | Indirect regularization |

