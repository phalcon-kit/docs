
Abstract contract for ORDER BY query configuration.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractOrder`

## Methods

### initializeDefaultOrder

Initialize default order configuration.

```php
public initializeDefaultOrder(): void
```

* This method is **abstract**.
***
### initializeOrder

Initialize request order configuration.

```php
public initializeOrder(): void
```

* This method is **abstract**.
***
### setOrder

Replace request order configuration.

```php
public setOrder(array|\Phalcon\Support\Collection|null $order): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                                         | Description |
|-----------|----------------------------------------------|-------------|
| `$order`  | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getOrder

Return request order configuration.

```php
public getOrder(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
### setDefaultOrder

Replace default order configuration.

```php
public setDefaultOrder(array|string|null $defaultOrder): void
```

* This method is **abstract**.
**Parameters:**

| Parameter       | Type                    | Description |
|-----------------|-------------------------|-------------|
| `$defaultOrder` | **array\|string\|null** |             |

***
### getDefaultOrder

Return default order configuration.

```php
public getDefaultOrder(): array|string|null
```

* This method is **abstract**.
***
