
Reusable implementation for mutable service/object options.

Classes using the trait get a simple lifecycle: constructor options are
captured as defaults, current options can be replaced or changed by key, and
`resetOptions()` restores the captured defaults. Override `initialize()` for
post-option setup that should run once during construction.

***

* Full name: `\PhalconKit\Support\Options\Options`

## Properties

### defaultOptions

Options captured during initialization and used by resetOptions().

```php
protected array<string,mixed> $defaultOptions
```

***
### options

Current mutable option values.

```php
protected array<string,mixed> $options
```

***

## Methods

### __construct

Construct the object and initialize its options.

```php
public __construct(array<string,mixed>|null $options = null): mixed
```

**Parameters:**

| Parameter  | Type                          | Description                    |
|------------|-------------------------------|--------------------------------|
| `$options` | **array<string,mixed>\|null** | Defaults to capture and apply. |

***
### initializeOptions

Capture defaults, apply the current options, and run initialize().

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

Override this in classes that need to derive internal state from options
during construction.

***
### setOptions

Replace or merge the current option set.

```php
public setOptions(array<string,mixed> $options, bool $merge = false): void
```

Options intentionally use PHP's null-coalescing read semantics: a key
stored with a null value remains present in the raw option array, but


- **See:** \PhalconKit\Support\Options\getOption() returns the caller default and
- **See:** \PhalconKit\Support\Options\hasOption()
reports false for that key.

**Parameters:**

| Parameter  | Type                    | Description                                                       |
|------------|-------------------------|-------------------------------------------------------------------|
| `$options` | **array<string,mixed>** | Options to apply.                                                 |
| `$merge`   | **bool**                | Whether to merge into existing options instead of
replacing them. |

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
public setOption(string $key, mixed $value = null, bool $merge = false): void
```

Passing null stores the key in the raw option array, but the key still
reads as missing through

- **See:** \PhalconKit\Support\Options\getOption() and
- **See:** \PhalconKit\Support\Options\hasOption(). This
preserves the historical contract where null means "fall back to the
caller default" while still allowing callers to inspect raw options.

**Parameters:**

| Parameter | Type       | Description                                                         |
|-----------|------------|---------------------------------------------------------------------|
| `$key`    | **string** |                                                                     |
| `$value`  | **mixed**  |                                                                     |
| `$merge`  | **bool**   | Whether to merge the key/value pair into the existing
option array. |

***
### getOption

Return one option value or a default when it is missing or null.

```php
public getOption(string $key, mixed $default = null): mixed
```

**Parameters:**

| Parameter  | Type       | Description                                  |
|------------|------------|----------------------------------------------|
| `$key`     | **string** |                                              |
| `$default` | **mixed**  | Default returned when the option is not set. |

***
### hasOption

Return true when an option is present and not null.

```php
public hasOption(string $key): bool
```

This intentionally mirrors

- **See:** \PhalconKit\Support\Options\getOption() rather than
`array_key_exists()`: null-valued options are stored in the raw option
array but are treated as absent by the public lookup helpers.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |

***
### removeOption

Remove one option key when it exists in the raw option array.

```php
public removeOption(string $key): void
```

Removal uses `array_key_exists()` instead of `isset()` so callers can
delete a key even when it currently stores null.

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
