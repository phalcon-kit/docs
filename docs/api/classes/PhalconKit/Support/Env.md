
Loads dotenv files and exposes normalized environment values.

The helper keeps dotenv configuration in static state because bootstrap
config objects need environment values before the DI container exists. Values
loaded from dotenv are cached in

- **See:** ; callers can also set values
directly in tests or specialized bootstraps. `get()` normalizes common
string values (`true`, `false`, integers, and floats) so config defaults do
not need to repeat basic scalar casting.

***

* Full name: `\PhalconKit\Support\Env`

## Properties

### dotenv

Last Dotenv loader created by {@see load()}.

```php
public static \Dotenv\Dotenv|null $dotenv
```

* This property is **static**.

***

### vars

Cached dotenv values and explicit test/runtime overrides.

```php
public static array<string,mixed> $vars
```

* This property is **static**.

***

### paths

Directories searched for dotenv files.

```php
public static string[]|string|null $paths
```

* This property is **static**.

***

### names

Dotenv file names to load from the configured paths.

```php
public static string[]|string|null $names
```

* This property is **static**.

***

### type

Dotenv factory type: mutable, immutable, unsafe-mutable, or unsafe-immutable.

```php
public static string $type
```

* This property is **static**.

***

### shortCircuit

Whether dotenv should stop after the first matching file.

```php
public static bool $shortCircuit
```

* This property is **static**.

***

### fileEncoding

Optional file encoding passed to Dotenv.

```php
public static ?string $fileEncoding
```

* This property is **static**.

***

## Methods

### load

Configure and load dotenv files.

```php
public static load(string|array|null $paths = null, string|array|null $names = null, bool|null $shortCircuit = true, string|null $fileEncoding = null, string|null $type = null): \Dotenv\Dotenv
```

Null parameters reuse the current static settings. When no paths have
been configured,

- **See:** \PhalconKit\Support\setPaths() derives a path from `ENV_PATH`,
`ROOT_PATH`, `APP_PATH`, or the current working directory. Loaded values
are stored in
- **See:**  and also returned through the Dotenv instance.

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

Return the configured dotenv search paths.

```php
public static getPaths(): string|string[]|null
```

* This method is **static**.
**Return Value:**

Configured paths or null before load/setup.

***

### setPaths

Set dotenv search paths.

```php
public static setPaths(string|array|null $paths = null): void
```

Passing null asks the helper to derive a path from known bootstrap
constants. `APP_PATH` is converted to its parent directory because app
paths usually point to the application source folder rather than the
project root where `.env` normally lives.

* This method is **static**.
**Parameters:**

| Parameter | Type                    | Description |
|-----------|-------------------------|-------------|
| `$paths`  | **string\|array\|null** |             |

***

### getNames

Return dotenv file names loaded from the configured paths.

```php
public static getNames(): string|string[]|null
```

* This method is **static**.
**Return Value:**

Configured file names.

***

### setNames

Set dotenv file names.

```php
public static setNames(string|array|null $names): void
```

Passing null resets the loader to the conventional `.env` file name.

* This method is **static**.
**Parameters:**

| Parameter | Type                    | Description |
|-----------|-------------------------|-------------|
| `$names`  | **string\|array\|null** |             |

***

### getType

Return the Dotenv factory suffix for the configured loader type.

```php
public static getType(): string
```

Dotenv exposes static factories such as `createMutable()` and
`createUnsafeImmutable()`. This method converts the stored type string
into the suffix used by

- **See:** \PhalconKit\Support\load().

* This method is **static**.
**Return Value:**

Dotenv factory suffix.

**Throws:**

When the configured environment loader
type is unsupported.
- [`ConfigurationException`](../Exception/ConfigurationException.md)

***

### setType

Set the Dotenv loader type.

```php
public static setType(string|null $type = null): void
```

Invalid values are normalized to `mutable` for compatibility with older
bootstraps. A stricter invalid-type exception is tracked as a future
design question because changing this default could break existing
deployments.

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                                   |
|-----------|------------------|-------------------------------------------------------------------------------|
| `$type`   | **string\|null** | Loader type: `mutable`, `immutable`,
`unsafe-mutable`, or `unsafe-immutable`. |

***

### getShortCircuit

Return whether dotenv loading stops after the first matching file.

```php
public static getShortCircuit(): bool
```

* This method is **static**.
**Return Value:**

Current short-circuit setting.

***

### setShortCircuit

Set whether dotenv loading stops after the first matching file.

```php
public static setShortCircuit(bool|null $shortCircuit = true): void
```

* This method is **static**.
**Parameters:**

| Parameter       | Type           | Description                           |
|-----------------|----------------|---------------------------------------|
| `$shortCircuit` | **bool\|null** | Null restores the default true value. |

***

### getFileEncoding

Return the configured dotenv file encoding.

```php
public static getFileEncoding(): string|null
```

* This method is **static**.
**Return Value:**

Encoding passed to Dotenv, or null for its default.

***

### setFileEncoding

Set the dotenv file encoding.

```php
public static setFileEncoding(string|null $fileEncoding = null): void
```

* This method is **static**.
**Parameters:**

| Parameter       | Type             | Description                                         |
|-----------------|------------------|-----------------------------------------------------|
| `$fileEncoding` | **string\|null** | Encoding passed to Dotenv, or null for
its default. |

***

### getDotenv

Return the current Dotenv instance, loading defaults on first use.

```php
public static getDotenv(): \Dotenv\Dotenv
```

* This method is **static**.
**Return Value:**

Active Dotenv loader.

***

### get

Return an environment value with simple scalar normalization.

```php
public static get(string $key, mixed $default = null): mixed
```

String values equal to `true` or `false` are returned as booleans.
Numeric strings are returned as integers or floats. Other values are
returned unchanged, and missing keys return the caller-provided default.

* This method is **static**.
**Parameters:**

| Parameter  | Type       | Description                          |
|------------|------------|--------------------------------------|
| `$key`     | **string** | Environment key.                     |
| `$default` | **mixed**  | Fallback when the key is not loaded. |

**Return Value:**

Normalized environment value or fallback.

***

### set

Set or override one cached environment value.

```php
public static set(string $key, mixed $value): void
```

This affects PhalconKit's cached environment store only; it does not call
`putenv()` or mutate `$_ENV`.

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description      |
|-----------|------------|------------------|
| `$key`    | **string** | Environment key. |
| `$value`  | **mixed**  | Value to store.  |

***
