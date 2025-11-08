
***

* Full name: `\PhalconKit\Modules\Cli\Tasks\TsScaffoldTask`
* Parent class: [`\PhalconKit\Modules\Cli\Task`](../Task.md)

## Properties

### cliDoc

```php
public string $cliDoc
```

***

### path

```php
public string $path
```

***

### servicesPath

```php
public string $servicesPath
```

***

### modelsPath

```php
public string $modelsPath
```

***

### abstractsPath

```php
public string $abstractsPath
```

***

### interfacesPath

```php
public string $interfacesPath
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

### generateExportsAction

```php
public generateExportsAction(): array
```

***

### runAction

```php
public runAction(): array
```

***

### appendExport

```php
public appendExport(array $definitions, array& $exports): void
```

**Parameters:**

| Parameter      | Type      | Description |
|----------------|-----------|-------------|
| `$definitions` | **array** |             |
| `$exports`     | **array** |             |

***

### createInterfaceOutput

```php
public createInterfaceOutput(array $definitions, array $columns): string
```

**Parameters:**

| Parameter      | Type      | Description |
|----------------|-----------|-------------|
| `$definitions` | **array** |             |
| `$columns`     | **array** |             |

***

### createAbstractOutput

Creates a typescript abstract model output based on the given definitions.

```php
public createAbstractOutput(array $definitions, array $columns): string
```

**Parameters:**

| Parameter      | Type      | Description |
|----------------|-----------|-------------|
| `$definitions` | **array** |             |
| `$columns`     | **array** |             |

***

### createModelOutput

Creates a typescript model output based on the given definitions.

```php
public createModelOutput(array $definitions, array $related): string
```

**Parameters:**

| Parameter      | Type      | Description |
|----------------|-----------|-------------|
| `$definitions` | **array** |             |
| `$related`     | **array** |             |

***

### createServiceOutput

```php
public createServiceOutput(array $definitions): string
```

**Parameters:**

| Parameter      | Type      | Description |
|----------------|-----------|-------------|
| `$definitions` | **array** |             |

***

### getRelatedImportItems

```php
public getRelatedImportItems(array $related): string
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$related` | **array** |             |

***

### getRelatedDefaultItems

Returns a formatted string representation of the related default items.

```php
public getRelatedDefaultItems(array $related): string
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$related` | **array** |             |

***

### getRelatedMapItems

Returns a formatted string representation of the related map items.

```php
public getRelatedMapItems(array $related): string
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$related` | **array** |             |

***

### getRelatedProperties

Returns a formatted string representation of the related map items.

```php
public getRelatedProperties(array $related): string
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$related` | **array** |             |

***

### getPropertyItems

Returns a formatted string representation of the property items.

```php
public getPropertyItems(\Phalcon\Db\ColumnInterface[] $columns): string
```

**Parameters:**

| Parameter  | Type                              | Description                 |
|------------|-----------------------------------|-----------------------------|
| `$columns` | **\Phalcon\Db\ColumnInterface[]** | An array of column objects. |

**Return Value:**

A string representation of the property items.

***

### getRelatedMeta

```php
public getRelatedMeta(string $modelClassName): array
```

**Parameters:**

| Parameter         | Type       | Description |
|-------------------|------------|-------------|
| `$modelClassName` | **string** |             |

***

### getColumnTsType

```php
public getColumnTsType(\Phalcon\Db\ColumnInterface $column): string
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$column` | **\Phalcon\Db\ColumnInterface** |             |

***

### getDefaultValue

```php
public getDefaultValue(\Phalcon\Db\ColumnInterface $column, string $type): ?string
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$column` | **\Phalcon\Db\ColumnInterface** |             |
| `$type`   | **string**                      |             |

***

### getColumnName

```php
public getColumnName(string $name): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$name`   | **string** |             |

***

### getTableName

```php
public getTableName(string $name): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$name`   | **string** |             |

***

### getModelInstance

```php
public getModelInstance(string $modelClassName): \PhalconKit\Mvc\Model
```

**Parameters:**

| Parameter         | Type       | Description |
|-------------------|------------|-------------|
| `$modelClassName` | **string** |             |

***

### getModelNameFromClassName

```php
public getModelNameFromClassName(string $className): string
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$className` | **string** |             |

***

### saveFile

```php
public saveFile(string $file, string $text, bool $force = false): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$file`   | **string** |             |
| `$text`   | **string** |             |
| `$force`  | **bool**   |             |

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
