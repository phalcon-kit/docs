
***

* Full name: `\PhalconKit\Models\Abstracts\Interfaces\LogAbstractInterface`
* Parent interfaces:
  [`\PhalconKit\Mvc\ModelInterface`](../../../Mvc/ModelInterface.md)

## Methods

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

### getLevel

Returns the value of the field "level"
Column: level
Attributes: NotNull \| Numeric \| Size(1)

```php
public getLevel(): mixed
```

***

### setLevel

Sets the value of the field "level"
Column: level
Attributes: NotNull \| Numeric \| Size(1)

```php
public setLevel(mixed $level): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$level`  | **mixed** |             |

***

### getType

Returns the value of the field "type"
Column: type
Attributes: NotNull \| Size('critical','alert','error','warning','notice','info','debug','emergency','other') \| Type(18)

```php
public getType(): mixed
```

***

### setType

Sets the value of the field "type"
Column: type
Attributes: NotNull \| Size('critical','alert','error','warning','notice','info','debug','emergency','other') \| Type(18)

```php
public setType(mixed $type): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$type`   | **mixed** |             |

***

### getMessage

Returns the value of the field "message"
Column: message
Attributes: NotNull \| Type(6)

```php
public getMessage(): mixed
```

***

### setMessage

Sets the value of the field "message"
Column: message
Attributes: NotNull \| Type(6)

```php
public setMessage(mixed $message): void
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$message` | **mixed** |             |

***

### getContext

Returns the value of the field "context"
Column: context
Attributes: Type(24)

```php
public getContext(): mixed
```

***

### setContext

Sets the value of the field "context"
Column: context
Attributes: Type(24)

```php
public setContext(mixed $context): void
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$context` | **mixed** |             |

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
public addStringLengthValidation(\PhalconKit\Filter\Validation $validator, array|string $field, int $minChar, int $maxChar = 255, bool $allowEmpty = true): \PhalconKit\Filter\Validation
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
public addDateValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true, string $format = Column::DATE_FORMAT): \PhalconKit\Filter\Validation
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
public addDateTimeValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true, string $format = Column::DATETIME_FORMAT): \PhalconKit\Filter\Validation
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
public addJsonValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true, int $depth = 512, int $flags): \PhalconKit\Filter\Validation
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
public selectReadConnection(): \Phalcon\Db\Adapter\AdapterInterface
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

### setKeepMissingRelated

```php
public setKeepMissingRelated(array $keepMissingRelated): void
```

**Parameters:**

| Parameter             | Type      | Description |
|-----------------------|-----------|-------------|
| `$keepMissingRelated` | **array** |             |

***

### getKeepMissingRelated

```php
public getKeepMissingRelated(): array
```

***

### getKeepMissingRelatedAlias

```php
public getKeepMissingRelatedAlias(string $alias): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### setKeepMissingRelatedAlias

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

```php
public getRelationshipContext(): string
```

***

### setRelationshipContext

```php
public setRelationshipContext(string $context): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$context` | **string** |             |

***

### getDirtyRelated

```php
public getDirtyRelated(): array
```

***

### setDirtyRelated

```php
public setDirtyRelated(array $dirtyRelated): void
```

**Parameters:**

| Parameter       | Type      | Description |
|-----------------|-----------|-------------|
| `$dirtyRelated` | **array** |             |

***

### getDirtyRelatedAlias

```php
public getDirtyRelatedAlias(string $alias): mixed
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### setDirtyRelatedAlias

```php
public setDirtyRelatedAlias(string $alias, mixed $value): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |
| `$value`  | **mixed**  |             |

***

### hasDirtyRelated

```php
public hasDirtyRelated(): bool
```

***

### hasDirtyRelatedAlias

```php
public hasDirtyRelatedAlias(string $alias): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### assignRelated

```php
public assignRelated(array $data, ?array $whiteList = null, ?array $dataColumnMap = null): \Phalcon\Mvc\ModelInterface
```

**Parameters:**

| Parameter        | Type       | Description |
|------------------|------------|-------------|
| `$data`          | **array**  |             |
| `$whiteList`     | **?array** |             |
| `$dataColumnMap` | **?array** |             |

***

### postSaveRelatedRecordsAfter

```php
public postSaveRelatedRecordsAfter(\Phalcon\Mvc\Model\RelationInterface $relation, array $relatedRecords, \Phalcon\Support\Collection\CollectionInterface $visited): ?bool
```

