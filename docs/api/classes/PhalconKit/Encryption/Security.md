
{@inheritDoc}

***

* Full name: `\PhalconKit\Encryption\Security`
* Parent class: [`Security`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### __construct

```php
public __construct(?\Phalcon\Session\ManagerInterface $session = null, ?\Phalcon\Http\RequestInterface $request = null): mixed
```

**Parameters:**

| Parameter  | Type                                   | Description |
|------------|----------------------------------------|-------------|
| `$session` | **?\Phalcon\Session\ManagerInterface** |             |
| `$request` | **?\Phalcon\Http\RequestInterface**    |             |

***

### getConfig

```php
public getConfig(): \PhalconKit\Config\ConfigInterface
```

***

### hash

```php
public hash(string $password, array $options = []): string
```

**Parameters:**

| Parameter   | Type       | Description |
|-------------|------------|-------------|
| `$password` | **string** |             |
| `$options`  | **array**  |             |

***

### getRandom

```php
public getRandom(): \PhalconKit\Encryption\Security\Random
```

***
