
Find-definition compiler.

Purpose
- Accepts heterogeneous "find" inputs (Phalcon-style arrays + custom/nested condition blocks).
- Normalizes them into a single, merge-safe structure.
- Preserves existing behaviors:
  - Supports numeric Phalcon signature: [0 => '...', 1 => bind[], 2 => bindTypes[]]
  - Supports 'conditions' as string or list (merged as list, stringified later)
  - Supports nested condition blocks under 'conditions' (recursive compilation)
  - Enforces bind/bindTypes collision rules (only identical collisions are allowed)
  - Rejects merging unknown keys when they collide (explicit failure, not silent override)
  - Final stringification of group/order/distinct lists to CSV strings

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Compiler`

## Methods

### prepareCollectionToCompile

Convert a Collection into a recursively compiled array suitable for find compilation.

```php
public prepareCollectionToCompile(\Phalcon\Support\Collection $collection, int $level = 0): array<array-key,mixed>
```

Behavior:
- Recursively converts nested Collections to arrays.
- Drops null values (but keeps false/0/"").
- Preserves keys so named bind maps and field maps keep their semantic meaning.

**Parameters:**

| Parameter     | Type                            | Description |
|---------------|---------------------------------|-------------|
| `$collection` | **\Phalcon\Support\Collection** |             |
| `$level`      | **int**                         |             |

***
### compileFinds

Compile and merge multiple find definitions.

```php
public compileFinds(array<array-key,mixed> $finds): array<array-key,mixed>
```

**Parameters:**

| Parameter | Type                       | Description |
|-----------|----------------------------|-------------|
| `$finds`  | **array<array-key,mixed>** |             |

***
### mergeCompiledFind

Merge multiple *already compiled* find definitions.

```php
public mergeCompiledFind(array<array-key,mixed> $compiledFinds): array<array-key,mixed>
```

Merge rules (explicit and strict):
- Scalar keys that must match if provided by multiple inputs: limit, offset, column
- conditions: list-merge (stringification happens in afterMergeCompileFind)
- joins: list-merge
- columns/distinct/group/order/models: list-merge (later stringified by implodeUniqueToString)
- bind/bindTypes: collision allowed only when values are identical
- boolean flags: true wins
- other keys: disallow collisions (fail fast)

**Parameters:**

| Parameter        | Type                       | Description |
|------------------|----------------------------|-------------|
| `$compiledFinds` | **array<array-key,mixed>** |             |

***
### afterMergeCompileFind

Post-merge normalization hook.

```php
public afterMergeCompileFind(array<array-key,mixed>& $merged): void
```

Responsibilities:
- Convert merged conditions list into a single AND-string (preserves the previous "stringify after merge" behavior)
- Disallow integer-like keys in merged output (guards against accidental list merges at root)
- Convert group/order/distinct arrays into CSV strings (unique values only)

**Parameters:**

| Parameter | Type                       | Description |
|-----------|----------------------------|-------------|
| `$merged` | **array<array-key,mixed>** |             |

***
### compileFind

Compile a single find definition into a normalized/merge-ready structure.

```php
public compileFind(array<array-key,mixed> $find): array<array-key,mixed>
```

**Parameters:**

| Parameter | Type                       | Description |
|-----------|----------------------------|-------------|
| `$find`   | **array<array-key,mixed>** |             |

***
### beforeCompileFind

Hook: called before the find is compiled (in-place normalization).

```php
public beforeCompileFind(array<array-key,mixed>& $find): void
```

Current behavior (preserved):
- Promote group/order/columns string into a single-item list (non-empty only).

**Parameters:**

| Parameter | Type                       | Description |
|-----------|----------------------------|-------------|
| `$find`   | **array<array-key,mixed>** |             |

***
### afterCompileFind

Hook: called after the find is compiled (in-place cleanup and coercions).

```php
public afterCompileFind(array<array-key,mixed>& $find): void
```

Current behavior (preserved):
- Remove null values, empty arrays, and empty strings
- Enforce integer coercion for limit/offset when present
- Stringify group/order/distinct arrays into unique CSV strings (via implodeUniqueToString)

**Parameters:**

| Parameter | Type                       | Description |
|-----------|----------------------------|-------------|
| `$find`   | **array<array-key,mixed>** |             |

***
### implodeUniqueToString

Convert a list-like key into a string (unique CSV), in-place.

```php
private implodeUniqueToString(array<array-key,mixed>& $array, list<string> $keys = ['group', 'order', 'distinct']): void
```

Keys are expected to be:
- unset OR scalar string OR list of scalar strings

**Parameters:**

| Parameter | Type                       | Description |
|-----------|----------------------------|-------------|
| `$array`  | **array<array-key,mixed>** |             |
| `$keys`   | **list<string>**           |             |

***
### normalizeListValue

Normalize a value that is allowed to be either:
- string (treated as single-item list)
- array  (treated as list as-is)
- null   (treated as empty list)

```php
private normalizeListValue(mixed $value, string $keyName): list
```

Anything else is a hard error because merge semantics depend on predictable list types.

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$value`   | **mixed**  |             |
| `$keyName` | **string** |             |

***
