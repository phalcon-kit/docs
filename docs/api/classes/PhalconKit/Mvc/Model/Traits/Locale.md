
Adds locale-aware field and method fallbacks to models.

The trait lets consumers read/write logical fields such as `name` while the
model stores locale-specific columns like `nameEn` or `nameFr`. The current
locale is resolved from the model DI, so applications can switch locale
services per request while keeping the model code generic.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Locale`

## Methods

### _

Translate a key through the model's translate service.

```php
public _(string $translateKey, array<array-key,mixed> $placeholders = []): string
```

This is a model-level convenience wrapper around Phalcon's translate
adapter. It keeps model validation messages and computed labels aligned
with the same `translate` service used by the rest of the application.

**Parameters:**

| Parameter       | Type                       | Description                               |
|-----------------|----------------------------|-------------------------------------------|
| `$translateKey` | **string**                 | Translation key to resolve.               |
| `$placeholders` | **array<array-key,mixed>** | Placeholder values passed to
the adapter. |

**Return Value:**

Translated string returned by the adapter.

**Throws:**

When the translate service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### __call

Dispatch missing method calls to locale-suffixed methods when available.

```php
public __call(string $method, array<array-key,mixed> $arguments): mixed
```

For example, with locale `fr`, a call to `label()` will try `labelFr()`
before delegating to the parent model magic handler. This is intended for
computed localized accessors, not for replacing explicit public methods.

**Parameters:**

| Parameter    | Type                       | Description                                                    |
|--------------|----------------------------|----------------------------------------------------------------|
| `$method`    | **string**                 | Missing method name.                                           |
| `$arguments` | **array<array-key,mixed>** | Arguments forwarded to the
localized method or parent handler. |

**Return Value:**

Localized method result, or the parent magic-call result.

**Throws:**

When the parent Phalcon model magic handler
rejects the missing method.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When the locale service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### __set

Write missing logical properties to locale-suffixed model fields.

```php
public __set(string $property, mixed $value): void
```

For example, with locale `en`, assigning `$model->name = 'Value'` writes
to `nameEn` when that property exists on the model. If no localized field
exists, the assignment is delegated to the parent Phalcon model handler.

**Parameters:**

| Parameter   | Type       | Description                                    |
|-------------|------------|------------------------------------------------|
| `$property` | **string** | Logical property name requested by the caller. |
| `$value`    | **mixed**  | Value to write.                                |

**Throws:**

When the locale service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### __get

Read missing logical properties from locale-suffixed model fields.

```php
public __get(string $property): mixed
```

For example, with locale `en`, reading `$model->name` returns `nameEn`
when that property exists on the model. If no localized field exists, the
lookup is delegated to the parent Phalcon model handler.

**Parameters:**

| Parameter   | Type       | Description                                    |
|-------------|------------|------------------------------------------------|
| `$property` | **string** | Logical property name requested by the caller. |

**Return Value:**

Localized field value or the parent magic-get result.

**Throws:**

When the locale service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
