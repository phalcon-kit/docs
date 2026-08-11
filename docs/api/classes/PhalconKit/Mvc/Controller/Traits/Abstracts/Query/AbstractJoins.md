
Abstract contract for configured PHQL join definitions.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractJoins`

## Methods

### initializeJoins

Initialize join definitions.

```php
public initializeJoins(): void
```

* This method is **abstract**.
***
### setJoins

Replace join definitions.

```php
public setJoins(array|\Phalcon\Support\Collection|null $joins): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                                         | Description |
|-----------|----------------------------------------------|-------------|
| `$joins`  | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getJoins

Return join definitions.

```php
public getJoins(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
