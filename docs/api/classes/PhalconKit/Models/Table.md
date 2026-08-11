
Class Table

This class represents a Table object.
It extends the TableAbstract class and implements the TableInterface.

***

* Full name: `\PhalconKit\Models\Table`
* Parent class: [`\PhalconKit\Models\Abstracts\TableAbstract`](./Abstracts/TableAbstract.md)
* This class implements:
  [`\PhalconKit\Models\Interfaces\TableInterface`](./Interfaces/TableInterface.md)

## Methods

### initialize

```php
public initialize(): void
```

***

### validation

```php
public validation(): bool
```

***

## Inherited methods

### getAllowEmptyOption

```php
protected getAllowEmptyOption(bool $allowEmpty = true): bool|array
```

**Parameters:**

| Parameter     | Type     | Description |
|---------------|----------|-------------|
| `$allowEmpty` | **bool** |             |

***

### shouldSkipOptionalValidation

```php
protected shouldSkipOptionalValidation(array|string $field, bool $allowEmpty): bool
```

**Parameters:**

| Parameter     | Type              | Description |
|---------------|-------------------|-------------|
| `$field`      | **array\|string** |             |
| `$allowEmpty` | **bool**          |             |

***

### isOptionalEmptyValue

```php
protected isOptionalEmptyValue(mixed $value): bool
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***

### genericValidation

Apply generic validation to a validator object.

```php
public genericValidation(\PhalconKit\Filter\Validation|null $validator = null): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter    | Type                                    | Description                                                                                              |
|--------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------|
| `$validator` | **\PhalconKit\Filter\Validation\|null** | The validator object to apply the validation rules to. If null, a new Validation object will be created. |

**Return Value:**

The validator object with the generic validation rules applied.

***

### addNotEmptyValidation

Add validation to ensure that a field is not empty

```php
public addNotEmptyValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = false): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                      |
|---------------|-----------------------------------|--------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validation object to add the validation to   |
| `$field`      | **array\|string**                 | The name of the field to validate                |
| `$allowEmpty` | **bool**                          | Whether to allow empty values. Default is false. |

**Return Value:**

The updated validation object

***

### addPresenceValidation

Add presence validation to a field in a validator object

```php
public addPresenceValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                                        |
|---------------|-----------------------------------|--------------------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validator object to add the validation to                      |
| `$field`      | **array\|string**                 | The name of the field to validate                                  |
| `$allowEmpty` | **bool**                          | Whether to allow empty values for the field or not (default: true) |

**Return Value:**

The modified validator object after adding the validation

***

### addUnsignedIntValidation

Add validations for an unsigned integer field

