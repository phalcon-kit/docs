
***

* Full name: `\PhalconKit\Mvc\Model\Traits\Blameable\Deleted`

## Methods

### initializeDeleted

Initializing Deleted

```php
public initializeDeleted(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***
### normalizeNullableBlameId

```php
private normalizeNullableBlameId(mixed $id): ?int
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$id`     | **mixed** |             |

***
### normalizeNullableBlameDate

```php
private normalizeNullableBlameDate(mixed $date): ?string
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$date`   | **mixed** |             |

***
### isNullBlameValue

```php
private isNullBlameValue(mixed $value): bool
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***
### setDeletedBehavior

Set Deleted Behavior

```php
public setDeletedBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $deletedBehavior): void
```

**Parameters:**

| Parameter          | Type                                             | Description |
|--------------------|--------------------------------------------------|-------------|
| `$deletedBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** |             |

***
### getDeletedBehavior

Get Deleted Behavior

```php
public getDeletedBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

***
