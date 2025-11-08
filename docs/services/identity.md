# Identity Service

## Configurations

```ini
IDENTITY_AUTHORIZATION_HEADER=Authorization
IDENTITY_ADAPTER=session
IDENTITY_SESSION_MODE=jwt
IDENTITY_SESSION_KEY=phalcon-kit-identity
IDENTITY_SESSION_FALLBACK=false
IDENTITY_TOKEN_EXPIRATION=+1 day
IDENTITY_REFRESH_TOKEN_EXPIRATION=+7 days
```

### Identity Service Provider

```ini
PROVIDER_IDENTITY=\Zemit\Provider\Identity\ServiceProvider
```

### Identity Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Identity\ServiceProvider::class => Env::get('PROVIDER_IDENTITY', \Zemit\Provider\Identity\ServiceProvider::class),
    ],
    'identity' => [
        'authorizationHeader' => Env::get('IDENTITY_AUTHORIZATION_HEADER', 'Authorization'),
        'adapter' => Env::get('IDENTITY_ADAPTER', 'session'), // session | database
        'mode' => Env::get('IDENTITY_SESSION_MODE', 'jwt'), // jwt | string
        'sessionKey' => Env::get('IDENTITY_SESSION_KEY', 'phalcon-kit-identity'),
        'sessionFallback' => Env::get('IDENTITY_SESSION_FALLBACK', false),
        'token' => [
            'expiration' => $this->getDateTime(Env::get('IDENTITY_TOKEN_EXPIRATION', '+1 day'), $now)->getTimestamp(),
        ],
        'refreshToken' => [
            'expiration' => $this->getDateTime(Env::get('IDENTITY_REFRESH_TOKEN_EXPIRATION', '+7 day'), $now)->getTimestamp(),
        ],
    ],
]);
```

## Identity Service (`identity`)

!!! info "Identity Service Provider"
    Identity Service Provider (`identity`):
    [`\Zemit\Provider\Identity\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Identity/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$identity = $this->identity;

// Retrieving the service from the DI
$identity = $this->di->get('identity');

// Retrieving the service from the getDI()
$identity = $this->getDI()->get('identity');

// Retrieving the service from anywhere
$identity = Di::getDefault()->get('identity');
```
