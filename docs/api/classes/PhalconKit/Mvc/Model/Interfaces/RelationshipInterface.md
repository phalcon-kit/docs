
Interface for model relationship management

***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\RelationshipInterface`

## Methods

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
