
Abstract contract for REST order-field policy configuration.

Order fields are separate from filter/search fields because a field can be
safe to filter while still being too expensive, unstable, or semantically
wrong to expose as a client-controlled sort key.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Fields\AbstractOrderFields`

## Methods

### initializeOrderFields

Initialize the order-field allow-list for the current request.

```php
public initializeOrderFields(): void
```

* This method is **abstract**.
***
### setOrderFields

Replace the order-field policy.

```php
public setOrderFields(array|\Phalcon\Support\Collection|null $orderFields): void
```

* This method is **abstract**.
**Parameters:**

| Parameter      | Type                                         | Description                                                                                          |
|----------------|----------------------------------------------|------------------------------------------------------------------------------------------------------|
| `$orderFields` | **array\|\Phalcon\Support\Collection\|null** | Field policy collection, null for
unrestricted ordering, or an empty collection for a closed policy. |

***
### getOrderFields

Return the configured order-field policy.

```php
public getOrderFields(): \Phalcon\Support\Collection|null
```

* This method is **abstract**.
**Return Value:**

Field policy collection or null for unrestricted
ordering.

***
### hasOrderFields

Check whether an order-field policy has been configured.

```php
public hasOrderFields(): bool
```

* This method is **abstract**.
***
### mergeOrderFields

Merge additional order-field policy entries into the current policy.

```php
public mergeOrderFields(array|\Phalcon\Support\Collection $orderFields): void
```

* This method is **abstract**.
**Parameters:**

| Parameter      | Type                                   | Description                      |
|----------------|----------------------------------------|----------------------------------|
| `$orderFields` | **array\|\Phalcon\Support\Collection** | Additional field policy entries. |

***
