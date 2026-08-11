
Flatten nested arrays into dot-path keyed rule maps.

Integer keys with string values are treated as shorthand enabled fields. This
shape is used by exposure and controller field policies where nested config
needs to become a flat lookup table. Nested arrays also create an explicit
entry for their parent key with `false` when no direct parent rule exists,
allowing callers to distinguish a container node from an enabled leaf.

***

* Full name: `\PhalconKit\Support\Helper\Arr\FlattenKeys`

## Methods

### __invoke

Invoke the helper and always return an array.

```php
public __invoke(array<string|int,mixed> $collection = [], string $delimiter = '.', bool $lowerKey = true): array<array-key,mixed>
```

**Parameters:**

| Parameter     | Type                         | Description                                  |
|---------------|------------------------------|----------------------------------------------|
| `$collection` | **array<string\|int,mixed>** | Nested policy/config values.                 |
| `$delimiter`  | **string**                   | Delimiter used between nested path segments. |
| `$lowerKey`   | **bool**                     | Normalize string keys to lowercase.          |

***

### process

Flatten a nested rule map into delimiter-separated keys.

```php
public static process(array<string|int,mixed> $collection = [], string $delimiter = '.', bool $lowerKey = false, string|null $context = null): array<array-key,mixed>|null
```

Example input `['user' => ['email' => true]]` becomes
`['user.email' => true, 'user' => false]`. A list item like `['email']`
is treated as `['email' => true]` so concise allow-lists can be written
without repeating `true`.

* This method is **static**.
**Parameters:**

| Parameter     | Type                         | Description                                             |
|---------------|------------------------------|---------------------------------------------------------|
| `$collection` | **array<string\|int,mixed>** | Nested policy/config values.                            |
| `$delimiter`  | **string**                   | Key delimiter, normally `.`.                            |
| `$lowerKey`   | **bool**                     | Whether string keys should be normalized to lower
case. |
| `$context`    | **string\|null**             | Current recursion path.                                 |

***
