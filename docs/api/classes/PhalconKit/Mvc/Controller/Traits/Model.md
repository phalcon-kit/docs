
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

Gets the namespaces used for the model lookup.

```php
public getModelNamespaces(): array
```

If no model namespace is set, the namespaces defined in the loader will be returned.

**Return Value:**

The namespaces used for the model lookup.

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

***
### appendModelName

Appends the model name to the specified field string, if not already present.

```php
public appendModelName(string $field, string|null $modelName = null): string
```

**Parameters:**

| Parameter    | Type             | Description                                                                    |
|--------------|------------------|--------------------------------------------------------------------------------|
| `$field`     | **string**       | The field string to append the model name to.                                  |
| `$modelName` | **string\|null** | The name of the model to append. If null, the default model name will be used. |

**Return Value:**

The modified field string with the model name appended.

***
