
Abstract contract for GROUP BY query configuration.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractGroup`

## Methods

### initializeGroup

Initialize group configuration.

```php
public initializeGroup(): void
```

* This method is **abstract**.
***
### setGroup

Replace group configuration.

```php
public setGroup(array|\Phalcon\Support\Collection|null $group): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                                         | Description |
|-----------|----------------------------------------------|-------------|
| `$group`  | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getGroup

Return group configuration.

```php
public getGroup(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
### defaultGroup

Return the controller's default grouping policy.

```php
public defaultGroup(): array|string|null
```

* This method is **abstract**.
***
