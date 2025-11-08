# Router Component

## Introduction

In the Zemit framework, the Router component plays a role in directing incoming requests to the appropriate handlers.
It acts as a traffic director, analyzing requests and determining which parts of your application should respond.
Zemit enhances this functionality by offering two distinct types of routers: the CLI Router and the MVC Router.
This dual-router approach ensures seamless handling of different request types, catering to the specific needs of web
and command-line environments.

Both routers implement the `\Zemit\Router\RouterInterface`, ensuring a consistent interface while allowing
for their specialized behaviors. The Zemit Bootstrap intelligently registers the correct router based on
the application's context:

- If the application is loaded via the CLI or SAPI, it utilizes the CLI Router.
- For standard web requests, the MVC Router is employed.

This dual-router design in Zemit ensures that your application can efficiently handle and respond to a wide range of
interaction modes, whether they come from a web browser or a terminal.

### MVC Router

Engaged in web-based requests. It interprets URLs and maps them to the appropriate controller and action within your
application. The MVC Router extends the
[`\Phalcon\Mvc\Router`](https://docs.phalcon.io/latest/api/phalcon_mvc/#mvcrouter-){:target="_blank"},
integrating seamlessly with web-based MVC architecture.

!!! note "Further reading"
    For further details on routing specifics, you can refer to
    the [Phalcon MVC Router documentation](https://docs.phalcon.io/5.6/routing/){:target="_blank"} for web applications.

### CLI Router

Used when the application is accessed through the command-line interface (CLI).

This router interprets command-line arguments and directs them to the corresponding command handlers. It extends the
capabilities of the
[`\Phalcon\Cli\Router`](https://docs.phalcon.io/latest/api/phalcon_cli/#clirouter-){:target="_blank"},
tailoring it for command-line specific functionalities.

!!! note "Further reading"
    For further details on routing specifics, you can refer to
    the [Phalcon CLI Router documentation](https://docs.phalcon.io/5.6/application-cli/#routes){:target="_blank"} for
    command-line applications.

## Default Routes

In Zemit, a set of default routes is automatically added to streamline the development process. These routes follow a
similar approach to Phalcon's default routing but are further enhanced for modular functionality in Zemit. You have the
option to disable these default routes, if necessary, by passing `false` during the router instantiation.

### Implementation in Zemit

- The default routes in Zemit are defined using `\Zemit\Mvc\Router\ModuleRoute`.
- This approach groups the routes by module, allowing for efficient routing.

### Overview of Default MVC Routes

Zemit's default MVC routes provide a foundational set of paths, handling common routing patterns:

| **Route name**                   | **Route path**               | **Description**                                             |
|----------------------------------|------------------------------|-------------------------------------------------------------|
| default                          | /                            | Routes to the default module's index controller and action. |
| default-controller               | /:controller                 | Targets a specific controller in the default module.        |
| default-controller-action        | /:controller/:action         | Directs to a specific action within a given controller.     |
| default-controller-action-params | /:controller/:action/:params | Includes parameters for actions within controllers.         |

These routes cater to the typical needs of web applications, providing a simple yet flexible routing mechanism. Custom
routes can be added as needed, complementing or overriding these defaults to suit your application's specific
requirements.

### Localized MVC Routes

In addition to the standard default routes, Zemit also provides localized MVC routes. These routes incorporate
localization settings, allowing for the dynamic inclusion of locale information in the URL structure. This feature is
particularly useful for applications catering to a multi-lingual audience.

#### Handling Locale in Routes

- Zemit's routing system intelligently loops through the allowed locales to create localized versions of the default
  routes.
- The `:locale` placeholder in these routes is actually a regular expression pattern (
  e.g., `{locale:(en|en_CA|fr|fr_CA)}`), which includes all allowed locales defined in the application's configuration.

!!! warning
    Ensure that the locales you intend to use are correctly specified in your application's configuration settings. The
    router uses these settings to construct the localized routes.

#### Overview of Localized Routes

Below is a table outlining the structure of Zemit's localized MVC routes, accommodating different locales:

| **Route name**                  | **Route path**                       | **Description**                                                        |
|---------------------------------|--------------------------------------|------------------------------------------------------------------------|
| locale                          | /:locale                             | Routes to the default action for the specified locale.                 |
| locale-controller               | /:locale/:controller                 | Targets a specific controller within the context of the given locale.  |
| locale-controller-action        | /:locale/:controller/:action         | Directs to a specific action in a controller for the specified locale. |
| locale-controller-action-params | /:locale/:controller/:action/:params | Includes parameters for actions within a controller for a locale.      |

With these localized routes, Zemit supports multi-language routing, allowing each locale to have its own set of named
routes. For example, if you configure the allowed locales as `en`, `en_CA`, `fr`, `fr_CA`, each of these locales will
have its respective routes, ensuring a seamless multi-lingual user experience.

#### Examples: Localized Routes for Different Locales

Zemit allows for the creation of locale-specific routes, tailoring the routing paths to different language or regional settings. Here are examples of how these localized routes are defined for various locales:

=== "Locale: `en`"

    This example showcases the route configuration for the English (`en`) locale:
    
    | **Route name**              | **Route path**                  |
    |-----------------------------|---------------------------------|
    | en                          | /en                             |
    | en-controller               | /en/:controller                 |
    | en-controller-action        | /en/:controller/:action         |
    | en-controller-action-params | /en/:controller/:action/:params |

=== "Locale: `fr`"

    This example showcases the route configuration for the French (`fr`) locale:
    
    | **Route name**              | **Route path**                  |
    |-----------------------------|---------------------------------|
    | fr                          | /fr                             |
    | fr-controller               | /fr/:controller                 |
    | fr-controller-action        | /fr/:controller/:action         |
    | fr-controller-action-params | /fr/:controller/:action/:params |

=== "Locale: `fr_CA`"

    This example showcases the route configuration for the Canadian French (`fr_CA`) locale:
    
    | **Route name**                 | **Route path**                     |
    |--------------------------------|------------------------------------|
    | fr-ca                          | /fr_CA                             |
    | fr-ca-controller               | /fr_CA/:controller                 |
    | fr-ca-controller-action        | /fr_CA/:controller/:action         |
    | fr-ca-controller-action-params | /fr_CA/:controller/:action/:params |

=== "Locale: `en_CA`"
    
    This example showcases the route configuration for the Canadian English (`en_CA`) locale:
    
    | **Route name**                 | **Route path**                     |
    |--------------------------------|------------------------------------|
    | en-ca                          | /en_CA                             |
    | en-ca-controller               | /en_CA/:controller                 |
    | en-ca-controller-action        | /en_CA/:controller/:action         |
    | en-ca-controller-action-params | /en_CA/:controller/:action/:params |

Each set of localized routes provides a clear, structured approach to handling requests in different language contexts,
ensuring that your application can serve a diverse user base effectively.

### Modules MVC Routes

Zemit's routing system is also capable of handling module-specific routes, allowing for a structured and organized
approach to routing within different segments of your application. The default MVC Routes dynamically generate routes
for each registered module, facilitating modularity and scalability.

#### Examples: Module-Specific and Localized Routes

Each of these routes is tailored to the specific module, ensuring that the routing within this module is both efficient
and intuitive. Localized routes add an extra layer of flexibility, allowing each module to respond to different language
settings in a seamless manner.

For the each module, the following routes illustrate how Zemit configures both standard and localized routes for a
specific module:

=== "Module: `frontend`"

    Here are the default MVC routes for the `frontend` module:
    
    | **Route name**                    | **Route path**                        |
    |-----------------------------------|---------------------------------------|
    | frontend                          | /frontend                             |
    | frontend-controller               | /frontend/:controller                 |
    | frontend-controller-action        | /frontend/:controller/:action         |
    | frontend-controller-action-params | /frontend/:controller/:action/:params |

    In addition, localized routes for the `frontend` module are set up to accommodate different language preferences:
    
    | **Route name**                           | **Route path**                                |
    |------------------------------------------|-----------------------------------------------|
    | locale-frontend                          | /:locale/frontend                             |
    | locale-frontend-controller               | /:locale/frontend/:controller                 |
    | locale-frontend-controller-action        | /:locale/frontend/:controller/:action         |
    | locale-frontend-controller-action-params | /:locale/frontend/:controller/:action/:params |

=== "Module: `admin`"

    Here are the default MVC routes for the `admin` module:
    
    | **Route name**                    | **Route path**                        |
    |-----------------------------------|---------------------------------------|
    | admin                          | /admin                             |
    | admin-controller               | /admin/:controller                 |
    | admin-controller-action        | /admin/:controller/:action         |
    | admin-controller-action-params | /admin/:controller/:action/:params |

    In addition, localized routes for the `admin` module are set up to accommodate different language preferences:
    
    | **Route name**                           | **Route path**                                |
    |------------------------------------------|-----------------------------------------------|
    | locale-admin                          | /:locale/admin                             |
    | locale-admin-controller               | /:locale/admin/:controller                 |
    | locale-admin-controller-action        | /:locale/admin/:controller/:action         |
    | locale-admin-controller-action-params | /:locale/admin/:controller/:action/:params |

=== "Module: `api`"

    Here are the default MVC routes for the `api` module:
    
    | **Route name**                    | **Route path**                        |
    |-----------------------------------|---------------------------------------|
    | api                          | /api                             |
    | api-controller               | /api/:controller                 |
    | api-controller-action        | /api/:controller/:action         |
    | api-controller-action-params | /api/:controller/:action/:params |

    In addition, localized routes for the `api` module are set up to accommodate different language preferences:
    
    | **Route name**                           | **Route path**                                |
    |------------------------------------------|-----------------------------------------------|
    | locale-api                          | /:locale/api                             |
    | locale-api-controller               | /:locale/api/:controller                 |
    | locale-api-controller-action        | /:locale/api/:controller/:action         |
    | locale-api-controller-action-params | /:locale/api/:controller/:action/:params |

### Hostname MVC Routes

Zemit provides the capability to bind specific hostnames to modules within your MVC application. This feature allows
different modules to be invoked based on the hostname used to access the application, facilitating the creation of
multi-site architectures with ease.

#### How Hostname Routing Works

- **Module Binding**: By binding a hostname to a module, you dictate that this module should be used by default when the
  application is accessed through the associated hostname.

- **Regular Expressions**: Hostnames can be defined using regular expressions, granting you the flexibility to match a
  range of domain patterns to different modules.

- **Multi-Site Applications**: This feature is particularly useful for multi-site applications, where each site (
  identified by its hostname) corresponds to a specific module within the same application.

#### Advantages

- **Shared Services and Components**: Despite being separated by hostnames, all modules in the application can access
  shared services and common components, ensuring a consistent foundation across your multi-site setup.

- **Module Enhancements**: The hostname configuration takes advantage of all module features, such as default route
  handling and localization.

- **Sub-Modules Concept**: With hostname-based routing, each module can be thought of as a 'sub-module' within the
  broader application context, each catering to a specific site or domain.

By leveraging hostname MVC routes, you create a versatile and scalable application structure, where each module operates
contextually based on the accessed hostname, yet remains integrated within the overall Zemit framework.

#### Configuration Example

```php
<?php
use \Zemit\Bootstrap\Config;

$config = new Config([

    // Define your modules
    'modules' => [
        'api' => [
            'className' => \App\Modules\Api\Module::class,
            'path' => APP_PATH . '/Modules/Api/Module.php',
        ],
        'website' => [
            'className' => \App\Modules\Website\Module::class,
            'path' => APP_PATH . '/Modules/Website/Module.php',
        ],
        // add more modules...
    ],
    
    // Define your router hostnames
    'router' => [
        'hostnames' => [
            'api.example.com' => [
                'namespace' => 'App\\Modules\\Api\\Controllers',
                'module' => 'api',
            ],
            '(www.|)website.example.com' => [
                'namespace' => 'App\\Modules\\Website\\Controllers',
                'module' => 'website',
            ],
        ],
    ],
    
]);

return $config;
```

### Native MVC Routes

### Default CLI Routes

| **Route name**             | **Route path**         |
|----------------------------|------------------------|
| default                    | /                      |
| default-task               | /:task                 |
| default-task-action        | /:task/:action         |
| default-task-action-params | /:task/:action/:params |


## Creating your own Router

Developing a custom Router within the Zemit framework can be beneficial for extending or overriding the native 
functionalities provided by Phalcon or Zemit. This approach allows you to introduce specific routing behaviors 
or features that are uniquely tailored to the needs of your application, while still maintaining a well-organized 
and structured codebase.

#### Why Create a Custom Router?

- **Custom Functionality**: If your application requires specialized routing logic that goes beyond the capabilities of
  the standard Phalcon or Zemit routers, a custom Router is the way to go.

- **Enhanced Flexibility**: With a custom Router, you gain the flexibility to implement complex routing rules, handle
  requests in a specific manner, or integrate with other systems in ways that the default routers might not support.

- **Consistency and Structure**: Even with customizations, your application can maintain a consistent and structured
  approach to handling requests, ensuring that your routing logic aligns seamlessly with the rest of your application's
  architecture.

Creating your own Router involves subclassing the existing Phalcon or Zemit Router classes and then implementing the
additional functionalities as required. This custom Router can then be registered with the application, replacing or
supplementing the default routing mechanism.

### Extending MVC Router

```php title="./app/Bootstrap/Router.php"
<?php

namespace App\Bootstrap;

use Zemit\Config\ConfigInterface;

class MvcRouter extends \Zemit\Bootstrap\Router implements \Zemit\Mvc\RouterInterface
{
    public function __construct(bool $defaultRoutes = true, ?ConfigInterface $config = null)
    {
        parent::__construct($defaultRoutes, $config);
        
        // add your custom route here
        // ...
    }
}
```


### Extending CLI Router

```php title="./app/Bootstrap/Router.php"
<?php

namespace App\Bootstrap;

class CliRouter extends \Zemit\Cli\Router implements \Zemit\Cli\RouterInterface
{
    public function __construct(bool $defaultRoutes = true)
    {
        parent::__construct($defaultRoutes, $config);
        
        // add your custom route here
        // ...
    }
}
```

### Adding Your Custom Routers

Once you have created your custom routers in Zemit, the next step is to integrate them into your application. This is
done during the initialization phase of the bootstrap component. By setting up your custom routers here, Zemit will
utilize them when the router service is loaded from the Dependency Injection (DI) container, ensuring that your
application's routing is handled as per your custom logic.

#### Integration in the Bootstrap Component

To integrate your custom routers, you'll modify the `initialize` method in your Bootstrap class. Here, you'll
conditionally set the custom router based on the application's context — whether it's a console (CLI) or a web (MVC)
request. This approach ensures that the appropriate router is used in each scenario.

Here's an example of how you can add your custom routers:

```php
<?php
namespace App;

use App\Bootstrap\CliRouter;
use App\Bootstrap\MvcRouter;

class Bootstrap extends \Zemit\Bootstrap
{    
    public function initialize(): void
    {
        // Set the custom router based on the application context
        $this->setRouter(
            $this->isConsole()
            ? new CliRouter()
            : new MvcRouter()
        );
    }
}
```

### Overriding Router Service

Zemit's **Router Service Provider** is registered in the later stages of the application's bootstrap process.
When this service is loaded, specific Zemit business logic is applied to ensure smooth routing functionality.
However, there might be scenarios where the default routing behavior of Zemit does not align with the specific
requirements of your application. In such cases, customizing the Router Service becomes essential.

To override the default Router Service with your custom implementation, you need to modify the service provider
configuration within Zemit. This allows you to introduce your custom routing logic or modify how the application
handles routing processes. Here’s how you can achieve this:

- **Custom Service Provider**: Create a custom Service Provider that defines your desired routing behavior. This provider should manage the instantiation and configuration of your router, tailoring it to the specific needs of your application.

- **Update Configuration**: In your application's configuration file, update the service provider mapping to reference your custom Router Service Provider. This tells Zemit to use your custom provider instead of the default one when setting up the routing service.


```ini title=".env"
PROVIDER_ROUTER=\App\Provider\Router\ServiceProvider
```

```php title="./app/Provider/Router/ServiceProvider.php"
<?php
namespace App\Provider\Router;

use Zemit\Bootstrap;
use Phalcon\Di\DiInterface;
use App\Bootstrap\MvcRouter;
use App\Bootstrap\CliRouter;

class ServiceProvider extends \Zemit\Provider\AbstractServiceProvider
{
    protected string $serviceName = 'router';
    
    public function register(DiInterface $di): void
    {
        $di->setShared($this->getName(), function () use ($di) {
            
            $bootstrap = $di->get('bootstrap');
            assert($bootstrap instanceof Bootstrap);
            
            $config = $bootstrap->getConfig();
            
            $router = $bootstrap->router ?? $bootstrap->isCli()
                ? new CliRouter(true)
                : new Router(true, $config);
            
            $defaults = $config->pathToArray($bootstrap->isCli() ? 'router.cli' : 'router.defaults') ?? [];
            $router->setDefaults($defaults);
            $router->setDI($di);
            
            if ($router instanceof Router) {
                $router->setEventsManager($di->get('eventsManager'));
                $router->setConfig($config);
                $router->baseRoutes();
                $router->hostnamesRoutes();
                $router->modulesRoutes($di->get('application'));
            }
            
            return $router;
        });
    }
}
```

By customizing the Router Service Provider, you gain greater control over how requests are handled within your application,
enabling you to tailor routing logic in a way that best suits your application's architecture and business requirements.
