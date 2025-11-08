
This trait provides soft delete functionality to a model class.

It allows you to mark a record as deleted without actually deleting it from the database.
When a record is marked as deleted, it won't be retrieved in queries unless explicitly requested.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\SoftDelete`

## Properties

### skipped

```php
protected bool $skipped
```

***

## Methods

### initializeSoftDelete

Initializing SoftDelete

```php
public initializeSoftDelete(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***
### setSoftDeleteBehavior

Set the SoftDeleteBehavior variable
Attach the SoftDelete behavior class

```php
public setSoftDeleteBehavior(\PhalconKit\Mvc\Model\Behavior\SoftDelete $softDeleteBehavior): void
```

**Parameters:**

| Parameter             | Type                                          | Description |
|-----------------------|-----------------------------------------------|-------------|
| `$softDeleteBehavior` | **\PhalconKit\Mvc\Model\Behavior\SoftDelete** |             |

***
### getSoftDeleteBehavior

Return the soft delete behavior instance

```php
public getSoftDeleteBehavior(): \PhalconKit\Mvc\Model\Behavior\SoftDelete
```

***
### disableSoftDelete

Disable the soft delete for the current instance
Note: SoftDelete behavior must be attached

```php
public disableSoftDelete(): void
```

***
### enableSoftDelete

Enable the soft delete for the current instance
Note: SoftDelete behavior must be attached

```php
public enableSoftDelete(): void
```

***
### isDeleted

Helper method to check if the row is soft deleted

```php
public isDeleted(?string $field = null, ?int $deletedValue = null): bool
```

**Parameters:**

| Parameter       | Type        | Description |
|-----------------|-------------|-------------|
| `$field`        | **?string** |             |
| `$deletedValue` | **?int**    |             |

***
### restore

Restore a previously Soft-deleted entry and fire events
Events:
- beforeRestore
- notRestored
- afterRestore

```php
public restore(?string $field = null, ?int $notDeletedValue = null): bool
```

**Parameters:**

| Parameter          | Type        | Description |
|--------------------|-------------|-------------|
| `$field`           | **?string** |             |
| `$notDeletedValue` | **?int**    |             |

***
