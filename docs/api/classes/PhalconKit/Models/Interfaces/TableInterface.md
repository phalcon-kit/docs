
***

* Full name: `\PhalconKit\Models\Interfaces\TableInterface`
* Parent interfaces:
  [`\PhalconKit\Models\Abstracts\Interfaces\TableAbstractInterface`](../Abstracts/Interfaces/TableAbstractInterface.md)

## Inherited methods

### genericValidation

```php
public genericValidation(?\PhalconKit\Filter\Validation $validator = null): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter    | Type                               | Description |
|--------------|------------------------------------|-------------|
| `$validator` | **?\PhalconKit\Filter\Validation** |             |

***

### addNotEmptyValidation

```php
public addNotEmptyValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = false): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$allowEmpty` | **bool**                          |             |

***

### addPresenceValidation

```php
public addPresenceValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$allowEmpty` | **bool**                          |             |

***

### addUnsignedIntValidation

```php
public addUnsignedIntValidation(\PhalconKit\Filter\Validation $validator, array|string $field = 'id', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$allowEmpty` | **bool**                          |             |

***

### addUnsignedBigIntValidation

```php
public addUnsignedBigIntValidation(\PhalconKit\Filter\Validation $validator, array|string $field = 'id', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$allowEmpty` | **bool**                          |             |

***

### addNumberValidation

```php
public addNumberValidation(\PhalconKit\Filter\Validation $validator, array|string $field, int $min, int $max, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$min`        | **int**                           |             |
| `$max`        | **int**                           |             |
| `$allowEmpty` | **bool**                          |             |

***

### addStringLengthValidation

```php
public addStringLengthValidation(\PhalconKit\Filter\Validation $validator, array|string $field, int $minChar = 0, int $maxChar = 255, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$minChar`    | **int**                           |             |
| `$maxChar`    | **int**                           |             |
| `$allowEmpty` | **bool**                          |             |

***

### addInclusionInValidation

```php
public addInclusionInValidation(\PhalconKit\Filter\Validation $validator, array|string $field, array $domainList = [], bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$domainList` | **array**                         |             |
| `$allowEmpty` | **bool**                          |             |

***

### addBooleanValidation

```php
public addBooleanValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$allowEmpty` | **bool**                          |             |

***

### addInclusionValidation

```php
public addInclusionValidation(\PhalconKit\Filter\Validation $validator, array|string $field, array $domain = [], bool $allowEmpty = true, bool $strict = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$domain`     | **array**                         |             |
| `$allowEmpty` | **bool**                          |             |
| `$strict`     | **bool**                          |             |

***

### addUniquenessValidation

```php
public addUniquenessValidation(\PhalconKit\Filter\Validation $validator, string|array $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **string\|array**                 |             |
| `$allowEmpty` | **bool**                          |             |

***

### addEmailValidation

```php
public addEmailValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$allowEmpty` | **bool**                          |             |

***

### addDateValidation

```php
public addDateValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true, string $format = \PhalconKit\Db\Column::DATE_FORMAT): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$allowEmpty` | **bool**                          |             |
| `$format`     | **string**                        |             |

***

### addDateTimeValidation

```php
public addDateTimeValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true, string $format = \PhalconKit\Db\Column::DATETIME_FORMAT): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$allowEmpty` | **bool**                          |             |
| `$format`     | **string**                        |             |

***

### addJsonValidation

```php
public addJsonValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true, int $depth = 512, int $flags = 0): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$allowEmpty` | **bool**                          |             |
| `$depth`      | **int**                           |             |
| `$flags`      | **int**                           |             |

***

### addColorValidation

```php
public addColorValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **array\|string**                 |             |
| `$allowEmpty` | **bool**                          |             |

***

### addIdValidation

```php
public addIdValidation(\PhalconKit\Filter\Validation $validator, string $field = 'id'): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter    | Type                              | Description |
|--------------|-----------------------------------|-------------|
| `$validator` | **\PhalconKit\Filter\Validation** |             |
| `$field`     | **string**                        |             |

***

### addPositionValidation

```php
public addPositionValidation(\PhalconKit\Filter\Validation $validator, string $field = 'position', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **string**                        |             |
| `$allowEmpty` | **bool**                          |             |

***

### addSoftDeleteValidation

```php
public addSoftDeleteValidation(\PhalconKit\Filter\Validation $validator, string $field = 'deleted', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **string**                        |             |
| `$allowEmpty` | **bool**                          |             |

***

### addUuidValidation

```php
public addUuidValidation(\PhalconKit\Filter\Validation $validator, string $field = 'uuid', bool $allowEmpty = false): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description |
|---------------|-----------------------------------|-------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |             |
| `$field`      | **string**                        |             |
| `$allowEmpty` | **bool**                          |             |

***

### addCrudValidation

```php
public addCrudValidation(\PhalconKit\Filter\Validation $validator, string $userIdField, string $dateField, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter      | Type                              | Description |
|----------------|-----------------------------------|-------------|
| `$validator`   | **\PhalconKit\Filter\Validation** |             |
| `$userIdField` | **string**                        |             |
| `$dateField`   | **string**                        |             |
| `$allowEmpty`  | **bool**                          |             |

***

### addCreatedValidation

```php
public addCreatedValidation(\PhalconKit\Filter\Validation $validator, string $createdByField = 'createdBy', string $createdAtField = 'createdAt', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter         | Type                              | Description |
|-------------------|-----------------------------------|-------------|
| `$validator`      | **\PhalconKit\Filter\Validation** |             |
| `$createdByField` | **string**                        |             |
| `$createdAtField` | **string**                        |             |
| `$allowEmpty`     | **bool**                          |             |

***

### addUpdatedValidation

```php
public addUpdatedValidation(\PhalconKit\Filter\Validation $validator, string $updatedByField = 'updatedBy', string $updatedAtField = 'updatedAt', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter         | Type                              | Description |
|-------------------|-----------------------------------|-------------|
| `$validator`      | **\PhalconKit\Filter\Validation** |             |
| `$updatedByField` | **string**                        |             |
| `$updatedAtField` | **string**                        |             |
| `$allowEmpty`     | **bool**                          |             |

***

### addDeletedValidation

```php
public addDeletedValidation(\PhalconKit\Filter\Validation $validator, string $deletedField = 'deletedBy', string $dateField = 'deletedAt', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter       | Type                              | Description |
|-----------------|-----------------------------------|-------------|
| `$validator`    | **\PhalconKit\Filter\Validation** |             |
| `$deletedField` | **string**                        |             |
| `$dateField`    | **string**                        |             |
| `$allowEmpty`   | **bool**                          |             |

***

### addRestoredValidation

```php
public addRestoredValidation(\PhalconKit\Filter\Validation $validator, string $restoredByField = 'restoredBy', string $restoredAtField = 'restoredAt', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter          | Type                              | Description |
|--------------------|-----------------------------------|-------------|
| `$validator`       | **\PhalconKit\Filter\Validation** |             |
| `$restoredByField` | **string**                        |             |
| `$restoredAtField` | **string**                        |             |
| `$allowEmpty`      | **bool**                          |             |

***

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

### initializeSlug

```php
public initializeSlug(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setSlugBehavior

```php
public setSlugBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $slugBehavior): void
```

**Parameters:**

| Parameter       | Type                                             | Description |
|-----------------|--------------------------------------------------|-------------|
| `$slugBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** |             |

***

### getSlugBehavior

```php
public getSlugBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

***

### initializeSecurity

```php
public initializeSecurity(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setSecurityBehavior

```php
public setSecurityBehavior(\PhalconKit\Mvc\Model\Behavior\Security $securityBehavior): void
```

**Parameters:**

| Parameter           | Type                                        | Description |
|---------------------|---------------------------------------------|-------------|
| `$securityBehavior` | **\PhalconKit\Mvc\Model\Behavior\Security** |             |

***

### getSecurityBehavior

```php
public getSecurityBehavior(): \PhalconKit\Mvc\Model\Behavior\Security
```

***

### getReplicationLag

```php
public static getReplicationLag(): ?int
```

* This method is **static**.
***

### setReplicationLag

```php
public static setReplicationLag(?int $replicationLag = null): void
```

* This method is **static**.
**Parameters:**

| Parameter         | Type     | Description |
|-------------------|----------|-------------|
| `$replicationLag` | **?int** |             |

***

### getReplicationReadyAt

```php
public static getReplicationReadyAt(): ?int
```

* This method is **static**.
***

### setReplicationReadyAt

```php
public static setReplicationReadyAt(?int $replicationReadyAt = null): void
```

* This method is **static**.
**Parameters:**

| Parameter             | Type     | Description |
|-----------------------|----------|-------------|
| `$replicationReadyAt` | **?int** |             |

***

### initializeReplication

```php
public initializeReplication(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### selectReadConnection

```php
public selectReadConnection(): \Phalcon\Contracts\Db\Adapter\Adapter
```

***

### addReadWriteConnectionBehavior

```php
public addReadWriteConnectionBehavior(): void
```

***

### isReplicationReady

```php
public isReplicationReady(): bool
```

***

### setStrictRelatedAssignment

Enable or disable strict validation for relationship payloads.

```php
public setStrictRelatedAssignment(bool $strictRelatedAssignment): void
```

Strict mode is intentionally opt-in because `assignRelated()` receives the
full model assignment payload, including scalar model columns. When
enabled, relation-specific mistakes such as non-whitelisted relation
aliases, unknown complex relation payloads, and unsupported payload types
throw PhalconKit exceptions while normal scalar field assignment remains
delegated to Phalcon.

**Parameters:**

| Parameter                  | Type     | Description |
|----------------------------|----------|-------------|
| `$strictRelatedAssignment` | **bool** |             |

***

### isStrictRelatedAssignment

Check whether strict relationship assignment is enabled.

```php
public isStrictRelatedAssignment(): bool
```

**Return Value:**

True when relation payload mistakes should throw exceptions
instead of using the legacy skip/ignore behavior.

***

### setRelationshipOptions

Replace the relationship behavior option group.

```php
public setRelationshipOptions(array $options): void
```

Supported options include:
 - `enforceDirectOwnership`: reject `HAS_ONE`/`HAS_MANY` records that
   already belong to another parent before the relation save rewrites
   their foreign key.
 - `allowUnownedDirectRelationAdoption`: when ownership enforcement is
   enabled, allow direct child records with empty relationship keys to be
   attached to the current parent.
 - `autoRestoreDirectRelations`: restore owned soft-deleted
   `HAS_ONE`/`HAS_MANY` children during relationship save.

Callers may also provide an optional `aliases` array whose keys are
relationship aliases and whose values override these same options for
that alias only.

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$options` | **array** |             |

***

### getRelationshipOptions

Return merged relationship options.

```php
public getRelationshipOptions(?string $alias = null): array
```

Passing an alias applies any configured per-alias override on top of the
global relationship options. The returned array contains only behavior
option keys, not the raw override map.

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$alias`  | **?string** |             |

***

### getRelationshipOption

Return one merged relationship option.

```php
public getRelationshipOption(string $option, string|null $alias = null, mixed $default = null): mixed
```

**Parameters:**

| Parameter  | Type             | Description                                          |
|------------|------------------|------------------------------------------------------|
| `$option`  | **string**       | Relationship option key.                             |
| `$alias`   | **string\|null** | Optional relationship alias for per-alias
overrides. |
| `$default` | **mixed**        | Value returned when the option is unknown.           |

***

### setKeepMissingRelated

Replace keep-missing behavior for related aliases.

```php
public setKeepMissingRelated(array<string,bool> $keepMissingRelated): void
```

Aliases are normalized case-insensitively. A false value means a
submitted authoritative relationship list should delete missing existing
children or intermediate nodes during save.

**Parameters:**

| Parameter             | Type                   | Description                                     |
|-----------------------|------------------------|-------------------------------------------------|
| `$keepMissingRelated` | **array<string,bool>** | Keep-missing flags keyed
by relationship alias. |

***

### getKeepMissingRelated

Return keep-missing behavior keyed by normalized relationship alias.

```php
public getKeepMissingRelated(): array<string,bool>
```

***

### getKeepMissingRelatedAlias

Return whether missing records should be kept for one alias.

```php
public getKeepMissingRelatedAlias(string $alias): bool
```

Unknown aliases default to true for legacy append/merge behavior.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### setKeepMissingRelatedAlias

Set keep-missing behavior for one relationship alias.

```php
public setKeepMissingRelatedAlias(string $alias, bool $keepMissing): void
```

**Parameters:**

| Parameter      | Type       | Description |
|----------------|------------|-------------|
| `$alias`       | **string** |             |
| `$keepMissing` | **bool**   |             |

***

### getRelationshipContext

Return the current nested relationship context used for messages.

```php
public getRelationshipContext(): string
```

***

### setRelationshipContext

Set the current nested relationship context used for messages.

```php
public setRelationshipContext(string $context): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$context` | **string** |             |

***

### getDirtyRelated

Return relationships assigned for persistence with the model.

```php
public getDirtyRelated(): array<string,mixed>
```

***

### setDirtyRelated

Replace relationships assigned for persistence with the model.

```php
public setDirtyRelated(array<string,mixed> $dirtyRelated): void
```

Aliases are normalized case-insensitively.

**Parameters:**

| Parameter       | Type                    | Description                                       |
|-----------------|-------------------------|---------------------------------------------------|
| `$dirtyRelated` | **array<string,mixed>** | Dirty related values keyed by
relationship alias. |

***

### getDirtyRelatedAlias

Return one dirty relationship value by alias.

```php
public getDirtyRelatedAlias(string $alias): mixed
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### setDirtyRelatedAlias

Store one dirty relationship value by alias.

```php
public setDirtyRelatedAlias(string $alias, mixed $value): void
```

Implementations also mirror the value to a declared relation property
when the model defines one.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |
| `$value`  | **mixed**  |             |

***

### hasDirtyRelated

Return whether any dirty relationship is pending save.

```php
public hasDirtyRelated(): bool
```

***

### hasDirtyRelatedAlias

Return whether a dirty relationship exists for one alias.

```php
public hasDirtyRelatedAlias(string $alias): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### getLoadedRelated

Return eager-loaded relationship values attached for read/export only.

```php
public getLoadedRelated(): array<string,mixed>
```

***

### setLoadedRelated

Replace eager-loaded relationship values attached for read/export only.

```php
public setLoadedRelated(array<string,mixed> $loadedRelated): void
```

**Parameters:**

| Parameter        | Type                    | Description                                        |
|------------------|-------------------------|----------------------------------------------------|
| `$loadedRelated` | **array<string,mixed>** | Loaded related values keyed by
relationship alias. |

***

### getLoadedRelatedAlias

Return one eager-loaded relationship value by alias.

```php
public getLoadedRelatedAlias(string $alias): mixed
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### setLoadedRelatedAlias

Store one eager-loaded relationship value by alias.

```php
public setLoadedRelatedAlias(string $alias, mixed $value): void
```

Implementations also mirror the value to a declared relation property
when the model defines one.

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |
| `$value`  | **mixed**  |             |

***

### hasLoadedRelatedAlias

Return whether an eager-loaded relationship exists for one alias.

```php
public hasLoadedRelatedAlias(string $alias): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### assignRelated

Assign nested relationship payloads and leave scalar fields to Phalcon.

```php
public assignRelated(array<string,mixed> $data, array|null $whiteList = null, array|null $dataColumnMap = null): \Phalcon\Mvc\ModelInterface
```

Known relation aliases can receive model instances, arrays, traversables,
scalar primary-key values, or list payloads. `$whiteList` and
`$dataColumnMap` follow Phalcon assignment conventions and can include
nested relation-specific field policies.

**Parameters:**

| Parameter        | Type                    | Description                           |
|------------------|-------------------------|---------------------------------------|
| `$data`          | **array<string,mixed>** | Assignment payload.                   |
| `$whiteList`     | **array\|null**         | Optional scalar/relation whitelist.   |
| `$dataColumnMap` | **array\|null**         | Optional external-to-model field map. |

**Return Value:**

The assigned model instance.

***

### postSaveRelatedRecordsAfter

Save non-through related records after the parent model is saved.

```php
public postSaveRelatedRecordsAfter(\Phalcon\Mvc\Model\RelationInterface $relation, array<int,\Phalcon\Mvc\ModelInterface> $relatedRecords, \Phalcon\Support\Collection\CollectionInterface $visited): bool|null
```

Implementations copy parent relationship keys into each child and then
save each child through Phalcon's visited graph.

**Parameters:**

| Parameter         | Type                                                | Description                                |
|-------------------|-----------------------------------------------------|--------------------------------------------|
| `$relation`       | **\Phalcon\Mvc\Model\RelationInterface**            | Relation metadata being saved.             |
| `$relatedRecords` | **array<int,\Phalcon\Mvc\ModelInterface>**          | Related records to save.                   |
| `$visited`        | **\Phalcon\Support\Collection\CollectionInterface** | Phalcon visited graph for recursive
saves. |

**Return Value:**

False on failure, true on success, or null when the
relation is a through relation.

***

### postSaveRelatedThroughAfter

Save through-relation target and intermediate records after parent save.

```php
public postSaveRelatedThroughAfter(\Phalcon\Mvc\Model\RelationInterface $relation, array<int,\Phalcon\Mvc\ModelInterface> $relatedRecords, \Phalcon\Support\Collection\CollectionInterface $visited): bool|null
```

Implementations save target records first and then create/update the
intermediate relationship node that points back to the parent.

**Parameters:**

| Parameter         | Type                                                | Description                                |
|-------------------|-----------------------------------------------------|--------------------------------------------|
| `$relation`       | **\Phalcon\Mvc\Model\RelationInterface**            | Through relation metadata being saved.     |
| `$relatedRecords` | **array<int,\Phalcon\Mvc\ModelInterface>**          | Related target records.                    |
| `$visited`        | **\Phalcon\Support\Collection\CollectionInterface** | Phalcon visited graph for recursive
saves. |

**Return Value:**

False on failure, true on success, or null when the
relation is not a through relation.

***

### findFirstByPrimaryKeys

Find one model row using the complete primary-key payload.

```php
public findFirstByPrimaryKeys(array<string,mixed> $data, class-string|null $modelClass): \Phalcon\Mvc\ModelInterface|\Phalcon\Mvc\Model\Row|null
```

**Parameters:**

| Parameter     | Type                    | Description                                                          |
|---------------|-------------------------|----------------------------------------------------------------------|
| `$data`       | **array<string,mixed>** | Data that may contain primary-key
values.                            |
| `$modelClass` | **class-string\|null**  | Model class to query, or the current
implementation class when null. |

***

### getEntityFromData

Resolve, create, and assign a related entity from array data.

```php
public getEntityFromData(array<string,mixed> $data, array<string,mixed> $configuration = []): \Phalcon\Mvc\ModelInterface|\Phalcon\Mvc\Model\Row|null
```

Implementations first try primary-key lookup, then relation-key lookup,
then instantiate a new related model when no existing entity is found.

**Parameters:**

| Parameter        | Type                    | Description                   |
|------------------|-------------------------|-------------------------------|
| `$data`          | **array<string,mixed>** | Related entity data.          |
| `$configuration` | **array<string,mixed>** | Relation assignment metadata. |

***

### appendMessages

Append messages to the current model with relationship metadata.

```php
public appendMessages(\Phalcon\Messages\Message[] $messages = [], string|null $context = null, int|null $index = 0): void
```

**Parameters:**

| Parameter   | Type                            | Description                      |
|-------------|---------------------------------|----------------------------------|
| `$messages` | **\Phalcon\Messages\Message[]** | Messages to append.              |
| `$context`  | **string\|null**                | Relationship context to prepend. |
| `$index`    | **int\|null**                   | Optional list index to prepend.  |

***

### appendMessagesFromRecord

Append validation/save messages from one related record.

```php
public appendMessagesFromRecord(?\Phalcon\Mvc\ModelInterface $record = null, ?string $context = null, ?int $index = 0): void
```

**Parameters:**

| Parameter  | Type                             | Description |
|------------|----------------------------------|-------------|
| `$record`  | **?\Phalcon\Mvc\ModelInterface** |             |
| `$context` | **?string**                      |             |
| `$index`   | **?int**                         |             |

***

### appendMessagesFromResultset

Append validation/save messages from a related resultset.

```php
public appendMessagesFromResultset(?\Phalcon\Mvc\Model\ResultsetInterface $resultset = null, ?string $context = null, ?int $index = 0): void
```

**Parameters:**

| Parameter    | Type                                       | Description |
|--------------|--------------------------------------------|-------------|
| `$resultset` | **?\Phalcon\Mvc\Model\ResultsetInterface** |             |
| `$context`   | **?string**                                |             |
| `$index`     | **?int**                                   |             |

***

### appendMessagesFromRecordList

Append validation/save messages from an iterable related record list.

```php
public appendMessagesFromRecordList(?iterable $recordList = null, ?string $context = null, ?int $index = 0): void
```

**Parameters:**

| Parameter     | Type          | Description |
|---------------|---------------|-------------|
| `$recordList` | **?iterable** |             |
| `$context`    | **?string**   |             |
| `$index`      | **?int**      |             |

***

### rebuildMessageContext

Build a nested message context from an existing message and new context.

```php
public rebuildMessageContext(\Phalcon\Messages\Message $message, string $context): ?string
```

**Parameters:**

| Parameter  | Type                          | Description |
|------------|-------------------------------|-------------|
| `$message` | **\Phalcon\Messages\Message** |             |
| `$context` | **string**                    |             |

***

### rebuildMessageIndex

Build a nested message index from an existing message and new index.

```php
public rebuildMessageIndex(\Phalcon\Messages\Message $message, ?int $index): ?string
```

**Parameters:**

| Parameter  | Type                          | Description |
|------------|-------------------------------|-------------|
| `$message` | **\Phalcon\Messages\Message** |             |
| `$index`   | **?int**                      |             |

***

### relatedToArray

Export loaded and dirty related records to arrays.

```php
public relatedToArray(array|null $columns = null, bool $useGetter = true): array<string,mixed>
```

**Parameters:**

| Parameter    | Type            | Description                                           |
|--------------|-----------------|-------------------------------------------------------|
| `$columns`   | **array\|null** | Optional column selection map.                        |
| `$useGetter` | **bool**        | Whether related model `toArray()` should use
getters. |

***

### initializePosition

```php
public initializePosition(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setPositionBehavior

```php
public setPositionBehavior(\PhalconKit\Mvc\Model\Behavior\Position $positionBehavior): void
```

**Parameters:**

| Parameter           | Type                                        | Description |
|---------------------|---------------------------------------------|-------------|
| `$positionBehavior` | **\PhalconKit\Mvc\Model\Behavior\Position** |             |

***

### getPositionBehavior

```php
public getPositionBehavior(): \PhalconKit\Mvc\Model\Behavior\Position
```

***

### reorder

```php
public reorder(?int $position = null, ?string $positionField = null): bool
```

**Parameters:**

| Parameter        | Type        | Description |
|------------------|-------------|-------------|
| `$position`      | **?int**    |             |
| `$positionField` | **?string** |             |

***

### initializeOptions

```php
public initializeOptions(): void
```

***

### getOptionsManager

```php
public getOptionsManager(): \PhalconKit\Support\Options\ManagerInterface
```

***

### setOptionsManager

```php
public setOptionsManager(\PhalconKit\Support\Options\ManagerInterface $optionsManager): void
```

**Parameters:**

| Parameter         | Type                                             | Description |
|-------------------|--------------------------------------------------|-------------|
| `$optionsManager` | **\PhalconKit\Support\Options\ManagerInterface** |             |

***

### getColumnMap

```php
public getColumnMap(): ?array
```

***

### getPrimaryKeys

```php
public getPrimaryKeys(): array
```

***

### getPrimaryKeysValues

```php
public getPrimaryKeysValues(): array
```

***

### _

```php
public _(string $translateKey, array $placeholders = []): string
```

**Parameters:**

| Parameter       | Type       | Description |
|-----------------|------------|-------------|
| `$translateKey` | **string** |             |
| `$placeholders` | **array**  |             |

***

### __call

```php
public __call(string $method, array $arguments): mixed
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$method`    | **string** |             |
| `$arguments` | **array**  |             |

***

### __set

```php
public __set(string $property, mixed $value): void
```

**Parameters:**

| Parameter   | Type       | Description |
|-------------|------------|-------------|
| `$property` | **string** |             |
| `$value`    | **mixed**  |             |

***

### __get

```php
public __get(string $property): mixed
```

**Parameters:**

| Parameter   | Type       | Description |
|-------------|------------|-------------|
| `$property` | **string** |             |

***

### jsonEncode

```php
public jsonEncode(mixed $value, int $flags = \PhalconKit\Mvc\Model\Interfaces\JSON_UNESCAPED_SLASHES, int $depth = 512): string|false
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |
| `$flags`  | **int**   |             |
| `$depth`  | **int**   |             |

***

### jsonDecode

```php
public jsonDecode(string $json, ?bool $associative = null, int $depth = 512, int $flags = 0): mixed
```

**Parameters:**

| Parameter      | Type       | Description |
|----------------|------------|-------------|
| `$json`        | **string** |             |
| `$associative` | **?bool**  |             |
| `$depth`       | **int**    |             |
| `$flags`       | **int**    |             |

***

### loadInstance

```php
public static loadInstance(): static
```

* This method is **static**.
***

### getIdentityService

Resolve the identity manager used by model identity helpers.

```php
public getIdentityService(): \PhalconKit\Identity\ManagerInterface
```

Implementations should resolve the service from the model DI and surface
missing or incompatible services as a PhalconKit service exception.

**Return Value:**

Identity manager used by the model helpers.

**Throws:**

When the service cannot be
resolved or does not implement the expected contract.
- [`ServiceException`](../../Exception/ServiceException.md)

***

### isLoggedIn

Check whether the primary or delegated identity is authenticated.

```php
public isLoggedIn(bool $as = false): bool
```

**Parameters:**

| Parameter | Type     | Description                                                                              |
|-----------|----------|------------------------------------------------------------------------------------------|
| `$as`     | **bool** | When true, checks delegated/impersonated identity state
instead of the primary identity. |

**Return Value:**

True when the selected identity is logged in.

**Throws:**

When the identity service
cannot be resolved by the implementation.
- [`ServiceException`](../../Exception/ServiceException.md)

***

### isLoggedInAs

Check whether a delegated/impersonated identity is active.

```php
public isLoggedInAs(): bool
```

**Return Value:**

True when the current identity is acting as another user.

**Throws:**

When the identity service
cannot be resolved by the implementation.
- [`ServiceException`](../../Exception/ServiceException.md)

***

### getCurrentUser

Return the current primary or delegated user.

```php
public getCurrentUser(bool $as = false): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type     | Description                                         |
|-----------|----------|-----------------------------------------------------|
| `$as`     | **bool** | When true, returns the delegated/impersonated user. |

**Return Value:**

Matching user model, or null when unavailable.

**Throws:**

When the identity service
cannot be resolved by the implementation.
- [`ServiceException`](../../Exception/ServiceException.md)

***

### getCurrentUserAs

Return the delegated/impersonated user model.

```php
public getCurrentUserAs(): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Return Value:**

Delegated user, or null when no delegated
identity is active.

**Throws:**

When the identity service
cannot be resolved by the implementation.
- [`ServiceException`](../../Exception/ServiceException.md)

***

### getCurrentUserId

Return the current primary or delegated user ID.

```php
public getCurrentUserId(bool $as = false): int|null
```

**Parameters:**

| Parameter | Type     | Description                                            |
|-----------|----------|--------------------------------------------------------|
| `$as`     | **bool** | When true, returns the delegated/impersonated user ID. |

**Return Value:**

User ID, or null when no matching user is available.

**Throws:**

When the identity service
cannot be resolved by the implementation.
- [`ServiceException`](../../Exception/ServiceException.md)

***

### getCurrentUserIdCallback

Build a deferred callback for resolving the current user ID.

```php
public getCurrentUserIdCallback(bool $as = false): callable
```

Behaviors use this to evaluate identity state during model lifecycle
events instead of capturing a stale ID at initialization time.

**Parameters:**

| Parameter | Type     | Description                                             |
|-----------|----------|---------------------------------------------------------|
| `$as`     | **bool** | When true, the callback resolves the delegated user ID. |

**Return Value:**

Callback returning the selected user ID.

***

### hash

```php
public hash(string $string, ?string $salt = null, ?string $workFactor = null): string
```

**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$string`     | **string**  |             |
| `$salt`       | **?string** |             |
| `$workFactor` | **?string** |             |

***

### checkHash

```php
public checkHash(?string $hash = null, ?string $string = null, int $maxPassLength = 0): bool
```

**Parameters:**

| Parameter        | Type        | Description |
|------------------|-------------|-------------|
| `$hash`          | **?string** |             |
| `$string`        | **?string** |             |
| `$maxPassLength` | **int**     |             |

***

### expose

```php
public expose(?array $columns = null, ?bool $expose = null, ?bool $protected = null): array
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$columns`   | **?array** |             |
| `$expose`    | **?bool**  |             |
| `$protected` | **?bool**  |             |

***

### findWith

```php
public static findWith(array $arguments): array
```

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***

### findFirstWith

```php
public static findFirstWith(array $arguments): ?\Phalcon\Mvc\ModelInterface
```

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***

### with

```php
public static with(array $arguments): array
```

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***

### firstWith

```php
public static firstWith(array $arguments): ?\Phalcon\Mvc\ModelInterface
```

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***

### load

```php
public load(array $arguments): ?\Phalcon\Mvc\ModelInterface
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***

### getParametersFromArguments

```php
public static getParametersFromArguments(array& $arguments): mixed
```

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***

### initializeUpdated

```php
public initializeUpdated(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setUpdatedBehavior

```php
public setUpdatedBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $updatedBehavior): void
```

**Parameters:**

| Parameter          | Type                                             | Description |
|--------------------|--------------------------------------------------|-------------|
| `$updatedBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** |             |

***

### getUpdatedBehavior

```php
public getUpdatedBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

***

### initializeRestored

```php
public initializeRestored(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setRestoredBehavior

```php
public setRestoredBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $restoredBehavior): void
```

**Parameters:**

| Parameter           | Type                                             | Description |
|---------------------|--------------------------------------------------|-------------|
| `$restoredBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** |             |

***

### getRestoredBehavior

```php
public getRestoredBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

***

### initializeDeleted

```php
public initializeDeleted(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setDeletedBehavior

```php
public setDeletedBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $deletedBehavior): void
```

**Parameters:**

| Parameter          | Type                                             | Description |
|--------------------|--------------------------------------------------|-------------|
| `$deletedBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** |             |

***

### getDeletedBehavior

```php
public getDeletedBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

***

### initializeCreated

```php
public initializeCreated(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setCreatedBehavior

```php
public setCreatedBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $createdBehavior): void
```

**Parameters:**

| Parameter          | Type                                             | Description |
|--------------------|--------------------------------------------------|-------------|
| `$createdBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** |             |

***

### getCreatedBehavior

```php
public getCreatedBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

***

### getDateCallback

```php
public getDateCallback(string $format, ?int $timestamp = null): \Closure
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$format`    | **string** |             |
| `$timestamp` | **?int**   |             |

***

### initializeBlameable

```php
public initializeBlameable(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### setBlameableBehavior

```php
public setBlameableBehavior(\PhalconKit\Mvc\Model\Behavior\Blameable $blameableBehavior): void
```

**Parameters:**

| Parameter            | Type                                         | Description |
|----------------------|----------------------------------------------|-------------|
| `$blameableBehavior` | **\PhalconKit\Mvc\Model\Behavior\Blameable** |             |

***

### getBlameableBehavior

```php
public getBlameableBehavior(): \PhalconKit\Mvc\Model\Behavior\Blameable
```

***

### addUserRelationship

```php
public addUserRelationship(string $field = 'userId', string $alias = 'UserEntity', array $params = [], string $ref = 'id', string $type = 'belongsTo', ?string $class = null): ?\Phalcon\Mvc\Model\Relation
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$field`  | **string**  |             |
| `$alias`  | **string**  |             |
| `$params` | **array**   |             |
| `$ref`    | **string**  |             |
| `$type`   | **string**  |             |
| `$class`  | **?string** |             |

***

### addBehavior

```php
public addBehavior(\Phalcon\Mvc\Model\BehaviorInterface $behavior): void
```

**Parameters:**

| Parameter   | Type                                     | Description |
|-------------|------------------------------------------|-------------|
| `$behavior` | **\Phalcon\Mvc\Model\BehaviorInterface** |             |

***

### getBehavior

```php
public getBehavior(string $behaviorName): ?\Phalcon\Mvc\Model\BehaviorInterface
```

**Parameters:**

| Parameter       | Type       | Description |
|-----------------|------------|-------------|
| `$behaviorName` | **string** |             |

***

### setBehavior

```php
public setBehavior(string $behaviorName, \Phalcon\Mvc\Model\BehaviorInterface $behavior): void
```

**Parameters:**

| Parameter       | Type                                     | Description |
|-----------------|------------------------------------------|-------------|
| `$behaviorName` | **string**                               |             |
| `$behavior`     | **\Phalcon\Mvc\Model\BehaviorInterface** |             |

***

### hasBehavior

```php
public hasBehavior(string $behaviorName): bool
```

**Parameters:**

| Parameter       | Type       | Description |
|-----------------|------------|-------------|
| `$behaviorName` | **string** |             |

***

### removeBehavior

```php
public removeBehavior(string $behaviorName): void
```

**Parameters:**

| Parameter       | Type       | Description |
|-----------------|------------|-------------|
| `$behaviorName` | **string** |             |

***

### getAttribute

```php
public getAttribute(string $attribute): mixed
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$attribute` | **string** |             |

***

### setAttribute

```php
public setAttribute(string $attribute, mixed $value): void
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$attribute` | **string** |             |
| `$value`     | **mixed**  |             |

***

### getId

Returns the value of the field "id"
Column: id
Attributes: First \| Primary \| NotNull \| Numeric \| Unsigned \| AutoIncrement \| Size(1) \| Type(14)

```php
public getId(): mixed
```

***

### setId

Sets the value of the field "id"
Column: id
Attributes: First \| Primary \| NotNull \| Numeric \| Unsigned \| AutoIncrement \| Size(1) \| Type(14)

```php
public setId(mixed $id): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$id`     | **mixed** |             |

***

### getUuid

Returns the value of the field "uuid"
Column: uuid
Attributes: NotNull \| Size(36) \| Type(5)

```php
public getUuid(): mixed
```

***

### setUuid

Sets the value of the field "uuid"
Column: uuid
Attributes: NotNull \| Size(36) \| Type(5)

```php
public setUuid(mixed $uuid): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$uuid`   | **mixed** |             |

***

### getWorkspaceId

Returns the value of the field "workspaceId"
Column: workspace_id
Attributes: NotNull \| Numeric \| Unsigned \| Size(1) \| Type(14)

```php
public getWorkspaceId(): mixed
```

***

### setWorkspaceId

Sets the value of the field "workspaceId"
Column: workspace_id
Attributes: NotNull \| Numeric \| Unsigned \| Size(1) \| Type(14)

```php
public setWorkspaceId(mixed $workspaceId): void
```

**Parameters:**

| Parameter      | Type      | Description |
|----------------|-----------|-------------|
| `$workspaceId` | **mixed** |             |

***

### getLabel

Returns the value of the field "label"
Column: label
Attributes: NotNull \| Size(60) \| Type(2)

```php
public getLabel(): mixed
```

***

### setLabel

Sets the value of the field "label"
Column: label
Attributes: NotNull \| Size(60) \| Type(2)

```php
public setLabel(mixed $label): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$label`  | **mixed** |             |

***

### getDescription

Returns the value of the field "description"
Column: description
Attributes: Size(240) \| Type(2)

```php
public getDescription(): mixed
```

***

### setDescription

Sets the value of the field "description"
Column: description
Attributes: Size(240) \| Type(2)

```php
public setDescription(mixed $description): void
```

**Parameters:**

| Parameter      | Type      | Description |
|----------------|-----------|-------------|
| `$description` | **mixed** |             |

***

### getIcon

Returns the value of the field "icon"
Column: icon
Attributes: Size(64) \| Type(2)

```php
public getIcon(): mixed
```

***

### setIcon

Sets the value of the field "icon"
Column: icon
Attributes: Size(64) \| Type(2)

```php
public setIcon(mixed $icon): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$icon`   | **mixed** |             |

***

### getColor

Returns the value of the field "color"
Column: color
Attributes: Size(9) \| Type(5)

```php
public getColor(): mixed
```

***

### setColor

Sets the value of the field "color"
Column: color
Attributes: Size(9) \| Type(5)

```php
public setColor(mixed $color): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$color`  | **mixed** |             |

***

### getDeleted

Returns the value of the field "deleted"
Column: deleted
Attributes: NotNull \| Numeric \| Unsigned \| Size(1) \| Type(26)

```php
public getDeleted(): mixed
```

***

### setDeleted

Sets the value of the field "deleted"
Column: deleted
Attributes: NotNull \| Numeric \| Unsigned \| Size(1) \| Type(26)

```php
public setDeleted(mixed $deleted): void
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$deleted` | **mixed** |             |

***

### getCreatedAt

Returns the value of the field "createdAt"
Column: created_at
Attributes: NotNull \| Type(4)

```php
public getCreatedAt(): mixed
```

***

### setCreatedAt

Sets the value of the field "createdAt"
Column: created_at
Attributes: NotNull \| Type(4)

```php
public setCreatedAt(mixed $createdAt): void
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$createdAt` | **mixed** |             |

***

### getCreatedBy

Returns the value of the field "createdBy"
Column: created_by
Attributes: Numeric \| Unsigned \| Size(1) \| Type(14)

```php
public getCreatedBy(): mixed
```

***

### setCreatedBy

Sets the value of the field "createdBy"
Column: created_by
Attributes: Numeric \| Unsigned \| Size(1) \| Type(14)

```php
public setCreatedBy(mixed $createdBy): void
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$createdBy` | **mixed** |             |

***

### getUpdatedAt

Returns the value of the field "updatedAt"
Column: updated_at
Attributes: Type(4)

```php
public getUpdatedAt(): mixed
```

***

### setUpdatedAt

Sets the value of the field "updatedAt"
Column: updated_at
Attributes: Type(4)

```php
public setUpdatedAt(mixed $updatedAt): void
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$updatedAt` | **mixed** |             |

***

### getUpdatedBy

Returns the value of the field "updatedBy"
Column: updated_by
Attributes: Numeric \| Unsigned \| Size(1) \| Type(14)

```php
public getUpdatedBy(): mixed
```

***

### setUpdatedBy

Sets the value of the field "updatedBy"
Column: updated_by
Attributes: Numeric \| Unsigned \| Size(1) \| Type(14)

```php
public setUpdatedBy(mixed $updatedBy): void
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$updatedBy` | **mixed** |             |

***

### getDeletedAt

Returns the value of the field "deletedAt"
Column: deleted_at
Attributes: Type(4)

```php
public getDeletedAt(): mixed
```

***

### setDeletedAt

Sets the value of the field "deletedAt"
Column: deleted_at
Attributes: Type(4)

```php
public setDeletedAt(mixed $deletedAt): void
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$deletedAt` | **mixed** |             |

***

### getDeletedBy

Returns the value of the field "deletedBy"
Column: deleted_by
Attributes: Numeric \| Unsigned \| Size(1) \| Type(14)

```php
public getDeletedBy(): mixed
```

***

### setDeletedBy

Sets the value of the field "deletedBy"
Column: deleted_by
Attributes: Numeric \| Unsigned \| Size(1) \| Type(14)

```php
public setDeletedBy(mixed $deletedBy): void
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$deletedBy` | **mixed** |             |

***
