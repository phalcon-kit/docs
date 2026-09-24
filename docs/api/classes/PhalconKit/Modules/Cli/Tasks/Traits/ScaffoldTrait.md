
Resolve CLI scaffold options, generated PHP headers, paths, and namespaces.

Requires Core's CLI dispatcher with normalized camelCase option keys. Paths are
composed without creating directories or resolving real paths; relative roots
stay relative and a leading slash bypasses the configured root. Directory
fragments used below the project root should include their trailing slash.
Table filters are cached on first use for the lifetime of the task. File writes
and overwrite decisions belong to the consuming scaffold task.

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

Return the --license override or default header text.

```php
public getLicenseStamp(): string|null
```

**Return Value:**

Header text, or an empty string when --no-license is set.
The nullable signature is retained for task overrides.

***
### getStrictTypes

Return the strict_types declaration for a generated PHP file.

```php
public getStrictTypes(): string|null
```

**Return Value:**

Declaration text, or an empty string when --no-strict-types
is set. The nullable signature is retained for task overrides.

***
### getPhpFileHeader

Builds the normalized opening PHP header for scaffolded files.

```php
public getPhpFileHeader(): string
```

Optional fragments, such as the license stamp and strict-types
declaration, are trimmed before joining so disabled fragments do not
leave extra blank lines in generated files.

**Return Value:**

Header text ending with exactly one blank line before the
next top-level statement, typically a namespace declaration.

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

True when --table is empty or includes this exact table name.

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

Skip controller generation when --no-controllers is set.

```php
public isNoControllers(): bool
```

***
### isNoInterfaces

Skip model interface generation when --no-interfaces is set.

```php
public isNoInterfaces(): bool
```

***
### isNoAbstracts

Skip abstract model generation when --no-abstracts is set.

```php
public isNoAbstracts(): bool
```

***
### isNoModels

Skip concrete model generation when --no-models is set.

```php
public isNoModels(): bool
```

***
### isNoEnums

Skip enum generation when --no-enums is set.

```php
public isNoEnums(): bool
```

***
### isNoTests

Skip test generation when --no-tests is set.

```php
public isNoTests(): bool
```

***
### isNoStrictTypes

Omit the strict_types declaration when --no-strict-types is set.

```php
public isNoStrictTypes(): bool
```

***
### isNoLicense

Omit the generated license header when --no-license is set.

```php
public isNoLicense(): bool
```

***
### isNoComments

Omit optional generated documentation when --no-comments is set.

```php
public isNoComments(): bool
```

***
### isNoGetSetMethods

Omit generated accessors when --no-get-set-methods is set.

```php
public isNoGetSetMethods(): bool
```

***
### isNoValidations

Omit generated validation methods when --no-validations is set.

```php
public isNoValidations(): bool
```

***
### isNoRelationships

Omit generated relation definitions when --no-relationships is set.

```php
public isNoRelationships(): bool
```

***
### isNoColumnMap

Omit generated column maps when --no-column-map is set.

```php
public isNoColumnMap(): bool
```

***
### isNoSetSource

Omit generated source-table assignment when --no-set-source is set.

```php
public isNoSetSource(): bool
```

***
### isNoTypings

Omit optional generated type declarations when --no-typings is set.

```php
public isNoTypings(): bool
```

***
### isGranularTypings

Use the more specific scaffold type mappings requested by --granular-typings.

```php
public isGranularTypings(): bool
```

***
### isAddRawValueType

Include Phalcon RawValue in generated types when --add-raw-value-type is set.

```php
public isAddRawValueType(): bool
```

***
### isProtectedProperties

Generate protected model properties when --protected-properties is set.

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

| Parameter | Type       | Description                                     |
|-----------|------------|-------------------------------------------------|
| `$path`   | **string** | The path to be checked. (default: empty string) |

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

Path under --directory, or the unchanged absolute $path.
A relative --directory produces a relative result.

***
### getSrcDirectory

Compose a path using the `srcDir` dispatcher option under the project directory.

```php
public getSrcDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description                                                    |
|-----------|------------|----------------------------------------------------------------|
| `$path`   | **string** | Suffix to append; a leading slash returns this path unchanged. |

**Return Value:**

Composed path, which may remain relative to the working directory.

***
### getTestsDirectory

Compose a path using the `testsDir` dispatcher option under the project directory.

```php
public getTestsDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description                                                    |
|-----------|------------|----------------------------------------------------------------|
| `$path`   | **string** | Suffix to append; a leading slash returns this path unchanged. |

