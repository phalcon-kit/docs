
***

* Full name: `\PhalconKit\Support\Options\Manager`
* This class implements:
  [`\PhalconKit\Support\Options\ManagerInterface`](./ManagerInterface.md),
  [`\PhalconKit\Support\Options\OptionsInterface`](./OptionsInterface.md)

## Methods

### get

```php
public get(string $key, mixed $default = null): mixed
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$key`     | **string** |             |
| `$default` | **mixed**  |             |

***

### has

```php
public has(string $key): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |

***

### set

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

```php
public remove(string $key): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |

***

### reset

```php
public reset(): void
```

***

### clear

```php
public clear(): void
```

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
