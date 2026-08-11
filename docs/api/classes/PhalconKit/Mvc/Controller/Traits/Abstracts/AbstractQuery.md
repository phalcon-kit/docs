
Abstract contract consumed by traits that delegate to the REST query layer.

Controllers using only part of the query stack can include this trait to
document the methods they expect from the full

- **See:** \PhalconKit\Mvc\Controller\Traits\Query
composition without coupling to one concrete controller class.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\AbstractQuery`

## Methods

### initializeFind

Initialize the prepared find-option collection.

```php
public initializeFind(): void
```

* This method is **abstract**.
***
### setFind

Replace the prepared find-option collection.

```php
public setFind(array|\Phalcon\Support\Collection|null $find): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                                         | Description |
|-----------|----------------------------------------------|-------------|
| `$find`   | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getFind

Return the prepared find-option collection.

```php
public getFind(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
### prepareFind

Compile the current find collection into Phalcon query options.

```php
public prepareFind(\Phalcon\Support\Collection|null $find = null, bool $ignoreKey = false): array<string|int,mixed>
```

* This method is **abstract**.
**Parameters:**

| Parameter    | Type                                  | Description                                                                    |
|--------------|---------------------------------------|--------------------------------------------------------------------------------|
| `$find`      | **\Phalcon\Support\Collection\|null** | Optional collection to compile instead of
the controller's current find state. |
| `$ignoreKey` | **bool**                              | Preserve compatibility with the concrete query
compiler signature.             |

***
### find

Execute a model find query.

```php
public find(array<string|int,mixed>|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                               | Description                    |
|-----------|------------------------------------|--------------------------------|
| `$find`   | **array<string\|int,mixed>\|null** | Optional Phalcon find options. |

***
### findWith

Execute a find query and eager-load relations.

```php
public findWith(array<string,mixed>|null $with = null, array<string|int,mixed>|null $find = null): array<int|string,mixed>
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                               | Description                    |
|-----------|------------------------------------|--------------------------------|
| `$with`   | **array<string,mixed>\|null**      | Eager-load relation map.       |
| `$find`   | **array<string\|int,mixed>\|null** | Optional Phalcon find options. |

***
### findFirst

Execute a model find-first query.

```php
public findFirst(array<string|int,mixed>|null $find = null): \Phalcon\Mvc\ModelInterface|false|null
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                               | Description                    |
|-----------|------------------------------------|--------------------------------|
| `$find`   | **array<string\|int,mixed>\|null** | Optional Phalcon find options. |

***
### findFirstWith

Execute a find-first query and eager-load relations.

```php
public findFirstWith(array<string,mixed>|null $with = null, array<string|int,mixed>|null $find = null): ?\Phalcon\Mvc\ModelInterface
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                               | Description                    |
|-----------|------------------------------------|--------------------------------|
| `$with`   | **array<string,mixed>\|null**      | Eager-load relation map.       |
| `$find`   | **array<string\|int,mixed>\|null** | Optional Phalcon find options. |

***
### average

Execute an average aggregate query.

```php
public average(array<string|int,mixed>|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                               | Description                 |
|-----------|------------------------------------|-----------------------------|
| `$find`   | **array<string\|int,mixed>\|null** | Optional aggregate options. |

***
### count

Execute a count aggregate query.

```php
public count(array<string|int,mixed>|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|int|false
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                               | Description                 |
|-----------|------------------------------------|-----------------------------|
| `$find`   | **array<string\|int,mixed>\|null** | Optional aggregate options. |

***
### sum

Execute a sum aggregate query.

```php
public sum(array<string|int,mixed>|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                               | Description                 |
|-----------|------------------------------------|-----------------------------|
| `$find`   | **array<string\|int,mixed>\|null** | Optional aggregate options. |

***
### maximum

Execute a maximum aggregate query.

```php
public maximum(array<string|int,mixed>|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                               | Description                 |
|-----------|------------------------------------|-----------------------------|
| `$find`   | **array<string\|int,mixed>\|null** | Optional aggregate options. |

***
### minimum

Execute a minimum aggregate query.

```php
public minimum(array<string|int,mixed>|null $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                               | Description                 |
|-----------|------------------------------------|-----------------------------|
| `$find`   | **array<string\|int,mixed>\|null** | Optional aggregate options. |

***
### getCalculationFind

Normalize find options before aggregate execution.

```php
protected getCalculationFind(array<string|int,mixed>|null $find = null): array<string|int,mixed>
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                               | Description                 |
|-----------|------------------------------------|-----------------------------|
| `$find`   | **array<string\|int,mixed>\|null** | Optional aggregate options. |

***
### generateBindKey

Generate a collision-resistant bind key for query parameters.

```php
public generateBindKey(string $prefix): string
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$prefix` | **string** |             |

***
