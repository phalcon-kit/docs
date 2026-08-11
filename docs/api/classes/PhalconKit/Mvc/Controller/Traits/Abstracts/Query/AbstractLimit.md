
Abstract contract for REST query limit policy.

Implementations distinguish between a requested limit, a maximum allowed
limit, and the default values used when requests omit pagination options.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractLimit`

## Methods

### initializeLimit

Initialize the requested limit from controller parameters.

```php
public initializeLimit(): void
```

* This method is **abstract**.
***
### setLimit

Replace the requested limit.

```php
public setLimit(?int $limit): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$limit`  | **?int** |             |

***
### getLimit

Return the effective requested limit.

```php
public getLimit(): ?int
```

* This method is **abstract**.
***
### setMaxLimit

Replace the maximum allowed limit.

```php
public setMaxLimit(?int $maxLimit): void
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type     | Description |
|-------------|----------|-------------|
| `$maxLimit` | **?int** |             |

***
### getMaxLimit

Return the maximum allowed limit.

```php
public getMaxLimit(): ?int
```

* This method is **abstract**.
***
### defaultLimit

Return the default requested limit.

```php
public defaultLimit(): ?int
```

* This method is **abstract**.
***
### defaultMaxLimit

Return the default maximum allowed limit.

```php
public defaultMaxLimit(): ?int
```

* This method is **abstract**.
***
