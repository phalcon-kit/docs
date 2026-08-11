
Factory and registry for named Phalcon logger instances.

The service is configured from the `logger` and `loggers` config sections.
It lazily builds named loggers, caches them for repeated calls, and applies
formatter/adapter options consistently across default and logger-specific
configuration.

***

* Full name: `\PhalconKit\Logger\Loggers`

**See Also:**

* https://docs.phalcon.io/5.18/logger/

## Properties

### loggers

Cached logger instances keyed by logger name.

```php
public array<string,\Phalcon\Logger\LoggerInterface> $loggers
```

***

## Methods

### getFormatter

Create a configured formatter by name.

```php
public getFormatter(string|null $formatter = null, array<string,mixed> $options = []): \Phalcon\Logger\Formatter\FormatterInterface
```

The formatter name is resolved from the configured `formatters` map. Line
formatters receive the optional `format` value and all
AbstractFormatter instances receive the optional `dateFormat` value.

**Parameters:**

| Parameter    | Type                    | Description                                                |
|--------------|-------------------------|------------------------------------------------------------|
| `$formatter` | **string\|null**        | The name of the formatter to retrieve. Defaults to 'line'. |
| `$options`   | **array<string,mixed>** | Formatter options from the selected
logger config.         |

**Return Value:**

The retrieved formatter.

**Throws:**

If the formatter name is not configured or
the configured formatter class does not implement
FormatterInterface.
- [`ConfigurationException`](../Exception/ConfigurationException.md)

***

### getAdapters

Create configured logger adapters for one or more driver names.

```php
public getAdapters(string|array|null $loggerDrivers = null, array<string,mixed> $options = [], \Phalcon\Logger\Formatter\FormatterInterface|null $formatter = null): array<string,\Phalcon\Logger\Adapter\AdapterInterface>
```

Driver names are resolved from the configured `drivers` map. The method
accepts either an array of names or a comma-separated string such as
`noop,stream`. Every adapter receives the provided formatter before it is
returned.

**Parameters:**

| Parameter        | Type                                                   | Description                                                                                                                       |
|------------------|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `$loggerDrivers` | **string\|array\|null**                                | The logger drivers to use. Defaults to null.                                                                                      |
| `$options`       | **array<string,mixed>**                                | Adapter options from the selected
logger config. Stream adapters expect `path` and `filename`;
custom adapters receive `options`. |
| `$formatter`     | **\Phalcon\Logger\Formatter\FormatterInterface\|null** | The formatter to attach to the adapters. Defaults to null.                                                                        |

**Return Value:**

The array of logger adapters by
driver name.

**Throws:**

If a driver name is not configured or the
configured adapter class does not implement AdapterInterface.
- [`ConfigurationException`](../Exception/ConfigurationException.md)

***

### load

Build, cache, and return a named logger.

```php
public load(string $name): \Phalcon\Logger\LoggerInterface
```

Logger-specific options in the `loggers.<name>` config section override
the `logger.default` values. Missing named logger config falls back to the
default logger options, which makes ad-hoc logger names possible while
preserving a consistent adapter/formatter setup.

**Parameters:**

| Parameter | Type       | Description                     |
|-----------|------------|---------------------------------|
| `$name`   | **string** | The name of the logger to load. |

**Return Value:**

The loaded logger.

**Throws:**

If formatter or adapter configuration is
invalid.
- [`ConfigurationException`](../Exception/ConfigurationException.md)

***

### get

Retrieve a cached logger or lazily load it from configuration.

```php
public get(string $name): \Phalcon\Logger\LoggerInterface
```

**Parameters:**

| Parameter | Type       | Description                         |
|-----------|------------|-------------------------------------|
| `$name`   | **string** | The name of the logger to retrieve. |

**Return Value:**

The retrieved logger.

**Throws:**

If formatter or adapter configuration is
invalid while loading the logger.
- [`ConfigurationException`](../Exception/ConfigurationException.md)

***

### set

Store or replace a named logger instance.

```php
public set(string $name, \Phalcon\Logger\LoggerInterface $logger): void
```

**Parameters:**

| Parameter | Type                                | Description                    |
|-----------|-------------------------------------|--------------------------------|
| `$name`   | **string**                          | The name of the logger to set. |
| `$logger` | **\Phalcon\Logger\LoggerInterface** | The logger to set.             |

***

### createFormatter

Instantiate a configured formatter class after validating its contract.

```php
private createFormatter(string $formatter, string $formatterClass): \Phalcon\Logger\Formatter\FormatterInterface
```

Formatter names come from configuration, so this private helper guards the
dynamic class name before instantiation and returns a framework-scoped
exception when configuration is invalid.

**Parameters:**

| Parameter         | Type       | Description                         |
|-------------------|------------|-------------------------------------|
| `$formatter`      | **string** | Logical formatter name from config. |
| `$formatterClass` | **string** | Configured formatter class name.    |

**Return Value:**

Formatter instance.

**Throws:**

When the configured class does not
implement Phalcon's formatter contract.
- [`ConfigurationException`](../Exception/ConfigurationException.md)

***

### createAdapter

Instantiate a configured adapter class for a logger driver.

```php
private createAdapter(string $loggerDriver, string $adapterClass, array<string,mixed> $options): \Phalcon\Logger\Adapter\AdapterInterface
```

Built-in Phalcon adapters have different constructor signatures, so this
method centralizes those differences. Custom adapters are expected to
accept the configured `options` array.

**Parameters:**

| Parameter       | Type                    | Description                      |
|-----------------|-------------------------|----------------------------------|
| `$loggerDriver` | **string**              | Logical driver name from config. |
| `$adapterClass` | **string**              | Configured adapter class name.   |
| `$options`      | **array<string,mixed>** | Resolved logger options.         |

**Return Value:**

Adapter instance ready to receive a formatter.

**Throws:**

When the configured class does not
implement Phalcon's adapter contract.
- [`ConfigurationException`](../Exception/ConfigurationException.md)

***

### createCustomAdapter

Instantiate a custom logger adapter with its configured options array.

```php
private createCustomAdapter(string $adapterClass, array<string,mixed> $options): \Phalcon\Logger\Adapter\AdapterInterface
```

This keeps built-in adapter branching small while still allowing
applications to register their own Phalcon-compatible adapter classes in
config.

**Parameters:**

| Parameter       | Type                    | Description                                               |
|-----------------|-------------------------|-----------------------------------------------------------|
| `$adapterClass` | **string**              | Adapter class already validated against
AdapterInterface. |
| `$options`      | **array<string,mixed>** | Resolved logger options.                                  |

**Return Value:**

Custom adapter instance.

***

## Inherited methods

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
