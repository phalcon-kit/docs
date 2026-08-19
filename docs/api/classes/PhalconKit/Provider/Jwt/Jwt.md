
Helper around Phalcon's JWT builder, parser, signer, and validator services.

The helper keeps the most recently created builder/parser/validator/token on
the instance so existing identity flows can build, parse, and validate a
token in multiple steps. Applications normally receive this service from the
`jwt` DI service configured by `Provider\Jwt\ServiceProvider`.

***

* Full name: `\PhalconKit\Provider\Jwt\Jwt`

## Properties

### options

Default JWT options used when a method does not receive an explicit
override.

```php
public array<string,mixed> $options
```

Recognized keys include `signer`, `algo`, `expiration`, `notBefore`,
`issuedAt`, `issuer`, `audience`, `contentType`, `passphrase`, `id`,
and `subject`.

***

### signer

Current signer used by new builders and signature validation.

```php
public \Phalcon\Encryption\Security\JWT\Signer\AbstractSigner $signer
```

***

### builder

Most recently initialized JWT builder, if any.

```php
public ?\Phalcon\Encryption\Security\JWT\Builder $builder
```

***

### parser

Most recently initialized JWT parser, if any.

```php
public ?\Phalcon\Encryption\Security\JWT\Token\Parser $parser
```

***

### validator

Most recently initialized JWT validator, if any.

```php
public ?\Phalcon\Encryption\Security\JWT\Validator $validator
```

***

### token

Most recently built or parsed token, if any.

```php
public ?\Phalcon\Encryption\Security\JWT\Token\Token $token
```

***

## Methods

### __construct

Create the JWT helper with default options and initialize its signer.

```php
public __construct(array<string,mixed> $defaultOptions = []): mixed
```

**Parameters:**

| Parameter         | Type                    | Description                                                                     |
|-------------------|-------------------------|---------------------------------------------------------------------------------|
| `$defaultOptions` | **array<string,mixed>** | Defaults used by builder(),
signer(), validateToken(), and getDefaultOptions(). |

**Throws:**

When the configured signer class does not
extend Phalcon's JWT AbstractSigner.
- [`ConfigurationException`](../../Exception/ConfigurationException.md)

***

### signer

Initialize and store the JWT signer.

```php
public signer(string|null $signer = null, string|null $algo = null): \Phalcon\Encryption\Security\JWT\Signer\AbstractSigner
```

The signer class name may be passed directly, or read from
`$this->options['signer']`. When no signer is configured, Phalcon's HMAC
signer is used with the configured `algo` or `sha512`.

**Parameters:**

| Parameter | Type             | Description                                       |
|-----------|------------------|---------------------------------------------------|
| `$signer` | **string\|null** | Signer class name; it must extend
AbstractSigner. |
| `$algo`   | **string\|null** | Hash algorithm passed to the signer
constructor.  |

**Throws:**

When the signer class does not extend
AbstractSigner.
- [`ConfigurationException`](../../Exception/ConfigurationException.md)

***

### builder

Initialize and store a JWT builder using default and explicit options.

```php
public builder(array<string,mixed> $options = []): \Phalcon\Encryption\Security\JWT\Builder
```

Explicit options override constructor defaults. The resulting builder is
stored on `$this->builder` so buildToken() can be called without passing
the builder again.

Recognized option keys are `passphrase`, `expiration`, `notBefore`,
`issuedAt`, `issuer`, `audience`, `contentType`, `id`, and `subject`.

**Parameters:**

| Parameter  | Type                    | Description               |
|------------|-------------------------|---------------------------|
| `$options` | **array<string,mixed>** | Builder option overrides. |

**Throws:**

- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### parser

Initialize and store a JWT parser.

```php
public parser(): \Phalcon\Encryption\Security\JWT\Token\Parser
```

The parser is stored on `$this->parser` for consumers that inspect the
helper state after parseToken().

***

### validator

Initialize and store a JWT validator for a token.

```php
public validator(\Phalcon\Encryption\Security\JWT\Token\Token|null $token = null, int $timeShift = 0): \Phalcon\Encryption\Security\JWT\Validator
```

If no token is passed, the most recently built or parsed token is used.

**Parameters:**

