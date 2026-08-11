
Translation adapter backed by a nested PHP array.

Phalcon's NativeArray adapter supports flat translation maps. This adapter
adds delimiter-based nested lookup, while still preserving exact flat-key
lookup precedence. A flat key such as `button.save` wins over a nested path
`button => ['save' => ...]` when both exist.

Missing keys return the original key by default. Set `triggerError` to true
when development/test environments should fail fast on missing translations.

Usage example:
```php
$interpolator = new InterpolatorFactory();
$options = [
    'content' => [
        'en' => [
            'welcome' => 'Welcome to our website!',
            'goodbye' => 'Goodbye!',
        ],
        'fr' => [
            'welcome' => 'Bienvenue sur notre site web!',
            'goodbye' => 'Au revoir!',
        ],
    ],
    'triggerError' => false,
    'delimiter' => '.',
];

$translator = new NestedNativeArray($interpolator, $options);

// Check if translation exists
$translator->has('en.welcome'); // returns true

// Get translated string
$translator->query('fr.goodbye'); // returns 'Au revoir!'

// Get translated string with placeholders
$translator->query('en.welcome', ['name' => 'John']); // returns 'Welcome to our website, John!'
```

***

* Full name: `\PhalconKit\Translate\Adapter\NestedNativeArray`
* Parent class: [`AbstractAdapter`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  `ArrayAccess`

**See Also:**

* https://docs.phalcon.io/latest/translate/

## Properties

### translate

Translation content indexed by flat keys or nested arrays.

```php
private array<string,mixed> $translate
```

***

### delimiter

Delimiter used when resolving nested translation paths.

```php
protected non-empty-string $delimiter
```

***

## Methods

### __construct

Create a nested-array translation adapter.

```php
public __construct(\Phalcon\Translate\InterpolatorFactory $interpolator, array<string,mixed> $options): mixed
```

Supported options:
- `content`: translation content as flat keys, nested arrays, or both.
- `triggerError`: throw a RuntimeException when a key is missing.
- `delimiter`: non-empty delimiter used for nested lookup.

**Parameters:**

| Parameter       | Type                                       | Description                                          |
|-----------------|--------------------------------------------|------------------------------------------------------|
| `$interpolator` | **\Phalcon\Translate\InterpolatorFactory** | Factory used by Phalcon for
placeholder replacement. |
| `$options`      | **array<string,mixed>**                    | Adapter options.                                     |

***

### exists

Check whether a translation exists for the given key.

```php
public exists(string $index): bool
```

* **Warning:** this method is **deprecated**. This means that this method will likely be removed in a future version.
**Parameters:**

| Parameter | Type       | Description               |
|-----------|------------|---------------------------|
| `$index`  | **string** | Translation key to check. |

**Return Value:**

True when the key exists.

**See Also:**

* \PhalconKit\Translate\Adapter\has()

***

### has

Return true when a flat or nested translation key exists.

```php
public has(string $index): bool
```

Exact flat keys are checked first. If no exact key exists, the key is
split by the configured delimiter and resolved through nested arrays.

**Parameters:**

| Parameter | Type       | Description               |
|-----------|------------|---------------------------|
| `$index`  | **string** | Translation key to check. |

**Return Value:**

True when the key resolves to a configured translation.

***

### notFound

Return the missing key fallback or throw when strict mode is enabled.

```php
public notFound(string $index): string
```

**Parameters:**

| Parameter | Type       | Description              |
|-----------|------------|--------------------------|
| `$index`  | **string** | Missing translation key. |

**Return Value:**

Original key when `triggerError` is false.

**Throws:**

When `triggerError` is true.
- [`RuntimeException`](../../Exception/RuntimeException.md)

***

### query

Return a translated string for a flat or nested key.

```php
public query(string $translateKey, array<string,mixed> $placeholders = []): string
```

Exact flat keys are returned before nested lookup is attempted. Nested
values are resolved with the configured delimiter and then passed through
Phalcon's placeholder interpolator.

**Parameters:**

| Parameter       | Type                    | Description                                    |
|-----------------|-------------------------|------------------------------------------------|
| `$translateKey` | **string**              | Translation key to resolve.                    |
| `$placeholders` | **array<string,mixed>** | Placeholder values passed to the
interpolator. |

**Return Value:**

Translated string, or the missing-key fallback.

**Throws:**

When the key is missing and `triggerError` is
true.
- [`RuntimeException`](../../Exception/RuntimeException.md)

***

### toArray

Return the raw translation content.

```php
public toArray(): array<string,mixed>
```

**Return Value:**

Translation content exactly as configured.

***
