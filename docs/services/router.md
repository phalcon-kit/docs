# Router Service

## Configuration

### Setting Default Routes

=== "Defaults"

    ```ini
    ROUTER_DEFAULT_NAMESPACE=Zemit\\Modules\\Frontend\\Controllers
    ROUTER_DEFAULT_MODULE=frontend
    ROUTER_DEFAULT_CONTROLLER=index
    ROUTER_DEFAULT_ACTION=index
    ```

=== "Cli"

    ```ini
    ROUTER_CLI_DEFAULT_NAMESPACE=Zemit\\Modules\\Cli\\Tasks
    ROUTER_CLI_DEFAULT_MODULE=cli
    ROUTER_CLI_DEFAULT_TASK=help
    ROUTER_CLI_DEFAULT_ACTION=main
    ```

=== "Not Found"

    ```ini
    ROUTER_NOTFOUND_NAMESPACE=
    ROUTER_NOTFOUND_MODULE=
    ROUTER_NOTFOUND_CONTROLLER=error
    ROUTER_NOTFOUND_TASK=error
    ROUTER_NOTFOUND_ACTION=notFound
    ```

=== "Fatal"

    ```ini
    ROUTER_FATAL_NAMESPACE=
    ROUTER_FATAL_MODULE=
    ROUTER_FATAL_CONTROLLER=error
    ROUTER_FATAL_TASK=error
    ROUTER_FATAL_ACTION=fatal
    ```

=== "Forbidden"

    ```ini
    ROUTER_FORBIDDEN_NAMESPACE=
    ROUTER_FORBIDDEN_MODULE=
    ROUTER_FORBIDDEN_CONTROLLER=error
    ROUTER_FORBIDDEN_TASK=error
    ROUTER_FORBIDDEN_ACTION=forbidden
    ```

=== "Unauthorized"

    ```ini
    ROUTER_UNAUTHORIZED_NAMESPACE=
    ROUTER_UNAUTHORIZED_MODULE=
    ROUTER_UNAUTHORIZED_CONTROLLER=error
    ROUTER_UNAUTHORIZED_TASK=error
    ROUTER_UNAUTHORIZED_ACTION=unauthorized
    ```

=== "Maintenance"

    ```ini
    ROUTER_MAINTENANCE_NAMESPACE=
    ROUTER_MAINTENANCE_MODULE=
    ROUTER_MAINTENANCE_CONTROLLER=error
    ROUTER_MAINTENANCE_TASK=error
    ROUTER_MAINTENANCE_ACTION=maintenance
    ```

=== "Error"

    ```ini
    ROUTER_ERROR_NAMESPACE=
    ROUTER_ERROR_MODULE=
    ROUTER_ERROR_CONTROLLER=error
    ROUTER_ERROR_TASK=error
    ROUTER_ERROR_ACTION=index
    ```

### Changing the Router Service Provider

```ini
PROVIDER_ROUTER=\Zemit\Provider\Router\ServiceProvider
```

## Router Service (`router`)

!!! info "Router Service Provider"
    Router Service Provider (`router`):
    [`\Zemit\Provider\Router\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Router/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$router = $this->router;

// Retrieving the service from the DI
$router = $this->di->get('router');

// Retrieving the service from the getDI()
$router = $this->getDI()->get('router');

// Retrieving the service from anywhere
$router = Di::getDefault()->get('router');
```
