
Class BackupAbstract

This class defines a Backup abstract model that extends the AbstractModel class and implements the BackupAbstractInterface.
It provides properties and methods for managing Backup data.

***

* Full name: `\PhalconKit\Models\Abstracts\BackupAbstract`
* Parent class: [`\PhalconKit\Models\AbstractModel`](../AbstractModel.md)
* This class implements:
  [`\PhalconKit\Models\Abstracts\Interfaces\BackupAbstractInterface`](./Interfaces/BackupAbstractInterface.md)
* This class is an **Abstract class**

## Properties

### id

Column: id
Attributes: First \| Primary \| NotNull \| Numeric \| Unsigned \| AutoIncrement \| Size(1) \| Type(14)

```php
public mixed $id
```

***

### uuid

Column: uuid
Attributes: NotNull \| Size(36) \| Type(5)

```php
public mixed $uuid
```

***

### label

Column: label
Attributes: NotNull \| Size(120) \| Type(2)

```php
public mixed $label
```

***

### deleted

Column: deleted
Attributes: NotNull \| Numeric \| Unsigned \| Size(1) \| Type(26)

```php
public mixed $deleted
```

***

### createdAt

Column: created_at
Attributes: NotNull \| Type(4)

```php
public mixed $createdAt
```

***

### createdBy

Column: created_by
Attributes: Numeric \| Unsigned \| Size(1) \| Type(14)

```php
public mixed $createdBy
```

***

### updatedAt

Column: updated_at
Attributes: Type(4)

```php
public mixed $updatedAt
```

***

### updatedBy

Column: updated_by
Attributes: Numeric \| Unsigned \| Size(1) \| Type(14)

```php
public mixed $updatedBy
```

***

### deletedAt

Column: deleted_at
Attributes: Type(4)

```php
public mixed $deletedAt
```

***

### deletedBy

Column: deleted_by
Attributes: Numeric \| Unsigned \| Size(1) \| Type(14)

```php
public mixed $deletedBy
```

***

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

### getLabel

Returns the value of the field "label"
Column: label
Attributes: NotNull \| Size(120) \| Type(2)

```php
public getLabel(): mixed
```

***

### setLabel

Sets the value of the field "label"
Column: label
Attributes: NotNull \| Size(120) \| Type(2)

```php
public setLabel(mixed $label): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$label`  | **mixed** |             |

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

## Inherited methods

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
public addStringLengthValidation(\PhalconKit\Filter\Validation $validator, array|string $field, int $minChar, int $maxChar = 255, bool $allowEmpty = true): \PhalconKit\Filter\Validation
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
public addDateValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true, string $format = Column::DATE_FORMAT): \PhalconKit\Filter\Validation
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
public addDateTimeValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true, string $format = Column::DATETIME_FORMAT): \PhalconKit\Filter\Validation
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
public addJsonValidation(\PhalconKit\Filter\Validation $validator, array|string $field, bool $allowEmpty = true, int $depth = 512, int $flags): \PhalconKit\Filter\Validation
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

Initializing Uuid

```php
public initializeUuid(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### getBinaryUuid

Get Binary Uuid

```php
private getBinaryUuid(string $uuid): string
```

**Parameters:**

| Parameter | Type       | Description                                         |
|-----------|------------|-----------------------------------------------------|
| `$uuid`   | **string** | The UUID string to convert to binary representation |

**Return Value:**

The binary representation of the given UUID

***

### setUuidBehavior

Set Uuid Behavior

```php
public setUuidBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $uuidBehavior): void
```

**Parameters:**

| Parameter       | Type                                             | Description |
|-----------------|--------------------------------------------------|-------------|
| `$uuidBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** |             |

***

### getUuidBehavior

Get Uuid Behavior

