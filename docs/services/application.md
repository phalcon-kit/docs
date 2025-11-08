# Application Service

## Overview

The Application Service is primarily responsible for handling MVC (Model-View-Controller) requests in web server
environments. This service is integral to the web application's lifecycle, orchestrating the interaction between the
user interface, business logic, and data model.

### Role in MVC Architecture

The Application Service in Zemit operates at the heart of the MVC architecture. It serves as the entry point for web
requests, channeling them through the appropriate controllers and views, thereby ensuring a seamless and organized flow
of data and responses.

### Integration into DI System

A key feature of Zemit's Application Service is its integration with the Dependency Injection (DI) system. The Core
Application Component is injected into the DI container, providing easy access to this service throughout the
application. This integration facilitates a more modular and testable codebase, as dependencies can be managed and
injected efficiently.

### Accessing the Core Application Component

For an in-depth understanding of the functionalities and usage of the Core Application Component within Zemit's
Application Service, refer to the [Zemit Core Application Component documentation](../../core/application/). This
documentation provides comprehensive insights into how the component is structured, its role within the MVC framework,
and how it can be leveraged to build robust and scalable web applications.

## Configuration

### Changing the Application Service Provider

```ini
PROVIDER_APPLICATION=\Zemit\Provider\Application\ServiceProvider
```

## Application Service (`application`)

!!! info "Application Service Provider"
    Application Service Provider (`application`):
    [`\Zemit\Provider\Application\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Application/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$application = $this->application;

// Retrieving the service from the DI
$application = $this->di->get('application');

// Retrieving the service from the getDI()
$application = $this->getDI()->get('application');

// Retrieving the service from anywhere
$application = Di::getDefault()->get('application');
```