```php
public addUnsignedIntValidation(\PhalconKit\Filter\Validation $validator, array|string $field = 'id', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                            |
|---------------|-----------------------------------|--------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validation object to add rules to                  |
| `$field`      | **array\|string**                 | The name of the field to validate (default: 'id')      |
| `$allowEmpty` | **bool**                          | Whether to allow the field to be empty (default: true) |

**Return Value:**

The updated validation object with the added rules

***

### addUnsignedBigIntValidation

Add basic validations for the specified field to ensure it is an unsigned big integer

```php
public addUnsignedBigIntValidation(\PhalconKit\Filter\Validation $validator, array|string $field = 'id', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                               |
|---------------|-----------------------------------|-----------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validation object to add rules to                     |
| `$field`      | **array\|string**                 | The name of the field to validate (default is 'id')       |
| `$allowEmpty` | **bool**                          | Whether empty values are allowed or not (default is true) |

**Return Value:**

The updated validation object

***

### addNumberValidation

Add number validations for a given field

```php
public addNumberValidation(\PhalconKit\Filter\Validation $validator, array|string $field, int $min, int $max, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                     |
|---------------|-----------------------------------|-------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validation object to add the validations to |
| `$field`      | **array\|string**                 | The name of the field to validate               |
| `$min`        | **int**                           | The minimum value allowed for the field         |
| `$max`        | **int**                           | The maximum value allowed for the field         |
| `$allowEmpty` | **bool**                          | Specifies whether the field can be empty        |

**Return Value:**

The modified validation object with the number validations added

***

### addStringLengthValidation

Add string length validations for a field

```php
public addStringLengthValidation(\PhalconKit\Filter\Validation $validator, array|string $field, int $minChar = 0, int $maxChar = 255, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                             |
|---------------|-----------------------------------|---------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validation object to add the validations to         |
| `$field`      | **array\|string**                 | The name of the field to be validated                   |
| `$minChar`    | **int**                           | The minimum number of characters allowed (default: 0)   |
| `$maxChar`    | **int**                           | The maximum number of characters allowed (default: 255) |
| `$allowEmpty` | **bool**                          | Whether empty values are allowed (default: true)        |

**Return Value:**

The validation object with the added validations

***

### addInclusionInValidation

Add inclusion validation for a field

```php
public addInclusionInValidation(\PhalconKit\Filter\Validation $validator, array|string $field, array $domainList = [], bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                       |
|---------------|-----------------------------------|---------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validation object                             |
| `$field`      | **array\|string**                 | The name of the field to be validated             |
| `$domainList` | **array**                         | The list of valid values for the field            |
| `$allowEmpty` | **bool**                          | Set to true to allow empty values (default: true) |

**Return Value:**

The updated validation object with the inclusion validation added

***

### addBooleanValidation

Add basic validations for a boolean field
- Must not be empty
- Must be a boolean value (1, 0, true, false)

```php
public addBooleanValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                          |
|---------------|-----------------------------------|------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validation object to add the validations to      |
| `$field`      | **array\|string**                 | The name of the field to validate                    |
| `$allowEmpty` | **bool**                          | Whether to allow empty values or not (default: true) |

**Return Value:**

The updated validation object

***

### addInclusionValidation

Add inclusion validation for a specified field

```php
public addInclusionValidation(\PhalconKit\Filter\Validation $validator, array|string $field, array $domain = [], bool $allowEmpty = true, bool $strict = true): \PhalconKit\Filter\Validation
```

This method adds an inclusion validation rule to the given validator object for the specified field.
The inclusion rule checks if the value of the field is included in the specified domain.

**Parameters:**

| Parameter     | Type                              | Description                                                             |
|---------------|-----------------------------------|-------------------------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validator object to which the rule should be added                  |
| `$field`      | **array\|string**                 | The name of the field to be validated                                   |
| `$domain`     | **array**                         | The array of allowed values for the field                               |
| `$allowEmpty` | **bool**                          | Whether to allow empty values for the field (default: true)             |
| `$strict`     | **bool**                          | Whether to use strict comparison for checking inclusion (default: true) |

**Return Value:**

The updated validator object

***

### addUniquenessValidation

Add uniqueness validation for the specified field(s)

```php
public addUniquenessValidation(\PhalconKit\Filter\Validation $validator, string|array $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                          |
|---------------|-----------------------------------|------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validation object to add the validation rules to |
| `$field`      | **string\|array**                 | The field(s) to apply the uniqueness validation to   |
| `$allowEmpty` | **bool**                          | Whether to allow empty values for the field(s)       |

**Return Value:**

The modified validation object

***

### addEmailValidation

Add email validation to a field

```php
public addEmailValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                                 |
|---------------|-----------------------------------|-------------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validator object                                        |
| `$field`      | **array\|string**                 | The field name to add the validation to                     |
| `$allowEmpty` | **bool**                          | Whether to allow empty values for the field (default: true) |

**Return Value:**

The modified validator object

***

### addDateValidation

Add basic validations for the date field
- Must not be empty
- Must be a valid date in the specified format

```php
public addDateValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true, string $format = \PhalconKit\Db\Column::DATE_FORMAT): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                                          |
|---------------|-----------------------------------|----------------------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validation object to add the validations to                      |
| `$field`      | **array\|string**                 | The name of the date field to validate                               |
| `$allowEmpty` | **bool**                          | Whether to allow empty values for the date field (default: true)     |
| `$format`     | **string**                        | The expected format of the date field (default: Column::DATE_FORMAT) |

**Return Value:**

The updated validation object

***

### addDateTimeValidation

Add basic validations for the datetime field
- Must not be empty
- Must be a valid datetime format

```php
public addDateTimeValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true, string $format = \PhalconKit\Db\Column::DATETIME_FORMAT): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                                   |
|---------------|-----------------------------------|---------------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validation object                                         |
| `$field`      | **array\|string**                 | The name of the field to validate                             |
| `$allowEmpty` | **bool**                          | Specifies if the field is allowed to be empty (default: true) |
| `$format`     | **string**                        | The format of the datetime (default: Column::DATETIME_FORMAT) |

**Return Value:**

The updated validation object

***

### addJsonValidation

Add validations for a JSON field
- Must not be empty (unless allowEmpty is set to true)
- Must be a valid JSON string

```php
public addJsonValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true, int $depth = 512, int $flags = 0): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                         |
|---------------|-----------------------------------|-----------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validator object to add the validations to      |
| `$field`      | **array\|string**                 | The name of the JSON field to validate              |
| `$allowEmpty` | **bool**                          | Whether to allow an empty value for the field       |
| `$depth`      | **int**                           | The maximum depth of the JSON string (default: 512) |
| `$flags`      | **int**                           | JSON flags to be used (default: 0)                  |

**Return Value:**

The updated validator object

***

### addColorValidation

Add basic validations for the color field
- Must not be empty (unless $allowEmpty is set to true)
- Must be a valid hex color code

```php
public addColorValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                      |
|---------------|-----------------------------------|--------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validation object                            |
| `$field`      | **array\|string**                 | The name of the field to validate                |
| `$allowEmpty` | **bool**                          | Whether empty values are allowed (default: true) |

**Return Value:**

The modified validation object

***

### addIdValidation

Add basic validations for the id field
- Must be an unsigned integer

```php
public addIdValidation(\PhalconKit\Filter\Validation $validator, string $field = 'id'): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter    | Type                              | Description                                                  |
|--------------|-----------------------------------|--------------------------------------------------------------|
| `$validator` | **\PhalconKit\Filter\Validation** | The validation object to add validation rules to             |
| `$field`     | **string**                        | The name of the field to add validations for (default: 'id') |

**Return Value:**

The updated validation object

***

### addPositionValidation

Add position validation to a validator object.

```php
public addPositionValidation(\PhalconKit\Filter\Validation $validator, string $field = 'position', bool $allowEmpty = true, bool $allowRawValue = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter        | Type                              | Description                                                             |
|------------------|-----------------------------------|-------------------------------------------------------------------------|
| `$validator`     | **\PhalconKit\Filter\Validation** | The validator object to add the validation rules to.                    |
| `$field`         | **string**                        | The field name to apply the validation rules to. Default is 'position'. |
| `$allowEmpty`    | **bool**                          | Whether empty values are allowed. Default is true.                      |
| `$allowRawValue` | **bool**                          | Whether raw values are allowed. Default is true.                        |

**Return Value:**

The updated validator object with the position validation added.

***

### addSoftDeleteValidation

Add soft delete validation to a validator object.

```php
public addSoftDeleteValidation(\PhalconKit\Filter\Validation $validator, string $field = 'deleted', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                                            |
|---------------|-----------------------------------|------------------------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validator object to add the validation rules to.                   |
| `$field`      | **string**                        | The field name to apply the validation rules to. Default is 'deleted'. |
| `$allowEmpty` | **bool**                          | Whether empty values are allowed. Default is true.                     |

**Return Value:**

The updated validator object with the soft delete validation added.

***

### addUuidValidation

Add UUID validation to a validator object.

```php
public addUuidValidation(\PhalconKit\Filter\Validation $validator, string $field = 'uuid', bool $allowEmpty = false): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                              | Description                                                         |
|---------------|-----------------------------------|---------------------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** | The validator object to add the validation rules to.                |
| `$field`      | **string**                        | The field name to apply the validation rules to. Default is 'uuid'. |
| `$allowEmpty` | **bool**                          | Whether empty values are allowed. Default is false.                 |

**Return Value:**

The updated validator object with the UUID validation added.

***

### addCrudValidation

Add CRUD validation to a validator object.

```php
public addCrudValidation(\PhalconKit\Filter\Validation $validator, string $userIdField, string $dateField, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter      | Type                              | Description                                          |
|----------------|-----------------------------------|------------------------------------------------------|
| `$validator`   | **\PhalconKit\Filter\Validation** | The validator object to add the validation rules to. |
| `$userIdField` | **string**                        | The field name for the user ID validation rules.     |
| `$dateField`   | **string**                        | The field name for the date validation rules.        |
| `$allowEmpty`  | **bool**                          | Whether empty values are allowed. Default is true.   |

**Return Value:**

The updated validator object with the CRUD validation added.

***

### addCreatedValidation

Add created validation to a validator object.

```php
public addCreatedValidation(\PhalconKit\Filter\Validation $validator, string $createdByField = 'createdBy', string $createdAtField = 'createdAt', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter         | Type                              | Description                                                                                          |
|-------------------|-----------------------------------|------------------------------------------------------------------------------------------------------|
| `$validator`      | **\PhalconKit\Filter\Validation** | The validator object to add the validation rules to.                                                 |
| `$createdByField` | **string**                        | The field name to apply the validation rules for the "created by" user. Default is 'createdBy'.      |
| `$createdAtField` | **string**                        | The field name to apply the validation rules for the "created at" timestamp. Default is 'createdAt'. |
| `$allowEmpty`     | **bool**                          | Whether empty values are allowed. Default is true.                                                   |

**Return Value:**

The updated validator object with the created validation added.

***

### addUpdatedValidation

Add updated validation to a validator object.

```php
public addUpdatedValidation(\PhalconKit\Filter\Validation $validator, string $updatedByField = 'updatedBy', string $updatedAtField = 'updatedAt', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter         | Type                              | Description                                                                        |
|-------------------|-----------------------------------|------------------------------------------------------------------------------------|
| `$validator`      | **\PhalconKit\Filter\Validation** | The validator object to add the validation rules to.                               |
| `$updatedByField` | **string**                        | The field name to apply the updated by validation rule to. Default is 'updatedBy'. |
| `$updatedAtField` | **string**                        | The field name to apply the updated at validation rule to. Default is 'updatedAt'. |
| `$allowEmpty`     | **bool**                          | Whether empty values are allowed. Default is true.                                 |

**Return Value:**

The updated validator object with the updated validation added.

***

### addDeletedValidation

Add deleted validation to a validator object.

```php
public addDeletedValidation(\PhalconKit\Filter\Validation $validator, string $deletedField = 'deletedBy', string $dateField = 'deletedAt', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter       | Type                              | Description                                                                                |
|-----------------|-----------------------------------|--------------------------------------------------------------------------------------------|
| `$validator`    | **\PhalconKit\Filter\Validation** | The validator object to add the validation rules to.                                       |
| `$deletedField` | **string**                        | The field name to apply the validation rules to for deleted user. Default is 'deletedBy'.  |
| `$dateField`    | **string**                        | The field name to apply the validation rules to for deletion date. Default is 'deletedAt'. |
| `$allowEmpty`   | **bool**                          | Whether empty values are allowed. Default is true.                                         |

**Return Value:**

The updated validator object with the deleted validation added.

***

### addRestoredValidation

Add restored validation to a validator object.

```php
public addRestoredValidation(\PhalconKit\Filter\Validation $validator, string $restoredByField = 'restoredBy', string $restoredAtField = 'restoredAt', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter          | Type                              | Description                                                              |
|--------------------|-----------------------------------|--------------------------------------------------------------------------|
| `$validator`       | **\PhalconKit\Filter\Validation** | The validator object to add the validation rules to.                     |
| `$restoredByField` | **string**                        | The field name for the restored by information. Default is 'restoredBy'. |
| `$restoredAtField` | **string**                        | The field name for the restored at information. Default is 'restoredAt'. |
| `$allowEmpty`      | **bool**                          | Whether empty values are allowed. Default is true.                       |

**Return Value:**

The updated validator object with the restored validation added.

***

### initializeUuid

Initialize the UUID transform behavior for create validation.

```php
public initializeUuid(array<string,mixed>|null $options = null): void
```

Options default to the model options manager under `uuid`. Supported
keys are:

- `field`: target attribute name, default `uuid`
- `native`: when true, use database `UUID()` expressions
- `binary`: when true, store UUIDs as binary values

**Parameters:**

| Parameter  | Type                          | Description            |
|------------|-------------------------------|------------------------|
| `$options` | **array<string,mixed>\|null** | UUID behavior options. |

**Throws:**

When the security service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getBinaryUuid

Convert a canonical UUID string to its packed binary representation.

```php
private getBinaryUuid(string $uuid): string
```

**Parameters:**

| Parameter | Type       | Description                          |
|-----------|------------|--------------------------------------|
| `$uuid`   | **string** | UUID string with or without hyphens. |

**Return Value:**

Binary bytes suitable for binary UUID columns.

***

### setUuidBehavior

Register the UUID transform behavior under the standard behavior name.

```php
public setUuidBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $uuidBehavior): void
```

**Parameters:**

| Parameter       | Type                                             | Description                        |
|-----------------|--------------------------------------------------|------------------------------------|
| `$uuidBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** | Configured transformable behavior. |

**Throws:**

When the current models manager does not expose
the PhalconKit behavior registry.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getUuidBehavior

Retrieve the registered UUID transform behavior.

```php
public getUuidBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

**Return Value:**

Transformable behavior responsible for UUID values.

**Throws:**

When the current models manager does not expose
the PhalconKit behavior registry.
- [`ServiceException`](../Exception/ServiceException.md)

***

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

The native ORM events flag is read from INI here because the trait can be
used without access to the original model setup options.

**Parameters:**

| Parameter          | Type        | Description |
|--------------------|-------------|-------------|
| `$field`           | **?string** |             |
| `$notDeletedValue` | **?int**    |             |

***

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
- [`LogicException`](../Exception/LogicException.md)

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
- [`LogicException`](../Exception/LogicException.md)

***

### initializeSlug

Initializes the slug behavior for the model.

```php
public initializeSlug(array|null $options = null): void
```

**Parameters:**

| Parameter  | Type            | Description                                                                       |
|------------|-----------------|-----------------------------------------------------------------------------------|
| `$options` | **array\|null** | Optional. An array containing the options for the slug behavior. Default is null. |

***

### setSlugBehavior

Sets the slug behavior for the model.

```php
public setSlugBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $slugBehavior): void
```

**Parameters:**

| Parameter       | Type                                             | Description                                            |
|-----------------|--------------------------------------------------|--------------------------------------------------------|
| `$slugBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** | A Transformable object representing the slug behavior. |

***

### getSlugBehavior

Returns the slug behavior associated with the model.

```php
public getSlugBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

**Return Value:**

The slug behavior associated with the model.

***

### initializeSecurity

Initializes the security

```php
public initializeSecurity(array|null $options = null): void
```

**Parameters:**

| Parameter  | Type            | Description                                                                                                                                                                          |
|------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$options` | **array\|null** | An optional array of security options. If not provided,
the method will attempt to fetch the options from the options manager.
If no options are found, an empty array will be used. |

***

### setSecurityBehavior

Sets the security behavior

```php
public setSecurityBehavior(\PhalconKit\Mvc\Model\Behavior\Security $securityBehavior): void
```

**Parameters:**

| Parameter           | Type                                        | Description                   |
|---------------------|---------------------------------------------|-------------------------------|
| `$securityBehavior` | **\PhalconKit\Mvc\Model\Behavior\Security** | The security behavior to set. |

***

### getSecurityBehavior

Retrieves the security behavior

```php
public getSecurityBehavior(): \PhalconKit\Mvc\Model\Behavior\Security
```

**Return Value:**

The security behavior instance.

***

### setConnectionService

Set the default connection service used by Phalcon for this model.

```php
public setConnectionService(string $connectionService): void
```

Implemented by Phalcon's model base class.

* This method is **abstract**.
**Parameters:**

| Parameter            | Type       | Description                                 |
|----------------------|------------|---------------------------------------------|
| `$connectionService` | **string** | DI service name for the default
connection. |

***

### setReadConnectionService

Set the read connection service used by Phalcon for this model.

```php
public setReadConnectionService(string $connectionService): void
```

* This method is **abstract**.
**Parameters:**

| Parameter            | Type       | Description                          |
|----------------------|------------|--------------------------------------|
| `$connectionService` | **string** | DI service name for read operations. |

***

### setWriteConnectionService

Set the write connection service used by Phalcon for this model.

```php
public setWriteConnectionService(string $connectionService): void
```

* This method is **abstract**.
**Parameters:**

| Parameter            | Type       | Description                           |
|----------------------|------------|---------------------------------------|
| `$connectionService` | **string** | DI service name for write operations. |

***

### getWriteConnectionService

Return the configured write connection service name.

```php
public getWriteConnectionService(): string
```

* This method is **abstract**.
**Return Value:**

DI service name for write operations.

***

### getReadConnectionService

Return the configured read connection service name.

```php
public getReadConnectionService(): string
```

* This method is **abstract**.
**Return Value:**

DI service name for read operations.

***

### getReplicationLag

Return the configured replica lag window in milliseconds.

```php
public static getReplicationLag(): int|null
```

* This method is **static**.
**Return Value:**

Lag window, or null before replication initialization.

***

### setReplicationLag

Set the replica lag window in milliseconds.

```php
public static setReplicationLag(int|null $replicationLag = null): void
```

* This method is **static**.
**Parameters:**

| Parameter         | Type          | Description                                                       |
|-------------------|---------------|-------------------------------------------------------------------|
| `$replicationLag` | **int\|null** | Lag window to use after write events, or
null to clear the value. |

***

### getReplicationReadyAt

Return the timestamp after which replica reads may resume.

```php
public static getReplicationReadyAt(): int|null
```

* This method is **static**.
**Return Value:**

Unix timestamp in milliseconds, or null when reads are
not currently pinned to the write connection.

***

### setReplicationReadyAt

Set the timestamp after which replica reads may resume.

```php
public static setReplicationReadyAt(int|null $replicationReadyAt = null): void
```

* This method is **static**.
**Parameters:**

| Parameter             | Type          | Description                                                           |
|-----------------------|---------------|-----------------------------------------------------------------------|
| `$replicationReadyAt` | **int\|null** | Unix timestamp in milliseconds, or
null to mark the replica as ready. |

***

### initializeReplication

Initialize read/write connection services for replica-aware models.

```php
public initializeReplication(array<array-key,mixed>|null $options = null): void
```

The trait reads `database.drivers.mysql.readonly.enable` from the config
service. When enabled, it configures connection service names and attaches
write-event listeners that temporarily pin reads to the write connection.

**Parameters:**

| Parameter  | Type                             | Description                                                                                                                         |
|------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `$options` | **array<array-key,mixed>\|null** | Optional replication
options. Supported keys are `lag`, `connectionService`,
`readConnectionService`, and `writeConnectionService`. |

**Throws:**

When the config service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### selectReadConnection

Select the connection used for model reads.

```php
public selectReadConnection(): \Phalcon\Db\Adapter\AdapterInterface
```

When there is no active replica-cooldown window, the configured read
connection service is returned. Immediately after write-like events,
reads are pinned back to the write connection until the lag window
expires, which avoids stale reads from asynchronous replicas.

**Return Value:**

Read connection when replicas are ready; write
connection while reads are pinned after a mutation.

**Throws:**

When the read or write connection service cannot
be resolved through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### addReadWriteConnectionBehavior

Attach lifecycle listeners that pin reads to the write connection.

```php
public addReadWriteConnectionBehavior(): void
```

Each write-like event updates `replicationReadyAt` to `now + lag`. Native
Phalcon requires a compatible events manager to attach these callbacks.

**Throws:**

When the model events manager is missing or does
not implement Phalcon's events manager contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### isReplicationReady

Determine whether reads may use a replica again.

```php
public isReplicationReady(): bool
```

When the cooldown has expired, the ready timestamp is cleared so future
calls remain ready until another write event updates it.

**Return Value:**

True when the replica cooldown is absent or expired.

***

### nowMs

Return the current process time in milliseconds.

```php
protected static nowMs(): int
```

This helper keeps replication timestamps integer-based and easy to
compare without leaking floating-point microtime values into public
replication state.

* This method is **static**.
**Return Value:**

Unix timestamp in milliseconds.

***

### appendMessage

```php
public appendMessage(\Phalcon\Messages\MessageInterface $message): \Phalcon\Mvc\ModelInterface
```

* This method is **abstract**.
**Parameters:**

| Parameter  | Type                                   | Description |
|------------|----------------------------------------|-------------|
| `$message` | **\Phalcon\Messages\MessageInterface** |             |

***

### setStrictRelatedAssignment

Enable or disable strict validation for relationship payloads.

```php
public setStrictRelatedAssignment(bool $strictRelatedAssignment): void
```

Leave this disabled for legacy forms that may send extra nested data.
Enable it in API/resource layers where relation aliases are controlled by
explicit save-field policies and a malformed relation should fail loudly.

**Parameters:**

| Parameter                  | Type     | Description |
|----------------------------|----------|-------------|
| `$strictRelatedAssignment` | **bool** |             |

***

### isStrictRelatedAssignment

Return whether malformed relationship payloads should throw exceptions.

```php
public isStrictRelatedAssignment(): bool
```

***

### setRelationshipOptions

Replace the configured relationship behavior options.

```php
public setRelationshipOptions(array $options): void
```

The option group is intentionally stored in the shared model options
manager so applications can opt into stricter behavior per model without
changing generated relationship declarations.

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$options` | **array** |             |

***

### getRelationshipOptions

Return relationship options, optionally including a per-alias override.

```php
public getRelationshipOptions(?string $alias = null): array
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$alias`  | **?string** |             |

***

### getConfiguredRelationshipOptions

Read relationship defaults from bootstrap config when available.

```php
private getConfiguredRelationshipOptions(): array<string,mixed>
```

The config path is intentionally feature-specific (`model.relationship`)
rather than part of the generic model options manager.

***

### getRelationshipOption

Return one configured relationship behavior option.

```php
public getRelationshipOption(string $option, ?string $alias = null, mixed $default = null): mixed
```

**Parameters:**

| Parameter  | Type        | Description |
|------------|-------------|-------------|
| `$option`  | **string**  |             |
| `$alias`   | **?string** |             |
| `$default` | **mixed**   |             |

***

### getRelationshipAliasOptions

```php
private getRelationshipAliasOptions(array $configured, string $alias): array
```

**Parameters:**

| Parameter     | Type       | Description |
|---------------|------------|-------------|
| `$configured` | **array**  |             |
| `$alias`      | **string** |             |

***

### setKeepMissingRelated

Set the missing related configuration list

```php
public setKeepMissingRelated(array $keepMissingRelated): void
```

**Parameters:**

| Parameter             | Type      | Description |
|-----------------------|-----------|-------------|
| `$keepMissingRelated` | **array** |             |

***

### getKeepMissingRelated

Return the missing related configuration list

```php
public getKeepMissingRelated(): array<string,bool>
```

***

### getKeepMissingRelatedAlias

Return the keepMissing configuration for a specific relationship alias

```php
public getKeepMissingRelatedAlias(string $alias): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### setKeepMissingRelatedAlias

Set the keepMissing configuration for a specific relationship alias

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

Get the current relationship context

```php
public getRelationshipContext(): string
```

***

### setRelationshipContext

Set the current relationship context

```php
public setRelationshipContext(string $context): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$context` | **string** |             |

***

### getDirtyRelated

Return the dirtyRelated entities

```php
public getDirtyRelated(): array<string,mixed>
```

***

### setDirtyRelated

Set the dirtyRelated entities

```php
public setDirtyRelated(array $dirtyRelated): void
```

**Parameters:**

| Parameter       | Type      | Description |
|-----------------|-----------|-------------|
| `$dirtyRelated` | **array** |             |

***

### getDirtyRelatedAlias

Return the dirtyRelated entities

```php
public getDirtyRelatedAlias(string $alias): mixed
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### setDirtyRelatedAlias

Return the dirtyRelated entities

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

Check whether the current entity has dirty related or not

```php
public hasDirtyRelated(): bool
```

***

### hasDirtyRelatedAlias

Check whether the current entity has dirty related or not

```php
public hasDirtyRelatedAlias(string $alias): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### getLoadedRelated

Return the eager-loaded related entities

```php
public getLoadedRelated(): array<string,mixed>
```

***

### setLoadedRelated

Set the eager-loaded related entities

```php
public setLoadedRelated(array $loadedRelated): void
```

**Parameters:**

| Parameter        | Type      | Description |
|------------------|-----------|-------------|
| `$loadedRelated` | **array** |             |

***

### getLoadedRelatedAlias

Return eager-loaded related entities for one alias

```php
public getLoadedRelatedAlias(string $alias): mixed
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### setLoadedRelatedAlias

Set eager-loaded related entities for one alias

```php
public setLoadedRelatedAlias(string $alias, mixed $value): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |
| `$value`  | **mixed**  |             |

***

### hasLoadedRelatedAlias

Check whether an eager-loaded relation alias exists

```php
public hasLoadedRelatedAlias(string $alias): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### setRelated

Store a related value in both Phalcon's native relation cache and
PhalconKit's read-only eager-loading cache.

```php
public setRelated(string $alias, mixed $records): \Phalcon\Mvc\ModelInterface
```

Phalcon 5.18's native eager loader calls this method while hydrating
`find(['eager' => [...]])` results. Mirroring the value keeps direct
property access, `getRelated()`, exports, and native
`isRelationshipLoaded()` checks consistent without marking the relation
for persistence.

**Parameters:**

| Parameter  | Type       | Description                             |
|------------|------------|-----------------------------------------|
| `$alias`   | **string** | Registered relationship alias.          |
| `$records` | **mixed**  | Related model, row, resultset, or null. |

**Return Value:**

The current model instance.

***

### normalizeRelationAlias

```php
private normalizeRelationAlias(string $alias): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |

***

### normalizeRelationAliases

```php
private normalizeRelationAliases(array $related): array
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$related` | **array** |             |

***

### writeDeclaredRelatedAlias

```php
private writeDeclaredRelatedAlias(string $alias, mixed $value): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$alias`  | **string** |             |
| `$value`  | **mixed**  |             |

***

### assign

Assigns values to the model from an array, with options to control which fields are assigned.

```php
public assign(array $data, array|null $whiteList = null, array|null $dataColumnMap = null): \Phalcon\Mvc\ModelInterface
```

Handles related records using `assignRelated` method and passes remaining values to the parent's assign method.

**Parameters:**

| Parameter        | Type            | Description                                                                        |
|------------------|-----------------|------------------------------------------------------------------------------------|
| `$data`          | **array**       | The array of data to assign to the model.                                          |
| `$whiteList`     | **array\|null** | An optional array specifying which fields in the model can be assigned.            |
| `$dataColumnMap` | **array\|null** | An optional column map to transform external keys into internal model field names. |

**Return Value:**

Returns the updated ModelInterface instance.

**Throws:**

- [`InvalidArgumentException`](../Exception/InvalidArgumentException.md)

***

### assignRelated

Assign related

```php
public assignRelated(array $data, array|null $whiteList = null, array|null $dataColumnMap = null): \Phalcon\Mvc\ModelInterface
```

Single
[alias => new Alias()] // create new alias

Many
[alias => [new Alias()]] // create new alias
[alias => [1, 2, 3, 4]] // append / merge 1, 2, 3, 4
[alias => [false, 1, 2, 4]]; // delete 3

**Parameters:**

| Parameter        | Type            | Description |
|------------------|-----------------|-------------|
| `$data`          | **array**       |             |
| `$whiteList`     | **array\|null** |             |
| `$dataColumnMap` | **array\|null** |             |

**Throws:**

- [`InvalidArgumentException`](../Exception/InvalidArgumentException.md)

***

### isRelatedAssignmentWhiteListed

Check whether a relation alias is allowed by a nested assignment whitelist.

```php
private isRelatedAssignmentWhiteListed(string $alias, array $whiteList): bool
```

The whitelist can contain relation aliases as plain values or as keys that
point to nested allowed fields. This mirrors existing PhalconKit save-field
payloads without forcing callers to choose one representation.

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$alias`     | **string** |             |
| `$whiteList` | **array**  |             |

***

### isRelationPayload

Determine whether an unknown key carries relationship-shaped data.

```php
private isRelationPayload(mixed $value): bool
```

Scalar unknown keys are left to native model assignment. Complex values
are the only safe candidates for strict relationship-alias validation
because they are how REST/save payloads express nested relations.

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***

### isModelAssignmentField

Check whether a non-relation assignment key is a known model field.

```php
private isModelAssignmentField(string $field, ?array $dataColumnMap = null): bool
```

Strict relationship assignment must not reject JSON/array columns or
mapped model attributes just because their values look like nested
relation payloads. The optional data column map is checked first because
callers may use external request keys that Phalcon maps before writing.

**Parameters:**

| Parameter        | Type       | Description |
|------------------|------------|-------------|
| `$field`         | **string** |             |
| `$dataColumnMap` | **?array** |             |

***

### isDirectOwnedRelationType

```php
private isDirectOwnedRelationType(?int $type): bool
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$type`   | **?int** |             |

***

### assertDirectRelatedRecordCanBeAssigned

```php
private assertDirectRelatedRecordCanBeAssigned(?string $alias, ?int $type, array $relationFields, array $referencedFields, \Phalcon\Mvc\EntityInterface $record): void
```

**Parameters:**

| Parameter           | Type                             | Description |
|---------------------|----------------------------------|-------------|
| `$alias`            | **?string**                      |             |
| `$type`             | **?int**                         |             |
| `$relationFields`   | **array**                        |             |
| `$referencedFields` | **array**                        |             |
| `$record`           | **\Phalcon\Mvc\EntityInterface** |             |

***

### getDirectRelatedOwnershipState

```php
private getDirectRelatedOwnershipState(array $relationFields, array $referencedFields, \Phalcon\Mvc\EntityInterface $record): string
```

**Parameters:**

| Parameter           | Type                             | Description |
|---------------------|----------------------------------|-------------|
| `$relationFields`   | **array**                        |             |
| `$referencedFields` | **array**                        |             |
| `$record`           | **\Phalcon\Mvc\EntityInterface** |             |

***

### isEmptyRelationValue

```php
private isEmptyRelationValue(mixed $value): bool
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***

### isSameRelationValue

```php
private isSameRelationValue(mixed $expected, mixed $actual): bool
```

**Parameters:**

| Parameter   | Type      | Description |
|-------------|-----------|-------------|
| `$expected` | **mixed** |             |
| `$actual`   | **mixed** |             |

***

### prepareDirectRelatedRecordForSave

```php
private prepareDirectRelatedRecordForSave(\Phalcon\Mvc\Model\RelationInterface $relation, \Phalcon\Mvc\EntityInterface $record, ?string $alias, ?int $index = null): bool
```

**Parameters:**

| Parameter   | Type                                     | Description |
|-------------|------------------------------------------|-------------|
| `$relation` | **\Phalcon\Mvc\Model\RelationInterface** |             |
| `$record`   | **\Phalcon\Mvc\EntityInterface**         |             |
| `$alias`    | **?string**                              |             |
| `$index`    | **?int**                                 |             |

***

### preSaveRelatedRecords

Saves related records that must be stored prior to save the master record
 Refactored based on the native cphalcon version, so we can support :
 - combined keys on relationship definition
 - relationship context within the model messages based on the alias definition

```php
protected preSaveRelatedRecords(\Phalcon\Db\Adapter\AdapterInterface $connection, \Phalcon\Mvc\ModelInterface[] $related, \Phalcon\Support\Collection\CollectionInterface $visited): bool
```

**Parameters:**

| Parameter     | Type                                                | Description |
|---------------|-----------------------------------------------------|-------------|
| `$connection` | **\Phalcon\Db\Adapter\AdapterInterface**            |             |
| `$related`    | **\Phalcon\Mvc\ModelInterface[]**                   |             |
| `$visited`    | **\Phalcon\Support\Collection\CollectionInterface** |             |

**Throws:**

- [`InvalidArgumentException`](../Exception/InvalidArgumentException.md)

***

### postSaveRelatedRecords

Processes the saving of related records for the current model.

```php
protected postSaveRelatedRecords(\Phalcon\Db\Adapter\AdapterInterface $connection, array|object[]|\Phalcon\Mvc\ModelInterface[] $related, \Phalcon\Support\Collection\CollectionInterface $visited): bool
```

Performs operations based on relationship types such as HAS_MANY, HAS_ONE, HAS_MANY_THROUGH, etc.
Handles automatic deletion of missing related records and ensures correct binding and transaction management.

NOTE: we need this, this behavior only happens:
- in many-to-many nodes
Fix uniqueness on combined keys in node entities, and possibly more...

**Parameters:**

| Parameter     | Type                                                | Description                                                  |
|---------------|-----------------------------------------------------|--------------------------------------------------------------|
| `$connection` | **\Phalcon\Db\Adapter\AdapterInterface**            | Database connection instance used for transactions.          |
| `$related`    | **array\|object[]\|\Phalcon\Mvc\ModelInterface[]**  | Related records to be saved, provided as arrays or objects.  |
| `$visited`    | **\Phalcon\Support\Collection\CollectionInterface** | A collection of already visited models to prevent recursion. |

**Return Value:**

Returns true on successful processing of related records, false if an error occurs.

**Throws:**

Throws an exception if there are no defined relations for a given alias or if invalid data types are provided.
- [`InvalidArgumentException`](../Exception/InvalidArgumentException.md)

**See Also:**

* https://forum.phalconphp.com/discussion/2190/many-to-many-expected-behaviour
* http://stackoverflow.com/questions/23374858/update-a-records-n-n-relationships
* https://github.com/phalcon/cphalcon/issues/2871

***

### postSaveRelatedRecordsAfter

Handles the saving process of related records after the parent record's save operation.

```php
public postSaveRelatedRecordsAfter(\Phalcon\Mvc\Model\RelationInterface $relation, array|object[]|\Phalcon\Mvc\ModelInterface[] $relatedRecords, \Phalcon\Support\Collection\CollectionInterface $visited): bool|null
```

It assigns referenced fields to the related records and ensures they are saved with proper relationships maintained.
If the relation is defined as `Through`, this method skips further processing.

**Parameters:**

| Parameter         | Type                                                | Description                                                             |
|-------------------|-----------------------------------------------------|-------------------------------------------------------------------------|
| `$relation`       | **\Phalcon\Mvc\Model\RelationInterface**            | The relation instance that provides information about the relationship. |
| `$relatedRecords` | **array\|object[]\|\Phalcon\Mvc\ModelInterface[]**  | An array of related records to be saved.                                |
| `$visited`        | **\Phalcon\Support\Collection\CollectionInterface** | A collection to track visited records to prevent infinite recursion.    |

**Return Value:**

Returns `true` if all related records are saved successfully, `false` if an error occurs during saving,
and `null` if the relation is of type `Through`.

**Throws:**

If there is an error during the save operation for a related record.
- [`InvalidArgumentException`](../Exception/InvalidArgumentException.md)

***

### postSaveRelatedThroughAfter

Handles saving related records for through relationships after the primary records have been saved.

```php
public postSaveRelatedThroughAfter(\Phalcon\Mvc\Model\RelationInterface $relation, array|object[]|\Phalcon\Mvc\ModelInterface[] $relatedRecords, \Phalcon\Support\Collection\CollectionInterface $visited): bool|null
```

Primarily used to manage intermediate models and ensure proper linkage and saving of related records
in many-to-many or has-one-through relationships.

**Parameters:**

| Parameter         | Type                                                | Description                                                                        |
|-------------------|-----------------------------------------------------|------------------------------------------------------------------------------------|
| `$relation`       | **\Phalcon\Mvc\Model\RelationInterface**            | The relation object defining the association details.                              |
| `$relatedRecords` | **array\|object[]\|\Phalcon\Mvc\ModelInterface[]**  | An array of related records to be processed and saved.                             |
| `$visited`        | **\Phalcon\Support\Collection\CollectionInterface** | A collection of visited records to maintain state and prevent circular references. |

**Return Value:**

Returns true if all related records and intermediate records were successfully saved.
Returns false if any save operation failed.
Returns null if the relation is not a through relationship.

**Throws:**

If the intermediate model or related records cannot be properly saved.
- [`InvalidArgumentException`](../Exception/InvalidArgumentException.md)

***

### findFirstByPrimaryKeys

Find the first record by its primary key attributes.

```php
public findFirstByPrimaryKeys(array $data, string|null $modelClass): \Phalcon\Mvc\ModelInterface|\Phalcon\Mvc\Model\Row|null
```

**Parameters:**

| Parameter     | Type             | Description                                                                                       |
|---------------|------------------|---------------------------------------------------------------------------------------------------|
| `$data`       | **array**        | The data containing the primary key values.                                                       |
| `$modelClass` | **string\|null** | The class name of the model to search for. If not provided, the current model class will be used. |

**Return Value:**

The found record entity.

***

### getEntityFromData

Get the entity object from the given data.

```php
public getEntityFromData(array $data, array $configuration = []): \Phalcon\Mvc\ModelInterface|\Phalcon\Mvc\Model\Row|null
```

It will try to find the existing record and then assign the new data.
- Will first try using the primary key of the related record
- Then will try using the defined relationship fields using the relationship alias

**Parameters:**

| Parameter        | Type      | Description                                                                                                                                                                                                                                                      |
|------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$data`          | **array** | The data array.                                                                                                                                                                                                                                                  |
| `$configuration` | **array** | The configuration options.
- alias: The alias name.
- fields: The fields array.
- modelClass: The model class.
- readFields: The read fields array.
- type: The relationship type.
- whiteList: The whitelist array.
- dataColumnMap: The data column map array. |

**Return Value:**

The entity object or null if not found.

***

### appendMessages

```php
public appendMessages(array $messages = [], ?string $context = null, ?int $index = null): void
```

**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$messages` | **array**   |             |
| `$context`  | **?string** |             |
| `$index`    | **?int**    |             |

***

### appendMessagesFromRecord

Appends messages from a record to the current messages container.

```php
public appendMessagesFromRecord(\Phalcon\Mvc\ModelInterface|null $record = null, string|null $context = null, int|null $index = null): void
```

**Parameters:**

| Parameter  | Type                                  | Description                                                          |
|------------|---------------------------------------|----------------------------------------------------------------------|
| `$record`  | **\Phalcon\Mvc\ModelInterface\|null** | The record from which to append the messages.                        |
| `$context` | **string\|null**                      | The context in which the messages should be added. Defaults to null. |
| `$index`   | **int\|null**                         | The index at which the messages should be added. Defaults to 0.      |

***

### appendMessagesFromResultset

Append messages from a resultset to the current message container.

```php
public appendMessagesFromResultset(\Phalcon\Mvc\Model\ResultsetInterface|null $resultset = null, string|null $context = null, int|null $index = null): void
```

**Parameters:**

| Parameter    | Type                                            | Description                                                                                                                          |
|--------------|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `$resultset` | **\Phalcon\Mvc\Model\ResultsetInterface\|null** | The resultset containing the messages to be appended. If not provided, no messages will be appended.                                 |
| `$context`   | **string\|null**                                | The context to assign to the appended messages. If not provided, the default context will be used.                                   |
| `$index`     | **int\|null**                                   | The index at which the messages should be inserted in the messages array. If not provided, the messages will be appended at the end. |

***

### appendMessagesFromRecordList

Appends messages from a record list to the current message container.

```php
public appendMessagesFromRecordList(iterable|null $recordList = null, string|null $context = null, int|null $index = null): void
```

**Parameters:**

| Parameter     | Type               | Description                                  |
|---------------|--------------------|----------------------------------------------|
| `$recordList` | **iterable\|null** | The list of records to append messages from. |
| `$context`    | **string\|null**   | The context to associate with the messages.  |
| `$index`      | **int\|null**      | The index to use for the messages.           |

***

### rebuildMessageContext

Rebuilds the message context.

```php
public rebuildMessageContext(\Phalcon\Messages\Message $message, string|null $context = null): string
```

This method appends the given context to the previous context stored in the message metadata.
If there is no previous context, only the given context is returned.

**Parameters:**

| Parameter  | Type                          | Description                                           |
|------------|-------------------------------|-------------------------------------------------------|
| `$message` | **\Phalcon\Messages\Message** | The message object whose context needs to be rebuilt. |
| `$context` | **string\|null**              | The context to be appended.                           |

**Return Value:**

The rebuilt context

***

### rebuildMessageIndex

Rebuilds the message index.

```php
public rebuildMessageIndex(\Phalcon\Messages\Message $message, int|null $index = null): string
```

This method constructs the new message index based on the provided $index argument
and the previous index stored in the message's metadata. It returns the new index
as a string.

**Parameters:**

| Parameter  | Type                          | Description                                               |
|------------|-------------------------------|-----------------------------------------------------------|
| `$message` | **\Phalcon\Messages\Message** | The message object for which the index is being rebuilt.  |
| `$index`   | **int\|null**                 | The new index to be assigned to the message. Can be null. |

**Return Value:**

The new index as a string

***

### relatedToArray

Retrieves the related records as an array.

```php
public relatedToArray(array|null $columns = null, bool $useGetter = true): array<string,mixed>
```

If $columns is provided, only the specified columns will be included in the array.
If $useGetter is set to true, it will use the getter methods of the related records.

**Parameters:**

| Parameter    | Type            | Description                                                                     |
|--------------|-----------------|---------------------------------------------------------------------------------|
| `$columns`   | **array\|null** | (optional) The columns to include in the array for each related record          |
| `$useGetter` | **bool**        | (optional) Whether to use getter methods of the related records (default: true) |

**Return Value:**

The related records as an array

***

### getRelated

Overriding default phalcon getRelated in order to fix an important issue
where the related record is being stored into the "related" property and then
passed from the collectRelatedToSave and is mistakenly saved without the user consent

```php
public getRelated(string $alias, mixed $arguments = null): mixed
```

**Parameters:**

| Parameter    | Type       | Description                                                                                                                                                                                                                           |
|--------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$alias`     | **string** |                                                                                                                                                                                                                                       |
| `$arguments` | **mixed**  |
Values populated by Phalcon 5.18's native eager loader are returned from
PhalconKit's read-only cache. Uncached relationships continue through
the models manager so they are never added to Phalcon's dirty relation
save pipeline. |

**Return Value:**

Cached related data or the models manager query result.

**Throws:**

- [`InvalidArgumentException`](../Exception/InvalidArgumentException.md)

***

### toArray

Returns the instance as an array representation

```php
public toArray(array $columns = null, bool $useGetter = true): array
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$columns`   | **array** |             |
| `$useGetter` | **bool**  |             |

***

### initializePosition

Initializes the position behavior for the current object.

```php
public initializePosition(array|null $options = null): void
```

Sets the position options and sets the position behavior accordingly.

**Parameters:**

| Parameter  | Type            | Description                                                                                                 |
|------------|-----------------|-------------------------------------------------------------------------------------------------------------|
| `$options` | **array\|null** | The options for the position behavior.
If not provided, the default position behavior options will be used. |

***

### setPositionBehavior

Sets the position behavior for the current object.

```php
public setPositionBehavior(\PhalconKit\Mvc\Model\Behavior\Position $positionBehavior): void
```

**Parameters:**

| Parameter           | Type                                        | Description                      |
|---------------------|---------------------------------------------|----------------------------------|
| `$positionBehavior` | **\PhalconKit\Mvc\Model\Behavior\Position** | The position behavior to be set. |

***

### getPositionBehavior

Retrieves the position behavior attached to the current object.

```php
public getPositionBehavior(): \PhalconKit\Mvc\Model\Behavior\Position
```

**Return Value:**

The position behavior object.

**Throws:**

if the position behavior is not found.
- [`LogicException`](../Exception/LogicException.md)

***

### reorder

Reorders the current object's position in the list.

```php
public reorder(int|null $position = null, string|null $positionField = null): bool
```

- Update position+1 done using afterSave event

**Parameters:**

| Parameter        | Type             | Description                                                                                            |
|------------------|------------------|--------------------------------------------------------------------------------------------------------|
| `$position`      | **int\|null**    | The new position for the object. If not provided, the default behavior's position field will be used.  |
| `$positionField` | **string\|null** | The field on which the position is stored. If not provided, the default behavior's field will be used. |

**Return Value:**

Returns true if the reorder operation was successful, false otherwise.

**Throws:**

When the trait is used on an incompatible model.
- [`LogicException`](../Exception/LogicException.md)

***

### requirePositionModel

Require the trait host to be a PhalconKit model.

```php
protected requirePositionModel(): \PhalconKit\Mvc\Model
```

Position reordering depends on model events, assignment, snapshots, and
persistence APIs. This helper keeps `reorder()` readable while producing
a deterministic PhalconKit exception if the trait is composed into an
incompatible class.

**Throws:**

When the trait host is not a PhalconKit model.
- [`LogicException`](../Exception/LogicException.md)

***

### initializeOptions

Initialize the Options Manager for the current instance

```php
public initializeOptions(): void
```

***

### getOptionsManager

Get the Options Manager for the current instance

```php
public getOptionsManager(): \PhalconKit\Support\Options\ManagerInterface
```

**Return Value:**

The Options Manager for the current instance

***

### setOptionsManager

Sets the options manager.

```php
public setOptionsManager(\PhalconKit\Support\Options\ManagerInterface $optionsManager): void
```

**Parameters:**

| Parameter         | Type                                             | Description                    |
|-------------------|--------------------------------------------------|--------------------------------|
| `$optionsManager` | **\PhalconKit\Support\Options\ManagerInterface** | The options manager to be set. |

***

### getColumnMap

Get the column mapping of the model

```php
public getColumnMap(): array|null
```

**Return Value:**

The column mapping of the model, or null if no mapping is defined

***

### getPrimaryKeys

Retrieves the primary keys attributes of the model.

```php
public getPrimaryKeys(): array
```

**Return Value:**

Array containing the primary keys of the model.

***

### getPrimaryKeysValues

Retrieves the values of the primary keys attributes of the entity.

```php
public getPrimaryKeysValues(): array
```

**Return Value:**

Array containing the values of the primary keys attributes of the entity.

***

### _

Translate a key through the model's translate service.

```php
public _(string $translateKey, array<array-key,mixed> $placeholders = []): string
```

This is a model-level convenience wrapper around Phalcon's translate
adapter. It keeps model validation messages and computed labels aligned
with the same `translate` service used by the rest of the application.

**Parameters:**

| Parameter       | Type                       | Description                               |
|-----------------|----------------------------|-------------------------------------------|
| `$translateKey` | **string**                 | Translation key to resolve.               |
| `$placeholders` | **array<array-key,mixed>** | Placeholder values passed to
the adapter. |

**Return Value:**

Translated string returned by the adapter.

**Throws:**

When the translate service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### __call

Dispatch missing method calls to locale-suffixed methods when available.

```php
public __call(string $method, array<array-key,mixed> $arguments): mixed
```

For example, with locale `fr`, a call to `label()` will try `labelFr()`
before delegating to the parent model magic handler. This is intended for
computed localized accessors, not for replacing explicit public methods.

**Parameters:**

| Parameter    | Type                       | Description                                                    |
|--------------|----------------------------|----------------------------------------------------------------|
| `$method`    | **string**                 | Missing method name.                                           |
| `$arguments` | **array<array-key,mixed>** | Arguments forwarded to the
localized method or parent handler. |

**Return Value:**

Localized method result, or the parent magic-call result.

**Throws:**

When the parent Phalcon model magic handler
rejects the missing method.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When the locale service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### __set

Handles dynamic model writes before Phalcon sees them.

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

Handles dynamic model reads before Phalcon sees them.

```php
public __get(string $property): mixed
```

**Parameters:**

| Parameter   | Type       | Description |
|-------------|------------|-------------|
| `$property` | **string** |             |

***

### prepareLifeCycleQuery

Apply safety defaults to a lifecycle query builder.

```php
public static prepareLifeCycleQuery(\Phalcon\Mvc\Model\Query\BuilderInterface $builder, array<string,mixed>|null $parameters = null): void
```

A model with no resolved policy query should never accidentally match all
records. When parameters are empty, the builder receives a `false`
condition and empty bind arrays so the resulting query is intentionally
empty.

* This method is **static**.
**Parameters:**

| Parameter     | Type                                          | Description                                                             |
|---------------|-----------------------------------------------|-------------------------------------------------------------------------|
| `$builder`    | **\Phalcon\Mvc\Model\Query\BuilderInterface** | Builder that will be executed by the
lifecycle task.                    |
| `$parameters` | **array<string,mixed>\|null**                 | Policy query parameters
resolved from config or supplied by the caller. |

***

### getLifeCyclePolicy

Return the lifecycle policy configured for the current model class.

```php
public static getLifeCyclePolicy(): array<string,mixed>
```

The config maps model class names to policy names under
`dataLifeCycle.models`; the policy payload is then read from
`dataLifeCycle.policies`. Missing mappings return an empty policy.

* This method is **static**.
**Return Value:**

Policy payload for the calling model class.

**Throws:**

When the default DI or config service cannot be
resolved through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getLifeCyclePolicyQuery

Return only the lifecycle query portion of the configured policy.

```php
public static getLifeCyclePolicyQuery(): array<string,mixed>|null
```

* This method is **static**.
**Return Value:**

Query definition accepted by Phalcon's
model query builder, or null when no policy query is configured.

**Throws:**

When the lifecycle policy cannot be resolved.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getLifeCycleQuery

Build the executable lifecycle query for the current model class.

```php
public static getLifeCycleQuery(array<string,mixed>|null $parameters = null, \Phalcon\Mvc\Model\Query\BuilderInterface|null $builder = null): \Phalcon\Mvc\Model\QueryInterface
```

Callers may pass explicit query parameters or a preconfigured builder for
tests and custom lifecycle workflows. When both are omitted, the
configured policy query is used.

* This method is **static**.
**Parameters:**

| Parameter     | Type                                                | Description                |
|---------------|-----------------------------------------------------|----------------------------|
| `$parameters` | **array<string,mixed>\|null**                       | Query parameters to apply. |
| `$builder`    | **\Phalcon\Mvc\Model\Query\BuilderInterface\|null** | Optional builder override. |

**Return Value:**

Executable query for lifecycle processing.

**Throws:**

When the default DI or models manager service
cannot be resolved through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getBuilder

Create a lifecycle query builder for the current model class.

```php
public static getBuilder(array<string,mixed>|null $parameters = null): \Phalcon\Mvc\Model\Query\BuilderInterface
```

The builder is initialized from the provided parameters and forced to use
the calling model class as its `from` model. A top-level `limit` parameter
is applied explicitly because Phalcon's builder parameters do not always
preserve that value when lifecycle tasks construct custom arrays.

* This method is **static**.
**Parameters:**

| Parameter     | Type                          | Description               |
|---------------|-------------------------------|---------------------------|
| `$parameters` | **array<string,mixed>\|null** | Query-builder parameters. |

**Return Value:**

Builder scoped to the calling model class.

**Throws:**

When the default DI or models manager service
cannot be resolved through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### findLifeCycle

Execute the lifecycle query and return matching records.

```php
public static findLifeCycle(array<string,mixed>|null $parameters = null): mixed
```

If a resultset is returned and the policy parameters include a
`hydration` value, the resultset hydrate mode is updated before returning
it to the caller. Non-resultset query outputs are returned untouched to
preserve native Phalcon behavior.

* This method is **static**.
**Parameters:**

| Parameter     | Type                          | Description                                                  |
|---------------|-------------------------------|--------------------------------------------------------------|
| `$parameters` | **array<string,mixed>\|null** | Query parameters or null to
use the configured policy query. |

**Return Value:**

Query execution result, usually a Phalcon model resultset.

**Throws:**

When the lifecycle query cannot be built because
required DI services are unavailable or incompatible.
- [`ServiceException`](../Exception/ServiceException.md)

***

### jsonEncode

Encodes a value to JSON.

```php
public jsonEncode(mixed $value, int $flags = \PhalconKit\Mvc\Model\Traits\JSON_UNESCAPED_SLASHES, int $depth = 512): string|false
```

**Parameters:**

| Parameter | Type      | Description                                                                              |
|-----------|-----------|------------------------------------------------------------------------------------------|
| `$value`  | **mixed** | The value to be encoded.                                                                 |
| `$flags`  | **int**   | [Optional] Bitmask of JSON encode options.
Defaults to JSON_UNESCAPED_SLASHES.           |
| `$depth`  | **int**   | [Optional] The maximum depth of recursion when encoding nested objects.
Defaults to 512. |

**Return Value:**

The JSON encoded string on success, or `false` on failure.

***

### jsonDecode

Decodes a JSON string.

```php
public jsonDecode(string $json, bool|null $associative = null, int $depth = 512, int $flags = 0): mixed
```

**Parameters:**

| Parameter      | Type           | Description                                                                                                                                                                                                              |
|----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$json`        | **string**     | The JSON string to be decoded.                                                                                                                                                                                           |
| `$associative` | **bool\|null** | [Optional] When `true`, returned objects will be converted into associative arrays.
When `false`, objects will be returned as generic objects. If `null`, objects
will be returned based on the JSON_NUMERIC_CHECK flag. |
| `$depth`       | **int**        | [Optional] The maximum depth of recursion when decoding nested objects.
Defaults to 512.                                                                                                                                 |
| `$flags`       | **int**        | [Optional] Bitmask of JSON decode options.
Defaults to 0.                                                                                                                                                                |

**Return Value:**

The decoded value on success, or the original JSON string on failure.

***

### validateJsonDepth

Validates that the provided depth is within the supported JSON recursion range.

```php
private validateJsonDepth(int $depth): int<1, 2147483647>
```

**Parameters:**

| Parameter | Type    | Description                      |
|-----------|---------|----------------------------------|
| `$depth`  | **int** | The recursion depth to validate. |

**Return Value:**

The validated depth.

**Throws:**

If depth is outside the valid range.
- [`InvalidArgumentException`](../Exception/InvalidArgumentException.md)

***

### loadInstance

```php
public static loadInstance(): static
```

* This method is **static**.
***

### getIdentityService

Resolve the current identity manager from the model DI.

```php
public getIdentityService(): \PhalconKit\Identity\ManagerInterface
```

The service must implement `PhalconKit\Identity\ManagerInterface`; this
allows applications to provide custom identity managers without extending
the concrete core manager class.

**Return Value:**

Current identity manager service.

**Throws:**

When the identity service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### isLoggedIn

Check whether the current identity is logged in.

```php
public isLoggedIn(bool $as = false): bool
```

**Parameters:**

| Parameter | Type     | Description                                                                          |
|-----------|----------|--------------------------------------------------------------------------------------|
| `$as`     | **bool** | When true, checks delegated/impersonated identity state
instead of the primary user. |

**Return Value:**

True when the requested identity state is authenticated.

**Throws:**

When the identity service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### isLoggedInAs

Check whether the current identity is acting as another user.

```php
public isLoggedInAs(): bool
```

**Return Value:**

True when a delegated/impersonated user is active.

**Throws:**

When the identity service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getCurrentUser

Return the current user model from the identity service.

```php
public getCurrentUser(bool $as = false): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type     | Description                                                                     |
|-----------|----------|---------------------------------------------------------------------------------|
| `$as`     | **bool** | When true, returns the delegated/impersonated user
instead of the primary user. |

**Return Value:**

Current user, delegated user, or null when no
matching identity is available.

**Throws:**

When the identity service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getCurrentUserAs

Return the delegated user model from the identity service.

```php
public getCurrentUserAs(): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Return Value:**

Delegated/impersonated user, or null when no
delegated identity is active.

**Throws:**

When the identity service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getCurrentUserId

Return the integer ID of the current or delegated user.

```php
public getCurrentUserId(bool $as = false): int|null
```

**Parameters:**

| Parameter | Type     | Description                                                                           |
|-----------|----------|---------------------------------------------------------------------------------------|
| `$as`     | **bool** | When true, returns the delegated/impersonated user ID
instead of the primary user ID. |

**Return Value:**

User ID cast to int, or null when no user is available
or the user does not expose an ID.

**Throws:**

When the identity service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getCurrentUserIdCallback

Build a callback that returns the current or delegated user ID.

```php
public getCurrentUserIdCallback(bool $as = false): callable
```

Behaviors can store this closure and evaluate it later during lifecycle
events, ensuring they use the identity state at execution time rather
than initialization time.

**Parameters:**

| Parameter | Type     | Description                                             |
|-----------|----------|---------------------------------------------------------|
| `$as`     | **bool** | When true, the callback resolves the delegated user ID. |

**Return Value:**

Callback returning the requested user ID or null.

***

### hash

Hash a string

```php
public hash(string $string, string|null $salt = null, string|null $workFactor = null): string
```

**Parameters:**

| Parameter     | Type             | Description                                                           |
|---------------|------------------|-----------------------------------------------------------------------|
| `$string`     | **string**       | The string to be hashed                                               |
| `$salt`       | **string\|null** | (optional) The salt value to be appended to the string before hashing |
| `$workFactor` | **string\|null** | (optional) The work factor to determine the hashing cost              |

**Return Value:**

The salted hash value of the input string

**Throws:**

When the config or security service cannot be
resolved through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### checkHash

Checks whether a given hash is valid for a given string.

```php
public checkHash(string|null $hash = null, string|null $string = null, int $maxPassLength = 0): bool
```

**Parameters:**

| Parameter        | Type             | Description                                                       |
|------------------|------------------|-------------------------------------------------------------------|
| `$hash`          | **string\|null** | The hash value to be checked.                                     |
| `$string`        | **string\|null** | The string to be hashed and checked against the given hash value. |
| `$maxPassLength` | **int**          | The maximum length of the password.                               |

**Return Value:**

Returns true if the hash is valid for the string, false otherwise.

**Throws:**

When the config or security service cannot be
resolved through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### findInById

```php
public static findInById(array $idList = []): \Phalcon\Mvc\Model\ResultsetInterface
```

* This method is **static**.
**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$idList` | **array** |             |

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

### fireEventCancel

```php
public fireEventCancel(string $eventName): bool
```

* This method is **abstract**.
**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$eventName` | **string** |             |

***

### ensureTraversableResultset

```php
private static ensureTraversableResultset(\Phalcon\Mvc\Model\ResultsetInterface $resultset): \Phalcon\Mvc\Model\ResultsetInterface&\Traversable
```

* This method is **static**.
**Parameters:**

| Parameter    | Type                                      | Description |
|--------------|-------------------------------------------|-------------|
| `$resultset` | **\Phalcon\Mvc\Model\ResultsetInterface** |             |

***

### find

Run Phalcon's native static finder for the model using this trait.

```php
public static find(mixed $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface
```

The explicit `mixed` parameter mirrors PhalconKit's patched
`phalcon/ide-stubs` contract for `Phalcon\Mvc\Model::find()`. Keeping the
abstract dependency in sync with the upstream model API prevents static
analyzers and downstream projects from seeing this trait as a narrower,
incompatible declaration.

Eager loading requires an iterable Phalcon resultset because
`findWith()` delegates the returned records to the eager-loading loader.

* This method is **static**.* This method is **abstract**.
**Parameters:**

| Parameter     | Type      | Description                                                                             |
|---------------|-----------|-----------------------------------------------------------------------------------------|
| `$parameters` | **mixed** | Native Phalcon find parameters, usually an
array, string, integer primary key, or null. |

**Return Value:**

Resultset returned by the concrete model
implementation.

***

### findFirst

Run Phalcon's native static first-record finder for the model using this trait.

```php
public static findFirst(mixed $parameters = null): mixed
```

Phalcon can return a model instance, a row, false, null, or another value
depending on hydration and extension behavior, so this dependency keeps
the same broad `mixed` return declared by the patched Phalcon stubs.
`findFirstWith()` narrows that value at runtime and only eager-loads when
a real model instance is returned.

* This method is **static**.* This method is **abstract**.
**Parameters:**

| Parameter     | Type      | Description                                                                                   |
|---------------|-----------|-----------------------------------------------------------------------------------------------|
| `$parameters` | **mixed** | Native Phalcon find-first parameters, usually an
array, string, integer primary key, or null. |

**Return Value:**

Native result returned by the concrete model implementation.

***

### count

Counts the number of records that match the given parameters.

```php
public static count(mixed $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface|int
```

This method wraps the core static `count` model call with beforeCount/afterCount cancellable events.
The "beforeCount" event can cancel the operation. Since Phalcon 5.16's
native contract cannot return false for count(), cancellation returns 0.

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                               |
|---------------|-----------|-------------------------------------------|
| `$parameters` | **mixed** | Optional native Phalcon count parameters. |

**Return Value:**

The count result or a ResultsetInterface, depending on the implementation.

**See Also:**

* \Phalcon\Mvc\Model::count()

***

### sum

Executes a sum operation on the underlying data with optional parameters.

```php
public static sum(mixed $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface|float
```

This method supports cancellable events triggered before and after execution.
If the "beforeSum" event cancels the operation, this method returns 0.0
to satisfy Phalcon 5.16's native return contract.

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                             |
|---------------|-----------|-----------------------------------------|
| `$parameters` | **mixed** | Optional native Phalcon sum parameters. |

**Return Value:**

Returns the sum result as a float or a result set interface.

**See Also:**

* \Phalcon\Mvc\Model::sum()

***

### average

Calculates the average of results based on the provided parameters. It wraps the method execution
with before/after cancellable events.

```php
public static average(array $parameters = []): \Phalcon\Mvc\Model\ResultsetInterface|float
```

Example events triggered:
- beforeAverage()
- afterAverage()

If the "beforeAverage" event cancels the operation, 0.0 is returned to
satisfy Phalcon 5.16's native return contract.

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                    |
|---------------|-----------|----------------------------------------------------------------|
| `$parameters` | **array** | Parameters to define the criteria for calculating the average. |

**Return Value:**

The calculated average or a ResultsetInterface, depending on the implementation.

**See Also:**

* \Phalcon\Mvc\Model::average()

***

### minimum

Calculates the minimum value of a specified column in the database according to the given conditions.

```php
public static minimum(mixed $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                                                           |
|---------------|-----------|-------------------------------------------------------------------------------------------------------|
| `$parameters` | **mixed** | Native Phalcon parameters to customize the query,
such as conditions, column selection, or groupings. |

**Return Value:**

Returns the minimum value as a float, a ResultsetInterface object, or false if no matching records are found or the operation fails.

***

### maximum

Calculates the maximum value of a specified column in the database based on the given conditions.

```php
public static maximum(mixed $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                                                           |
|---------------|-----------|-------------------------------------------------------------------------------------------------------|
| `$parameters` | **mixed** | Native Phalcon parameters to customize the query,
such as conditions, column selection, or groupings. |

**Return Value:**

Returns the computed maximum value as a float, a ResultsetInterface object for detailed results, or false on failure.

***

### fireEventCancelCall

Wraps core static model calls (find, findFirst, count, sum, average, minimum, maximum)
 with beforeX/afterX cancellable events.

```php
public static fireEventCancelCall(string $method, callable $callable): mixed
```

Example (beforeX/afterX events):
- beforeAverage()
- beforeSum()
- beforeCount()
- beforeFind()
- beforeFindFirst()
- afterAverage()
- afterSum()
- afterCount()
- afterFind()
- afterFindFirst()

Returns false if the "beforeX" event cancels the operation. Callers
whose native Phalcon contracts cannot return false must normalize this
sentinel before returning.

* This method is **static**.
**Parameters:**

| Parameter   | Type         | Description |
|-------------|--------------|-------------|
| `$method`   | **string**   |             |
| `$callable` | **callable** |             |

***

### findWith

Example:

```php
public static findWith(array $arguments): array
```

```php
$limit = 100;
$offset = max(0, $this->request->getQuery('page', 'int') - 1) * $limit;

$manufacturers = Manufacturer::with('Robots.Parts', [
    'limit' => [$limit, $offset]
]);

foreach ($manufacturers as $manufacturer) {
    foreach ($manufacturer->robots as $robot) {
        foreach ($robot->parts as $part) { ... }
    }
}
```

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***

### findFirstWith

Same as EagerLoadingTrait::findWith() for a single record

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

* This method is **static**.* **Warning:** this method is **deprecated**. This means that this method will likely be removed in a future version.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

**See Also:**

* static::findWith()

***

### firstWith

```php
public static firstWith(array $arguments): ?\Phalcon\Mvc\ModelInterface
```

* This method is **static**.* **Warning:** this method is **deprecated**. This means that this method will likely be removed in a future version.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

**See Also:**

* static::findFirstWith()

***

### __callStatic

Dynamically handles static method calls for the class, forwarding them to
appropriate internal methods based on the method name patterns.

```php
public static __callStatic(string $method, array $arguments = []): array|\Phalcon\Mvc\ModelInterface|null
```

The method provides a mechanism to resolve calls like "findFirstWithBy..."/"firstWithBy..."
and "findWithBy..."/"withBy..." to their corresponding mapped operations.

The static magic method keeps the existing PhalconKit `findWithBy*`
surface. Moving this to native `missingMethods()` remains a compatibility
decision because it would change where dynamic calls are intercepted.

* This method is **static**.
**Parameters:**

| Parameter    | Type       | Description                                        |
|--------------|------------|----------------------------------------------------|
| `$method`    | **string** | The name of the static method being called.        |
| `$arguments` | **array**  | An array of arguments passed to the static method. |

**Return Value:**

Returns the result of the forwarded operation, which may be
an array, an implementation of ModelInterface, or null.

***

### findFirstWithBy

Call native Phalcon FindFirstBy function then eager load relationships from the model

```php
protected static findFirstWithBy(string $forwardMethod, array $arguments): ?\Phalcon\Mvc\ModelInterface
```

* This method is **static**.
**Parameters:**

| Parameter        | Type       | Description |
|------------------|------------|-------------|
| `$forwardMethod` | **string** |             |
| `$arguments`     | **array**  |             |

***

### findWithBy

Call native Phalcon findBy function then eager load relationships from the resultset

```php
protected static findWithBy(string $forwardMethod, array $arguments): ?array
```

* This method is **static**.
**Parameters:**

| Parameter        | Type       | Description |
|------------------|------------|-------------|
| `$forwardMethod` | **string** |             |
| `$arguments`     | **array**  |             |

***

### load

Example:

```php
public load(array $arguments): ?\Phalcon\Mvc\ModelInterface
```

```php
$manufacturer = Manufacturer::findFirstById(51);

$manufacturer->load('Robots.Parts');

foreach ($manufacturer->robots as $robot) {
   foreach ($robot->parts as $part) { ... }
}
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***

### getParametersFromArguments

Get the query parameters from a list of arguments

```php
public static getParametersFromArguments(array& $arguments): mixed
```

The final argument is treated as the native Phalcon finder parameters
when at least two arguments were passed. Eager loading needs complete
parent models so relation keys are available, therefore custom `columns`
selections are expanded to include `*` before the parameters are passed
to `find()` or `findFirst()`. Native Phalcon accepts both array and
string column definitions, so both shapes are normalized without changing
any other finder options.

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***

### subCount

Count rows through a subquery generated by the models manager.

```php
public static subCount(mixed $find): int
```

The supplied find definition is converted to a query builder for the
calling model class, compiled to SQL, and wrapped in
`SELECT COUNT(*) FROM (...)`. Bind parameters and bind types are reused
from the generated query.

* This method is **static**.
**Parameters:**

| Parameter | Type      | Description                                                                                                                                                           |
|-----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$find`   | **mixed** | Phalcon find parameters accepted by the models manager
builder. Non-array values are wrapped as a single-item parameter
array for compatibility with model find APIs. |

**Return Value:**

Total row count reported by the database.

**Throws:**

When the default DI, models manager, or database
service cannot be resolved through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### initializeCache

Initialize model cache invalidation for the current model.

```php
public initializeCache(): void
```

The `models` service supplies framework model class mappings used for
the default blacklist. After the blacklist is prepared, the trait adds
the flush behavior unless this model instance or class is excluded.

**Throws:**

When the models service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### addFlushCacheBehavior

Add an after-event behavior that clears the shared models cache.

```php
public addFlushCacheBehavior(array<int,class-string|object|string>|null $flushModelsCacheBlackList = null): void
```

The behavior is skipped when `preventFlushCache` is true or the current
model is an instance of one of the blacklisted classes. Cache clearing is
attempted only when snapshots indicate that persisted data changed.

**Parameters:**

| Parameter                    | Type                                              | Description                                                                              |
|------------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------|
| `$flushModelsCacheBlackList` | **array<int,class-string\|object\|string>\|null** |
Classes that should not receive the flush behavior. Defaults to the
instance blacklist. |

**Throws:**

When the modelsCache service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### isInstanceOf

Check whether a model instance belongs to any configured class.

```php
public isInstanceOf(array<int,mixed> $classes = [], \Phalcon\Mvc\ModelInterface|null $that = null): bool
```

This helper supports cache blacklist checks while allowing tests or
callers to pass an explicit instance. Invalid values are ignored instead
of being passed to `instanceof`, because a malformed application-provided
blacklist entry should not turn cache-behavior initialization into a PHP
fatal error.

**Parameters:**

| Parameter  | Type                                  | Description                                                           |
|------------|---------------------------------------|-----------------------------------------------------------------------|
| `$classes` | **array<int,mixed>**                  | Class names, objects, or ignored
malformed values to compare against. |
| `$that`    | **\Phalcon\Mvc\ModelInterface\|null** | Optional model instance to inspect.
Defaults to the current model.    |

**Return Value:**

True when the model is an instance of at least one class.

***

### initializeBlameable

Initialize the blameable behavior and user relationship.

```php
public initializeBlameable(array<array-key,mixed>|null $options = null): void
```

When no options are provided, the trait reads `blameable` options from
the model options manager. Missing audit, audit-detail, and user classes
are filled from the PhalconKit `models` service so applications using
custom model classes keep one central mapping.

**Parameters:**

| Parameter  | Type                             | Description                                                                                                                                                                                                                                   |
|------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$options` | **array<array-key,mixed>\|null** | Behavior options. Common
keys include `auditClass`, `auditDetailClass`, `userClass`,
`userField`, `auditEnabled`, and `auditDetailEnabled`. Audit is
opt-in; set `auditEnabled` to `true` for applications that install
and use audit tables. |

**Throws:**

When the models service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../Exception/ServiceException.md)

***

### setBlameableBehavior

Register the blameable behavior under the standard behavior name.

```php
public setBlameableBehavior(\PhalconKit\Mvc\Model\Behavior\Blameable $blameableBehavior): void
```

The behavior is stored in the PhalconKit model behavior registry as
`blameable`, which lets other traits and application code retrieve the
same instance later.

**Parameters:**

| Parameter            | Type                                         | Description                   |
|----------------------|----------------------------------------------|-------------------------------|
| `$blameableBehavior` | **\PhalconKit\Mvc\Model\Behavior\Blameable** | Configured behavior instance. |

**Throws:**

When the current models manager does not expose
the PhalconKit behavior registry.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getBlameableBehavior

Retrieve the registered blameable behavior.

```php
public getBlameableBehavior(): \PhalconKit\Mvc\Model\Behavior\Blameable
```

**Throws:**

When the current models manager does not expose
the PhalconKit behavior registry.
- [`ServiceException`](../Exception/ServiceException.md)

***

### addUserRelationship

Add a user relationship when the configured attribution field exists.

```php
public addUserRelationship(string $field = 'userId', string $alias = 'UserEntity', array<array-key,mixed> $params = [], string $ref = 'id', string $type = 'belongsTo', string|null $class = null): \Phalcon\Mvc\Model\Relation|null
```

**Parameters:**

| Parameter | Type                       | Description                                                                              |
|-----------|----------------------------|------------------------------------------------------------------------------------------|
| `$field`  | **string**                 |                                                                                          |
| `$alias`  | **string**                 | The alias name for the user entity. Default is 'UserEntity'.                             |
| `$params` | **array<array-key,mixed>** | Additional relationship
parameters.                                                      |
| `$ref`    | **string**                 | The reference field in the user entity. Default is 'id'.                                 |
| `$type`   | **string**                 | Relationship method to call on the model, usually
`belongsTo`.                           |
| `$class`  | **string\|null**           | User model class. When null, the class is
resolved from the PhalconKit `models` service. |

**Return Value:**

Created relationship, or null when the model does
not expose the configured attribution field.

**Throws:**

When the models service cannot be resolved while
deriving the default user class.
- [`ServiceException`](../Exception/ServiceException.md)

***

### getAttribute

Returns the value of the specified attribute.

```php
public getAttribute(string $attribute): mixed|null
```

**Parameters:**

| Parameter    | Type       | Description                |
|--------------|------------|----------------------------|
| `$attribute` | **string** | The name of the attribute. |

**Return Value:**

The value of the specified attribute if it exists, otherwise null.

***

### setAttribute

Sets the value of the specified attribute.

```php
public setAttribute(string $attribute, mixed $value): void
```

**Parameters:**

| Parameter    | Type       | Description                            |
|--------------|------------|----------------------------------------|
| `$attribute` | **string** | The name of the attribute.             |
| `$value`     | **mixed**  | The value to be set for the attribute. |

***

### save

```php
public save(): bool
```

***

### create

```php
public create(): bool
```

***

### update

```php
public update(): bool
```

***

### doSave

```php
public doSave(\Phalcon\Support\Collection\CollectionInterface $visited): bool
```

**Parameters:**

| Parameter  | Type                                                | Description |
|------------|-----------------------------------------------------|-------------|
| `$visited` | **\Phalcon\Support\Collection\CollectionInterface** |             |

***

### initialize

```php
public initialize(): void
```

***

### normalizeNullableNullStrings

```php
protected normalizeNullableNullStrings(): void
```

***

### setup

Enables/disables options in the ORM
- We do this here in order to keep behaviour consistencies between different environments
--------------------------------
 caseInsensitiveColumnMap - false - Case insensitive column map
 castLastInsertIdToInt - false - Casts the lastInsertId to an integer
 castOnHydrate - false - Automatic cast to original types on hydration
 columnRenaming - true - Column renaming
 disableAssignSetters - false - Disable setters
 enableImplicitJoins - true - Enable implicit joins
 events - true - Callbacks, hooks and event notifications from all the models
 exceptionOnFailedMetaDataSave - false - Throw an exception when there is a failed meta-data save
 exceptionOnFailedSave - false - Throw an exception when there is a failed save()
 ignoreUnknownColumns - false - Ignore unknown columns on the model
 lateStateBinding - false - Late state binding of the Phalcon\Mvc\Model::cloneResultMap() method
 notNullValidations - true - Automatically validate the not null columns present
 phqlLiterals - true - Literals in the PHQL parser
 prefetchRecords - 0 - The number of records to prefetch when getting data from the ORM
 updateSnapshotOnSave - true - Update snapshots on save()
 virtualForeignKeys - true - Virtual foreign keys
--------------------------------

```php
public static setup(array|null $options = null): void
```

* This method is **static**.
**Parameters:**

| Parameter  | Type            | Description |
|------------|-----------------|-------------|
| `$options` | **array\|null** |             |

**See Also:**

* https://docs.phalcon.io/5.18/db-models#model-features

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

### addDefaultRelationships

Adds the default relationships to the model.

```php
public addDefaultRelationships(): void
```

***

### addDefaultValidations

Adds the default validations to the model.

```php
public addDefaultValidations(\PhalconKit\Filter\Validation|null $validator = null): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter    | Type                                    | Description |
|--------------|-----------------------------------------|-------------|
| `$validator` | **\PhalconKit\Filter\Validation\|null** |             |

***

### columnMap

Returns an array that maps the column names of the database
table to the corresponding property names of the model.

```php
public columnMap(): array
```

***
