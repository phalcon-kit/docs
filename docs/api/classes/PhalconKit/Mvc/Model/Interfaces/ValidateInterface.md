
***

* Full name: `\PhalconKit\Mvc\Model\Interfaces\ValidateInterface`

## Methods

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
