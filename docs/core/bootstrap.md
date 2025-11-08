# Bootstrap Component

The Bootstrap feature in Phalcon Kit is responsible for setting up and handling the 
application using the Mvc design pattern or the Cli (console). It follows a series 
of steps to ensure that the application is properly initialized and configured. 

These steps include setting a shared event manager, custom initialization, reading 
configuration files and command line parameters, setting up the default Dependency 
Injection (DI) container, preparing PHP configuration, and registering service providers. 

The Bootstrap also prepares and loads the different modules of the application before 
finally handling it. By using the Bootstrap, you can easily set up and manage your application.

## Quick Start
To create a customized bootstrap with the Phalcon Kit, you will need to create
a new class that extends from the `\PhalconKit\Bootstrap` class. This will allow you to personalize
the bootstrap to your needs by overriding any of its methods as desired. For example, you
may want to initialize the configuration with your own class. Keep in mind that you are 
free to customize the bootstrap to fit your specific requirements and workflow.

## Method #1: Procedural 

### Minimalistic approach
```php title="index.php"
<?php

use PhalconKit\Bootstrap;

$bootstrap = new Bootstrap();

echo $bootstrap->run();
```

### Customizable approach
```php title="index.php"
<?php
use PhalconKit\Bootstrap;
use PhalconKit\Bootstrap\Config;
use PhalconKit\Bootstrap\Router;

$config = new Config();
$config->set('debug', true);

$router = new Router();
$router->add('my-route', ['controller' => 'MyRoute']);

$bootstrap = new Bootstrap();
$bootstrap->setConfig($config);
$bootstrap->setRouter($router);

echo $bootstrap->run();
```

## Method #2: Extending

Extending the `PhalconKit\Bootstrap` class will give you the most flexibility
because you can modify default behaviors at your convenience. There is mainly
two phases that you can inject your own core components and services:
The `initialization` phase and then the `registration` phase.

### Initialization phase

This initialization phase is called right before the `run()` method is called.
This makes it the best place for you to manage and initialize your own components and services.

This is the recommended method because it keeps a well organized and structured architecture
following the PSR-4 standard while allowing you to customize your app during the initialization
phase of the bootstrap.

```php title="./app/Bootstrap.php"
<?php
namespace App;

use PhalconKit\Bootstrap;
use App\Bootstrap\Config;
use App\Bootstrap\Router;

class Bootstrap extends \PhalconKit\Bootstrap
{
    public function initialize(): void
    {
        $this->setConfig(new Config());
        $this->setRouter(new Router());
    }
}
```

Then in your entry point `./index.php` you can simply run your own `\App\Bootstrap` as usual.
```php title="./index.php"
<?php

use Phalcon\Loader;
use App\Bootstrap;

$loader = new Loader();
$loader->registerFiles(['./vendor/autoload.php']);
$loader->registerNamespaces(['App' => './src/']);
$loader->register();

echo (new Bootstrap())->run();
```

### Registration phase

The registration phases are called after the `initialize()` method.
This approach is considered more advanced and only needed if you want to keep the native Phalcon Kit
behavior and allow sub-applications to initialize their own components and then add more business logic to it.

```php title="./app/Bootstrap.php"
<?php
namespace App;

use App\Provider\Config\ServiceProvider as ConfigServiceProvider;
use PhalconKit\Config\ConfigInterface;

class Bootstrap extends \PhalconKit\Bootstrap
{
    public function registerConfig(): void
    {
        if (!$this->di->has('config')) {
            $configService = new ConfigServiceProvider($this->di);
            $configService->register($this->di);
        }
        $this->config ??= $this->di->get('config');
    }
    
    public function registerServices(): void
    {
        // ...
    }
    
    public function registerModules(): void
    {
        // ...
    }
    
    public function registerRouter(): void
    {
        // ...
    }
}
```
