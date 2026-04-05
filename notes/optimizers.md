# Optimizers

Optimizers are algorithms or methods used to adjust the weights and biases of a machine learning model to minimize the loss function. Its job is to decide how much and in which direction to update the model’s parameters after each forward and backward pass during training. The choice of optimizer can significantly affect the speed of convergence and the final performance of the model.

### Common Optimizers

1. **Stochastic Gradient Descent (SGD)**
- Basic optimizer.
- Updates weights using gradient of one mini-batch at a time.
- Formula: w = w - lr * gradient
- Still used when you want strong generalization.

2. **RMSProp**
   - Adapts the learning rate for each parameter individually.
   - Helps in dealing with non-stationary objectives.

3. **AdaGrad**
   - Adapts the learning rate based on the historical gradients.
   - Performs well for sparse data.
   - 
4. **Adam (Adaptive Moment Estimation)**
   - Combines the benefits of AdaGrad and RMSProp.
   - Most widely used optimizer.
   - Combines Momentum (helps accelerate in relevant direction) and RMSprop (adaptive learning rates).

5. **AdamW**
   - A variant of Adam that decouples weight decay from the gradient update.
   - Often leads to better generalization.
   - Recommended for training large language models and transformers.

### Choosing an Optimizer

- **SGD**: Simple and effective for many problems, especially with large datasets.
- **Adam**: Often preferred for deep learning due to faster convergence.
- **RMSProp**: Useful for recurrent neural networks.
- **AdaGrad**: Good for sparse data scenarios.

### Best Practice
Optimizers are algorithms that update the weights of a neural network to minimize the loss function. The most commonly used ones are SGD, Adam, and AdamW.SGD is simple but slow. Adam combines momentum and adaptive learning rates, making it fast and robust. AdamW improves upon Adam by decoupling weight decay, which leads to better generalization, especially when training large models and transformers.In practice, for most modern deep learning tasks, AdamW with a proper learning rate and weight decay is the go-to optimizer.

| Optimizer | Year | Key Idea | Advantages | Disadvantages | Best For |
|-----------|------|----------|------------|---------------|----------|
| SGD | - | Stochastic Gradient Descent | Simple, stable, good generalization | Slow convergence, sensitive to learning rate | Basic models |
| Momentum | - | Adds momentum to SGD | Faster convergence, reduces oscillations | Still needs careful tuning | - |
| RMSprop | 2012 | Adaptive learning rate per parameter | Good for non-stationary problems | Can sometimes overshoot | RNNs |
| Adagrad | 2011 | Adaptive learning rate (per parameter) | Good for sparse data | Learning rate decays too aggressively | Sparse features |
| Adam | 2014 | Momentum + RMSprop combined | Very popular, fast, robust | Can sometimes generalize poorly | Most deep learning tasks |
| AdamW | 2017 | Adam + decoupled weight decay | Best overall for modern training | Slightly more memory | LLMs, Transformers |
| Lion | 2023 | Newer optimizer | Faster and more memory efficient | Less tested | Large models |
| Sophia | 2023 | Second-order inspired | Very fast convergence | Still emerging | Cutting-edge |
