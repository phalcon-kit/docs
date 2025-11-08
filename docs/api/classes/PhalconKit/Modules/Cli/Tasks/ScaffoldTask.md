
***

* Full name: `\PhalconKit\Modules\Cli\Tasks\ScaffoldTask`
* Parent class: [`\PhalconKit\Modules\Cli\Task`](../Task.md)

## Properties

### cliDoc

```php
public string $cliDoc
```

***

## Methods

### getDefinitionsAction

```php
public getDefinitionsAction(string $name): array
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$name`   | **string** |             |

***

### runAction

```php
public runAction(): array
```

***

### createControllerOutput

```php
public createControllerOutput(array $definitions, array $columns, array $relationships): string
```

**Parameters:**

| Parameter        | Type      | Description |
|------------------|-----------|-------------|
| `$definitions`   | **array** |             |
| `$columns`       | **array** |             |
| `$relationships` | **array** |             |

***

### createModelInterfaceOutput

Generates the output for a model interface.

```php
public createModelInterfaceOutput(array $definitions): string
```

**Parameters:**

| Parameter      | Type      | Description                                         |
|----------------|-----------|-----------------------------------------------------|
| `$definitions` | **array** | The definitions for generating the model interface. |

**Return Value:**

The generated model interface output as a string.

***

### createAbstractInterfaceOutput

Generates the abstract interface output based on the given definitions and columns.

```php
public createAbstractInterfaceOutput(array $definitions, array $columns, array $relationships): string
```

**Parameters:**

| Parameter        | Type      | Description                                                  |
|------------------|-----------|--------------------------------------------------------------|
| `$definitions`   | **array** | The definitions for the abstract interface.                  |
| `$columns`       | **array** | The columns for which to generate getter and setter methods. |
| `$relationships` | **array** | The columns for which to generate getter and setter methods. |

**Return Value:**

The generated abstract interface output as a string.

***

### createAbstractOutput

Generates an abstract class output for the given definitions, table, columns, and tables.

```php
public createAbstractOutput(array $definitions, array $columns, array $relationships): string
```

**Parameters:**

| Parameter        | Type      | Description                              |
|------------------|-----------|------------------------------------------|
| `$definitions`   | **array** | The definitions for the abstract output. |
| `$columns`       | **array** | The columns.                             |
| `$relationships` | **array** | The relationship items.                  |

**Return Value:**

The abstract output as a string.

***

### createEnumOutput

```php
public createEnumOutput(string $enumName, \Phalcon\Db\Column $column): string
```

**Parameters:**

| Parameter   | Type                   | Description |
|-------------|------------------------|-------------|
| `$enumName` | **string**             |             |
| `$column`   | **\Phalcon\Db\Column** |             |

***

### createModelOutput

Generates a comment for the createModelOutput method.

```php
public createModelOutput(array $definitions): string
```

**Parameters:**

| Parameter      | Type      | Description                     |
|----------------|-----------|---------------------------------|
| `$definitions` | **array** | The array of model definitions. |

**Return Value:**

The generated comment.

***

### createModelTestOutput

```php
public createModelTestOutput(array $definitions, array $columns): string
```

**Parameters:**

| Parameter      | Type      | Description |
|----------------|-----------|-------------|
| `$definitions` | **array** |             |
| `$columns`     | **array** |             |

***

### getModelClassComments

```php
public getModelClassComments(array $definitions): string
```

**Parameters:**

| Parameter      | Type      | Description |
|----------------|-----------|-------------|
| `$definitions` | **array** |             |

***

### getValidationItems

Generates a string containing validation items for each column in the provided array.

```php
public getValidationItems(array $columns): string
```

**Parameters:**

| Parameter  | Type      | Description                          |
|------------|-----------|--------------------------------------|
| `$columns` | **array** | An array of ColumnInterface objects. |

**Return Value:**

The generated validation items string.

***

### getRelationshipItems

Generates relationship items for a given table.

```php
public getRelationshipItems(string $table, array $columns, array $tables): array
```

**Parameters:**

| Parameter  | Type       | Description                  |
|------------|------------|------------------------------|
| `$table`   | **string** | The name of the table.       |
| `$columns` | **array**  | The array of column objects. |
| `$tables`  | **array**  | The array of table names.    |

**Return Value:**

An array containing the generated relationship items.

***

### getColumnMapMethod

```php
public getColumnMapMethod(array $columns): string
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$columns` | **array** |             |

***

### getColumnMapComment

Returns the documentation comment for the `getColumnMap` method.

```php
public getColumnMapComment(): string
```

**Return Value:**

The documentation comment for the `getColumnMap` method.

***

### getColumnMapItems

Generates a string representation of column map items for a given array of columns.

```php
public getColumnMapItems(array $columns): string
```

**Parameters:**

