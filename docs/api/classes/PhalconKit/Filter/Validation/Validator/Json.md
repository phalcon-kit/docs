
Validate that a field contains a syntactically valid JSON string.

The validator intentionally checks strings only. It does not accept decoded
arrays, objects, integers, or booleans, because controllers and models that
use this validator are asserting the transport/storage representation rather
than the decoded PHP value.

`json_validate()` is used instead of `json_decode()` so validation does not
allocate decoded structures just to prove syntax. The optional `depth` and
`flags` options are passed through to PHP's JSON validator.

***

* Full name: `\PhalconKit\Filter\Validation\Validator\Json`
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

Create the JSON validator.

```php
public __construct(array<string,mixed> $options = []): mixed
```

Supported options:
- `message`/`template`: native Phalcon message customization.
- `allowEmpty`: native Phalcon empty-value handling, including
  per-field maps, is honored before JSON syntax is checked.
- `depth`: maximum nesting depth passed to `json_validate()`.
- `flags`: JSON validation flags passed to `json_validate()`.

**Parameters:**

| Parameter  | Type                    | Description                                                    |
|------------|-------------------------|----------------------------------------------------------------|
| `$options` | **array<string,mixed>** | Native Phalcon validator options plus
JSON validation options. |

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

True when the value is an allowed empty value or valid JSON.

***
