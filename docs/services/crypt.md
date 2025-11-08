# Crypt Service

The `crypt` service is using the
[Phalcon Cryptography Component](https://docs.phalcon.io/latest/encryption-crypt/?h=crypt){:target="_blank"}

## Configurations

```ini
CRYPT_PAD_FACTORY = \Phalcon\Encryption\Crypt\PadFactory
CRYPT_PADDING_SCHEME = 0
CRYPT_HASH_ALGORITHM = sha256
CRYPT_USE_SIGNING = true
CRYPT_CIPHER = aes-256-cfb
CRYPT_KEY = T4\xb1\x8d\xa9\x98\x05\\x8c\xbe\x1d\x07&[\x99\x18\xa4~Lc1\xbeW\xb3
CRYPT_AUTH_DATA =
CRYPT_AUTH_TAG =
CRYPT_AUTH_TAG_LENGTH =
```

### Crypt Key Configuration

The component offers a getter and a setter for the key to be used. Once the key is set, it will be used for any
encrypting or decrypting operation

```ini
# Bad Key
CRYPT_KEY = "le password"

# Better key
CRYPT_KEY = "#1dj8$=dp?.ak//j1V$~%0X"

# Good key
CRYPT_KEY = T4\xb1\x8d\xa9\x98\x05\\x8c\xbe\x1d\x07&[\x99\x18\xa4~Lc1\xbeW\xb3
```

### Crypt Service Provider

```ini
PROVIDER_CRYPT = \PhalconKit\Provider\Crypt\ServiceProvider
```

### Crypt Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Crypt\ServiceProvider::class => Env::get('PROVIDER_CRYPT', \PhalconKit\Provider\Crypt\ServiceProvider::class),
    ],
    'crypt' => [
        'paddingFactory' => Env::get('CRYPT_PAD_FACTORY', \Phalcon\Encryption\Crypt\PadFactory::class),
        'paddingScheme' => Env::get('CRYPT_PADDING_SCHEME', \Phalcon\Encryption\Crypt::PADDING_DEFAULT),
        'hashAlgorithm' => Env::get('CRYPT_HASH_ALGORITHM', 'sha256'),
        'useSigning' => Env::get('CRYPT_USE_SIGNING', true),
        'cipher' => Env::get('CRYPT_CIPHER', 'aes-256-cfb'),
        'key' => Env::get('CRYPT_KEY', 'T4\xb1\x8d\xa9\x98\x05\\x8c\xbe\x1d\x07&[\x99\x18\xa4~Lc1\xbeW\xb3'),
        'authData' => Env::get('CRYPT_AUTH_DATA', ''),
        'authTag' => Env::get('CRYPT_AUTH_TAG', ''),
        'authTagLength' => Env::get('CRYPT_AUTH_TAG_LENGTH', 16),
    ],
]);
```

## Crypt Service (`crypt`)

!!! info "Crypt Service Provider"
    Crypt Service Provider (`crypt`):
    [`\PhalconKit\Provider\Crypt\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Crypt/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$crypt = $this->crypt;

// Retrieving the service from the DI
$crypt = $this->di->get('crypt');

// Retrieving the service from the getDI()
$crypt = $this->getDI()->get('crypt');

// Retrieving the service from anywhere
$crypt = Di::getDefault()->get('crypt');
```
