# Gradient Boosting

Gradient Boosting (also called Gradient Boosting Machines or GMB/GBDT when using decision trees) is a powerful ensemble learning technique that builds a strong predictive model by combining many weak models—typically shallow decision trees—in a sequential, additive way.

The key idea behind gradient boosting is to build the model in a stage-wise fashion, where each new model is trained to correct the errors made by the previous models. This is done by fitting the new model to the negative gradient of the loss function with respect to the current model's predictions, hence the name "gradient boosting."

It is the foundation behind popular libraries like XGBoost, LightGBM, and CatBoost, which dominate tabular data tasks such as churn prediction.

## Core Intuition
Instead of training a bunch of independent models and averaging them (like in Random Forest), gradient boosting trains the next model specifically to correct the errors (residuals) of the previous ones.

In the standard and most popular form of gradient boosting—known as Gradient Boosted Decision Trees (GBDT)—each new model added to the ensemble is a decision tree. These trees are deliberately kept "weak" or simple:

- They are usually shallow (small max_depth, often 3–8).
- They have limited leaf nodes.
- They focus on fitting the residuals (errors) from the previous ensemble.

These shallow trees are connected sequentially, meaning each tree is built one after another in a specific order:

1. **First tree:** Trained on the original target values (or initial residuals).
2. **Second tree:** Trained to predict the errors (residuals) left by the first tree.
3. **Third tree:** Trained to predict the errors left by the combination of the first two trees.
4. **And so on...**

Each new tree receives a **learning rate** (shrinkage parameter, typically 0.01–0.3) that controls how much it contributes to the final prediction. This prevents any single tree from dominating and helps the model generalize better.

The final prediction is the **weighted sum** of all trees:

```
Final Prediction = Initial Prediction + (learning_rate × Tree₁) + (learning_rate × Tree₂) + ... + (learning_rate × Treeₙ)
```

This sequential, additive process is what makes gradient boosting so powerful—it systematically reduces prediction errors with each iteration, focusing computational effort where the model is weakest.

## Comparision with Random Forest

| Aspect | Gradient Boosting | Random Forest |
|---|---|---|
| Training | Sequential (each tree corrects the previous) | Parallel (independent trees) |
| Focus | Reduces bias by focusing on errors | Reduces variance through averaging |
| Speed | Slower to train (can't parallelize easily) | Faster to train |
| Accuracy | Often higher when tuned well | Very good, more stable on small data |
| Overfitting risk | Higher (needs regularization & early stopping) | Lower due to randomness |
| Best for | Maximum predictive power on tabular data | Quick, robust baseline |

