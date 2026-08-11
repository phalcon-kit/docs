
Config adapter shape expected by Phalcon DevTools.

PhalconKit's normal database config supports named drivers and adapter class
names. DevTools expects a flatter database array with a short adapter name,
so this config extracts the selected driver and normalizes it for DevTools
commands.

***

* Full name: `\PhalconKit\Bootstrap\Devtools`
* Parent class: [`\PhalconKit\Bootstrap\Config`](./Config.md)

## Methods

### __construct

Build a DevTools-compatible database config from PhalconKit config data.

```php
public __construct(array<string,mixed> $data = [], bool $insensitive = true): mixed
```

**Parameters:**

| Parameter      | Type                    | Description                                     |
|----------------|-------------------------|-------------------------------------------------|
| `$data`        | **array<string,mixed>** | Application config overrides.                   |
| `$insensitive` | **bool**                | Whether config keys should be case-insensitive. |

**Throws:**

When the selected database driver does not
define a valid adapter class.
- [`ConfigurationException`](../Exception/ConfigurationException.md)

***

## Inherited methods

### pathToArray

Resolve a config path and normalize the result to an array.

```php
public pathToArray(string $path, array|null $defaultValue = null, string|null $delimiter = null): array|null
```

`null` is preserved so callers can distinguish a missing optional path
from a configured scalar value. Native Phalcon config objects are
converted through `toArray()`, and any other non-null value is cast to an
array.

**Parameters:**

| Parameter       | Type             | Description                                          |
|-----------------|------------------|------------------------------------------------------|
| `$path`         | **string**       | Path understood by Phalcon's native `path()` method. |
| `$defaultValue` | **array\|null**  | Default returned when the path is
missing.           |
| `$delimiter`    | **string\|null** | Optional path delimiter.                             |

**Return Value:**

Normalized array value, or null when the path
resolves to null.

***

### merge

Merge data into this config instance.

```php
public merge(array|\Phalcon\Config\ConfigInterface $toMerge, bool $append = false): \Phalcon\Config\ConfigInterface
```

When `$append` is false, native Phalcon merge behavior is used. When
`$append` is true, numeric-keyed values are appended while associative
values are replaced recursively. This is useful for framework config
fragments such as provider lists, permission features, and default seed
data where applications need to extend list values instead of replacing
the whole list.

**Parameters:**

| Parameter  | Type                                       | Description                                  |
|------------|--------------------------------------------|----------------------------------------------|
| `$toMerge` | **array\|\Phalcon\Config\ConfigInterface** | Data to merge into this
config.              |
| `$append`  | **bool**                                   | Use PhalconKit append-aware merge semantics. |

**Return Value:**

The current mutated config instance.

**Throws:**

When append mode receives a value that
cannot be converted to an array.
- [`InvalidArgumentException`](../Exception/InvalidArgumentException.md)

***

### internalMergeAppend

Append-merge two arrays recursively.

```php
final protected internalMergeAppend(array $source, array $target): array
```

Integer keys are appended to preserve list-style config fragments.
String keys replace existing values unless both sides contain arrays, in
which case the merge recurses.

* This method is **final**.
**Parameters:**

| Parameter | Type      | Description           |
|-----------|-----------|-----------------------|
| `$source` | **array** | Base config data.     |
| `$target` | **array** | Incoming config data. |

**Return Value:**

Merged config data.

***

### getDateTime

Return a modified immutable date.

```php
public getDateTime(string $modifier, \DateTimeImmutable|null $dateTime = null): \DateTimeImmutable
```

This helper keeps date-modifier config strongly typed in lifecycle and
retention code. When no base date is provided, the current time is used.

**Parameters:**

| Parameter   | Type                         | Description                                                                                    |
|-------------|------------------------------|------------------------------------------------------------------------------------------------|
| `$modifier` | **string**                   | Date/time modifier accepted by
`DateTimeImmutable::modify()`, such as `-1 month` or `+7 days`. |
| `$dateTime` | **\DateTimeImmutable\|null** | Optional base date.                                                                            |

**Return Value:**

Modified date.

**Throws:**

If the modifier cannot be parsed.
- [`DateMalformedStringException`](https://www.php.net/manual/en/class.datemalformedstringexception.php){:target="_blank"}

***

### defineConst

Define path/environment constants expected by legacy and generated code.

```php
public defineConst(): void
```

Existing constants are never overwritten. Values are read from Env first
and then fall back to conservative defaults relative to the current
project root.

***

### __construct

Merge default framework config with application-provided overrides.

```php
public __construct(array<string,mixed> $data = [], bool $insensitive = false): mixed
```

The constructor calls `defineConst()` before building config so path
constants are available while default provider/module/model arrays are
prepared. `$data` is appended using the config merge strategy, allowing
applications to override or extend framework defaults.

**Parameters:**

| Parameter      | Type                    | Description                                     |
|----------------|-------------------------|-------------------------------------------------|
| `$data`        | **array<string,mixed>** | Application overrides.                          |
| `$insensitive` | **bool**                | Whether config keys should be case-insensitive. |

***
