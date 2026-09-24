
Build model validation rules without running validation or saving the model.

Every add* method mutates and returns the supplied validator for chaining.
Field names refer to mapped model attributes; arrays are passed to Phalcon's
validator API (for example, a composite uniqueness check). Core's implementation
uses model metadata/attributes and the translation service for error messages.
Unless a helper states otherwise, allowEmpty=false adds a presence rule.

***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\ValidateInterface`

**See Also:**

* \PhalconKit\Mvc\Model\Traits\Validate

## Methods

### genericValidation

Add position, soft-delete, and created/updated/deleted/restored audit rules.

```php
public genericValidation(\PhalconKit\Filter\Validation|null $validator = null): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter    | Type                                    | Description                                |
|--------------|-----------------------------------------|--------------------------------------------|
| `$validator` | **\PhalconKit\Filter\Validation\|null** | Existing validator, or null to create one. |

**Return Value:**

The validator after adding rules for declared convention fields.

***

### addNotEmptyValidation

Add a presence rule only when empty values are forbidden.

```php
public addNotEmptyValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field, bool $allowEmpty = false): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description                          |
|---------------|---------------------------------------|--------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                                      |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names.             |
| `$allowEmpty` | **bool**                              | True leaves the validator unchanged. |

***

### addPresenceValidation

Add Phalcon's PresenceOf rule with the translated "required" message.

```php
public addPresenceValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description                                            |
|---------------|---------------------------------------|--------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                                                        |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names.                               |
| `$allowEmpty` | **bool**                              | Forwarded directly to PresenceOf's empty-value policy. |

***

### addUnsignedIntValidation

Add numeric and inclusive unsigned INT range checks.

```php
public addUnsignedIntValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field = 'id', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description                                                                                                                         |
|---------------|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                                                                                                                                     |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names.                                                                                                            |
| `$allowEmpty` | **bool**                              | Skip an optional single field containing null, an empty
string, or Core's case-insensitive SQL NULL sentinel. Zero is a real value. |

***

### addUnsignedBigIntValidation

Add numeric and inclusive unsigned BIGINT range checks.

```php
public addUnsignedBigIntValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field = 'id', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description                                           |
|---------------|---------------------------------------|-------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                                                       |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names.                              |
| `$allowEmpty` | **bool**                              | Apply the same optional-value policy as unsigned INT. |

**See Also:**

* \PhalconKit\Mvc\Model\Interfaces\self::addUnsignedIntValidation()

***

### addNumberValidation

Add numeric validation and an inclusive range check.

```php
public addNumberValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field, int $min, int $max, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description              |
|---------------|---------------------------------------|--------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                          |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names. |
| `$min`        | **int**                               | Lowest permitted value.  |
| `$max`        | **int**                               | Highest permitted value. |
| `$allowEmpty` | **bool**                              |                          |

***

### addStringLengthValidation

Add inclusive minimum and maximum character-length checks.

```php
public addStringLengthValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field, int $minChar = 0, int $maxChar = 255, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description                           |
|---------------|---------------------------------------|---------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                                       |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names.              |
| `$minChar`    | **int**                               | Minimum length for a non-empty value. |
| `$maxChar`    | **int**                               | Maximum length for a non-empty value. |
| `$allowEmpty` | **bool**                              |                                       |

***

### addInclusionInValidation

Add a domain membership check using Phalcon's default comparison mode.

```php
public addInclusionInValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field, array<array-key,mixed> $domainList = [], bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description              |
|---------------|---------------------------------------|--------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                          |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names. |
| `$domainList` | **array<array-key,mixed>**            | Allowed values.          |
| `$allowEmpty` | **bool**                              |                          |

**See Also:**

* \PhalconKit\Mvc\Model\Interfaces\self::addInclusionValidation() - For an explicit strict-comparison setting.

***

### addBooleanValidation

Accept only true, false, 1, 0, '1', and '0' with strict comparisons.

```php
public addBooleanValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

The value is validated without coercion. False and zero are never treated as empty.

**Parameters:**

| Parameter     | Type                                  | Description                            |
|---------------|---------------------------------------|----------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                                        |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names.               |
| `$allowEmpty` | **bool**                              | Also accept null and the empty string. |

***

### addInclusionValidation

Add a domain membership check with an explicit comparison mode.