| Parameter  | Type      | Description          |
|------------|-----------|----------------------|
| `$columns` | **array** | An array of columns. |

**Return Value:**

The string representation of the column map items.

***

### getPropertyItems

Generates property items for each column in the given array.

```php
public getPropertyItems(array $columns): string
```

**Parameters:**

| Parameter  | Type      | Description                          |
|------------|-----------|--------------------------------------|
| `$columns` | **array** | An array of ColumnInterface objects. |

**Return Value:**

The generated property items.

***

### getPropertyComment

Generates the comment for a property with the given column name and property type.

```php
public getPropertyComment(\Phalcon\Db\ColumnInterface $column, array $definitions): string
```

**Parameters:**

| Parameter      | Type                            | Description               |
|----------------|---------------------------------|---------------------------|
| `$column`      | **\Phalcon\Db\ColumnInterface** | The column object.        |
| `$definitions` | **array**                       | The property definitions. |

**Return Value:**

The generated property comment.

***

### getGetSetMethods

Generates a string representation of getters and setters for a given array of columns.

```php
public getGetSetMethods(array $columns, string $type = 'default', string $property = 'model'): string
```

**Parameters:**

| Parameter   | Type       | Description                                                                                              |
|-------------|------------|----------------------------------------------------------------------------------------------------------|
| `$columns`  | **array**  | An array of columns.                                                                                     |
| `$type`     | **string** | (optional) The type of code to generate. Can be 'default', 'interface', or 'test'. Default is 'default'. |
| `$property` | **string** | (optional) The name of the property to use in setter methods. Default is 'model'.                        |

**Return Value:**

The string representation of the getters and setters.

***

### getSetMethodComment

Generates a comment for a getter or setter method for a specific column.

```php
public getSetMethodComment(\Phalcon\Db\ColumnInterface $column, array $definitions, bool $get): string
```

**Parameters:**

| Parameter      | Type                            | Description                                                      |
|----------------|---------------------------------|------------------------------------------------------------------|
| `$column`      | **\Phalcon\Db\ColumnInterface** | The column object.                                               |
| `$definitions` | **array**                       | The property definitions.                                        |
| `$get`         | **bool**                        | Determines whether the comment is for a getter or setter method. |

**Return Value:**

The generated comment.

***

### getColumnAttributes

```php
public getColumnAttributes(\Phalcon\Db\ColumnInterface $column): string
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$column` | **\Phalcon\Db\ColumnInterface** |             |

***

### getPropertyDefinitions

```php
public getPropertyDefinitions(\Phalcon\Db\ColumnInterface $column): array
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$column` | **\Phalcon\Db\ColumnInterface** |             |

***

### saveFile

Saves a file with the given text content.

```php
public saveFile(string $file, string $text, bool $force = false): bool
```

**Parameters:**

| Parameter | Type       | Description                                                         |
|-----------|------------|---------------------------------------------------------------------|
| `$file`   | **string** | The path of the file to be saved.                                   |
| `$text`   | **string** | The content to be written to the file.                              |
| `$force`  | **bool**   | Determines whether to overwrite an existing file. Default is false. |

**Return Value:**

Returns true if the file was saved successfully, false otherwise.

***

## Inherited methods

### beforeExecuteRoute

```php
public beforeExecuteRoute(): void
```

***

### helpAction

```php
public helpAction(): void
```

***

### mainAction

```php
public mainAction(): ?array
```

***

### afterExecuteRoute

Handle rest response automagically

```php
public afterExecuteRoute(\Phalcon\Cli\Dispatcher $dispatcher): void
```

**Parameters:**

| Parameter     | Type                        | Description |
|---------------|-----------------------------|-------------|
| `$dispatcher` | **\Phalcon\Cli\Dispatcher** |             |

**Throws:**

- [`CliException`](../../../Exception/CliException.md)

***

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

### getLicenseStamp

Retrieves the license stamp.

```php
public getLicenseStamp(): string|null
```

**Return Value:**

The license stamp, or null if there is no license.

***

### getStrictTypes

Retrieves the value of the 'strictTypes' property.

```php
public getStrictTypes(): string|null
```

**Return Value:**

The value of the 'strictTypes' property, or null if the 'no-strict-types' parameter is set.

***

### isWhitelistedTable

Checks if the given table is whitelisted.

```php
public isWhitelistedTable(string $table): bool
```

**Parameters:**

| Parameter | Type       | Description              |
|-----------|------------|--------------------------|
| `$table`  | **string** | The table name to check. |

**Return Value:**

Returns true if the table is whitelisted, false otherwise.

***

### isExcludedTable

Determines if a table is excluded.

```php
public isExcludedTable(string $table): bool
```

**Parameters:**

