
NestedNativeArray class is an implementation of the Translate Adapter interface that uses
a nested array as the translation source.

Usage example:
```
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
$translator->exists('en.welcome'); // returns true

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

## Properties

### translate

Translation array.

```php
private array $translate
```

***

### triggerError

```php
private bool $triggerError
```

***

### delimiter

Sets the value of the delimiter.

```php
protected string $delimiter
```

***

## Methods

### __construct

PhalconKit\Translate\Adapter\NestedNativeArray constructor

```php
public __construct(\Phalcon\Translate\InterpolatorFactory $interpolator, array $options): mixed
```

**Parameters:**

| Parameter       | Type                                       | Description                                                                   |
|-----------------|--------------------------------------------|-------------------------------------------------------------------------------|
| `$interpolator` | **\Phalcon\Translate\InterpolatorFactory** |                                                                               |
| `$options`      | **array**                                  | [
    'content' => '',
    'triggerError' => false,
    'delimiter' => '.',
] |

***

### exists

Returns whether a translation exists for the given index

```php
public exists(string $index): bool
```

* **Warning:** this method is **deprecated**. This means that this method will likely be removed in a future version.
**Parameters:**

| Parameter | Type       | Description                    |
|-----------|------------|--------------------------------|
| `$index`  | **string** | The translation index to check |

**Return Value:**

True if a translation exists for the index, false otherwise

**See Also:**

* \PhalconKit\Translate\Adapter\has()

***

### has

Returns true if the translation for the given index exists, false otherwise.

```php
public has(string $index): bool
```

**Parameters:**

| Parameter | Type       | Description                            |
|-----------|------------|----------------------------------------|
| `$index`  | **string** | The index of the translation to check. |

**Return Value:**

Returns true if the translation for the given index exists, false otherwise.

***

### notFound

Returns the index if translation key is not found
Throws exception if triggerError is enabled and translation key is not found

```php
public notFound(string $index): string
```

**Parameters:**

| Parameter | Type       | Description         |
|-----------|------------|---------------------|
| `$index`  | **string** | The translation key |

**Return Value:**

Returns the index

**Throws:**

Throws exception if triggerError is enabled and translation key is not found
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### query

Queries for a translated string based on the given translate key and optional placeholders.

```php
public query(string $translateKey, array $placeholders = []): string
```

**Parameters:**

| Parameter       | Type       | Description                                                            |
|-----------------|------------|------------------------------------------------------------------------|
| `$translateKey` | **string** | The translate key to query for a translated string.                    |
| `$placeholders` | **array**  | An optional array of placeholders to replace in the translated string. |

**Return Value:**

The translated string or the not found string if the translate key is not found.

**Throws:**

Throws exception if triggerError is enabled and translation key is not found
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### toArray

Converts the translate data to an array.

```php
public toArray(): array
```

**Return Value:**

The translate data as an array.

***
