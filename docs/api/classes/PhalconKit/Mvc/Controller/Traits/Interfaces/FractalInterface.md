
Contract for Fractal-backed REST response transformation.

Controllers can use these methods to transform models, resultsets, and
arbitrary values through a configured Fractal manager and transformer.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\FractalInterface`

## Methods

### getFractalManager

Return the current Fractal manager, creating one when needed.

```php
public getFractalManager(): \PhalconKit\Fractal\Manager
```

***

### setFractalManager

Replace or reset the current Fractal manager.

```php
public setFractalManager(?\PhalconKit\Fractal\Manager $manager): void
```

**Parameters:**

| Parameter  | Type                             | Description |
|------------|----------------------------------|-------------|
| `$manager` | **?\PhalconKit\Fractal\Manager** |             |

***

### getFractalSerializer

Return the serializer used by new Fractal managers.

```php
public getFractalSerializer(): \League\Fractal\Serializer\SerializerAbstract
```

***

### setFractalSerializer

Set the serializer used by new Fractal managers.

```php
public setFractalSerializer(\League\Fractal\Serializer\SerializerAbstract $serializer): void
```

**Parameters:**

| Parameter     | Type                                              | Description |
|---------------|---------------------------------------------------|-------------|
| `$serializer` | **\League\Fractal\Serializer\SerializerAbstract** |             |

***

### getTransformer

Return the controller's configured transformer.

```php
public getTransformer(): \League\Fractal\TransformerAbstract
```

***

### setTransformer

Replace or reset the controller's transformer.

```php
public setTransformer(?\League\Fractal\TransformerAbstract $transformer = null): void
```

**Parameters:**

| Parameter      | Type                                     | Description |
|----------------|------------------------------------------|-------------|
| `$transformer` | **?\League\Fractal\TransformerAbstract** |             |

***

### hasTransformer

Determine whether a transformer is currently configured.

```php
public hasTransformer(): bool
```

***

### transformModel

Transform one Phalcon model.

```php
public transformModel(\Phalcon\Mvc\ModelInterface $model, ?\League\Fractal\TransformerAbstract $transformer = null, ?\PhalconKit\Fractal\Manager $fractalManager = null): array<array-key,mixed>|null
```

**Parameters:**

| Parameter         | Type                                     | Description |
|-------------------|------------------------------------------|-------------|
| `$model`          | **\Phalcon\Mvc\ModelInterface**          |             |
| `$transformer`    | **?\League\Fractal\TransformerAbstract** |             |
| `$fractalManager` | **?\PhalconKit\Fractal\Manager**         |             |

***

### transformResultset

Transform a Phalcon model resultset.

```php
public transformResultset(\Phalcon\Mvc\Model\ResultsetInterface $resultset, ?\League\Fractal\TransformerAbstract $transformer = null, ?\PhalconKit\Fractal\Manager $fractalManager = null): array<array-key,mixed>|null
```

**Parameters:**

| Parameter         | Type                                      | Description |
|-------------------|-------------------------------------------|-------------|
| `$resultset`      | **\Phalcon\Mvc\Model\ResultsetInterface** |             |
| `$transformer`    | **?\League\Fractal\TransformerAbstract**  |             |
| `$fractalManager` | **?\PhalconKit\Fractal\Manager**          |             |

***

### transformItem

Transform one arbitrary item.

```php
public transformItem(mixed $data, ?\League\Fractal\TransformerAbstract $transformer = null, ?\PhalconKit\Fractal\Manager $fractalManager = null): array<array-key,mixed>|null
```

**Parameters:**

| Parameter         | Type                                     | Description |
|-------------------|------------------------------------------|-------------|
| `$data`           | **mixed**                                |             |
| `$transformer`    | **?\League\Fractal\TransformerAbstract** |             |
| `$fractalManager` | **?\PhalconKit\Fractal\Manager**         |             |

***

### transformCollection

Transform an arbitrary collection.

```php
public transformCollection(mixed $data, ?\League\Fractal\TransformerAbstract $transformer = null, ?\PhalconKit\Fractal\Manager $fractalManager = null): array<array-key,mixed>|null
```

**Parameters:**

| Parameter         | Type                                     | Description |
|-------------------|------------------------------------------|-------------|
| `$data`           | **mixed**                                |             |
| `$transformer`    | **?\League\Fractal\TransformerAbstract** |             |
| `$fractalManager` | **?\PhalconKit\Fractal\Manager**         |             |

***
