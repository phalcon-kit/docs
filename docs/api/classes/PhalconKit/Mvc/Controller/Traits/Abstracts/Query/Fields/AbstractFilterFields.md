
Abstract contract for fields that may appear in request filters.

A null policy keeps filtering unrestricted for backward compatibility. A
non-null collection enables allow-list mode, and an empty collection is an
explicit closed policy.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Fields\AbstractFilterFields`

## Methods

### initializeFilterFields

Initialize the filter-field policy for the current controller/action.

```php
public initializeFilterFields(): void
```

* This method is **abstract**.
***
### setFilterFields

Replace the filter-field policy.

```php
public setFilterFields(array|\Phalcon\Support\Collection|null $filterFields): void
```

* This method is **abstract**.
**Parameters:**

| Parameter       | Type                                         | Description                                                                                           |
|-----------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `$filterFields` | **array\|\Phalcon\Support\Collection\|null** | Field policy collection, null for
unrestricted filtering, or an empty collection for a closed policy. |

***
### getFilterFields

Return the configured filter-field policy.

```php
public getFilterFields(): \Phalcon\Support\Collection|null
```

* This method is **abstract**.
**Return Value:**

Field policy collection or null for unrestricted
filtering.

***
