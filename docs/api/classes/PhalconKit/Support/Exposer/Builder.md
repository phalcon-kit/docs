
***

* Full name: `\PhalconKit\Support\Exposer\Builder`
* This class implements:
  [`\PhalconKit\Support\Exposer\BuilderInterface`](./BuilderInterface.md)

## Properties

### value

```php
private mixed $value
```

***

### parent

```php
private mixed $parent
```

***

### columns

```php
private ?array $columns
```

***

### field

```php
private ?string $field
```

***

### key

```php
private ?string $key
```

***

### contextKey

```php
private ?string $contextKey
```

***

### expose

```php
private bool $expose
```

***

### protected

```php
private bool $protected
```

***

## Methods

### getValue

```php
public getValue(): mixed
```

***

### setValue

```php
public setValue(mixed $value = null): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***

### getParent

```php
public getParent(): mixed
```

***

### setParent

```php
public setParent(mixed $parent = null): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$parent` | **mixed** |             |

***

### getKey

```php
public getKey(): ?string
```

***

### setKey

```php
public setKey(?string $key = null): void
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$key`    | **?string** |             |

***

### getContextKey

```php
public getContextKey(): ?string
```

***

### setContextKey

```php
public setContextKey(?string $contextKey = null): void
```

**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$contextKey` | **?string** |             |

***

### getField

```php
public getField(): ?string
```

***

### setField

```php
public setField(?string $field = null): void
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$field`  | **?string** |             |

***

### getColumns

```php
public getColumns(): ?array
```

***

### setColumns

```php
public setColumns(?array $columns = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$columns` | **?array** |             |

***

### getExpose

```php
public getExpose(): bool
```

***

### setExpose

```php
public setExpose(bool $expose): void
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$expose` | **bool** |             |

***

### getProtected

```php
public getProtected(): bool
```

***

### setProtected

```php
public setProtected(bool $protected): void
```

**Parameters:**

| Parameter    | Type     | Description |
|--------------|----------|-------------|
| `$protected` | **bool** |             |

***

### getFullKey

Retrieves the full key constructed from the context and the key.

```php
public getFullKey(): string|null
```

The full key is determined based on the following conditions:
- If the key is empty, the context is returned.
- If the context is empty, the key is returned.
- If both are present, the result is a concatenation of context and key separated by a dot.

**Return Value:**

The constructed full key or null if both key and context are null.

***

### processKey

Processes the given key by normalizing its format.

```php
public static processKey(string|null $key = null): string|null
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                                  |
|-----------|------------------|------------------------------------------------------------------------------|
| `$key`    | **string\|null** | The input key to be processed. It can be null, an empty string, or a string. |

**Return Value:**

Returns the processed key in a normalized format or an empty string if the input is null, empty, or a valid integer string.

***
