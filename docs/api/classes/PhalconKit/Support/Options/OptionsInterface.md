
Contract for objects that expose mutable runtime options.

Implementations distinguish between default options captured at
initialization time and the current mutable option set. This lets services
temporarily override options and later reset them without reconstructing the
object.

***

* Full name: `\PhalconKit\Support\Options\OptionsInterface`

## Methods

### __construct

Initialize the object with an optional default option set.

```php
public __construct(array<string,mixed>|null $options = null): mixed
```

**Parameters:**

| Parameter  | Type                          | Description                    |
|------------|-------------------------------|--------------------------------|
| `$options` | **array<string,mixed>\|null** | Defaults to capture and apply. |

***

### initializeOptions

Capture defaults, apply current options, and run object initialization.

```php
public initializeOptions(array<string,mixed>|null $options = null): void
```

**Parameters:**

| Parameter  | Type                          | Description                    |
|------------|-------------------------------|--------------------------------|
| `$options` | **array<string,mixed>\|null** | Defaults to capture and apply. |

***

### initialize

Optional hook called after options are initialized.

```php
public initialize(): void
```

***

### setOptions

Replace the current option set.

```php
public setOptions(array<string,mixed> $options): void
```

Null-valued entries remain present in the raw option array but are read
as missing by

- **See:** \PhalconKit\Support\Options\getOption().

**Parameters:**

| Parameter  | Type                    | Description       |
|------------|-------------------------|-------------------|
| `$options` | **array<string,mixed>** | Options to apply. |

***

### getOptions

Return the current option set.

```php
public getOptions(): array<string,mixed>
```

***

### setOption

Store or replace one option value.

```php
public setOption(string $key, mixed $value = null): void
```

Passing null stores the key in the raw option array, but public lookups
treat that key as missing.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |
| `$value`  | **mixed**  |             |

***

### getOption

Return one option value or a default when it is missing or null.

```php
public getOption(string $key, mixed $default = null): mixed
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$key`     | **string** |             |
| `$default` | **mixed**  |             |

***

### removeOption

Remove one option key when it exists in the raw option array.

```php
public removeOption(string $key): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |

***

### resetOptions

Restore current options to the initialized defaults.

```php
public resetOptions(): void
```

***

### clearOptions

Remove all current option values.

```php
public clearOptions(): void
```

***
