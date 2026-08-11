
***

* Full name: `\PhalconKit\Mvc\Model\Traits\EagerLoad`

## Methods

### find

Run Phalcon's native static finder for the model using this trait.

```php
public static find(mixed $parameters = null): \Phalcon\Mvc\Model\ResultsetInterface
```

The explicit `mixed` parameter mirrors PhalconKit's patched
`phalcon/ide-stubs` contract for `Phalcon\Mvc\Model::find()`. Keeping the
abstract dependency in sync with the upstream model API prevents static
analyzers and downstream projects from seeing this trait as a narrower,
incompatible declaration.

Eager loading requires an iterable Phalcon resultset because
`findWith()` delegates the returned records to the eager-loading loader.

* This method is **static**.* This method is **abstract**.
**Parameters:**

| Parameter     | Type      | Description                                                                             |
|---------------|-----------|-----------------------------------------------------------------------------------------|
| `$parameters` | **mixed** | Native Phalcon find parameters, usually an
array, string, integer primary key, or null. |

**Return Value:**

Resultset returned by the concrete model
implementation.

***
### findFirst

Run Phalcon's native static first-record finder for the model using this trait.

```php
public static findFirst(mixed $parameters = null): mixed
```

Phalcon can return a model instance, a row, false, null, or another value
depending on hydration and extension behavior, so this dependency keeps
the same broad `mixed` return declared by the patched Phalcon stubs.
`findFirstWith()` narrows that value at runtime and only eager-loads when
a real model instance is returned.

* This method is **static**.* This method is **abstract**.
**Parameters:**

| Parameter     | Type      | Description                                                                                   |
|---------------|-----------|-----------------------------------------------------------------------------------------------|
| `$parameters` | **mixed** | Native Phalcon find-first parameters, usually an
array, string, integer primary key, or null. |

**Return Value:**

Native result returned by the concrete model implementation.

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

The static magic method keeps the existing PhalconKit `findWithBy*`
surface. Moving this to native `missingMethods()` remains a compatibility
decision because it would change where dynamic calls are intercepted.

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

The final argument is treated as the native Phalcon finder parameters
when at least two arguments were passed. Eager loading needs complete
parent models so relation keys are available, therefore custom `columns`
selections are expanded to include `*` before the parameters are passed
to `find()` or `findFirst()`. Native Phalcon accepts both array and
string column definitions, so both shapes are normalized without changing
any other finder options.

* This method is **static**.
**Parameters:**

| Parameter    | Type      | Description |
|--------------|-----------|-------------|
| `$arguments` | **array** |             |

***
