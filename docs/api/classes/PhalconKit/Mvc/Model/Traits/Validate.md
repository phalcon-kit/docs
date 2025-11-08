
***

* Full name: `\PhalconKit\Mvc\Model\Traits\Validate`

## Methods

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
