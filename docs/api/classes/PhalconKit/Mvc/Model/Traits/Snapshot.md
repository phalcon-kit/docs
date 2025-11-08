
Trait that provides snapshot functionality for a model.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Snapshot`

## Methods

### keepSnapshots

```php
protected keepSnapshots(bool $keepSnapshot): void
```

* This method is **abstract**.
**Parameters:**

| Parameter       | Type     | Description |
|-----------------|----------|-------------|
| `$keepSnapshot` | **bool** |             |

***
### initializeSnapshot

Initialize the snapshot for the model.

```php
public initializeSnapshot(array|null $options = null): void
```

**Parameters:**

| Parameter  | Type            | Description                                                       |
|------------|-----------------|-------------------------------------------------------------------|
| `$options` | **array\|null** | An array of options for initializing the snapshot (default: null) |

***
### setSnapshotBehavior

Set the SnapshotBehavior for the model

```php
public setSnapshotBehavior(\PhalconKit\Mvc\Model\Behavior\Snapshot $snapshotBehavior): void
```

**Parameters:**

| Parameter           | Type                                        | Description                          |
|---------------------|---------------------------------------------|--------------------------------------|
| `$snapshotBehavior` | **\PhalconKit\Mvc\Model\Behavior\Snapshot** | The SnapshotBehavior instance to set |

***
### getSnapshotBehavior

Get the SnapshotBehavior instance for the model.

```php
public getSnapshotBehavior(): \PhalconKit\Mvc\Model\Behavior\Snapshot
```

**Return Value:**

The SnapshotBehavior instance.

***
### hasChangedCallback

Creates a closure that can be used as a callback to determine if a model attribute has changed.

```php
public hasChangedCallback(callable $callback, bool $anyField = true): \Closure
```

**Parameters:**

| Parameter   | Type         | Description                                                              |
|-------------|--------------|--------------------------------------------------------------------------|
| `$callback` | **callable** | The callback function to be executed if the model attribute has changed. |
| `$anyField` | **bool**     | Determines whether to check for changes in any field (default: true).    |

**Return Value:**

A closure that takes a Model instance and a field name as arguments, and returns the result of the callback
function if the attribute has changed, or the value of the attribute if it has not changed.

***
