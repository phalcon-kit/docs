
Abstract contract for SELECT DISTINCT configuration.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractDistinct`

## Methods

### initializeDistinct

Initialize distinct-field configuration.

```php
public initializeDistinct(): void
```

* This method is **abstract**.
***
### setDistinct

Replace distinct-field configuration.

```php
public setDistinct(array|\Phalcon\Support\Collection|null $distinct): void
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type                                         | Description |
|-------------|----------------------------------------------|-------------|
| `$distinct` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getDistinct

Return distinct-field configuration.

```php
public getDistinct(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
