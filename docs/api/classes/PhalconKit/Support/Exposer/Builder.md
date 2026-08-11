
Mutable state container used by {@see Exposer} during exposure traversal.

This class is deliberately simple and strict. It enforces a **single invariant**
that the entire exposure system relies on:

**All keys are strings. The root path is represented by the empty string (`''`).**

`null` is never used to represent keys or paths once inside the Builder.

Responsibilities:
- Hold the current traversal state (value, parent, key, context).
- Hold global exposure configuration (columns, protected flag).
- Be reused across recursion to avoid object churn.

Non-responsibilities:
- No exposure logic.
- No rule resolution.
- No traversal decisions.

All business logic lives in

- **See:** \PhalconKit\Support\Exposer\Exposer.

***

* Full name: `\PhalconKit\Support\Exposer\Builder`
* This class implements:
  [`\PhalconKit\Support\Exposer\BuilderInterface`](./BuilderInterface.md)

## Properties

### value

Current value being evaluated.

```php
private mixed $value
```

***

### parent

Parent value in the traversal graph.

```php
private mixed $parent
```

***

### columns

Flattened column rules (dot-path => rule).

```php
private array<array-key,mixed>|null $columns
```

***

### field

Optional logical field name (legacy / informational).

```php
private ?string $field
```

Not used by the Exposer core logic.

***

### key

Current local key (single segment).

```php
private string $key
```

Normalized and guaranteed to be a string.
Root is represented as ''.

***

### contextKey

Current context key (dot-path prefix).

```php
private string $contextKey
```

Normalized and guaranteed to be a string.
Root context is represented as ''.

***

### expose

Whether the current node is exposed.

```php
private bool $expose
```

***

### protected

Whether underscore-prefixed keys are allowed.

```php
private bool $protected
```

***

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

### getKey

Return the current local key.

```php
public getKey(): string
```

Guaranteed to be a string.
Root is represented as ''.

***

### setKey

Set the current local key.

```php
public setKey(?string $key = null): void
```

Any input is normalized via

- **See:** \PhalconKit\Support\Exposer\processKey().

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$key`    | **?string** |             |

***

### getContextKey

Return the current context key (dot-path prefix).

```php
public getContextKey(): string
```

Guaranteed to be a string.
Root context is represented as ''.

***

### setContextKey

Set the current context key.

```php
public setContextKey(?string $contextKey = null): void
```

Any input is normalized via

- **See:** \PhalconKit\Support\Exposer\processKey().

**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$contextKey` | **?string** |             |

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

### getColumns

Return the flattened exposure rule map.

```php
public getColumns(): array<array-key,mixed>|null
```

***

### setColumns

Replace the flattened exposure rule map.

```php
public setColumns(array<array-key,mixed>|null $columns = null): void
```

**Parameters:**

| Parameter  | Type                             | Description |
|------------|----------------------------------|-------------|
| `$columns` | **array<array-key,mixed>\|null** |             |

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

Return the fully-qualified dot-path key for the current node.

```php
public getFullKey(): string
```

Invariants:
- Always returns a string.
- Root path is ''.

Semantics:
- key='' and context=''      → ''
- key='' and context!=''     → context
- key!='' and context=''     → key
- key!='' and context!=''    → context.key

***

### processKey

Normalize a key or context segment.

```php
public static processKey(string|null $key = null): string
```

Rules:
- null, empty string, or integer-like strings collapse to '' (root).
- Whitespace becomes dots.
- Multiple dots collapse into one.
- Lowercased and trimmed of leading/trailing dots.

This guarantees:
- Stable dot-path generation.
- No accidental numeric keys.
- A single, canonical representation for root.

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description               |
|-----------|------------------|---------------------------|
| `$key`    | **string\|null** | Local key or context key. |

**Return Value:**

Canonical dot-path segment, or empty string for root.

***
