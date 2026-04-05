# Collaborative Filtering
Collaborative Filtering is one of the most popular and widely used techniques in Recommendation Systems.

## Types of Collaborative Filtering
### User-Based Collaborative Filtering

This method recommends items to a user based on the preferences of similar users. It identifies users who have similar tastes and recommends items that those similar users have liked.
Simple and intuitive, but can suffer from scalability issues as the number of users grows.

### Item-Based Collaborative Filtering
This method recommends items to a user based on the similarity between items. It identifies items that are similar to the ones the user has liked and recommends those similar items.
More scalable than user-based filtering, especially when the number of items is smaller than the number of users.

## How Collaborative Filtering Works
1. Build User-Item Interaction Matrix: Create a matrix where rows represent users, columns represent items, and values represent interactions (e.g., ratings, clicks).
2. Calculate Similarity: Compute similarity between users (for user-based) or items (for item-based) using metrics like cosine similarity, Pearson correlation, or Jaccard similarity.
3. Generate Recommendations: For user-based, recommend items liked by similar users. For item-based, recommend items similar to those the user has interacted with.

- Similar users: Compare rows (normalized dot product (cosine similarity) of row vectors)
- Similar items: Compare columns (normalized dot product (cosine similarity) of column vectors)

## Issues with Collaborative Filtering
1. Cold Start Problem: New users or items with no interactions cannot be recommended effectively.
2. Sparsity: User-item interaction matrices are often sparse, making it difficult to find similar users or items.
3. Scalability: As the number of users and items grows, the computational cost of finding similar users or items increases significantly.
4. Popularity Bias: Collaborative filtering may favor popular items, leading to less diverse recommendations and reinforcing existing trends.

## How Collaborative Filtering is improved

| Technique | Purpose |
|-----------|---------|
| Matrix Factorization (SVD, NMF) | Reduces sparsity by learning latent factors |
| Neural Collaborative Filtering (NCF) | Uses deep learning for non-linear patterns |
| Hybrid Approaches | Combines collaborative + content-based filtering |
| Session-based / Sequential | Uses recent user behavior instead of long history |


## Comparison with Content-Based Filtering
| Aspect | Collaborative Filtering | Content-Based Filtering |
|--------|-----------------------|------------------------|
| Basis for Recommendations | User-item interactions | Item features |
| Strengths | Can capture complex user preferences and item relationships | Can recommend new items based on features |
| Weaknesses | Cold start problem, sparsity, scalability issues | Limited to recommending items similar to those already interacted with |
| Use Cases | E-commerce, streaming services, social media | News recommendation, personalized content delivery |

## Matrix Factorization
This method decomposes the user-item interaction matrix into lower-dimensional matrices representing latent factors for users and items. It captures complex relationships between users and items, allowing for more accurate recommendations.

Matrix Factorization solves sparsity issue by breaking down this large sparse matrix into two much smaller matrices:
$$R \approx P \times Q^T$$
Where:

$R$ = Original User-Item Rating Matrix (very large & sparse) \
$P$ = User Latent Factor Matrix (Users × K) \
$Q$ = Item Latent Factor Matrix (Items × K) \
$K$ = Number of latent factors (usually 20 to 100) — a small number

## Training Matrix Factorization
The goal is to find matrices $P$ and $Q$ such that when multiplied, they closely approximate the known ratings in $R$. This is typically done by minimizing the following loss function:
$$\text{Loss} = \sum_{(u,i) \in K} (r_{ui} - p_u^T q_i)^2 + \lambda (||p_u||^2 + ||q_i||^2)$$
Where:
- $r_{ui}$ = Actual rating given by user $u$ to item $i$
- $p_u$ = Latent factor vector for user $u$
- $q_i$ = Latent factor vector for item $i$
- $\lambda$ = Regularization parameter to prevent overfitting

## Neural Collaborative Filtering (NCF)
NCF uses deep learning to model complex, non-linear interactions between users and items. It typically consists of embedding layers for users and items, followed by multiple hidden layers that capture the interactions between these embeddings. NCF can capture more complex patterns than traditional matrix factorization, making it suitable for large and complex datasets. However, it requires more computational resources and careful tuning to avoid overfitting.

[NCF code](../code/l1_regularization.py)