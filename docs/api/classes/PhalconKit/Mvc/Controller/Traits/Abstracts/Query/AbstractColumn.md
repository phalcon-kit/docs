
Abstract contract for aggregate column selection.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractColumn`

## Methods

### initializeColumn

Initialize aggregate column configuration.

```php
public initializeColumn(): void
```

* This method is **abstract**.
***
### setColumn

Replace aggregate column configuration.

```php
public setColumn(array|\Phalcon\Support\Collection|null $column): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                                         | Description |
|-----------|----------------------------------------------|-------------|
| `$column` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getColumn

Return aggregate column configuration.

```php
public getColumn(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
