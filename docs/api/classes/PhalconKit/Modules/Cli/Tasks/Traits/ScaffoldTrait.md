
Trait DescribesTrait

This trait provides methods to describe columns, references, and indexes of a database table.

***

* Full name: `\PhalconKit\Modules\Cli\Tasks\Traits\ScaffoldTrait`

## Properties

### namespace

```php
protected ?string $namespace
```

***
### directory

```php
protected string $directory
```

***
### srcDirectory

```php
protected string $srcDirectory
```

***
### testsDirectory

```php
protected string $testsDirectory
```

***
### enumsDirectory

```php
protected string $enumsDirectory
```

***
### modelsDirectory

```php
protected string $modelsDirectory
```

***
### abstractsDirectory

```php
protected string $abstractsDirectory
```

***
### interfacesDirectory

```php
protected string $interfacesDirectory
```

***
### controllersDirectory

```php
protected string $controllersDirectory
```

***
### modelsExtend

```php
protected string $modelsExtend
```

***
### interfacesExtend

```php
protected string $interfacesExtend
```

***
### testsExtend

```php
protected string $testsExtend
```

***
### controllersExtend

```php
protected string $controllersExtend
```

***
### whitelistedTables

```php
protected ?array $whitelistedTables
```

***
### excludedTables

```php
protected ?array $excludedTables
```

***
### licenseStamp

```php
public string $licenseStamp
```

***
### strictTypes

```php
public string $strictTypes
```

***

## Methods

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