```php
public addInclusionValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field, array<array-key,mixed> $domain = [], bool $allowEmpty = true, bool $strict = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description                                     |
|---------------|---------------------------------------|-------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                                                 |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names.                        |
| `$domain`     | **array<array-key,mixed>**            | Allowed values.                                 |
| `$allowEmpty` | **bool**                              |                                                 |
| `$strict`     | **bool**                              | Require both value and type to match when true. |

***

### addUniquenessValidation

Add model-backed uniqueness validation, querying the model's connection.

```php
public addUniquenessValidation(\PhalconKit\Filter\Validation $validator, string|array<string|int,string> $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description                              |
|---------------|---------------------------------------|------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                                          |
| `$field`      | **string\|array<string\|int,string>** | One unique attribute or a composite set. |
| `$allowEmpty` | **bool**                              |                                          |

**See Also:**

* \Phalcon\Filter\Validation\Validator\Uniqueness

***

### addEmailValidation

Add Phalcon's email-format validator and translated error message.

```php
public addEmailValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description              |
|---------------|---------------------------------------|--------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                          |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names. |
| `$allowEmpty` | **bool**                              |                          |

***

### addDateValidation

Add a date-format check, skipping optional single-field SQL NULL sentinels.

```php
public addDateValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field, bool $allowEmpty = true, string $format = \PhalconKit\Db\Column::DATE_FORMAT): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description                                           |
|---------------|---------------------------------------|-------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                                                       |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names.                              |
| `$allowEmpty` | **bool**                              |                                                       |
| `$format`     | **string**                            | PHP date format expected by Phalcon's Date validator. |

***

### addDateTimeValidation

Add a datetime-format check with the same optional policy as date validation.

```php
public addDateTimeValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field, bool $allowEmpty = true, string $format = \PhalconKit\Db\Column::DATETIME_FORMAT): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description                                              |
|---------------|---------------------------------------|----------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                                                          |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names.                                 |
| `$allowEmpty` | **bool**                              |                                                          |
| `$format`     | **string**                            | PHP date format, including the expected time components. |

***

### addJsonValidation

Validate a JSON string using Core's JSON validator.

```php
public addJsonValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field, bool $allowEmpty = true, int $depth = 512, int $flags = 0): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description                                                   |
|---------------|---------------------------------------|---------------------------------------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                                                               |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names.                                      |
| `$allowEmpty` | **bool**                              |                                                               |
| `$depth`      | **int**                               | Maximum nesting depth passed to JSON decoding.                |
| `$flags`      | **int**                               | JSON decoding flags; values are not rewritten by this helper. |

***

### addColorValidation

Add Core's hexadecimal color validator.

```php
public addColorValidation(\PhalconKit\Filter\Validation $validator, array<string|int,string>|string $field, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter     | Type                                  | Description              |
|---------------|---------------------------------------|--------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation**     |                          |
| `$field`      | **array<string\|int,string>\|string** | Attribute name or names. |
| `$allowEmpty` | **bool**                              |                          |

***

### addIdValidation

Add optional unsigned INT rules only if the named model property exists.

```php
public addIdValidation(\PhalconKit\Filter\Validation $validator, string $field = 'id'): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter    | Type                              | Description                                                      |
|--------------|-----------------------------------|------------------------------------------------------------------|
| `$validator` | **\PhalconKit\Filter\Validation** |                                                                  |
| `$field`     | **string**                        | Identity attribute; an unset auto-generated ID may remain empty. |

***

### addPositionValidation

Validate a declared position property against the unsigned INT range.

