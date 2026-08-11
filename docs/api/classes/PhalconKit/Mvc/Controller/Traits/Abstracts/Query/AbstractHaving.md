
Abstract contract for HAVING query conditions.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractHaving`

## Methods

### initializeHaving

Initialize HAVING conditions.

```php
public initializeHaving(): void
```

* This method is **abstract**.
***
### setHaving

Replace HAVING conditions.

```php
public setHaving(array|\Phalcon\Support\Collection|null $having): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                                         | Description |
|-----------|----------------------------------------------|-------------|
| `$having` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getHaving

Return HAVING conditions.

```php
public getHaving(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
