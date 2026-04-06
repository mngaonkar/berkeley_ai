# Feature Store
A Feature Store is a centralized, versioned repository for storing, managing, and serving ML features in production environments. It solves one of the biggest pain points in scaling ML systems: inconsistent, duplicated, and hard-to-serve feature engineering across training and inference.

## Characteristics of a Feature Store
1. Offline Store (e.g., BigQuery, S3 + Parquet, Snowflake)
- Used for training and batch inference. Stores historical feature values with point-in-time correct joins to avoid data leakage.

2. Online Store (e.g., Redis, DynamoDB, Cassandra)
- Serves low-latency features for real-time inference (sub-millisecond).

3. Feature Registry
- Metadata catalog that tracks feature definitions, versions, owners, schemas, and lineage.

4. Ingestion & Transformation Pipelines
- Automated pipelines (Spark, Dataflow, SageMaker Processing, etc.) that compute and push features to both offline and online stores.

5. Feature Serving API
- Unified interface to fetch features for training (batch) or inference (real-time).

## Key Benefits

- Consistency — Same feature code for training and serving.
- Reusability — Teams can discover and reuse features across projects.
- Low-latency serving — Critical for real-time applications.
- Governance & Lineage — Built-in tracking for compliance and debugging.
- Scalability — Handles both batch and streaming feature computation.

