# Security Service

The `security` service uses the [Phalcon Security Component](https://docs.phalcon.io/latest/encryption-security/){:target="_blank"}

## Configurations

```ini
SECURITY_WORK_FACTOR=12
SECURITY_HASH=11
SECURITY_SALT=>mY.Db5fR?k%~<ZWf\}Zh35_IFC]#0Xx
SECURITY_ARGON2_MEMORY_COST=65536
SECURITY_ARGON2_TIME_COST=4
SECURITY_ARGON2_THREADS=1
```

### Security Salt Configuration

```ini
SECURITY_SALT=>mY.Db5fR?k%~<ZWf\}Zh35_IFC]#0Xx
```

### Security Service Provider

```ini
PROVIDER_SECURITY=\Zemit\Provider\Security\ServiceProvider
```

### Security Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Security\ServiceProvider::class => Env::get('PROVIDER_SECURITY', \Zemit\Provider\Security\ServiceProvider::class),
    ],
    'security' => [ // phalcon security config
        'workFactor' => Env::get('SECURITY_WORK_FACTOR', 12), // workfactor for the phalcon security service
        'hash' => Env::get('SECURITY_HASH', Security::CRYPT_ARGON2ID), // set default hash to sha512
        'salt' => Env::get('SECURITY_SALT', '>mY.Db5fR?k%~<ZWf\}Zh35_IFC]#0Xx'), // salt for the phalcon security service
        'argon2' => [
            'memoryCost' => Env::get('SECURITY_ARGON2_MEMORY_COST', PASSWORD_ARGON2_DEFAULT_MEMORY_COST),
            'timeCost' => Env::get('SECURITY_ARGON2_TIME_COST', PASSWORD_ARGON2_DEFAULT_TIME_COST),
            'threads' => Env::get('SECURITY_ARGON2_THREADS', PASSWORD_ARGON2_DEFAULT_THREADS),
        ],
    ],
]);
```

## Security Service (`security`)

!!! info "Security Service Provider"
    Security Service Provider (`security`):
    [`\Zemit\Provider\Security\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Security/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$security = $this->security;

// Retrieving the service from the DI
$security = $this->di->get('security');

// Retrieving the service from the getDI()
$security = $this->getDI()->get('security');

// Retrieving the service from anywhere
$security = Di::getDefault()->get('security');
```
