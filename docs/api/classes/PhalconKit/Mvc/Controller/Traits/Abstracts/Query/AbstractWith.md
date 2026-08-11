
Abstract contract for eager-loading relation configuration.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractWith`

## Methods

### initializeWith

Initialize eager-loading relation configuration.

```php
public initializeWith(): void
```

* This method is **abstract**.
***
### setWith

Replace eager-loading relation configuration.

```php
public setWith(array|\Phalcon\Support\Collection|null $with): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                                         | Description |
|-----------|----------------------------------------------|-------------|
| `$with`   | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getWith

Return eager-loading relation configuration.

```php
public getWith(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
