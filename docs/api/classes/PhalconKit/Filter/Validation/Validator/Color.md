
***

* Full name: `\PhalconKit\Filter\Validation\Validator\Color`
* Parent class: [`AbstractValidator`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  `ValidatorInterface`

## Properties

### template

```php
protected $template
```

***

## Methods

### __construct

```php
public __construct(array $options = []): mixed
```

**Parameters:**

| Parameter  | Type      | Description                                                                |
|------------|-----------|----------------------------------------------------------------------------|
| `$options` | **array** | = [
    'message' => '',
    'template' => '',
    'allowEmpty' => false
] |

***

### validate

```php
public validate(\Phalcon\Filter\Validation $validation, mixed $field): bool
```

**Parameters:**

| Parameter     | Type                           | Description |
|---------------|--------------------------------|-------------|
| `$validation` | **\Phalcon\Filter\Validation** |             |
| `$field`      | **mixed**                      |             |

***

### isValidColor

Check if a given color is in a valid hexadecimal format.

```php
private isValidColor(string $color): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$color`  | **string** |             |

***