| Parameter    | Type                                                   | Description                                                 |
|--------------|--------------------------------------------------------|-------------------------------------------------------------|
| `$token`     | **\Phalcon\Encryption\Security\JWT\Token\Token\|null** | Token to validate, or null to use the current
helper token. |
| `$timeShift` | **int**                                                | Clock skew allowance passed to Phalcon's
validator.         |

**Throws:**

When no token is available.
- [`ServiceException`](../../Exception/ServiceException.md)

***

### buildToken

Build and store a token from a builder.

```php
public buildToken(\Phalcon\Encryption\Security\JWT\Builder|null $builder = null): \Phalcon\Encryption\Security\JWT\Token\Token
```

If no builder is passed, the most recently initialized builder is used.

**Parameters:**

| Parameter  | Type                                               | Description                                                |
|------------|----------------------------------------------------|------------------------------------------------------------|
| `$builder` | **\Phalcon\Encryption\Security\JWT\Builder\|null** | Builder to use, or null to use the current
helper builder. |

**Throws:**

When no builder is available.
- [`ServiceException`](../../Exception/ServiceException.md)
- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### parseToken

Parse an encoded JWT and store the resulting token.

```php
public parseToken(string $token): \Phalcon\Encryption\Security\JWT\Token\Token
```

**Parameters:**

| Parameter | Type       | Description         |
|-----------|------------|---------------------|
| `$token`  | **string** | Encoded JWT string. |

***

### validateToken

Validate a token using configured claims and signer settings.

```php
public validateToken(\Phalcon\Encryption\Security\JWT\Token\Token|null $token = null, int $timeShift = 0, array<string,mixed> $options = [], \Phalcon\Encryption\Security\JWT\Signer\AbstractSigner|null $signer = null): array<int|string,mixed>
```

If no token or signer is passed, the helper uses the current token and
signer. The method returns Phalcon validator errors; an empty array means
the token satisfied every enabled validation.

**Parameters:**

| Parameter    | Type                                                             | Description                                                                                                                                              |
|--------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$token`     | **\Phalcon\Encryption\Security\JWT\Token\Token\|null**           | Token to validate, or null to use the current
helper token.                                                                                              |
| `$timeShift` | **int**                                                          | Clock skew allowance passed to Phalcon's
validator.                                                                                                      |
| `$options`   | **array<string,mixed>**                                          | Validation option overrides.
Pass nullable `expectedSubject` to opt into validating the `sub`
claim without changing the subject used by token builders. |
| `$signer`    | **\Phalcon\Encryption\Security\JWT\Signer\AbstractSigner\|null** | Signer used for signature validation,
or null to use the current helper signer.                                                                          |

**Return Value:**

Validator errors.

**Throws:**

When no token is available.
- [`ServiceException`](../../Exception/ServiceException.md)
When the token fails validation.
- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When a token date cannot be parsed.
- [`DateMalformedStringException`](https://www.php.net/manual/en/class.datemalformedstringexception.php){:target="_blank"}

***

### getDefaultOptions

Merge explicit JWT options with constructor defaults and safe fallbacks.

```php
public getDefaultOptions(array<string,mixed> $options = []): array<string,mixed>
```

The returned array always contains `expiration`, `notBefore`, `issuedAt`,
`issuer`, `audience`, `contentType`, `passphrase`, `id`, and `subject`.

**Parameters:**

| Parameter  | Type                    | Description                |
|------------|-------------------------|----------------------------|
| `$options` | **array<string,mixed>** | Explicit option overrides. |

***

### createSigner

```php
private createSigner(string $signer, string $algo): \Phalcon\Encryption\Security\JWT\Signer\AbstractSigner
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$signer` | **string** |             |
| `$algo`   | **string** |             |

***

### requireToken

```php
private requireToken(?\Phalcon\Encryption\Security\JWT\Token\Token $token): \Phalcon\Encryption\Security\JWT\Token\Token
```

**Parameters:**

| Parameter | Type                                              | Description |
|-----------|---------------------------------------------------|-------------|
| `$token`  | **?\Phalcon\Encryption\Security\JWT\Token\Token** |             |

***

### requireBuilder

```php
private requireBuilder(?\Phalcon\Encryption\Security\JWT\Builder $builder): \Phalcon\Encryption\Security\JWT\Builder
```

**Parameters:**

| Parameter  | Type                                          | Description |
|------------|-----------------------------------------------|-------------|
| `$builder` | **?\Phalcon\Encryption\Security\JWT\Builder** |             |

***
