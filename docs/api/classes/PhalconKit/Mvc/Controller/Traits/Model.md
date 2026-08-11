
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Model`

## Properties

### modelName

The name of the model.

```php
protected ?string $modelName
```

***
### modelNamespaces

The namespaces for the model lookup.

```php
protected string[] $modelNamespaces
```

***
### modelColumnCache

Cached model column and mapped-attribute lookup tables.

```php
protected static array<class-string<\Phalcon\Mvc\ModelInterface>,array<string,bool>> $modelColumnCache
```

* This property is **static**.

***

## Methods

### getModelName

Retrieves the name of the model associated with the controller.

```php
public getModelName(): string|null
```

**Return Value:**

The name of the model associated with the controller, or null if not found.

***
### setModelName

Sets the name of the model to be used.

```php
public setModelName(string|null $modelName): void
```

**Parameters:**

| Parameter    | Type             | Description                      |
|--------------|------------------|----------------------------------|
| `$modelName` | **string\|null** | The name of the model to be set. |

***
### getModelNamespaces

Get namespaces used when deriving a model class from the controller name.

```php
public getModelNamespaces(): array<string,string>
```

Explicit namespaces set through

- **See:** \PhalconKit\Mvc\Controller\Traits\setModelNamespaces() win. When no
explicit map exists and the DI contains a `loader` service, the method
reads namespaces from Phalcon's autoloader. A registered but incompatible
loader is treated as a configuration error because otherwise model
inference would fail later with a less useful method-call error when PHP
assertions are disabled.

**Return Value:**

Namespace-to-directory map used for model
lookup.

**Throws:**

When the optional `loader` service is present
but is not a Phalcon autoload loader.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### setModelNamespaces

Set the namespaces for the models.

```php
public setModelNamespaces(array|null $modelNamespaces): void
```

**Parameters:**

| Parameter          | Type            | Description                             |
|--------------------|-----------------|-----------------------------------------|
| `$modelNamespaces` | **array\|null** | The array of namespaces for the models. |

***
### getModelNameFromController

Retrieves the model name from the controller by following certain naming conventions.

```php
public getModelNameFromController(array|null $namespaces = null, string $needle = 'Models'): string|null
```

**Parameters:**

| Parameter     | Type            | Description                                                                                                         |
|---------------|-----------------|---------------------------------------------------------------------------------------------------------------------|
| `$namespaces` | **array\|null** | Optional. An array of namespaces to search for the model. Default is null and will use $this->getModelNamespaces(). |
| `$needle`     | **string**      | Optional. The keyword to search for in the namespace. Default is 'Models'.                                          |

**Return Value:**

The model name if found, otherwise null.

***
### getControllerName

Returns the name of the controller.

```php
public getControllerName(): string
```

If the controller name is not set in the dispatcher, it extracts the controller name from the class name
of the current instance.

**Return Value:**

The name of the controller.

***
### loadModel

Loads a model by its name using the modelsManager.

```php
public loadModel(string|null $modelName = null): \Phalcon\Mvc\ModelInterface
```

**Parameters:**

| Parameter    | Type             | Description                                                                        |
|--------------|------------------|------------------------------------------------------------------------------------|
| `$modelName` | **string\|null** | The name of the model to load. Default is null and will use $this->getModelName(). |

**Return Value:**

The loaded model.

**Throws:**

When no model can be resolved or the resolved
class does not implement Phalcon's model contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### modelHasColumn

Determine whether the configured model exposes a database column or mapped
model attribute.

```php
public modelHasColumn(string $column, string|null $modelName = null): bool
```

The helper prefers generated model `columnMap()` definitions, then falls
back to Phalcon's model metadata for models that do not declare a column
map. Metadata availability depends on the application's configured
metadata strategy and cache; if metadata cannot be read safely, the helper
returns false instead of turning an optional controller condition into a
runtime failure.

**Parameters:**

| Parameter    | Type             | Description                                                                                     |
|--------------|------------------|-------------------------------------------------------------------------------------------------|
| `$column`    | **string**       | Database column name or mapped model attribute name.                                            |
| `$modelName` | **string\|null** | Optional model class; defaults to the
current controller model. Non-model strings return false. |

**Return Value:**

True when the model column map contains the raw column or
mapped attribute name.

***
### appendModelName

Normalize and qualify a field reference with the model (alias) name.

```php
public appendModelName(string $field, string|null $modelName = null): string
```

Responsibilities
----------------
• Provides **syntactic normalization only** (no metadata validation).
• Safely formats identifiers into PHQL bracket notation: [Alias].[column].
• Preserves SQL/PHQL function or expression calls (e.g. RAND(), COUNT(id)).
• Supports optional ORDER BY direction (ASC | DESC).
• Rejects obvious injection vectors.

Assumptions
-----------
• Column / alias allow-listing and validation occur upstream.
• This method must be deterministic and side-effect free.

Supported inputs
----------------
id                     → [Model].[id]
id desc                → [Model].[id] desc
alias.id               → [alias].[id]
COUNT(id)              → COUNT(id)
COUNT(id) DESC         → COUNT(id) desc
RAND()                 → RAND()
[alias].[id]           → unchanged

Rejected inputs
---------------
foo.bar.baz            → Invalid identifier
id; DROP TABLE         → Unsafe expression

**Parameters:**

| Parameter    | Type             | Description                     |
|--------------|------------------|---------------------------------|
| `$field`     | **string**       | Raw field string.               |
| `$modelName` | **string\|null** | Default alias if none provided. |

**Return Value:**

Normalized field string.

**Throws:**

When identifier or expression is unsafe.
- [`InvalidArgumentException`](../../../Exception/InvalidArgumentException.md)

***
### getPrimaryKeyAttributes

Retrieves the primary key attributes for a given model.

```php
public getPrimaryKeyAttributes(string|null $modelName = null): array
```

**Parameters:**

| Parameter    | Type             | Description                                                                                                       |
|--------------|------------------|-------------------------------------------------------------------------------------------------------------------|
| `$modelName` | **string\|null** | The name of the model to retrieve primary key attributes for. Default is null and will use $this->getModelName(). |

**Return Value:**

An array of primary key attributes for the model. Returns an empty array if no model name is specified.

***
### cacheModelColumns

```php
protected cacheModelColumns(class-string<\Phalcon\Mvc\ModelInterface> $modelName): void
```

**Parameters:**

| Parameter    | Type                                          | Description |
|--------------|-----------------------------------------------|-------------|
| `$modelName` | **class-string<\Phalcon\Mvc\ModelInterface>** |             |

***
### getGeneratedModelColumnMap

```php
protected getGeneratedModelColumnMap(\Phalcon\Mvc\ModelInterface $model): array<array-key,mixed>|null
```

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$model`  | **\Phalcon\Mvc\ModelInterface** |             |

***
### collectModelColumnMap

```php
protected collectModelColumnMap(array<string,bool>& $lookup, array<array-key,mixed>|null $columnMap): void
```

**Parameters:**

| Parameter    | Type                             | Description |
|--------------|----------------------------------|-------------|
| `$lookup`    | **array<string,bool>**           |             |
| `$columnMap` | **array<array-key,mixed>\|null** |             |

***
### collectModelAttributes

```php
protected collectModelAttributes(array<string,bool>& $lookup, array<array-key,mixed> $attributes): void
```

**Parameters:**

| Parameter     | Type                       | Description |
|---------------|----------------------------|-------------|
| `$lookup`     | **array<string,bool>**     |             |
| `$attributes` | **array<array-key,mixed>** |             |

***
### isExpression

```php
protected isExpression(string $field): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$field`  | **string** |             |

***
