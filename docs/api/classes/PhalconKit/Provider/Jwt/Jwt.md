
Issue, parse and validate JSON Web Tokens (JWT) as described in RFC 7519.

Builder (Phalcon\Encryption\Security\JWT\Builder)
Parser (Phalcon\Encryption\Security\JWT\Token\Parser)
Validator (Phalcon\Encryption\Security\JWT\Validator)

***

* Full name: `\PhalconKit\Provider\Jwt\Jwt`

## Properties

### options

```php
public array $options
```

***

### signer

```php
public \Phalcon\Encryption\Security\JWT\Signer\AbstractSigner $signer
```

***

### builder

```php
public ?\Phalcon\Encryption\Security\JWT\Builder $builder
```

***

### parser

```php
public ?\Phalcon\Encryption\Security\JWT\Token\Parser $parser
```

***

### validator

```php
public ?\Phalcon\Encryption\Security\JWT\Validator $validator
```

***

### token

```php
public ?\Phalcon\Encryption\Security\JWT\Token\Token $token
```

***

## Methods

### __construct

```php
public __construct(array $defaultOptions = []): mixed
```

**Parameters:**

| Parameter         | Type      | Description |
|-------------------|-----------|-------------|
| `$defaultOptions` | **array** |             |

***

### signer

Initialize JWT Signer

```php
public signer(?string $signer = null, ?string $algo = null): \Phalcon\Encryption\Security\JWT\Signer\AbstractSigner
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$signer` | **?string** |             |
| `$algo`   | **?string** |             |

***

### builder

Initialize JWT Builder and validate it

```php
public builder(array $options = []): \Phalcon\Encryption\Security\JWT\Builder
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$options` | **array** |             |

**Throws:**

- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### parser

Initialize JWT Parser

```php
public parser(): \Phalcon\Encryption\Security\JWT\Token\Parser
```

***

### validator

Initialize JWT Validator

```php
public validator(?\Phalcon\Encryption\Security\JWT\Token\Token $token = null, int $timeShift): \Phalcon\Encryption\Security\JWT\Validator
```

**Parameters:**

| Parameter    | Type                                              | Description |
|--------------|---------------------------------------------------|-------------|
| `$token`     | **?\Phalcon\Encryption\Security\JWT\Token\Token** |             |
| `$timeShift` | **int**                                           |             |

***

### buildToken

Build a token and validate it

```php
public buildToken(?\Phalcon\Encryption\Security\JWT\Builder $builder = null): \Phalcon\Encryption\Security\JWT\Token\Token
```

**Parameters:**

| Parameter  | Type                                          | Description |
|------------|-----------------------------------------------|-------------|
| `$builder` | **?\Phalcon\Encryption\Security\JWT\Builder** |             |

**Throws:**

- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### parseToken

Parse a jwt token and return the Token object

```php
public parseToken(string $token): \Phalcon\Encryption\Security\JWT\Token\Token
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$token`  | **string** |             |

***

### validateToken

Validate the token

```php
public validateToken(?\Phalcon\Encryption\Security\JWT\Token\Token $token = null, int $timeShift, array $options = [], ?\Phalcon\Encryption\Security\JWT\Signer\AbstractSigner $signer = null): array
```

**Parameters:**

| Parameter    | Type                                                        | Description |
|--------------|-------------------------------------------------------------|-------------|
| `$token`     | **?\Phalcon\Encryption\Security\JWT\Token\Token**           |             |
| `$timeShift` | **int**                                                     |             |
| `$options`   | **array**                                                   |             |
| `$signer`    | **?\Phalcon\Encryption\Security\JWT\Signer\AbstractSigner** |             |

**Throws:**

- [`\Phalcon\Encryption\Security\JWT\Exceptions\ValidatorException|\DateMalformedStringException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### getDefaultOptions

Get default JWT Builder Options

```php
public getDefaultOptions(array $options = []): array
```

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$options` | **array** |             |

***
