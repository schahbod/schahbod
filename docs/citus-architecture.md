# Citus Architecture Diagram

Use this in your Citus repository README.

```mermaid
flowchart TD
  S[Superset] --> C[Citus Coordinator]
  C --> W1[Worker 1]
  C --> W2[Worker 2]
```

Alternative ASCII version:

```text
                 +--------------+
                 |   Superset   |
                 +------+-------+
                        |
                 +------+-------+
                 |   Citus      |
                 | Coordinator  |
                 +------+-------+
                    +---+---+
                    |       |
                    v       v
                Worker 1  Worker 2
```
