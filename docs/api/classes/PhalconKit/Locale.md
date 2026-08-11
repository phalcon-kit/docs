
Allow to manage and lookup the locale for the localisation

***

* Full name: `\PhalconKit\Locale`
* Parent class: [`\PhalconKit\Di\Injectable`](./Di/Injectable.md)
* This class implements:
  [`\PhalconKit\Support\Options\OptionsInterface`](./Support/Options/OptionsInterface.md)

## Constants

| Constant       | Visibility | Type   | Value     |
|----------------|------------|--------|-----------|
| `MODE_DEFAULT` | public     | string | 'default' |
| `MODE_ROUTE`   | public     | string | 'route'   |
| `MODE_HTTP`    | public     | string | 'http'    |
| `MODE_SESSION` | public     | string | 'session' |

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