**Return Value:**

Composed path, which may remain relative to the working directory.

***
### getControllersDirectory

Compose a path using the `controllersDir` dispatcher option under the source directory.

```php
public getControllersDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description                                                    |
|-----------|------------|----------------------------------------------------------------|
| `$path`   | **string** | Suffix to append; a leading slash returns this path unchanged. |

**Return Value:**

Composed path, which may remain relative to the working directory.

***
### getModelsDirectory

Compose a path using the `modelsDir` dispatcher option under the source directory.

```php
public getModelsDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description                                                    |
|-----------|------------|----------------------------------------------------------------|
| `$path`   | **string** | Suffix to append; a leading slash returns this path unchanged. |

**Return Value:**

Composed path, which may remain relative to the working directory.

***
### getModelsInterfacesDirectory

Compose a path using the `interfacesDir` dispatcher option under the models directory.

```php
public getModelsInterfacesDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description                                                    |
|-----------|------------|----------------------------------------------------------------|
| `$path`   | **string** | Suffix to append; a leading slash returns this path unchanged. |

**Return Value:**

Composed path, which may remain relative to the working directory.

***
### getEnumsDirectory

Compose a path using the `enumsDir` dispatcher option under the models directory.

```php
public getEnumsDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description                                                    |
|-----------|------------|----------------------------------------------------------------|
| `$path`   | **string** | Suffix to append; a leading slash returns this path unchanged. |

**Return Value:**

Composed path, which may remain relative to the working directory.

***
### getAbstractsDirectory

Compose a path using the `abstractsDir` dispatcher option under the models directory.

```php
public getAbstractsDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description                                                    |
|-----------|------------|----------------------------------------------------------------|
| `$path`   | **string** | Suffix to append; a leading slash returns this path unchanged. |

**Return Value:**

Composed path, which may remain relative to the working directory.

***
### getAbstractsInterfacesDirectory

Compose a path using the `interfaceDir` dispatcher option under the abstract models directory.

```php
public getAbstractsInterfacesDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description                                                    |
|-----------|------------|----------------------------------------------------------------|
| `$path`   | **string** | Suffix to append; a leading slash returns this path unchanged. |

**Return Value:**

Composed path, which may remain relative to the working directory.

***
### getModelsTestsDirectory

Compose a path using the `modelsDir` dispatcher option under the tests directory.

```php
public getModelsTestsDirectory(string $path = ''): string
```

**Parameters:**

| Parameter | Type       | Description                                                    |
|-----------|------------|----------------------------------------------------------------|
| `$path`   | **string** | Suffix to append; a leading slash returns this path unchanged. |

**Return Value:**

Composed path, which may remain relative to the working directory.

***
### getModelsExtend

Return the model parent class name from `modelsExtend`, falling back to the task default.

```php
public getModelsExtend(): string
```

***
### getInterfacesExtend

Return the model parent interface name from `interfacesExtend`, falling back to the task default.

```php
public getInterfacesExtend(): string
```

***
### getTestsExtend

Return the test parent class name from `testsExtend`, falling back to the task default.

```php
public getTestsExtend(): string
```

***
### getControllersExtend

Return the controller parent class name from `controllersExtend`, falling back to the task default.

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

Derive the project root namespace from its configured directory and base namespace.

```php
public getNamespace(): string
```

***
### getControllersNamespace

Derive the controllers namespace from its configured directory and base namespace.

```php
public getControllersNamespace(): string
```

***
### getEnumsNamespace

Derive the model enums namespace from its configured directory and base namespace.

```php
public getEnumsNamespace(): string
```

***
### getModelsNamespace

Derive the models namespace from its configured directory and base namespace.

```php
public getModelsNamespace(): string
```

***
### getAbstractsNamespace

Derive the abstract models namespace from its configured directory and base namespace.

```php
public getAbstractsNamespace(): string
```

***
### getModelsInterfacesNamespace

Derive the model interfaces namespace from its configured directory and base namespace.

```php
public getModelsInterfacesNamespace(): string
```

***
### getAbstractsInterfacesNamespace

Derive the abstract model interfaces namespace from its configured directory and base namespace.

```php
public getAbstractsInterfacesNamespace(): string
```

***
### getModelsTestsNamespace

Derive the model tests namespace from its configured directory and base namespace.

```php
public getModelsTestsNamespace(): string
```

***
