
Minimal mutable key/value option manager contract.

This interface is useful when consumers need a small runtime options store
without exposing the full `OptionsInterface` lifecycle. Values are keyed by
strings and may be any PHP value.

***

* Full name: `\PhalconKit\Support\Options\ManagerInterface`

## Methods

### get

Return an option value or the provided default when it is not set.

```php
public get(string $key, mixed $default = null): mixed
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$key`     | **string** |             |
| `$default` | **mixed**  |             |

***

### set

Store or replace an option value.

```php
public set(string $key, mixed $value = null): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |
| `$value`  | **mixed**  |             |

***

### remove

Remove one option value when it exists.

```php
public remove(string $key): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |

***

### reset

Restore the manager to its constructor/default option set.

```php
public reset(): void
```

***

### clear

Remove all current option values.

```php
public clear(): void
```

***