| Parameter | Type       | Description                     |
|-----------|------------|---------------------------------|
| `$table`  | **string** | The name of the table to check. |

**Return Value:**

Returns true if the table is excluded, false otherwise.

***

### isNoControllers

```php
public isNoControllers(): bool
```

***

### isNoInterfaces

```php
public isNoInterfaces(): bool
```

***

### isNoAbstracts

```php
public isNoAbstracts(): bool
```

***

### isNoModels

```php
public isNoModels(): bool
```

***

### isNoEnums

```php
public isNoEnums(): bool
```

***

### isNoStrictTypes

```php
public isNoStrictTypes(): bool
```

***

### isNoLicense

```php
public isNoLicense(): bool
```

***

### isNoComments

```php
public isNoComments(): bool
```

***

### isNoGetSetMethods

```php
public isNoGetSetMethods(): bool
```

***

### isNoValidations

```php
public isNoValidations(): bool
```

***

### isNoRelationships

```php
public isNoRelationships(): bool
```

***

### isNoColumnMap

```php
public isNoColumnMap(): bool
```

***

### isNoSetSource

```php
public isNoSetSource(): bool
```

***

### isNoTypings

```php
public isNoTypings(): bool
```

***

### isGranularTypings

```php
public isGranularTypings(): bool
```

***

### isAddRawValueType

```php
public isAddRawValueType(): bool
```

***

### isProtectedProperties

```php
public isProtectedProperties(): bool
```

***

### isAbsolutePath

Determines if a given path is an absolute path.

```php
public isAbsolutePath(string $path = ''): bool
```

**Parameters:**

| Parameter | Type       | Description                             |
|-----------|------------|-----------------------------------------|
| `$path`   | **string** | The path to be checked. (default: null) |

**Return Value:**

Returns true if the path is an absolute path, false otherwise.

***

### absolutePathOr

Retrieves the absolute file or directory path.

```php
public absolutePathOr(string $path = '', string $fullPath = ''): string
```

**Parameters:**

| Parameter   | Type       | Description                                                  |
|-------------|------------|--------------------------------------------------------------|
| `$path`     | **string** | The relative or absolute path to the file or directory.      |
| `$fullPath` | **string** | The full path including directory for the file or directory. |

**Return Value:**

The absolute file or directory path. If the given path is absolute, it will be returned as is.
Otherwise, the full path including directory will be returned.

***

### getDirectory

Retrieves the directory path for a given file or directory path.

```php
public getDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description                                             |
|-----------|------------|---------------------------------------------------------|
| `$path`   | **string** | The relative or absolute path to the file or directory. |

**Return Value:**

The absolute directory path for the given file or directory path.

***

### getSrcDirectory

```php
public getSrcDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$path`   | **string** |             |

***

### getTestsDirectory

```php
public getTestsDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$path`   | **string** |             |

***

### getControllersDirectory

```php
public getControllersDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$path`   | **string** |             |

***

### getModelsDirectory

```php
public getModelsDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$path`   | **string** |             |

***

### getModelsInterfacesDirectory

```php
public getModelsInterfacesDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$path`   | **string** |             |

***

### getEnumsDirectory

```php
public getEnumsDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$path`   | **string** |             |

***

### getAbstractsDirectory

```php
public getAbstractsDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$path`   | **string** |             |

***

### getAbstractsInterfacesDirectory

```php
public getAbstractsInterfacesDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$path`   | **string** |             |

***

### getModelsTestsDirectory

```php
public getModelsTestsDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$path`   | **string** |             |

***

### getModelsExtend

```php
public getModelsExtend(): string
```

***

### getInterfacesExtend

```php
public getInterfacesExtend(): string
```

***

### getTestsExtend

```php
public getTestsExtend(): string
```

***

### getControllersExtend

```php
public getControllersExtend(): string
```

***

### getNamespaceFromPath

Converts a file system path to a PHP namespace.

```php
public getNamespaceFromPath(string $path): string
```

**Parameters:**

| Parameter | Type       | Description                           |
|-----------|------------|---------------------------------------|
| `$path`   | **string** | The file system path to be converted. |

**Return Value:**

The converted PHP namespace.

***

### getNamespace

```php
public getNamespace(): string
```

***

### getControllersNamespace

```php
public getControllersNamespace(): string
```

***

### getEnumsNamespace

```php
public getEnumsNamespace(): string
```

***

### getModelsNamespace

```php
public getModelsNamespace(): string
```

***

### getAbstractsNamespace

```php
public getAbstractsNamespace(): string
```

***

### getModelsInterfacesNamespace

```php
public getModelsInterfacesNamespace(): string
```

***

### getAbstractsInterfacesNamespace

```php
public getAbstractsInterfacesNamespace(): string
```

***

### getModelsTestsNamespace

```php
public getModelsTestsNamespace(): string
```

***
