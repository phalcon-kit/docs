
Replace string fragments throughout a nested array.

This helper is intentionally conservative: nested arrays are processed
recursively, string leaves are passed through `str_replace()`, and all other
values are returned unchanged. It is useful for config/template arrays that
contain placeholders alongside booleans, numbers, or nulls.

***

* Full name: `\PhalconKit\Support\Helper\Arr\RecursiveStrReplace`

## Methods

### __invoke

Invoke the helper and return an array result.

```php
public __invoke(array<string|int,mixed> $collection, array<string,string> $replaces): array<string|int,mixed>
```

**Parameters:**

| Parameter     | Type                         | Description         |
|---------------|------------------------------|---------------------|
| `$collection` | **array<string\|int,mixed>** | Input array.        |
| `$replaces`   | **array<string,string>**     | Search/replace map. |

***

### process

Recursively replace string values while preserving non-string values.

```php
public static process(array<string|int,mixed> $collection, array<string,string> $replaces): array<string|int,mixed>|null
```

* This method is **static**.
**Parameters:**

| Parameter     | Type                         | Description                                               |
|---------------|------------------------------|-----------------------------------------------------------|
| `$collection` | **array<string\|int,mixed>** | Input array.                                              |
| `$replaces`   | **array<string,string>**     | Search strings as keys and
replacement strings as values. |

***
