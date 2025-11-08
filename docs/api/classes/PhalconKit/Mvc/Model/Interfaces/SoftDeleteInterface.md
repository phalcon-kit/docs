
***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\SoftDeleteInterface`

## Methods

### initializeSoftDelete

```php
public initializeSoftDelete(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setSoftDeleteBehavior

```php
public setSoftDeleteBehavior(\PhalconKit\Mvc\Model\Behavior\SoftDelete $softDeleteBehavior): void
```

**Parameters:**

| Parameter             | Type                                          | Description |
|-----------------------|-----------------------------------------------|-------------|
| `$softDeleteBehavior` | **\PhalconKit\Mvc\Model\Behavior\SoftDelete** |             |

***

### getSoftDeleteBehavior

```php
public getSoftDeleteBehavior(): \PhalconKit\Mvc\Model\Behavior\SoftDelete
```

***

### disableSoftDelete

```php
public disableSoftDelete(): void
```

***

### enableSoftDelete

```php
public enableSoftDelete(): void
```

***

### isDeleted

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

```php
public restore(?string $field = null, ?int $notDeletedValue = null): bool
```

**Parameters:**

| Parameter          | Type        | Description |
|--------------------|-------------|-------------|
| `$field`           | **?string** |             |
| `$notDeletedValue` | **?int**    |             |

***