```php
public getUuidBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

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

```php
public setConnectionService(string $connectionService): void
```

* This method is **abstract**.
**Parameters:**

| Parameter            | Type       | Description |
|----------------------|------------|-------------|
| `$connectionService` | **string** |             |

***

### setReadConnectionService

```php
public setReadConnectionService(string $connectionService): void
```

* This method is **abstract**.
**Parameters:**

| Parameter            | Type       | Description |
|----------------------|------------|-------------|
| `$connectionService` | **string** |             |

***

### setWriteConnectionService

```php
public setWriteConnectionService(string $connectionService): void
```

* This method is **abstract**.
**Parameters:**

| Parameter            | Type       | Description |
|----------------------|------------|-------------|
| `$connectionService` | **string** |             |

***

### getWriteConnectionService

```php
public getWriteConnectionService(): string
```

* This method is **abstract**.
***

### getReadConnectionService

```php
public getReadConnectionService(): string
```

* This method is **abstract**.
***

### getReplicationLag

Get the replication lag value in milliseconds

```php
public static getReplicationLag(): ?int
```

* This method is **static**.
***

### setReplicationLag

Set the replication lag value in milliseconds

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

Get the replication lag value in milliseconds

```php
public static getReplicationReadyAt(): ?int
```

* This method is **static**.
***

### setReplicationReadyAt

Set the replication lag value in milliseconds

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

Replication Trait Initialization
- Set Read & Write Connection Service
- Add Replication Behavior

```php
public initializeReplication(?array $options = null): void
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$options` | **?array** |             |

***

### selectReadConnection

Dynamically selects a shard
- Prefer to read on the write master during the replica delay

```php
public selectReadConnection(): \Phalcon\Db\Adapter\AdapterInterface
```

Possible parameters which can be added if required
?array $intermediate = null, array $bindParams = [], array $bindTypes = []

***

### addReadWriteConnectionBehavior

Force write connection service to master if the model was previously saved

```php
public addReadWriteConnectionBehavior(): void
```

***

### isReplicationReady

Check whether the replica should be ready or not

```php
public isReplicationReady(): bool
```

**Return Value:**

true if replica should be ready

***

### nowMs

```php
protected static nowMs(): int
```

* This method is **static**.
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
public getKeepMissingRelated(): array
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
public getDirtyRelated(): array
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

- [`Exception`](../../../Exception.md)

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

- [`Exception`](../../../Exception.md)

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

- [`Exception`](../../../Exception.md)

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
- [`Exception`](../../../Exception.md)

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
- [`Exception`](../../../Exception.md)

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
- [`Exception`](../../../Exception.md)

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
public relatedToArray(array|null $columns = null, bool $useGetter = true): array
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
public getRelated(string $alias, mixed $arguments = null): false|int|\Phalcon\Mvc\Model\Resultset\Simple
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$alias`     | **string** |             |
| `$arguments` | **mixed**  |             |

**Throws:**

- [`Exception`](../../../Exception.md)

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

**Throws:**

- [`Exception`](../../../Exception.md)

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
- [`Exception`](../../../Exception.md)

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

- [`Exception`](../../../Exception.md)

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

Translate a given key using the translation service

```php
public _(string $translateKey, array $placeholders = []): string
```

**Parameters:**

| Parameter       | Type       | Description                                        |
|-----------------|------------|----------------------------------------------------|
| `$translateKey` | **string** | The key to be translated                           |
| `$placeholders` | **array**  | The placeholders to be replaced in the translation |

**Return Value:**

The translated string

***

### __call

Magic method to dynamically call localed named methods using the current locale
- Allow to call $this->methodName{Fr\|En\|Sp\|...}() from missing methodName method

```php
public __call(string $method, array $arguments): mixed|null
```

**Parameters:**

| Parameter    | Type       | Description      |
|--------------|------------|------------------|
| `$method`    | **string** | method name      |
| `$arguments` | **array**  | method arguments |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### __set

Magic setter to set localed named field automatically using the current locale
- Allow to set $this->name{Fr\|En\|Sp\|...} for missing name property

```php
public __set(string $property, mixed $value): void
```

**Parameters:**

