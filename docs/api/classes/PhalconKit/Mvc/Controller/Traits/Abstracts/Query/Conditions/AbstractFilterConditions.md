
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Conditions\AbstractFilterConditions`

## Methods

### initializeFilterConditions

```php
public initializeFilterConditions(): void
```

* This method is **abstract**.
***
### setFilterConditions

```php
public setFilterConditions(?\Phalcon\Support\Collection $filterConditions): void
```

* This method is **abstract**.
**Parameters:**

| Parameter           | Type                             | Description |
|---------------------|----------------------------------|-------------|
| `$filterConditions` | **?\Phalcon\Support\Collection** |             |

***
### getFilterConditions

```php
public getFilterConditions(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
### defaultFilterCondition

```php
public defaultFilterCondition(?array $filters, ?array $allowedFilters, bool $or = false): array|string|null
```

* This method is **abstract**.
**Parameters:**

| Parameter         | Type       | Description |
|-------------------|------------|-------------|
| `$filters`        | **?array** |             |
| `$allowedFilters` | **?array** |             |
| `$or`             | **bool**   |             |

***
### getFilterOperator

```php
public getFilterOperator(string $operator): string
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type       | Description |
|-------------|------------|-------------|
| `$operator` | **string** |             |

***
### getBindTypeFromRawValue

```php
public getBindTypeFromRawValue(mixed $rawValue = null): int
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type      | Description |
|-------------|-----------|-------------|
| `$rawValue` | **mixed** |             |

***
