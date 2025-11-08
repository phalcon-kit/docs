# Config Service

## Configurations

### Config Service Provider

```ini
PROVIDER_CONFIG=\PhalconKit\Provider\Config\ServiceProvider
```

### Config Configurations Object

```php
<?php
new Config([
    // global config
    'phalcon' => [],
    'core' => [],
    'app' => [],
    'php' => [],
    'debug' => [],
    'response' => [],
    'identity' => [],
    'models' => [],
    'providers' => [],
    'logger' => [],
    'filters' => [],
    'modules' => [],
    'router' => [],
    'gravatar' => [],
    'reCaptcha' => [],
    'aws' => [],
    'locale' => [],
    'translate' => [],
    'session' => [],
    'module' => [],
    'security' => [],
    'cache' => [],
    'metadata' => [],
    'annotations' => [],
    'mailer' => [],
    'cookies' => [],
    'oauth2' => [],
    'dotenv' => [],
    'client' => [],
    'permissions' => [],
    // ...
]);
```

## Config Service (`config`)

!!! info "Config Service Provider"
    Config Service Provider (`config`):
    [`\PhalconKit\Provider\Config\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Config/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$config = $this->config;

// Retrieving the service from the DI
$config = $this->di->get('config');

// Retrieving the service from the getDI()
$config = $this->getDI()->get('config');

// Retrieving the service from anywhere
$config = Di::getDefault()->get('config');
```
