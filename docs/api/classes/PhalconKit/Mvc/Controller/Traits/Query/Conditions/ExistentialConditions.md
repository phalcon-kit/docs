
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Conditions\ExistentialConditions`

## Methods

### getExistentialBucketKey

Small immutable key describing an existential “universe” we can safely coalesce.

```php
protected getExistentialBucketKey(string $originalField, bool $negated, string $scope): string
```

We coalesce ONLY when:
 - Same group level
 - Same relationship path (same $originalField relationship chain)
 - Same polarity (EXISTS vs NOT EXISTS)
 - AND-connected siblings only

Explicitly NOT coalesced:
 - Across OR boundaries
 - Across nested groups

Psalm fixes applied:
 - preg_replace() may return null → guarded fallback
 - strrpos() may return false → guarded before substr()

**Parameters:**

| Parameter        | Type       | Description |
|------------------|------------|-------------|
| `$originalField` | **string** |             |
| `$negated`       | **bool**   |             |
| `$scope`         | **string** |             |

***
### pushExistentialCondition

Accumulate a single existential predicate for AND-coalescing.

```php
protected pushExistentialCondition(array& $pending, string $bucketKey, string $originalField, bool $negated, string $compiledConditionSql, array $bind, array $bindTypes): void
```

IMPORTANT INVARIANTS (guaranteed by caller):
 - This method is ONLY called for AND-connected siblings
 - OR / XOR predicates are emitted immediately elsewhere
 - All predicates in a bucket share:
     - the same relationship universe
     - the same polarity (EXISTS vs NOT EXISTS)

This method MUST:
 - only accumulate
 - never emit SQL
 - never merge binds globally

**Parameters:**

| Parameter               | Type       | Description                |
|-------------------------|------------|----------------------------|
| `$pending`              | **array**  |                            |
| `$bucketKey`            | **string** |                            |
| `$originalField`        | **string** |                            |
| `$negated`              | **bool**   |                            |
| `$compiledConditionSql` | **string** | SQL fragment inside EXISTS |
| `$bind`                 | **array**  |                            |
| `$bindTypes`            | **array**  |                            |

***
### flushExistentialBuckets

Flush all accumulated existential buckets into SQL fragments.

```php
protected flushExistentialBuckets(array& $pending, array& $fragments, array& $bind, array& $bindTypes): void
```

GUARANTEED PRECONDITIONS:
 - Each bucket represents exactly ONE existential universe
 - Buckets contain ONLY AND-connected predicates
 - OR / XOR predicates have already been emitted

Therefore:
 - Each bucket emits EXACTLY ONE EXISTS / NOT EXISTS
 - All bucket binds are merged exactly once

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$pending`   | **array** |             |
| `$fragments` | **array** |             |
| `$bind`      | **array** |             |
| `$bindTypes` | **array** |             |

***
