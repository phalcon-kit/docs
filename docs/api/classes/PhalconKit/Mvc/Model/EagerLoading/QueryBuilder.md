
***

* Full name: `\PhalconKit\Mvc\Model\EagerLoading\QueryBuilder`
* Parent class: [`Builder`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class is marked as **final** and can't be subclassed
* This class is a **Final class**

## Constants

| Constant                    | Visibility | Type | Value                                                            |
|-----------------------------|------------|------|------------------------------------------------------------------|
| `E_NOT_ALLOWED_METHOD_CALL` | public     |      | 'When eager loading relations queries must return full entities' |

## Methods

### distinct

```php
public distinct(mixed $distinct): \Phalcon\Mvc\Model\Query\BuilderInterface
```

**Parameters:**

| Parameter   | Type      | Description |
|-------------|-----------|-------------|
| `$distinct` | **mixed** |             |

**Throws:**

- [`LogicException`](../../../../LogicException.md)

***

### columns

```php
public columns(mixed $columns): \Phalcon\Mvc\Model\Query\BuilderInterface
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$columns` | **mixed** |             |

**Throws:**

- [`LogicException`](../../../../LogicException.md)

***

### where

Replacing where to andWhere in order to avoid loosing relationship conditions

```php
public where(string $conditions, array $bindParams = [], array $bindTypes = []): \Phalcon\Mvc\Model\Query\BuilderInterface
```

**Parameters:**

| Parameter     | Type       | Description |
|---------------|------------|-------------|
| `$conditions` | **string** |             |
| `$bindParams` | **array**  |             |
| `$bindTypes`  | **array**  |             |

***
