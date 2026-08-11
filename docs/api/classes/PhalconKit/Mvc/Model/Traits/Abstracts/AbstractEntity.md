
***

* Full name: `\PhalconKit\Mvc\Model\Traits\Abstracts\AbstractEntity`

## Methods

### readAttribute

Read a raw model attribute through Phalcon's native entity API.

```php
public readAttribute(string $attribute): mixed
```

Model traits use this dependency when they need the stored value without
going through magic property access. The native extension currently keeps
this method untyped at runtime, so the abstract dependency remains
signature-compatible while documenting the same mixed-value contract as
the patched Phalcon model stub.

* This method is **abstract**.
**Parameters:**

| Parameter    | Type       | Description           |
|--------------|------------|-----------------------|
| `$attribute` | **string** | Model attribute name. |

**Return Value:**

Current raw attribute value.

***
### writeAttribute

Write a raw model attribute through Phalcon's native entity API.

```php
public writeAttribute(string $attribute, mixed $value): void
```

Phalcon's runtime extension currently exposes this method without a
native return type, so the abstract dependency intentionally stays
untyped for compatibility with both the extension and patched IDE stubs.

* This method is **abstract**.
**Parameters:**

| Parameter    | Type       | Description                           |
|--------------|------------|---------------------------------------|
| `$attribute` | **string** | Model attribute name.                 |
| `$value`     | **mixed**  | Value to assign to the raw attribute. |

***
