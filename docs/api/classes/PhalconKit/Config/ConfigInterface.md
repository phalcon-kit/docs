
PhalconKit configuration contract.

The interface extends Phalcon's native config contract with helpers used by
framework providers and bootstraps. Consumers should type against this
interface when they need `pathToArray()` in addition to native `get()`,
`path()`, `merge()`, and `toArray()` behavior.

***

* Full name: `\PhalconKit\Config\ConfigInterface`
* Parent interfaces:
  `ConfigInterface`

**See Also:**

* https://docs.phalcon.io/5.18/config/

## Methods

### pathToArray

Resolve a dot-path and normalize the result to a PHP array.

```php
public pathToArray(string $path, array|null $defaultValue = null, string|null $delimiter = null): array|null
```

Native Phalcon config paths can return scalars, arrays, config objects,
or the supplied default. This helper preserves null as "missing" while
converting config objects and scalar values into arrays for provider code
that expects normal PHP array options.

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
