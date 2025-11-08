
***

* Full name: `\PhalconKit\Logger\Loggers`

## Properties

### loggers

An array to store logger objects

```php
public \Phalcon\Logger\LoggerInterface[] $loggers
```

***

## Methods

### getFormatter

Gets a formatter based on the provided formatter name and options.

```php
public getFormatter(string|null $formatter = null, array $options = []): \Phalcon\Logger\Formatter\FormatterInterface
```

**Parameters:**

| Parameter    | Type             | Description                                                |
|--------------|------------------|------------------------------------------------------------|
| `$formatter` | **string\|null** | The name of the formatter to retrieve. Defaults to 'line'. |
| `$options`   | **array**        | The options for the formatter.                             |

**Return Value:**

The retrieved formatter.

**Throws:**

If the specified formatter is not defined.
- [`Exception`](../../Exception.md)

***

### getAdapters

Returns an array of logger adapters based on the given drivers, formatter, and options.

```php
public getAdapters(string|array|null $loggerDrivers = null, array $options = [], \Phalcon\Logger\Formatter\FormatterInterface|null $formatter = null): array
```

**Parameters:**

| Parameter        | Type                                                   | Description                                                        |
|------------------|--------------------------------------------------------|--------------------------------------------------------------------|
| `$loggerDrivers` | **string\|array\|null**                                | The logger drivers to use. Defaults to null.                       |
| `$options`       | **array**                                              | The options to configure the adapters. Defaults to an empty array. |
| `$formatter`     | **\Phalcon\Logger\Formatter\FormatterInterface\|null** | The formatter to attach to the adapters. Defaults to null.         |

**Return Value:**

The array of logger adapters.

**Throws:**

If a logger driver adapter is not defined.
- [`Exception`](../../Exception.md)

***

### load

Loads a logger with the given name.

```php
public load(string $name): \Phalcon\Logger\LoggerInterface
```

**Parameters:**

| Parameter | Type       | Description                     |
|-----------|------------|---------------------------------|
| `$name`   | **string** | The name of the logger to load. |

**Return Value:**

The loaded logger.

**Throws:**

- [`Exception`](../../Exception.md)

***

### get

Retrieves a logger with the given name.

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

If the logger cannot be loaded.
- [`Exception`](../../Exception.md)

***

### set

Sets a logger with the given name.

```php
public set(string $name, \Phalcon\Logger\LoggerInterface $logger): void
```

**Parameters:**

| Parameter | Type                                | Description                    |
|-----------|-------------------------------------|--------------------------------|
| `$name`   | **string**                          | The name of the logger to set. |
| `$logger` | **\Phalcon\Logger\LoggerInterface** | The logger to set.             |

***

## Inherited methods

### __construct

Constructs a new instance of the class.

```php
public __construct(array|null $options = null): mixed
```

**Parameters:**

| Parameter  | Type            | Description                                                                    |
|------------|-----------------|--------------------------------------------------------------------------------|
| `$options` | **array\|null** | An optional array of options to initialize the instance with. Default is null. |

***

### initializeOptions

Initializes the options for the object.

```php
public initializeOptions(array|null $options = null): void
```

**Parameters:**

| Parameter  | Type            | Description                                                          |
|------------|-----------------|----------------------------------------------------------------------|
| `$options` | **array\|null** | The options to be initialized. If null, an empty array will be used. |

***

### initialize

Initializes the object.

```php
public initialize(): void
```

This method is responsible for performing any necessary setup or initialization tasks for the object.
It does not accept any parameters and does not return a value.

***

### setOptions

Sets the options for the object.

```php
public setOptions(array $options, bool $merge = false): void
```

**Parameters:**

| Parameter  | Type      | Description                                                                    |
|------------|-----------|--------------------------------------------------------------------------------|
| `$options` | **array** | The array of options to be set.                                                |
| `$merge`   | **bool**  | Whether to merge the existing options with the new options. Defaults to false. |

***

### getOptions

Retrieves all options.

```php
public getOptions(): array
```

**Return Value:**

An array containing all the options.

***

### setOption

Sets the value of the option specified by the given key.

```php
public setOption(string $key, mixed $value = null, bool $merge = false): void
```

**Parameters:**

| Parameter | Type       | Description                                                                         |
|-----------|------------|-------------------------------------------------------------------------------------|
| `$key`    | **string** | The key of the option.                                                              |
| `$value`  | **mixed**  | The value to be set for the option.                                                 |
| `$merge`  | **bool**   | Whether to merge the new value with an existing value if the option already exists. |

***

### getOption

Retrieves the value of the option specified by the given key.

```php
public getOption(string $key, mixed $default = null): mixed
```

**Parameters:**

| Parameter  | Type       | Description                                                    |
|------------|------------|----------------------------------------------------------------|
| `$key`     | **string** | The key of the option.                                         |
| `$default` | **mixed**  | The default value to be returned if the option does not exist. |

**Return Value:**

The value of the option specified by the key, or the default value if the option does not exist.

***

### hasOption

Checks if the option specified by the given key exists.

```php
public hasOption(string $key): bool
```

**Parameters:**

| Parameter | Type       | Description            |
|-----------|------------|------------------------|
| `$key`    | **string** | The key of the option. |

**Return Value:**

Returns true if the option exists, false otherwise.

***

### removeOption

Remove an option by key

```php
public removeOption(string $key): void
```

Removes the option with the given key from the options array.

**Parameters:**

| Parameter | Type       | Description                         |
|-----------|------------|-------------------------------------|
| `$key`    | **string** | The key of the option to be removed |

***

### resetOptions

Reset all options to their default values
- Uses the defaultOptions property to set the options

```php
public resetOptions(): void
```

***

### clearOptions

Clear all options

```php
public clearOptions(): void
```

This method clears all the options stored in the class.
After calling this method, the options array will be empty.

***
