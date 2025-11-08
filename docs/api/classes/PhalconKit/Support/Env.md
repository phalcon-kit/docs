
This class provides utilities for managing environment variables and loading .env files.

It allows for easy access to environment variables and provides methods for setting and getting values.
It also initializes a Dotenv instance and loads .env files based on specified configurations.

***

* Full name: `\PhalconKit\Support\Env`

## Properties

### dotenv

Represents the instance of the Dotenv class.

```php
public static ?\Dotenv\Dotenv $dotenv
```

The Dotenv class is responsible for loading environment variables from the
".env" file into the application.

* This property is **static**.

***

### vars

Represents an array of variables.

```php
public static array $vars
```

The $vars variable is used to store a collection of key-value pairs,
where each key represents a variable name and the corresponding value
represents the value of that variable.

* This property is **static**.

***

### paths

Holds the value of the paths.

```php
public static string[]|string|null $paths
```

This variable represents the value of the paths and is initially set to null.
It can be assigned a different value during the runtime of the program.

* This property is **static**.

***

### names

Represents the array of filenames.

```php
public static string[]|string|null $names
```

The $names variable is an array that holds the filenames of the ".env" file(s) to be loaded.
This variable is used as an argument in the Dotenv class to specify the filenames to load.

* This property is **static**.

***

### type

Represents the type of data being declared.

```php
public static string $type
```

The $type variable is a string that indicates the mutability of the data. It can
have two possible values: "mutable" or "immutable".

* This property is **static**.

***

### shortCircuit

Represents a boolean flag that enables short-circuiting in the code.

```php
public static bool $shortCircuit
```

When the $shortCircuit variable is set to true, it indicates that the code
should perform short-circuit evaluation. Short-circuit evaluation allows
skipping the evaluation of subsequent conditions in a logical expression if
the final result can be determined early.

* This property is **static**.

***

### fileEncoding

Represents the encoding of the file.

```php
public static string|null $fileEncoding
```

The $fileEncoding variable is used to store the encoding of the file that
will be processed by the application. It is initially set to null and will be
updated with the actual encoding value during the file processing.

* This property is **static**.

***

## Methods

### load

Initializes the Dotenv instance with the specified configurations
and returns the loaded instance.

```php
public static load(string|array|null $paths = null, string|array|null $names = null, bool|null $shortCircuit = true, string|null $fileEncoding = null, string|null $type = null): \Dotenv\Dotenv
```

* This method is **static**.
**Parameters:**

| Parameter       | Type                    | Description                                                       |
|-----------------|-------------------------|-------------------------------------------------------------------|
| `$paths`        | **string\|array\|null** | The paths to search for dotenv files.                             |
| `$names`        | **string\|array\|null** | The names of the dotenv files to load.                            |
| `$shortCircuit` | **bool\|null**          | Whether to stop loading dotenv files after finding the first one. |
| `$fileEncoding` | **string\|null**        | The encoding of the dotenv files.                                 |
| `$type`         | **string\|null**        | The type of dotenv files to load.                                 |

**Return Value:**

The loaded Dotenv instance.

***

### getPaths

Retrieves an array of paths.

```php
public static getPaths(): string|string[]|null
```

If the paths array is not yet created, it will be loaded and returned.

* This method is **static**.
**Return Value:**

The array of paths.

***

### setPaths

Sets the paths for the application. If no paths are provided,
the paths will be set to null.

```php
public static setPaths(string|string[]|null $paths = null): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type                       | Description                                                                                                   |
|-----------|----------------------------|---------------------------------------------------------------------------------------------------------------|
| `$paths`  | **string\|string[]\|null** | The paths to be set for the application.
If null is provided, the paths will be set to null.
Default is null. |

***

### getNames

Get .env file names

```php
public static getNames(): string|string[]|null
```

* This method is **static**.
***

### setNames

Sets the names array. If the specified array is null, the existing names array will be cleared.

```php
public static setNames(string|string[]|null $names): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type                       | Description                                                            |
|-----------|----------------------------|------------------------------------------------------------------------|
| `$names`  | **string\|string[]\|null** | The array of names. If null, the existing names array will be cleared. |

***

### getType

Retrieves the type of the instance. If the type is not set, it will default to 'mutable'.

```php
public static getType(): string
```

The type is then transformed into a camel case string and the first letter is capitalized.

* This method is **static**.
**Return Value:**

The type of the instance.

**Throws:**

- [`Exception`](../../Exception.md)

***

### setType

Sets the type of the object. If the type is not provided or is not one of the allowed types,
the type will be set to 'mutable' by default.

```php
public static setType(string|null $type = null): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                                                            |
|-----------|------------------|--------------------------------------------------------------------------------------------------------|
| `$type`   | **string\|null** | The type of the object. Available types: 'mutable', 'immutable', 'unsafe-mutable', 'unsafe-immutable'. |

***

### getShortCircuit

Retrieves the short circuit value. If the short circuit value is not yet set,
it will return the default value.

```php
public static getShortCircuit(): bool
```

* This method is **static**.
**Return Value:**

The short circuit value.

***

### setShortCircuit

Sets the value of the shortCircuit property.

```php
public static setShortCircuit(bool $shortCircuit = true): void
```

* This method is **static**.
**Parameters:**

| Parameter       | Type     | Description                                  |
|-----------------|----------|----------------------------------------------|
| `$shortCircuit` | **bool** | The new value for the shortCircuit property. |

***

### getFileEncoding

Retrieves the file encoding. If the encoding is not yet set, it will return null.

```php
public static getFileEncoding(): ?string
```

* This method is **static**.
**Return Value:**

The file encoding.

***

### setFileEncoding

Sets the file encoding for the env file. If no file encoding is specified,
the default encoding will be used.

```php
public static setFileEncoding(string|null $fileEncoding = null): void
```

* This method is **static**.
**Parameters:**

| Parameter       | Type             | Description                                    |
|-----------------|------------------|------------------------------------------------|
| `$fileEncoding` | **string\|null** | The file encoding to be set. Defaults to null. |

***

### getDotenv

Retrieves the Dotenv instance. If the instance is not yet created,
it will be loaded and returned.

```php
public static getDotenv(): \Dotenv\Dotenv
```

* This method is **static**.
**Return Value:**

The Dotenv instance.

***

### get

Gets the value of an environment variable. Pass the $default for fallback value.

```php
public static get(string $key, mixed $default = null): mixed
```

* This method is **static**.
**Parameters:**

| Parameter  | Type       | Description                                 |
|------------|------------|---------------------------------------------|
| `$key`     | **string** | Key to get                                  |
| `$default` | **mixed**  | Value to fallback if the key can't be found |

**Return Value:**

Return the environment variable value or the default value

***

### set

Set an environment variable

```php
public static set(string $key, mixed $value): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description  |
|-----------|------------|--------------|
| `$key`    | **string** | Key to set   |
| `$value`  | **mixed**  | Value to set |

***
