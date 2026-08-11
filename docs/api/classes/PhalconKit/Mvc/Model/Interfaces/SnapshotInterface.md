
***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\SnapshotInterface`

## Methods

### initializeSnapshot

Initialize snapshot support for the model.

```php
public initializeSnapshot(array<string,mixed>|null $options = null): void
```

Implementations should configure Phalcon's native snapshot tracking and
attach the framework snapshot behavior. When no options are provided, the
model options manager is expected to provide the `snapshot` option group.

**Parameters:**

| Parameter  | Type                          | Description                |
|------------|-------------------------------|----------------------------|
| `$options` | **array<string,mixed>\|null** | Snapshot behavior options. |

***

### setSnapshotBehavior

Register the snapshot behavior used by this model instance.

```php
public setSnapshotBehavior(\PhalconKit\Mvc\Model\Behavior\Snapshot $snapshotBehavior): void
```

The behavior is stored in the model behavior registry under the snapshot
key so downstream code can replace or inspect it without depending on the
internal trait composition.

**Parameters:**

| Parameter           | Type                                        | Description                    |
|---------------------|---------------------------------------------|--------------------------------|
| `$snapshotBehavior` | **\PhalconKit\Mvc\Model\Behavior\Snapshot** | Behavior instance to register. |

***

### getSnapshotBehavior

Return the registered snapshot behavior.

```php
public getSnapshotBehavior(): \PhalconKit\Mvc\Model\Behavior\Snapshot
```

**Return Value:**

The behavior attached to the model snapshot key.

***

### getSnapshotChangedFields

Return model fields whose raw values differ from the stored snapshot.

```php
public getSnapshotChangedFields(array<int,string> $ignoreFields = []): list<string>
```

The result is intended for audit, replication, domain comparison, and API
response code that needs application model field names instead of mixed
database-column/native dirty-field names. Implementations should compare
raw attributes, normalize column-map names, and fall back to native
getChangedFields() only when no snapshot data exists.

**Parameters:**

| Parameter       | Type                  | Description                                                                                                                |
|-----------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------|
| `$ignoreFields` | **array<int,string>** | Database column or mapped model
field names to omit, commonly lifecycle fields such as updatedAt,
updatedBy, or updatedAs. |

**Return Value:**

Mapped model fields that differ from the snapshot.

***

### hasChangedCallback

Build a callback that recalculates a value when a model field changed.

```php
public hasChangedCallback(callable $callback, bool $anyField = true): \Closure
```

This helper is used by model behaviors that need to keep an existing raw
attribute when snapshots show the relevant value has not changed, while
still recalculating for new records or records without snapshot data.

**Parameters:**

| Parameter   | Type         | Description                                                                         |
|-------------|--------------|-------------------------------------------------------------------------------------|
| `$callback` | **callable** | Recalculation callback receiving the model and
field name.                          |
| `$anyField` | **bool**     | Whether any changed field should trigger the
callback, or only the requested field. |

**Return Value:**

Callback wrapper for behavior option definitions.

***
