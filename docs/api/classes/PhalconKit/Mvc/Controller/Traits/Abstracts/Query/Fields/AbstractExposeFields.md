
Abstract contract for list/detail exposure field policies.

Exposure fields shape standard REST responses. Null preserves the current
exposer default, while a non-null collection explicitly controls which
fields or nested paths may be serialized.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Fields\AbstractExposeFields`

## Methods

### initializeExposeFields

Initialize the exposure-field policy for standard REST responses.

```php
public initializeExposeFields(): void
```

* This method is **abstract**.
***
### setExposeFields

Replace the exposure-field policy.

```php
public setExposeFields(array|\Phalcon\Support\Collection|null $exposeFields): void
```

* This method is **abstract**.
**Parameters:**

| Parameter       | Type                                         | Description                                                                                                       |
|-----------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `$exposeFields` | **array\|\Phalcon\Support\Collection\|null** | Field policy collection, null for
default exposure behavior, or an empty collection for a closed
response policy. |

***
### getExposeFields

Return the configured exposure-field policy.

```php
public getExposeFields(): \Phalcon\Support\Collection|null
```

* This method is **abstract**.
**Return Value:**

Field policy collection or null for default
exposure behavior.

***
