
This trait provides methods for working with Fractal, a library for transforming data structures.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Fractal`

## Properties

### fractalManager

```php
public ?\PhalconKit\Fractal\Manager $fractalManager
```

***
### fractalSerializer

```php
public ?\League\Fractal\Serializer\SerializerAbstract $fractalSerializer
```

***
### transformer

```php
public ?\League\Fractal\TransformerAbstract $transformer
```

***

## Methods

### getFractalManager

Get the Fractal Manager object.

```php
public getFractalManager(): \PhalconKit\Fractal\Manager
```

This method returns the Fractal Manager object used for transforming data.
If the Fractal Manager object is not already created, it will be created
and initialized with the Fractal Serializer before being returned.

**Return Value:**

The Fractal Manager object.

***
### setFractalManager

Set the Fractal Manager for the class.

```php
public setFractalManager(\PhalconKit\Fractal\Manager|null $manager): void
```

**Parameters:**

| Parameter  | Type                                  | Description                                                                |
|------------|---------------------------------------|----------------------------------------------------------------------------|
| `$manager` | **\PhalconKit\Fractal\Manager\|null** | The Fractal Manager to be set. If null, the Fractal Manager will be unset. |

***
### getFractalSerializer

Get the fractal serializer for the class.

```php
public getFractalSerializer(): \League\Fractal\Serializer\SerializerAbstract
```

**Return Value:**

The fractal serializer instance.

***
### setFractalSerializer

Set the Fractal serializer for the class.

```php
public setFractalSerializer(\League\Fractal\Serializer\SerializerAbstract $serializer): void
```

**Parameters:**

| Parameter     | Type                                              | Description                       |
|---------------|---------------------------------------------------|-----------------------------------|
| `$serializer` | **\League\Fractal\Serializer\SerializerAbstract** | The Fractal serializer to be set. |

***
### getTransformer

Get the transformer for the class.

```php
public getTransformer(): \League\Fractal\TransformerAbstract
```

If the transformer has not been set, a new instance of ModelTransformer will be created.

**Return Value:**

The transformer for the class.

***
### setTransformer

Set the transformer for the class.

```php
public setTransformer(\League\Fractal\TransformerAbstract|null $transformer = null): void
```

**Parameters:**

| Parameter      | Type                                          | Description                                                        |
|----------------|-----------------------------------------------|--------------------------------------------------------------------|
| `$transformer` | **\League\Fractal\TransformerAbstract\|null** | The transformer to be set. If null, the transformer will be unset. |

***
### hasTransformer

Determine if a default transformer has been set for the fractal manager

```php
public hasTransformer(): bool
```

**Return Value:**

Returns true if a default transformer has been set, false otherwise

***
### transformModel

Transform a model using a transformer and optionally a fractal manager.

```php
public transformModel(\Phalcon\Mvc\ModelInterface $model, \League\Fractal\TransformerAbstract|null $transformer = null, \PhalconKit\Fractal\Manager|null $fractalManager = null): array|null
```

**Parameters:**

| Parameter         | Type                                          | Description                                                                            |
|-------------------|-----------------------------------------------|----------------------------------------------------------------------------------------|
| `$model`          | **\Phalcon\Mvc\ModelInterface**               | The model to transform.                                                                |
| `$transformer`    | **\League\Fractal\TransformerAbstract\|null** | The transformer to use. If not provided, the default transformer will be used.         |
| `$fractalManager` | **\PhalconKit\Fractal\Manager\|null**         | The fractal manager to use. If not provided, the default fractal manager will be used. |

**Return Value:**

The transformed model as an array, or null if the transformation fails.

***
### transformResultset

Transforms a resultset using the provided transformer and fractal manager.

```php
public transformResultset(\Phalcon\Mvc\Model\ResultsetInterface $resultset, \League\Fractal\TransformerAbstract|null $transformer = null, \PhalconKit\Fractal\Manager|null $fractalManager = null): array|null
```

**Parameters:**

| Parameter         | Type                                          | Description                                                            |
|-------------------|-----------------------------------------------|------------------------------------------------------------------------|
| `$resultset`      | **\Phalcon\Mvc\Model\ResultsetInterface**     | The resultset to be transformed.                                       |
| `$transformer`    | **\League\Fractal\TransformerAbstract\|null** | The transformer instance to be used for transformation (optional).     |
| `$fractalManager` | **\PhalconKit\Fractal\Manager\|null**         | The fractal manager instance to be used for transformation (optional). |

**Return Value:**

The transformed resultset as an array, or null if the transformation failed.

***
### transformItem

Transform an item using the specified transformer and Fractal manager

```php
public transformItem(mixed $data, \League\Fractal\TransformerAbstract|null $transformer = null, \PhalconKit\Fractal\Manager|null $fractalManager = null): array|null
```

**Parameters:**

| Parameter         | Type                                          | Description                                            |
|-------------------|-----------------------------------------------|--------------------------------------------------------|
| `$data`           | **mixed**                                     | The data to transform                                  |
| `$transformer`    | **\League\Fractal\TransformerAbstract\|null** | The transformer to use (optional, default is null)     |
| `$fractalManager` | **\PhalconKit\Fractal\Manager\|null**         | The Fractal manager to use (optional, default is null) |

**Return Value:**

The transformed item as an array

***
### transformCollection

Transform a collection of data using a specified transformer and Fractal manager.

```php
public transformCollection(mixed $data, \League\Fractal\TransformerAbstract|null $transformer = null, \PhalconKit\Fractal\Manager|null $fractalManager = null): array|null
```

**Parameters:**

| Parameter         | Type                                          | Description                                                                                |
|-------------------|-----------------------------------------------|--------------------------------------------------------------------------------------------|
| `$data`           | **mixed**                                     | The collection of data to be transformed.                                                  |
| `$transformer`    | **\League\Fractal\TransformerAbstract\|null** | The transformer to be used. If not provided, the default transformer will be used.         |
| `$fractalManager` | **\PhalconKit\Fractal\Manager\|null**         | The Fractal manager to be used. If not provided, the default Fractal manager will be used. |

**Return Value:**

The transformed data as an array.

***