| Parameter   | Type       | Description                      |
|-------------|------------|----------------------------------|
| `$property` | **string** | property name                    |
| `$value`    | **mixed**  | value to be set for the property |

***

### __get

Magic getter to get localed named field automatically using the current locale
- Allow to get $this->name{Fr\|En\|Sp\|...} from missing name property

```php
public __get(string $property): mixed
```

**Parameters:**

| Parameter   | Type       | Description   |
|-------------|------------|---------------|
| `$property` | **string** | property name |

***

### prepareLifeCycleQuery

Return the query for data retention

```php
public static prepareLifeCycleQuery(\Phalcon\Mvc\Model\Query\BuilderInterface $builder, ?array $parameters = null): void
```

* This method is **static**.
**Parameters:**

| Parameter     | Type                                          | Description |
|---------------|-----------------------------------------------|-------------|
| `$builder`    | **\Phalcon\Mvc\Model\Query\BuilderInterface** |             |
| `$parameters` | **?array**                                    |             |

***

### getLifeCyclePolicy

```php
public static getLifeCyclePolicy(): array
```

* This method is **static**.
***

### getLifeCyclePolicyQuery

```php
public static getLifeCyclePolicyQuery(): ?array
```

* This method is **static**.
***

### getLifeCycleQuery

Return the Query for data retention

```php
public static getLifeCycleQuery(?array $parameters = null, ?\Phalcon\Mvc\Model\Query\BuilderInterface $builder = null): \Phalcon\Mvc\Model\QueryInterface
```

* This method is **static**.
**Parameters:**

| Parameter     | Type                                           | Description |
|---------------|------------------------------------------------|-------------|
| `$parameters` | **?array**                                     |             |
| `$builder`    | **?\Phalcon\Mvc\Model\Query\BuilderInterface** |             |

***

### getBuilder

Return a Query Builder based on parameters

```php
public static getBuilder(?array $parameters = null): \Phalcon\Mvc\Model\Query\BuilderInterface
```

* This method is **static**.
**Parameters:**

| Parameter     | Type       | Description |
|---------------|------------|-------------|
| `$parameters` | **?array** |             |

***

### findLifeCycle

Find records to hard delete for data retention purpose

```php
public static findLifeCycle(?array $parameters = null): mixed
```

* This method is **static**.
**Parameters:**

| Parameter     | Type       | Description |
|---------------|------------|-------------|
| `$parameters` | **?array** |             |

***

### jsonEncode

Encodes a value to JSON.

```php
public jsonEncode(mixed $value, int $flags = JSON_UNESCAPED_SLASHES, int $depth = 512): string|false
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
public jsonDecode(string $json, bool|null $associative = null, int $depth = 512, int $flags): mixed
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
- [`InvalidArgumentException`](../../../InvalidArgumentException.md)

***

### loadInstance

```php
public static loadInstance(): static
```

* This method is **static**.
***

### getIdentityService

Get the current identity service from the DI

```php
public getIdentityService(): \PhalconKit\Identity\Manager
```

***

### isLoggedIn

Check if a user is logged in

```php
public isLoggedIn(bool $as = false): bool
```

**Parameters:**

| Parameter | Type     | Description                                               |
|-----------|----------|-----------------------------------------------------------|
| `$as`     | **bool** | Optional parameter to specify the identity state to check |

**Return Value:**

Returns true if the user is logged in, false otherwise

***

### isLoggedInAs

Check if the user is logged in as another user.

```php
public isLoggedInAs(): bool
```

**Return Value:**

True if the user is logged in as another user, false otherwise.

***

### getCurrentUser

Get the current user.

```php
public getCurrentUser(bool $as = false): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type     | Description                                                 |
|-----------|----------|-------------------------------------------------------------|
| `$as`     | **bool** | If true, return the UserInterface object. Default is false. |

**Return Value:**

Returns the current user as a UserInterface object if $as is true.
Returns null if there is no current user or the user is not found.

***

### getCurrentUserAs

Get the current delegated UserInterface object

