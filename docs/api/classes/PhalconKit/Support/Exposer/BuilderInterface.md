
Contract for the mutable state carrier used by the Exposer engine.

This interface deliberately encodes **strong invariants** required by the
exposure system. Implementations MUST respect them.

Core invariants:
- Keys and context keys are **always strings**.
- The root path is represented by the empty string (`''`).
- `null` is never used to represent a key or path once inside the Builder.

Rationale:
- Exposure rules are resolved via string-based dot-path matching.
- Parent traversal, child activation, and root deny rules depend on
  consistent string semantics.

***

* Full name: `\PhalconKit\Support\Exposer\BuilderInterface`

## Methods

### getValue

Get the current value being evaluated.

```php
public getValue(): mixed
```

***

### setValue

Set the current value being evaluated.

```php
public setValue(mixed $value = null): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***

### getParent

Get the parent value in the traversal graph.

```php
public getParent(): mixed
```

***

### setParent

Set the parent value in the traversal graph.

```php
public setParent(mixed $parent = null): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$parent` | **mixed** |             |

***

### getColumns

Get the flattened column rules map (dot-path => rule).

```php
public getColumns(): array<array-key,mixed>|null
```

***

### setColumns

Set the flattened column rules map.

```php
public setColumns(array<array-key,mixed>|null $columns = null): void
```

**Parameters:**

| Parameter  | Type                             | Description |
|------------|----------------------------------|-------------|
| `$columns` | **array<array-key,mixed>\|null** |             |

***

### getField

Get the logical field name (legacy / informational).

```php
public getField(): ?string
```

***

### setField

Set the logical field name.

```php
public setField(?string $field = null): void
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$field`  | **?string** |             |

***

### getKey

Get the current local key.

```php
public getKey(): string
```

MUST always return a string.
Root is represented as the empty string (`''`).

***

### setKey

Set the current local key.

```php
public setKey(?string $key = null): void
```

Implementations MUST normalize the key and collapse invalid values to `''`.

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$key`    | **?string** |             |

***

### getContextKey

Get the current context key (dot-path prefix).

```php
public getContextKey(): string
```

MUST always return a string.
Root context is represented as the empty string (`''`).

***

### setContextKey

Set the current context key.

```php
public setContextKey(?string $contextKey = null): void
```

Implementations MUST normalize the key and collapse invalid values to `''`.

**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$contextKey` | **?string** |             |

***

### getExpose

Whether the current node is exposed.

```php
public getExpose(): bool
```

***

### setExpose

Set whether the current node is exposed.

```php
public setExpose(bool $expose): void
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$expose` | **bool** |             |

***

### getProtected

Whether underscore-prefixed keys are allowed.

```php
public getProtected(): bool
```

***

### setProtected

Set whether underscore-prefixed keys are allowed.

```php
public setProtected(bool $protected): void
```

**Parameters:**

| Parameter    | Type     | Description |
|--------------|----------|-------------|
| `$protected` | **bool** |             |

***

### getFullKey

Get the fully-qualified dot-path key for the current node.

```php
public getFullKey(): string
```

MUST always return a string.
Root path is represented as the empty string (`''`).

***
