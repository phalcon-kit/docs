
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\FractalInterface`

## Methods

### getFractalManager

```php
public getFractalManager(): \PhalconKit\Fractal\Manager
```

***

### setFractalManager

```php
public setFractalManager(?\PhalconKit\Fractal\Manager $manager): void
```

**Parameters:**

| Parameter  | Type                             | Description |
|------------|----------------------------------|-------------|
| `$manager` | **?\PhalconKit\Fractal\Manager** |             |

***

### getFractalSerializer

```php
public getFractalSerializer(): \League\Fractal\Serializer\SerializerAbstract
```

***

### setFractalSerializer

```php
public setFractalSerializer(\League\Fractal\Serializer\SerializerAbstract $serializer): void
```

**Parameters:**

| Parameter     | Type                                              | Description |
|---------------|---------------------------------------------------|-------------|
| `$serializer` | **\League\Fractal\Serializer\SerializerAbstract** |             |

***

### getTransformer

```php
public getTransformer(): \League\Fractal\TransformerAbstract
```

***

### setTransformer

```php
public setTransformer(?\League\Fractal\TransformerAbstract $transformer = null): void
```

**Parameters:**

| Parameter      | Type                                     | Description |
|----------------|------------------------------------------|-------------|
| `$transformer` | **?\League\Fractal\TransformerAbstract** |             |

***

### hasTransformer

```php
public hasTransformer(): bool
```

***

### transformModel

```php
public transformModel(\Phalcon\Mvc\ModelInterface $model, ?\League\Fractal\TransformerAbstract $transformer = null, ?\PhalconKit\Fractal\Manager $fractalManager = null): ?array
```

**Parameters:**

| Parameter         | Type                                     | Description |
|-------------------|------------------------------------------|-------------|
| `$model`          | **\Phalcon\Mvc\ModelInterface**          |             |
| `$transformer`    | **?\League\Fractal\TransformerAbstract** |             |
| `$fractalManager` | **?\PhalconKit\Fractal\Manager**         |             |

***

### transformResultset

```php
public transformResultset(\Phalcon\Mvc\Model\ResultsetInterface $resultset, ?\League\Fractal\TransformerAbstract $transformer = null, ?\PhalconKit\Fractal\Manager $fractalManager = null): ?array
```

**Parameters:**

| Parameter         | Type                                      | Description |
|-------------------|-------------------------------------------|-------------|
| `$resultset`      | **\Phalcon\Mvc\Model\ResultsetInterface** |             |
| `$transformer`    | **?\League\Fractal\TransformerAbstract**  |             |
| `$fractalManager` | **?\PhalconKit\Fractal\Manager**          |             |

***

### transformItem

```php
public transformItem(mixed $data, ?\League\Fractal\TransformerAbstract $transformer = null, ?\PhalconKit\Fractal\Manager $fractalManager = null): ?array
```

**Parameters:**

| Parameter         | Type                                     | Description |
|-------------------|------------------------------------------|-------------|
| `$data`           | **mixed**                                |             |
| `$transformer`    | **?\League\Fractal\TransformerAbstract** |             |
| `$fractalManager` | **?\PhalconKit\Fractal\Manager**         |             |

***

### transformCollection

```php
public transformCollection(mixed $data, ?\League\Fractal\TransformerAbstract $transformer = null, ?\PhalconKit\Fractal\Manager $fractalManager = null): ?array
```

**Parameters:**

| Parameter         | Type                                     | Description |
|-------------------|------------------------------------------|-------------|
| `$data`           | **mixed**                                |             |
| `$transformer`    | **?\League\Fractal\TransformerAbstract** |             |
| `$fractalManager` | **?\PhalconKit\Fractal\Manager**         |             |

***
