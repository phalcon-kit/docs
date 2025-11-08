
***

* Full name: `\PhalconKit\Mvc\Model\Traits\EagerLoad`

## Methods

### find

```php
public static find(mixed $parameters = null): mixed
```

* This method is **static**.* This method is **abstract**.
**Parameters:**

| Parameter     | Type      | Description |
|---------------|-----------|-------------|
| `$parameters` | **mixed** |             |

***
### findFirst

```php
public static findFirst(mixed $parameters = null): mixed
```

* This method is **static**.* This method is **abstract**.
**Parameters:**

| Parameter     | Type      | Description |
|---------------|-----------|-------------|
| `$parameters` | **mixed** |             |

***
### findWith

Example:

```php
public static findWith(array $arguments): array
```

```php
$limit = 100;
$offset = max(0, $this->request->getQuery('page', 'int') - 1) * $limit;

$manufacturers = Manufacturer::with('Robots.Parts', [
    'limit' => [$limit, $offset]
]);

foreach ($manufacturers as $manufacturer) {
    foreach ($manufacturer->robots as $robot) {
        foreach ($robot->parts as $part) { ... }
    }
}
```

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***
### findFirstWith

Same as EagerLoadingTrait::findWith() for a single record

```php
public static findFirstWith(array $arguments): ?\Phalcon\Mvc\ModelInterface
```

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***
### with

```php
public static with(array $arguments): array
```

* This method is **static**.* **Warning:** this method is **deprecated**. This means that this method will likely be removed in a future version.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

**See Also:**

* static::findWith()

***
### firstWith

```php
public static firstWith(array $arguments): ?\Phalcon\Mvc\ModelInterface
```

* This method is **static**.* **Warning:** this method is **deprecated**. This means that this method will likely be removed in a future version.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

**See Also:**

* static::findFirstWith()

***
### __callStatic

Dynamically handles static method calls for the class, forwarding them to
appropriate internal methods based on the method name patterns.

```php
public static __callStatic(string $method, array $arguments = []): array|\Phalcon\Mvc\ModelInterface|null
```

The method provides a mechanism to resolve calls like "findFirstWithBy..."/"firstWithBy..."
and "findWithBy..."/"withBy..." to their corresponding mapped operations.

* This method is **static**.
**Parameters:**

| Parameter    | Type       | Description                                        |
|--------------|------------|----------------------------------------------------|
| `$method`    | **string** | The name of the static method being called.        |
| `$arguments` | **array**  | An array of arguments passed to the static method. |

**Return Value:**

Returns the result of the forwarded operation, which may be
an array, an implementation of ModelInterface, or null.

***
### findFirstWithBy

Call native Phalcon FindFirstBy function then eager load relationships from the model

```php
protected static findFirstWithBy(string $forwardMethod, array $arguments): ?\Phalcon\Mvc\ModelInterface
```

* This method is **static**.
**Parameters:**

| Parameter        | Type       | Description |
|------------------|------------|-------------|
| `$forwardMethod` | **string** |             |
| `$arguments`     | **array**  |             |

***
### findWithBy

Call native Phalcon findBy function then eager load relationships from the resultset

```php
protected static findWithBy(string $forwardMethod, array $arguments): ?array
```

* This method is **static**.
**Parameters:**

| Parameter        | Type       | Description |
|------------------|------------|-------------|
| `$forwardMethod` | **string** |             |
| `$arguments`     | **array**  |             |

***
### load

Example:

```php
public load(array $arguments): ?\Phalcon\Mvc\ModelInterface
```

```php
$manufacturer = Manufacturer::findFirstById(51);

$manufacturer->load('Robots.Parts');

foreach ($manufacturer->robots as $robot) {
   foreach ($robot->parts as $part) { ... }
}
```

**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***
### getParametersFromArguments

Get the query parameters from a list of arguments

```php
public static getParametersFromArguments(array& $arguments): mixed
```

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***
