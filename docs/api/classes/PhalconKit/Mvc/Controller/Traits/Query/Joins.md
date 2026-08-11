
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Joins`

## Properties

### joins

```php
protected ?\Phalcon\Support\Collection $joins
```

***

## Methods

### initializeJoins

Initializes the joins.

```php
public initializeJoins(): void
```

This method is responsible for initializing the joins.

***
### setJoins

Sets the joins for the find criteria.

```php
public setJoins(array|\Phalcon\Support\Collection|null $joins): void
```

**Parameters:**

| Parameter | Type                                         | Description                                          |
|-----------|----------------------------------------------|------------------------------------------------------|
| `$joins`  | **array\|\Phalcon\Support\Collection\|null** | The collection of joins.
Pass null to disable joins. |

***
### getJoins

Returns the joins collection.

```php
public getJoins(): \Phalcon\Support\Collection|null
```

This method retrieves the joins for the find criteria.
If joins fields have been set, it returns the collection of joins.
If no joins have been set, it returns null.

Note: The joins are used to add conditions during the find query and are not added to the result.

**Return Value:**

The collection of joins or null everything is allowed.

***
### mergeJoins

Merges the provided joins with the existing joins in the find criteria.

```php
public mergeJoins(array|\Phalcon\Support\Collection $joins): void
```

**Parameters:**

| Parameter | Type                                   | Description                           |
|-----------|----------------------------------------|---------------------------------------|
| `$joins`  | **array\|\Phalcon\Support\Collection** | The collection of joins to be merged. |

***
### normalizeJoins

Normalize join definitions into pure Phalcon joins and extract join-scoped bind data.

```php
protected normalizeJoins(array $joins): array{joins: array<int,array>, bind: array, bindTypes: array}
```

Supported join shapes (new format only):

 - [class, on, alias]
 - [class, on, alias, type]
 - [class, on, alias, payload]                      // type omitted
 - [class, on, alias, type, payload]

Where payload is either a single block:
 - ['conditions' => 'x = :x:', 'bind' => [...], 'bindTypes' => [...]]

Or a list of blocks:
 - [
     ['conditions' => 'a = :a:', 'bind' => [...], 'bindTypes' => [...]],
     ['conditions' => 'b = :b:', 'bind' => [...], 'bindTypes' => [...]],
   ]

Return:
 - joins:     list of Phalcon joins [class, onSql, alias, type?] (payload removed, ON merged)
 - bind:      merged bind map from payload blocks
 - bindTypes: merged bindTypes map from payload blocks

No mutation. No references.

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$joins`  | **array** |             |

***
### normalizeJoinPayload

Normalize a join payload into:
 - merged SQL condition (AND-combined, parenthesized)
 - merged bind
 - merged bindTypes

```php
protected normalizeJoinPayload(array $payload, int|string $joinIndex): array
```

Supported block variants (all equivalent):

 [
   'conditions' => 'a = :a:',
   'bind' => [...],
   'bindTypes' => [...],
 ]

 [
   0 => 'a = :a:',
   1 => [...],
   2 => [...],
 ]

 [
   0 => 'a = :a:',
   'bind' => [...],
   'bindTypes' => [...],
 ]

Multiple blocks:
 [
   [...],
   [...],
 ]

Rule:
 - Payload is a LIST OF BLOCKS iff payload[0] is an array.
 - Otherwise payload is a SINGLE BLOCK.

**Parameters:**

| Parameter    | Type            | Description |
|--------------|-----------------|-------------|
| `$payload`   | **array**       |             |
| `$joinIndex` | **int\|string** |             |

***
### mergeSqlConditions

Merge two SQL condition fragments using AND with safe parentheses.

```php
protected mergeSqlConditions(string $a, string $b): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$a`      | **string** |             |
| `$b`      | **string** |             |

***
