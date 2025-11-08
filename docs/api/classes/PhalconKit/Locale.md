
Allow to manage and lookup the locale for the localisation

***

* Full name: `\PhalconKit\Locale`
* Parent class: [`\PhalconKit\Di\Injectable`](./Di/Injectable.md)
* This class implements:
  [`\PhalconKit\Support\Options\OptionsInterface`](./Support/Options/OptionsInterface.md)

## Constants

| Constant       | Visibility | Type | Value     |
|----------------|------------|------|-----------|
| `MODE_DEFAULT` | public     |      | 'default' |
| `MODE_ROUTE`   | public     |      | 'route'   |
| `MODE_HTTP`    | public     |      | 'http'    |
| `MODE_SESSION` | public     |      | 'session' |

## Properties

### mode

Locale mode
Locale::MODE_DEFAULT 'default' (Router -> http)
Locale::MODE_SESSION 'session' (Router -> session -> http)

```php
public string $mode
```

***

### locale

The actual locale that was picked

```php
public string|null $locale
```

***

### sessionKey

Session key for storing the locale

```php
public string $sessionKey
```

***

### default

Default locale

```php
public string $default
```

This variable holds the default locale value for the application.
If no locale is explicitly specified, this value will be used.

***

### allowed

Array of allowed languages.

```php
public array $allowed
```

***

## Methods

### initialize

Initializes the object by setting its properties based on the provided options.

```php
public initialize(): void
```

This method retrieves the values of the sessionKey, allowed, default, and mode options using the getOption()
method. If these options are not provided, the default values specified in the class properties are used instead.

It then sets the obtained values to the corresponding class properties using the appropriate setter methods,
namely setAllowed(), setDefault(), and setMode(). Additionally, it assigns the obtained sessionKey value directly
to the sessionKey property.

Finally, the initialize() method prepares the default value by calling the prepare() method with the getDefault()
method as its parameter.

***

### get

Alias of the getLocale() method

```php
public get(): ?string
```

***

### getLocale

Retrieves the locale value of the object.

```php
public getLocale(): string|null
```

This method returns the value of the locale property, which represents the current locale of the object.
The locale property is set using the setLocale() method or may be null if no locale is set.

**Return Value:**

The locale value of the object, or null if no locale is set.

***

### setLocale

Set the current locale value

```php
public setLocale(?string $locale = null): void
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$locale` | **?string** |             |

***

### getDefault

Get the default locale

```php
public getDefault(): string
```

***

### setDefault

Set the default locale value

```php
public setDefault(string $locale): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$locale` | **string** |             |

***

### getAllowed

Get the list of possible locale

```php
public getAllowed(): array
```

***

### setAllowed

Set the allowed locale

```php
public setAllowed(array $allowed): void
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$allowed` | **array** |             |

***

### getMode

Get the defined mode

```php
public getMode(): string
```

***

### setMode

Set the mode

```php
public setMode(string $mode): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$mode`   | **string** |             |

***

### prepare

Prepare and set and return the locale based on the defined mode

```php
public prepare(?string $default = null): ?string
```

**Parameters:**

| Parameter  | Type        | Description |
|------------|-------------|-------------|
| `$default` | **?string** |             |

***

### getFromRoute

Retrieves the locale from the route

```php
public getFromRoute(?string $default = null): ?string
```

**Parameters:**

| Parameter  | Type        | Description |
|------------|-------------|-------------|
| `$default` | **?string** |             |

***

### getFromDispatcher

Retrieves the locale from the dispatcher

```php
public getFromDispatcher(?string $default = null): ?string
```

**Parameters:**

| Parameter  | Type        | Description |
|------------|-------------|-------------|
| `$default` | **?string** |             |

***

### getFromSession

Retrieves the locale from the session

```php
public getFromSession(?string $default = null): ?string
```

**Parameters:**

| Parameter  | Type        | Description |
|------------|-------------|-------------|
| `$default` | **?string** |             |

***

### getFromHttp

Retrieves the locale from the request
of getBestLanguage() header
or HTTP_ACCEPT_LANGUAGE header

```php
public getFromHttp(?string $default = null): ?string
```

**Parameters:**

| Parameter  | Type        | Description |
|------------|-------------|-------------|
| `$default` | **?string** |             |

***

### saveIntoSession

Save locale into session if mode contain session handling

```php
public saveIntoSession(?string $locale = null, ?bool $force = false): void
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$locale` | **?string** |             |
| `$force`  | **?bool**   |             |

***

### lookup

```php
public lookup(string|null $locale = null, array|null $allowed = null, bool $canonicalize = false, string|null $default = null): string|null
```

**Parameters:**

| Parameter       | Type             | Description                                                                                  |
|-----------------|------------------|----------------------------------------------------------------------------------------------|
| `$locale`       | **string\|null** | The locale to use as the language range when matching.                                       |
| `$allowed`      | **array\|null**  | An array containing a list of language tags to compare to locale. Maximum 100 items allowed. |
| `$canonicalize` | **bool**         | If true, the arguments will be converted to canonical form before matching.                  |
| `$default`      | **string\|null** | The locale to use if no match is found.                                                      |

**Return Value:**

The closest matching language tag or default value.

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
