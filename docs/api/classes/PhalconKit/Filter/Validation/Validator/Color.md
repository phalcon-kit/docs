
Validate CSS-style hexadecimal color strings.

Accepted values must include the leading `#` and contain 3, 4, 6, or 8
hexadecimal digits. That covers shorthand RGB/RGBA and full RGB/RGBA forms
such as `#fff`, `#ffff`, `#ffffff`, and `#ffffffff`.

Non-string values are rejected instead of being cast. This keeps validation
strict for request payloads where a color field should not silently accept
numbers, arrays, or already-decoded structured input.

***

* Full name: `\PhalconKit\Filter\Validation\Validator\Color`
* Parent class: [`AbstractValidator`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  `ValidatorInterface`

## Properties

### template

Default validation message used when no custom message is configured.

```php
protected string $template
```

***

## Methods

### __construct

Create the color validator.

```php
public __construct(array<string,mixed> $options = []): mixed
```

Common Phalcon validator options such as `message`, `template`, and
`allowEmpty` are forwarded to the native base validator. Native
empty-value handling, including per-field maps, is honored before the
strict color check runs.

**Parameters:**

| Parameter  | Type                    | Description                       |
|------------|-------------------------|-----------------------------------|
| `$options` | **array<string,mixed>** | Native Phalcon validator options. |

***

### validate

Validate the configured field value from the Phalcon validation context.

```php
public validate(\Phalcon\Filter\Validation $validation, mixed $field): bool
```

**Parameters:**

| Parameter     | Type                           | Description                                         |
|---------------|--------------------------------|-----------------------------------------------------|
| `$validation` | **\Phalcon\Filter\Validation** | Current validation context and message
collection.  |
| `$field`      | **mixed**                      | Field name or field identifier provided by Phalcon. |

**Return Value:**

True when the value is a supported hexadecimal color.

***

### isValidColor

Check if a given color is in a valid hexadecimal format.

```php
private isValidColor(string $color): bool
```

**Parameters:**

| Parameter | Type       | Description                                |
|-----------|------------|--------------------------------------------|
| `$color`  | **string** | Candidate color including the leading `#`. |

**Return Value:**

True for 3, 4, 6, or 8 hexadecimal digits.

***
