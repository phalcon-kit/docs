
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\AbstractQuery`

## Methods

### initializeFind

```php
public initializeFind(): void
```

* This method is **abstract**.
***
### setFind

```php
public setFind(?\Phalcon\Support\Collection $find): void
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type                             | Description |
|-----------|----------------------------------|-------------|
| `$find`   | **?\Phalcon\Support\Collection** |             |

***
### getFind

```php
public getFind(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
### find

```php
public find(?array $find = null): mixed
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$find`   | **?array** |             |

***
### findWith

```php
public findWith(?array $with = null, ?array $find = null): array
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$with`   | **?array** |             |
| `$find`   | **?array** |             |

***
### findFirst

```php
public findFirst(?array $find = null): \Phalcon\Mvc\ModelInterface|false|null
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$find`   | **?array** |             |

***
### findFirstWith

```php
public findFirstWith(?array $with = null, ?array $find = null): ?\Phalcon\Mvc\ModelInterface
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$with`   | **?array** |             |
| `$find`   | **?array** |             |

***
### average

```php
public average(?array $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$find`   | **?array** |             |

***
### count

```php
public count(?array $find = null): \Phalcon\Mvc\Model\ResultsetInterface|int|false
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$find`   | **?array** |             |

***
### sum

```php
public sum(?array $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$find`   | **?array** |             |

***
### maximum

```php
public maximum(?array $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$find`   | **?array** |             |

***
### minimum

```php
public minimum(?array $find = null): \Phalcon\Mvc\Model\ResultsetInterface|float|false
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$find`   | **?array** |             |

***
### getCalculationFind

```php
protected getCalculationFind(?array $find = null): array
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$find`   | **?array** |             |

***
### generateBindKey

```php
public generateBindKey(string $prefix): string
```

* This method is **abstract**.
**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$prefix` | **string** |             |

***
