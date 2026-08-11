
Defines PhalconKit's relationship assignment and export contract.

Models use this interface to distinguish two kinds of related data:
dirty relations that should be saved with the model, and loaded relations
that were attached for read/export purposes by eager loading. Implementors
may also opt into strict relationship assignment to convert malformed
relation payloads into framework exceptions instead of silently ignoring
them for legacy compatibility.

***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\RelationshipInterface`

## Methods

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