**Parameters:**

| Parameter         | Type                                                | Description |
|-------------------|-----------------------------------------------------|-------------|
| `$relation`       | **\Phalcon\Mvc\Model\RelationInterface**            |             |
| `$relatedRecords` | **array**                                           |             |
| `$visited`        | **\Phalcon\Support\Collection\CollectionInterface** |             |

***

### postSaveRelatedThroughAfter

```php
public postSaveRelatedThroughAfter(\Phalcon\Mvc\Model\RelationInterface $relation, array $relatedRecords, \Phalcon\Support\Collection\CollectionInterface $visited): ?bool
```

**Parameters:**

| Parameter         | Type                                                | Description |
|-------------------|-----------------------------------------------------|-------------|
| `$relation`       | **\Phalcon\Mvc\Model\RelationInterface**            |             |
| `$relatedRecords` | **array**                                           |             |
| `$visited`        | **\Phalcon\Support\Collection\CollectionInterface** |             |

***

### findFirstByPrimaryKeys

```php
public findFirstByPrimaryKeys(array $data, ?string $modelClass): \Phalcon\Mvc\ModelInterface|\Phalcon\Mvc\Model\Row|null
```

**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$data`       | **array**   |             |
| `$modelClass` | **?string** |             |

***

### getEntityFromData

```php
public getEntityFromData(array $data, array $configuration = []): \Phalcon\Mvc\ModelInterface|\Phalcon\Mvc\Model\Row|null
```

**Parameters:**

| Parameter        | Type      | Description |
|------------------|-----------|-------------|
| `$data`          | **array** |             |
| `$configuration` | **array** |             |

***

### appendMessages

```php
public appendMessages(array $messages = [], ?string $context = null, ?int $index): void
```

**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$messages` | **array**   |             |
| `$context`  | **?string** |             |
| `$index`    | **?int**    |             |

***

### appendMessagesFromRecord

```php
public appendMessagesFromRecord(?\Phalcon\Mvc\ModelInterface $record = null, ?string $context = null, ?int $index): void
```

**Parameters:**

| Parameter  | Type                             | Description |
|------------|----------------------------------|-------------|
| `$record`  | **?\Phalcon\Mvc\ModelInterface** |             |
| `$context` | **?string**                      |             |
| `$index`   | **?int**                         |             |

***

### appendMessagesFromResultset

```php
public appendMessagesFromResultset(?\Phalcon\Mvc\Model\ResultsetInterface $resultset = null, ?string $context = null, ?int $index): void
```

**Parameters:**

| Parameter    | Type                                       | Description |
|--------------|--------------------------------------------|-------------|
| `$resultset` | **?\Phalcon\Mvc\Model\ResultsetInterface** |             |
| `$context`   | **?string**                                |             |
| `$index`     | **?int**                                   |             |

***

### appendMessagesFromRecordList

```php
public appendMessagesFromRecordList(?iterable $recordList = null, ?string $context = null, ?int $index): void
```

**Parameters:**

| Parameter     | Type          | Description |
|---------------|---------------|-------------|
| `$recordList` | **?iterable** |             |
| `$context`    | **?string**   |             |
| `$index`      | **?int**      |             |

***

### rebuildMessageContext

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

```php
public relatedToArray(?array $columns = null, bool $useGetter = true): array
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$columns`   | **?array** |             |
| `$useGetter` | **bool**   |             |

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
public jsonEncode(mixed $value, int $flags = JSON_UNESCAPED_SLASHES, int $depth = 512): string|false
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
public jsonDecode(string $json, ?bool $associative = null, int $depth = 512, int $flags): mixed
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

```php
public getIdentityService(): \PhalconKit\Identity\Manager
```

***

### isLoggedIn

```php
public isLoggedIn(bool $as = false): bool
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |

***

### isLoggedInAs

```php
public isLoggedInAs(): bool
```

***

### getCurrentUser

```php
public getCurrentUser(bool $as = false): ?\PhalconKit\Models\Interfaces\UserInterface
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |

***

### getCurrentUserAs

```php
public getCurrentUserAs(): ?\PhalconKit\Models\Interfaces\UserInterface
```

***

### getCurrentUserId

```php
public getCurrentUserId(bool $as = false): ?int
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |

***

### getCurrentUserIdCallback

```php
public getCurrentUserIdCallback(bool $as = false): \Closure
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |

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
public checkHash(?string $hash = null, ?string $string = null, int $maxPassLength): bool
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
