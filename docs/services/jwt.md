# JWT Service

The `jwt` service is a basic and naive configuration wrapper of the
[Phalcon JWT component](https://docs.phalcon.io/latest/encryption-security-jwt/?h=jwt#signer){:target="_blank"}.

## JWT Configurations

```ini
SECURITY_JWT_SIGNER = \Phalcon\Encryption\Security\JWT\Signer\Hmac
SECURITY_JWT_ALGO = sha512
SECURITY_JWT_CONTENT_TYPE = application/json
SECURITY_JWT_EXPIRATION = +1 day
SECURITY_JWT_NOT_BEFORE = -1 minute
SECURITY_JWT_ISSUED_AT = now
SECURITY_JWT_ISSUER =
SECURITY_JWT_AUDIENCE =
SECURITY_JWT_ID =
SECURITY_JWT_SUBJECT =
SECURITY_JWT_PASSPHRASE = "Tf0PHY/^yDdJs*~)?x#xCNj_N[jW/`c*"
```

### JWT Secure Configurations

To ensure a decent level of security on your application, we strongly recommend to generate your own passphrase of
**32 characters**.

```ini
# Not secure, change the passphrase to your own
SECURITY_JWT_PASSPHRASE = "cKu%M:v|l">JdPf1z~C&^>cpFrtrkN2/"
```

### JWT Extend Expiration

You can extend the JWT validation period for your needs, the string value will be parsed using DateTime.
Valid formats are explained in
[Valid Date and Time Formats](https://www.php.net/manual/en/datetime.formats.php){:target="_blank"}.

```ini
SECURITY_JWT_EXPIRATION = +1 week
```

### JWT Change Signer

You can use your own Signer. It must implement the `\Phalcon\Encryption\Security\JWT\Signer\SignerInterface` interface
or extend the `Phalcon\Encryption\Security\JWT\Signer\AbstractSigner` classes.

```ini
SECURITY_JWT_SIGNER = \Phalcon\Encryption\Security\JWT\Signer\Hmac
```

### JWT Hmac Algorithms

The HMAC signer supports the `sha512`, `sha384`, and `sha256` algorithms. If none is supplied, the `sha512` is automatically
selected.

```ini
SECURITY_JWT_ALGO = sha512
```

### JWT Service Provider

```ini
PROVIDER_JWT = \Zemit\Provider\Jwt\ServiceProvider
```

### JWT Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Jwt\ServiceProvider::class => Env::get('PROVIDER_JWT', \Zemit\Provider\Jwt\ServiceProvider::class),
    ],
    'security' => [
        // ...
        'jwt' => [
            'signer' => Env::get('SECURITY_JWT_SIGNER', \Phalcon\Encryption\Security\JWT\Signer\Hmac::class),
            'algo' => Env::get('SECURITY_JWT_ALGO', 'sha512'),
            'contentType' => Env::get('SECURITY_JWT_CONTENT_TYPE', 'application/json'),
            'expiration' => $this->getDateTime(Env::get('SECURITY_JWT_EXPIRATION', '+1 day'), $now)->getTimestamp(),
            'notBefore' => $this->getDateTime(Env::get('SECURITY_JWT_NOT_BEFORE', '-1 minute'), $now)->getTimestamp(),
            'issuedAt' => $this->getDateTime(Env::get('SECURITY_JWT_ISSUED_AT', 'now'), $now)->getTimestamp(),
            'issuer' => Env::get('SECURITY_JWT_ISSUER', 'ZEMIT_CORE_DEFAULT_ISSUER'),
            'audience' => Env::get('SECURITY_JWT_AUDIENCE', 'ZEMIT_CORE_DEFAULT_AUDIENCE'),
            'id' => Env::get('SECURITY_JWT_ID', 'ZEMIT_CORE_DEFAULT_ID'),
            'subject' => Env::get('SECURITY_JWT_SUBJECT', 'ZEMIT_CORE_DEFAULT_SUBJECT'),
            'passphrase' => Env::get('SECURITY_JWT_PASSPHRASE', 'Tf0PHY/^yDdJs*~)?x#xCNj_N[jW/`c*'),
        ],
    ],
]);
```

## JWT Service (`jwt`)

!!! info "JWT Service Provider"
    Jwt Service Provider (`jwt`):
    [`\Zemit\Provider\Jwt\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Jwt/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$jwt = $this->jwt;

// Retrieving the service from the DI
$jwt = $this->di->get('jwt');

// Retrieving the service from the getDI()
$jwt = $this->getDI()->get('jwt');

// Retrieving the service from anywhere
$jwt = Di::getDefault()->get('jwt');
```
