
***

* Full name: `\PhalconKit\Mvc\Controller\RestInterface`
* Parent interfaces:
  [`\PhalconKit\Mvc\Controller\Traits\Interfaces\DebugInterface`](./Traits/Interfaces/DebugInterface.md),
  [`\PhalconKit\Mvc\Controller\Traits\Interfaces\BehaviorInterface`](./Traits/Interfaces/BehaviorInterface.md),
  [`\PhalconKit\Mvc\Controller\Traits\Interfaces\ParamsInterface`](./Traits/Interfaces/ParamsInterface.md),
  [`\PhalconKit\Mvc\Controller\Traits\Interfaces\FractalInterface`](./Traits/Interfaces/FractalInterface.md),
  [`\PhalconKit\Mvc\Controller\Traits\Interfaces\RestResponseInterface`](./Traits/Interfaces/RestResponseInterface.md)

## Inherited methods

### setRestErrorResponse

```php
public setRestErrorResponse(int $code = 400, string $status = 'Bad Request', mixed $response = null): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter   | Type       | Description |
|-------------|------------|-------------|
| `$code`     | **int**    |             |
| `$status`   | **string** |             |
| `$response` | **mixed**  |             |

***

### setRestResponse

```php
public setRestResponse(mixed $response = null, ?int $code = null, ?string $status = null, int $jsonOptions, int $depth = 512): \Phalcon\Http\ResponseInterface
```

**Parameters:**

| Parameter      | Type        | Description |
|----------------|-------------|-------------|
| `$response`    | **mixed**   |             |
| `$code`        | **?int**    |             |
| `$status`      | **?string** |             |
| `$jsonOptions` | **int**     |             |
| `$depth`       | **int**     |             |

***

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

### getParam

```php
public getParam(string $key, array|string|null $filters = null, mixed $default = null, ?array $params = null): mixed
```

**Parameters:**

| Parameter  | Type                    | Description |
|------------|-------------------------|-------------|
| `$key`     | **string**              |             |
| `$filters` | **array\|string\|null** |             |
| `$default` | **mixed**               |             |
| `$params`  | **?array**              |             |

***

### hasParam

```php
public hasParam(string $key, ?array $params = null, bool $cached = true): bool
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$key`    | **string** |             |
| `$params` | **?array** |             |
| `$cached` | **bool**   |             |

***

### getParams

```php
public getParams(?array $fields = null, bool $cached = true, bool $deep = true): array
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$fields` | **?array** |             |
| `$cached` | **bool**   |             |
| `$deep`   | **bool**   |             |

***

### getAllParams

```php
public getAllParams(?array $filters = null, bool $cached = true, bool $deep = true): array
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$filters` | **?array** |             |
| `$cached`  | **bool**   |             |
| `$deep`    | **bool**   |             |

***

### applyFilters

```php
public applyFilters(array<string,mixed> $params, array<string,array|string> $filters, bool $deep = true): array<string,mixed>
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$params`  | **array<string,mixed>**         |             |
| `$filters` | **array<string,array\|string>** |             |
| `$deep`    | **bool**                        |             |

***

### setDefaultFilters

```php
public setDefaultFilters(array<string,array|string> $filters): static
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$filters` | **array<string,array\|string>** |             |

***

### addDefaultFilters

```php
public addDefaultFilters(array<string,array|string> $filters): static
```

**Parameters:**

| Parameter  | Type                            | Description |
|------------|---------------------------------|-------------|
| `$filters` | **array<string,array\|string>** |             |

***

### removeFilters

```php
public removeFilters(string|array<int,string> $keys): static
```

**Parameters:**

| Parameter | Type                          | Description |
|-----------|-------------------------------|-------------|
| `$keys`   | **string\|array<int,string>** |             |

***

### clearDefaultFilters

```php
public clearDefaultFilters(): static
```

***

### getDefaultFilters

```php
public getDefaultFilters(): array
```

***

### getRawParams

```php
public getRawParams(bool $cached = true): array
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$cached` | **bool** |             |

***

### attachBehavior

```php
public attachBehavior(string $eventClass, ?string $eventType = null, ?int $priority = null): void
```

**Parameters:**

| Parameter     | Type        | Description |
|---------------|-------------|-------------|
| `$eventClass` | **string**  |             |
| `$eventType`  | **?string** |             |
| `$priority`   | **?int**    |             |

***

### attachBehaviors

```php
public attachBehaviors(array $behaviors = [], ?string $eventType = null, ?int $priority = null): void
```

**Parameters:**

| Parameter    | Type        | Description |
|--------------|-------------|-------------|
| `$behaviors` | **array**   |             |
| `$eventType` | **?string** |             |
| `$priority`  | **?int**    |             |

***

### isDebugEnabled

```php
public isDebugEnabled(): bool
```

***
