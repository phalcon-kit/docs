
Contract for resolving the model managed by a REST controller.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\ModelInterface`

## Methods

### getModelName

Return the explicit model class name, when one is configured.

```php
public getModelName(): class-string<\Phalcon\Mvc\ModelInterface>|null
```

***

### setModelName

Set the explicit model class name for this controller.

```php
public setModelName(class-string<\Phalcon\Mvc\ModelInterface>|null $modelName): void
```

**Parameters:**

| Parameter    | Type                                                | Description |
|--------------|-----------------------------------------------------|-------------|
| `$modelName` | **class-string<\Phalcon\Mvc\ModelInterface>\|null** |             |

***

### getModelNamespaces

Return namespace prefixes searched when deriving a model from a controller.

```php
public getModelNamespaces(): list<string>
```

***

### setModelNamespaces

Replace namespace prefixes searched when deriving a model from a controller.

```php
public setModelNamespaces(list<string>|null $modelNamespaces): void
```

**Parameters:**

| Parameter          | Type                   | Description |
|--------------------|------------------------|-------------|
| `$modelNamespaces` | **list<string>\|null** |             |

***

### getModelNameFromController

Infer a model class name from the controller namespace/class.

```php
public getModelNameFromController(list<string>|null $namespaces = null, string $needle = 'Models'): class-string<\Phalcon\Mvc\ModelInterface>|null
```

**Parameters:**

| Parameter     | Type                   | Description                                 |
|---------------|------------------------|---------------------------------------------|
| `$namespaces` | **list<string>\|null** | Optional namespace prefixes.                |
| `$needle`     | **string**             | Namespace segment to replace with `Models`. |

***

### getControllerName

Return the current controller route name.

```php
public getControllerName(): string
```

***

### loadModel

Resolve and instantiate the configured model class.

```php
public loadModel(class-string<\Phalcon\Mvc\ModelInterface>|null $modelName = null): \Phalcon\Mvc\ModelInterface
```

**Parameters:**

| Parameter    | Type                                                | Description        |
|--------------|-----------------------------------------------------|--------------------|
| `$modelName` | **class-string<\Phalcon\Mvc\ModelInterface>\|null** | Optional
override. |

***

### modelHasColumn

Determine whether the configured model exposes a raw database column or a
mapped model attribute name.

```php
public modelHasColumn(string $column, string|null $modelName = null): bool
```

Implementations should use generated `columnMap()` definitions or Phalcon
model metadata rather than issuing application-level data queries. Models
without generated maps may depend on the application's configured metadata
strategy and cache.

**Parameters:**

| Parameter    | Type             | Description                                                                                               |
|--------------|------------------|-----------------------------------------------------------------------------------------------------------|
| `$column`    | **string**       | Database column or mapped model attribute.                                                                |
| `$modelName` | **string\|null** | Optional model override; defaults to the
current controller model. Non-model strings should return false. |

***
