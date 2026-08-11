
Security service with PhalconKit random generation and Argon2 defaults.

The class preserves Phalcon's security API while replacing the random helper
with PhalconKit's implementation. When Argon2 hashing is selected, hash
options are completed from `security.argon2` config before falling back to
PHP's password defaults.

***

* Full name: `\PhalconKit\Encryption\Security`
* Parent class: [`Security`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### __construct

Create the security service and install the PhalconKit random helper.

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

Return the application config service used for security defaults.

```php
public getConfig(): \PhalconKit\Config\ConfigInterface
```

**Return Value:**

Configuration service registered in the DI.

***

### hash

Hash a password, merging configured Argon2 options when applicable.

```php
public hash(string $password, array<string,mixed> $options = []): string
```

Explicit options passed by the caller always win. Missing Argon2
`memory_cost`, `time_cost`, and `threads` values are filled from the
framework config before PHP defaults are used.

**Parameters:**

| Parameter   | Type                    | Description                      |
|-------------|-------------------------|----------------------------------|
| `$password` | **string**              | Password or secret to hash.      |
| `$options`  | **array<string,mixed>** | Algorithm-specific hash options. |

**Return Value:**

Password hash returned by Phalcon/PHP.

***

### getRandom

Return the PhalconKit random helper used by this security service.

```php
public getRandom(): \PhalconKit\Encryption\Security\Random
```

***