```php
public getCurrentUserAs(): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Return Value:**

The current user as UserInterface if available, null otherwise

***

### getCurrentUserId

Retrieves the ID of the currently logged-in user.

```php
public getCurrentUserId(bool $as = false): int|null
```

**Parameters:**

| Parameter | Type     | Description                                                                                                                                                                             |
|-----------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$as`     | **bool** | Optional flag indicating whether to retrieve the user as well.
If set to true, the complete user object will be returned.
If set to false (default), only the user ID will be returned. |

**Return Value:**

If $as is true, it returns the ID of the currently logged-in user as an integer.
If $as is false, it returns null if there is no logged-in user or
the ID of the currently logged-in user as an integer.

***

### getCurrentUserIdCallback

Retrieves a callback function that returns the ID of the currently logged-in user.

```php
public getCurrentUserIdCallback(bool $as = false): \Closure
```

**Parameters:**

| Parameter | Type     | Description                                                                                                                                                                             |
|-----------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$as`     | **bool** | Optional flag indicating whether to retrieve the user as well.
If set to true, the complete user object will be returned.
If set to false (default), only the user ID will be returned. |

**Return Value:**

A callback function that, when invoked, returns the ID of the currently logged-in user.
The returned ID will be null if there is no logged-in user or an integer if the user is logged in.

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

***

### checkHash

Checks whether a given hash is valid for a given string.

```php
public checkHash(string|null $hash = null, string|null $string = null, int $maxPassLength): bool
```

**Parameters:**

| Parameter        | Type             | Description                                                       |
|------------------|------------------|-------------------------------------------------------------------|
| `$hash`          | **string\|null** | The hash value to be checked.                                     |
| `$string`        | **string\|null** | The string to be hashed and checked against the given hash value. |
| `$maxPassLength` | **int**          | The maximum length of the password.                               |

**Return Value:**

Returns true if the hash is valid for the string, false otherwise.

***

### findInById

```php
public static findInById(array $idList = []): array|\Phalcon\Mvc\Model\Resultset|false
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

### find

```php
public static find(mixed $parameters = null): mixed
```

* This method is **static**.* This method is **abstract**.
**Parameters:**

| Parameter     | Type      | Description |
|---------------|-----------|-------------|
| `$parameters` | **mixed** |             |

***

### findFirst

```php
public static findFirst(mixed $parameters = null): mixed
```

* This method is **static**.* This method is **abstract**.
**Parameters:**

| Parameter     | Type      | Description |
|---------------|-----------|-------------|
| `$parameters` | **mixed** |             |

***

### count

Counts the number of records that match the given parameters.

```php
public static count(array|null|string $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface|int|false
```

This method wraps the core static `count` model call with beforeCount/afterCount cancellable events.
The "beforeCount" event can cancel the operation by returning false.

* This method is **static**.
**Parameters:**

| Parameter     | Type                    | Description                                        |
|---------------|-------------------------|----------------------------------------------------|
| `$parameters` | **array\|null\|string** | Optional parameters to filter the count operation. |

**Return Value:**

The count result or a ResultsetInterface, depending on the implementation.

**See Also:**

* \Phalcon\Mvc\Model::count()

***

### sum

Executes a sum operation on the underlying data with optional parameters.

```php
public static sum(array $parameters = []): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

This method supports cancellable events triggered before and after execution.
If the "beforeSum" event cancels the operation, this method returns false.

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                         |
|---------------|-----------|-----------------------------------------------------|
| `$parameters` | **array** | Optional parameters to customize the sum operation. |

**Return Value:**

Returns the sum result as a float, a result set interface, or false if the operation is canceled.

**See Also:**

* \Phalcon\Mvc\Model::sum()

***

### average

Calculates the average of results based on the provided parameters. It wraps the method execution
with before/after cancellable events.

```php
public static average(array $parameters = []): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

Example events triggered:
- beforeAverage()
- afterAverage()

