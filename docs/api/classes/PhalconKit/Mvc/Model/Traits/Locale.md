
This trait provides functionality to handle localization in models.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Locale`

## Methods

### _

Translate a given key using the translation service

```php
public _(string $translateKey, array $placeholders = []): string
```

**Parameters:**

| Parameter       | Type       | Description                                        |
|-----------------|------------|----------------------------------------------------|
| `$translateKey` | **string** | The key to be translated                           |
| `$placeholders` | **array**  | The placeholders to be replaced in the translation |

**Return Value:**

The translated string

***
### __call

Magic method to dynamically call localed named methods using the current locale
- Allow to call $this->methodName{Fr\|En\|Sp\|...}() from missing methodName method

```php
public __call(string $method, array $arguments): mixed|null
```

**Parameters:**

| Parameter    | Type       | Description      |
|--------------|------------|------------------|
| `$method`    | **string** | method name      |
| `$arguments` | **array**  | method arguments |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### __set

Magic setter to set localed named field automatically using the current locale
- Allow to set $this->name{Fr\|En\|Sp\|...} for missing name property

```php
public __set(string $property, mixed $value): void
```

**Parameters:**

| Parameter   | Type       | Description                      |
|-------------|------------|----------------------------------|
| `$property` | **string** | property name                    |
| `$value`    | **mixed**  | value to be set for the property |

***
### __get

Magic getter to get localed named field automatically using the current locale
- Allow to get $this->name{Fr\|En\|Sp\|...} from missing name property

```php
public __get(string $property): mixed
```

**Parameters:**

| Parameter   | Type       | Description   |
|-------------|------------|---------------|
| `$property` | **string** | property name |

***
