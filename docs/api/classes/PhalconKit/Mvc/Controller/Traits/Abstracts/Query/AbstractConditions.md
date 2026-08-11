
Abstract contract for the composed REST query condition collections.

The concrete condition stack combines permission, soft-delete, identity,
request-filter, and search conditions into one compiler input collection.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractConditions`

## Methods

### initializeConditions

Initialize all condition collections.

```php
public initializeConditions(): void
```

* This method is **abstract**.
***
### setConditions

Replace the composed condition collection.

```php
public setConditions(array|\Phalcon\Support\Collection|null $conditions): void
```

* This method is **abstract**.
**Parameters:**

| Parameter     | Type                                         | Description |
|---------------|----------------------------------------------|-------------|
| `$conditions` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getConditions

Return the composed condition collection.

```php
public getConditions(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