If the "beforeAverage" event cancels the operation, false is returned.

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
public static minimum(array $parameters = []): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                                            |
|---------------|-----------|----------------------------------------------------------------------------------------|
| `$parameters` | **array** | Parameters to customize the query, such as conditions, column selection, or groupings. |

**Return Value:**

Returns the minimum value as a float, a ResultsetInterface object, or false if no matching records are found or the operation fails.

***

### maximum

Calculates the maximum value of a specified column in the database based on the given conditions.

```php
public static maximum(array $parameters = []): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **static**.
**Parameters:**

| Parameter     | Type      | Description                                                                            |
|---------------|-----------|----------------------------------------------------------------------------------------|
| `$parameters` | **array** | Parameters to customize the query, such as conditions, column selection, or groupings. |

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

Returns false if the "beforeX" event cancels the operation.

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

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***

### subCount

```php
public static subCount(mixed $find): int
```

* This method is **static**.
**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$find`   | **mixed** |             |

***

### initializeCache

Initializing Cache

```php
public initializeCache(): void
```

***

### addFlushCacheBehavior

Adding Cache Behavior

```php
public addFlushCacheBehavior(?array $flushModelsCacheBlackList = null): void
```

**Parameters:**

| Parameter                    | Type       | Description |
|------------------------------|------------|-------------|
| `$flushModelsCacheBlackList` | **?array** |             |

***

### isInstanceOf

Check whether the current instance is any of the classes

```php
public isInstanceOf(array $classes = [], ?\Phalcon\Mvc\ModelInterface $that = null): bool
```

**Parameters:**

| Parameter  | Type                             | Description |
|------------|----------------------------------|-------------|
| `$classes` | **array**                        |             |
| `$that`    | **?\Phalcon\Mvc\ModelInterface** |             |

***

### initializeBlameable

Initialize Blameable

```php
public initializeBlameable(array|null $options = null): void
```

**Parameters:**

| Parameter  | Type            | Description                       |
|------------|-----------------|-----------------------------------|
| `$options` | **array\|null** | Options for the BlameableBehavior |

***

### setBlameableBehavior

Set Blameable Behavior.

```php
public setBlameableBehavior(\PhalconKit\Mvc\Model\Behavior\Blameable $blameableBehavior): void
```

**Parameters:**

| Parameter            | Type                                         | Description                              |
|----------------------|----------------------------------------------|------------------------------------------|
| `$blameableBehavior` | **\PhalconKit\Mvc\Model\Behavior\Blameable** | The `BlameableBehavior` instance to set. |

***

### getBlameableBehavior

Retrieves the BlameableBehavior instance associated with the current object.

```php
public getBlameableBehavior(): \PhalconKit\Mvc\Model\Behavior\Blameable
```

**Return Value:**

The BlameableBehavior instance.

***

### addUserRelationship

Adds a relationship between the current object and a user entity.

```php
public addUserRelationship(string $field = 'userId', string $alias = 'UserEntity', array $params = [], string $ref = 'id', string $type = 'belongsTo', string|null $class = null): \Phalcon\Mvc\Model\Relation|null
```

**Parameters:**

| Parameter | Type             | Description                                                                                                    |
|-----------|------------------|----------------------------------------------------------------------------------------------------------------|
| `$field`  | **string**       | The field name to create the relationship on. Default is 'userId'.                                             |
| `$alias`  | **string**       | The alias name for the user entity. Default is 'UserEntity'.                                                   |
| `$params` | **array**        | Additional parameters for the relationship. Default is an empty array.                                         |
| `$ref`    | **string**       | The reference field in the user entity. Default is 'id'.                                                       |
| `$type`   | **string**       | The type of relationship to create. Default is 'belongsTo'.                                                    |
| `$class`  | **string\|null** | The class name of the user entity. If null, it will be obtained from the identity or the global configuration. |

**Return Value:**

The created relationship object, or null if the specified field does not exist in the current object.

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

### initialize

```php
public initialize(): void
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

* https://docs.phalcon.io/latest/en/db-models#model-features

***
