
***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\SnapshotInterface`

## Methods

### initializeSnapshot

```php
public initializeSnapshot(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setSnapshotBehavior

```php
public setSnapshotBehavior(\PhalconKit\Mvc\Model\Behavior\Snapshot $snapshotBehavior): void
```

**Parameters:**

| Parameter           | Type                                        | Description |
|---------------------|---------------------------------------------|-------------|
| `$snapshotBehavior` | **\PhalconKit\Mvc\Model\Behavior\Snapshot** |             |

***

### getSnapshotBehavior

```php
public getSnapshotBehavior(): \PhalconKit\Mvc\Model\Behavior\Snapshot
```

***

### hasChangedCallback

```php
public hasChangedCallback(callable $callback, bool $anyField = true): \Closure
```

**Parameters:**

| Parameter   | Type         | Description |
|-------------|--------------|-------------|
| `$callback` | **callable** |             |
| `$anyField` | **bool**     |             |

***