```php
public addPositionValidation(\PhalconKit\Filter\Validation $validator, string $field = 'position', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

Core's trait permits RawValue expressions by default for database-side position
updates; implementations may expose a separate option to disable that exemption.

**Parameters:**

| Parameter     | Type                              | Description                  |
|---------------|-----------------------------------|------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |                              |
| `$field`      | **string**                        | Declared position attribute. |
| `$allowEmpty` | **bool**                          |                              |

***

### addSoftDeleteValidation

Normalize a declared soft-delete flag to integer YES/NO and add its rules.

```php
public addSoftDeleteValidation(\PhalconKit\Filter\Validation $validator, string $field = 'deleted', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

Unlike the general boolean helper, Core's implementation can write the normalized
attribute before validation. It adds strict membership in Column::YES/NO.

**Parameters:**

| Parameter     | Type                              | Description                     |
|---------------|-----------------------------------|---------------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |                                 |
| `$field`      | **string**                        | Declared soft-delete attribute. |
| `$allowEmpty` | **bool**                          |                                 |

***

### addUuidValidation

Add presence and uniqueness rules for a declared UUID attribute.

```php
public addUuidValidation(\PhalconKit\Filter\Validation $validator, string $field = 'uuid', bool $allowEmpty = false): \PhalconKit\Filter\Validation
```

This helper does not check a UUID's textual format or convert binary UUID values.

**Parameters:**

| Parameter     | Type                              | Description              |
|---------------|-----------------------------------|--------------------------|
| `$validator`  | **\PhalconKit\Filter\Validation** |                          |
| `$field`      | **string**                        | Declared UUID attribute. |
| `$allowEmpty` | **bool**                          |                          |

***

### addCrudValidation

Validate a declared audit user ID and its associated timestamp.

```php
public addCrudValidation(\PhalconKit\Filter\Validation $validator, string $userIdField, string $dateField, bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

An optional empty user ID skips this pair. A non-empty user ID requires the
corresponding declared timestamp to match Column::DATETIME_FORMAT.

**Parameters:**

| Parameter      | Type                              | Description                     |
|----------------|-----------------------------------|---------------------------------|
| `$validator`   | **\PhalconKit\Filter\Validation** |                                 |
| `$userIdField` | **string**                        | Audit actor attribute.          |
| `$dateField`   | **string**                        | Associated timestamp attribute. |
| `$allowEmpty`  | **bool**                          |                                 |

***

### addCreatedValidation

Apply audit-pair rules to the creation actor and timestamp.

```php
public addCreatedValidation(\PhalconKit\Filter\Validation $validator, string $createdByField = 'createdBy', string $createdAtField = 'createdAt', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter         | Type                              | Description                   |
|-------------------|-----------------------------------|-------------------------------|
| `$validator`      | **\PhalconKit\Filter\Validation** |                               |
| `$createdByField` | **string**                        | Creation actor attribute.     |
| `$createdAtField` | **string**                        | Creation timestamp attribute. |
| `$allowEmpty`     | **bool**                          |                               |

**See Also:**

* \PhalconKit\Mvc\Model\Interfaces\self::addCrudValidation()

***

### addUpdatedValidation

Apply audit-pair rules to the update actor and timestamp.

```php
public addUpdatedValidation(\PhalconKit\Filter\Validation $validator, string $updatedByField = 'updatedBy', string $updatedAtField = 'updatedAt', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter         | Type                              | Description                 |
|-------------------|-----------------------------------|-----------------------------|
| `$validator`      | **\PhalconKit\Filter\Validation** |                             |
| `$updatedByField` | **string**                        | Update actor attribute.     |
| `$updatedAtField` | **string**                        | Update timestamp attribute. |
| `$allowEmpty`     | **bool**                          |                             |

**See Also:**

* \PhalconKit\Mvc\Model\Interfaces\self::addCrudValidation()

***

### addDeletedValidation

Apply audit-pair rules to the deletion actor and timestamp.

```php
public addDeletedValidation(\PhalconKit\Filter\Validation $validator, string $deletedField = 'deletedBy', string $dateField = 'deletedAt', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter       | Type                              | Description                                            |
|-----------------|-----------------------------------|--------------------------------------------------------|
| `$validator`    | **\PhalconKit\Filter\Validation** |                                                        |
| `$deletedField` | **string**                        | Deletion actor attribute, despite the historical name. |
| `$dateField`    | **string**                        | Deletion timestamp attribute.                          |
| `$allowEmpty`   | **bool**                          |                                                        |

**See Also:**

* \PhalconKit\Mvc\Model\Interfaces\self::addCrudValidation()

***

### addRestoredValidation

Apply audit-pair rules to the restoration actor and timestamp.

```php
public addRestoredValidation(\PhalconKit\Filter\Validation $validator, string $restoredByField = 'restoredBy', string $restoredAtField = 'restoredAt', bool $allowEmpty = true): \PhalconKit\Filter\Validation
```

**Parameters:**

| Parameter          | Type                              | Description                      |
|--------------------|-----------------------------------|----------------------------------|
| `$validator`       | **\PhalconKit\Filter\Validation** |                                  |
| `$restoredByField` | **string**                        | Restoration actor attribute.     |
| `$restoredAtField` | **string**                        | Restoration timestamp attribute. |
| `$allowEmpty`      | **bool**                          |                                  |

**See Also:**

* \PhalconKit\Mvc\Model\Interfaces\self::addCrudValidation()

***
