
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
### getModelsMetaData

```php
public getModelsMetaData(): \Phalcon\Mvc\Model\MetaDataInterface
```

* This method is **abstract**.
***
### getChangedFields

```php
public getChangedFields(): array
```

* This method is **abstract**.
***
### getSnapshotData

```php
public getSnapshotData(): array
```

* This method is **abstract**.
***
### hasSnapshotData

```php
public hasSnapshotData(): bool
```

* This method is **abstract**.
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
### getSnapshotChangedFields

Return model fields whose raw values differ from the stored snapshot.

```php
public getSnapshotChangedFields(array<int,string> $ignoreFields = []): list<string>
```

Phalcon's native getChangedFields() reports the extension's current dirty
tracking state. This helper complements it for audit, domain comparison,
replication, and response-building code that needs a stable
snapshot-versus-current diff expressed with application model field names.

Snapshot arrays can be keyed by either database column names or mapped
model field names. Returned fields are normalized through the model column
map whenever metadata is available, unknown snapshot entries are ignored,
and current values are read through readAttribute() so model getters do
not format values or trigger domain side effects during comparison.

The ignore list accepts database column names and mapped model field names.
Use it for lifecycle or bookkeeping fields such as updatedAt, updatedBy,
updatedAs, or their database-column equivalents. Nullable fields preserve
PhalconKit's SQL "NULL" string convention by comparing those values as
null when metadata marks the field nullable.

When Phalcon has no snapshot for the model, the method falls back to
native getChangedFields(), still applying column-map normalization and the
ignore list. This method is intentionally not a replacement for native
dirty tracking and should not be used as the sole authorization context
for sensitive flows such as password reset or privileged account changes.

**Parameters:**

| Parameter       | Type                  | Description                                                          |
|-----------------|-----------------------|----------------------------------------------------------------------|
| `$ignoreFields` | **array<int,string>** | Database column or mapped model
field names to omit from the result. |

**Return Value:**

Mapped model field names whose snapshot value differs
from the current raw attribute value.

**Throws:**

When the trait host cannot expose Phalcon's raw
entity attribute API.
- [`LogicException`](../../../Exception/LogicException.md)

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
### getSnapshotFieldContext

Build the field metadata used to normalize snapshot keys and comparisons.

```php
private getSnapshotFieldContext(): array{columnMap: array<string,string>, databaseFields: array<string,true>|null, modelFields: array<string,true>|null, nullableFields: array<string,true>}
```

Metadata access is best-effort because callers can use model doubles or
partially bootstrapped models in tests. When metadata is unavailable the
helper keeps field names as provided, which mirrors Phalcon's native
changed-field behavior without inventing mappings.

***
### normalizeNativeChangedFields

Normalize native changed-field output through the same mapped-name rules.

```php
private normalizeNativeChangedFields(array<int,mixed> $changedFields, array<string,true> $ignoredFields, array{columnMap: array<string,string>, databaseFields: array<string,true>|null, modelFields: array<string,true>|null, nullableFields: array<string,true>} $context): list<string>
```

Native Phalcon changed fields are used only when no snapshot is available.
If metadata cannot identify a field, the original native name is kept so
the fallback remains faithful to Phalcon's own result.

**Parameters:**

| Parameter        | Type                                                                                                                                                            | Description                            |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| `$changedFields` | **array<int,mixed>**                                                                                                                                            | Native fields from getChangedFields(). |
| `$ignoredFields` | **array<string,true>**                                                                                                                                          | Normalized fields to omit.             |
| `$context`       | **array{columnMap: array<string,string>, databaseFields: array<string,true>\|null, modelFields: array<string,true>\|null, nullableFields: array<string,true>}** | Snapshot field metadata.               |

***
### normalizeSnapshotFieldName

Convert database-column snapshot keys and ignore entries to model fields.

```php
private normalizeSnapshotFieldName(string $field, array{columnMap: array<string,string>, databaseFields: array<string,true>|null, modelFields: array<string,true>|null, nullableFields: array<string,true>} $context): ?string
```

When metadata knows the model fields, unknown snapshot keys return null so
relation payloads or transient data stored alongside snapshots do not
create false changed-field results.

**Parameters:**

| Parameter  | Type                                                                                                                                                            | Description              |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| `$field`   | **string**                                                                                                                                                      |                          |
| `$context` | **array{columnMap: array<string,string>, databaseFields: array<string,true>\|null, modelFields: array<string,true>\|null, nullableFields: array<string,true>}** | Snapshot field metadata. |

***
### normalizeSnapshotIgnoredFields

Normalize ignore-list entries once so comparisons stay simple.

```php
private normalizeSnapshotIgnoredFields(array<int,string> $ignoreFields, array{columnMap: array<string,string>, databaseFields: array<string,true>|null, modelFields: array<string,true>|null, nullableFields: array<string,true>} $context): array<string,true>
```

**Parameters:**

| Parameter       | Type                                                                                                                                                            | Description                                            |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `$ignoreFields` | **array<int,string>**                                                                                                                                           | Database column or mapped model
field names to ignore. |
| `$context`      | **array{columnMap: array<string,string>, databaseFields: array<string,true>\|null, modelFields: array<string,true>\|null, nullableFields: array<string,true>}** | Snapshot field metadata.                               |

***
### normalizeSnapshotColumnMap

Normalize a Phalcon metadata column map into string keys and values.

```php
private normalizeSnapshotColumnMap(array<array-key,int|string> $columnMap): array<string,string>
```

**Parameters:**

| Parameter    | Type                             | Description              |
|--------------|----------------------------------|--------------------------|
| `$columnMap` | **array<array-key,int\|string>** | Raw metadata column map. |

**Return Value:**

Database column name to mapped model field.

***
### normalizeSnapshotComparisonValue

Normalize comparison values for nullable SQL NULL-string conventions.

```php
private normalizeSnapshotComparisonValue(string $field, mixed $value, array<string,true> $nullableFields): mixed
```

PhalconKit already converts "NULL" strings to null before persistence for
nullable attributes. The snapshot diff mirrors that rule during
comparison, without mutating the model or its snapshot arrays.

**Parameters:**

| Parameter         | Type                   | Description                          |
|-------------------|------------------------|--------------------------------------|
| `$field`          | **string**             |                                      |
| `$value`          | **mixed**              |                                      |
| `$nullableFields` | **array<string,true>** | Mapped model fields that allow null. |

***
### requireSnapshotEntity

Require the trait host to expose Phalcon's raw entity attribute API.

```php
private requireSnapshotEntity(): \Phalcon\Mvc\EntityInterface
```

Snapshot comparison intentionally avoids magic property access and domain
getters. If a downstream class composes this trait outside a Phalcon
entity, fail with a framework-scoped exception instead of a late method
error from readAttribute().

**Throws:**

When the trait host is not a Phalcon entity.
- [`LogicException`](../../../Exception/LogicException.md)

***
