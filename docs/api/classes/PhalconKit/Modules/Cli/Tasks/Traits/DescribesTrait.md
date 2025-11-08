
Trait DescribesTrait

This trait provides methods for describing table columns, references,
indexes, and determining the data type of columns. It also provides
methods for retrieving default values of columns, generating property
names based on column names, and generating table names based on
original names.

***

* Full name: `\PhalconKit\Modules\Cli\Tasks\Traits\DescribesTrait`

## Properties

### cachedColumns

```php
protected array $cachedColumns
```

***
### cachedIndexes

```php
protected array $cachedIndexes
```

***
### cachedReferences

```php
protected array $cachedReferences
```

***

## Methods

### describeColumns

Retrieves the columns of a given table.

```php
public describeColumns(string $table): array
```

**Parameters:**

| Parameter | Type       | Description                                    |
|-----------|------------|------------------------------------------------|
| `$table`  | **string** | The name of the table to describe the columns. |

**Return Value:**

An array of columns for the specified table.

***
### describeReferences

Retrieves the references of a given table.

```php
public describeReferences(string $table): array
```

**Parameters:**

| Parameter | Type       | Description                                       |
|-----------|------------|---------------------------------------------------|
| `$table`  | **string** | The name of the table to describe the references. |

**Return Value:**

An array of references for the specified table.

***
### describeIndexes

Retrieves the indexes of a given table.

```php
public describeIndexes(string $table): array
```

**Parameters:**

| Parameter | Type       | Description                                    |
|-----------|------------|------------------------------------------------|
| `$table`  | **string** | The name of the table to describe the indexes. |

**Return Value:**

An array of indexes for the specified table.

***
### isRawValue

Determines if a value is a Phalcon DB RawValue.

```php
public isRawValue(string|null $defaultValue = null): bool
```

**Parameters:**

| Parameter       | Type             | Description         |
|-----------------|------------------|---------------------|
| `$defaultValue` | **string\|null** | The value to check. |

**Return Value:**

Returns true if the value is a raw value, false otherwise.

***
### getColumnType

Determines the PHP data type of column.

```php
public getColumnType(\Phalcon\Db\ColumnInterface $column): string
```

**Parameters:**

| Parameter | Type                            | Description          |
|-----------|---------------------------------|----------------------|
| `$column` | **\Phalcon\Db\ColumnInterface** | The column to check. |

**Return Value:**

The data type of the column. Possible values are:
- 'bool' for boolean columns.
- 'int' for integer columns.
- 'float' for decimal or float columns.
- 'double' for double columns.
- 'string' for all other column types.

***
### getDefaultValue

Retrieves the default value for a column.

```php
public getDefaultValue(\Phalcon\Db\ColumnInterface $column): mixed
```

**Parameters:**

| Parameter | Type                            | Description                                           |
|-----------|---------------------------------|-------------------------------------------------------|
| `$column` | **\Phalcon\Db\ColumnInterface** | The column object to retrieve the default value from. |

**Return Value:**

Returns the default value of the column as a string, integer, boolean, float, or null based on the column type.

***
### getPropertyName

Retrieves the property name based on the given name.

```php
public getPropertyName(string $name): string
```

**Parameters:**

| Parameter | Type       | Description                                        |
|-----------|------------|----------------------------------------------------|
| `$name`   | **string** | The name from which to retrieve the property name. |

**Return Value:**

Returns the property name as a string.

***
### getTableName

Retrieves the table name based on the given name.

```php
public getTableName(string $name): string
```

**Parameters:**

| Parameter | Type       | Description                     |
|-----------|------------|---------------------------------|
| `$name`   | **string** | The original name of the table. |

**Return Value:**

Returns the table name with the first letter capitalized and all other letters unchanged.

***
