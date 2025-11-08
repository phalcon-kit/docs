# Request Component

## Introduction

In the realm of web development, effectively managing HTTP requests is crucial for a seamless interaction between the
user's browser and the server. Phalcon Kit's Request component, an extension of `\Phalcon\Http\Request`, is meticulously
designed to serve this purpose. By enhancing the capabilities of the Phalcon framework, it provides a robust and
intuitive interface for handling and interpreting HTTP requests within your application.

!!! note "Phalcon Request Component"
    For a deeper understanding of the underlying functionality, you can explore
    the [Phalcon Request Component documentation](https://docs.phalcon.io/latest/request/){:target="_blank"} and
    the [Phalcon HTTP Request API](https://docs.phalcon.io/latest/api/phalcon_http/#httprequest){:target="_blank"}.

## Enhanced and Extended Features in Phalcon Kit

Building on the foundation of Phalcon's `\Phalcon\Http\Request`, the Phalcon Kit Request Component (`PhalconKit\Http\Request`)
introduces extended functionalities that enhance its capabilities in handling HTTP requests. This component is
particularly tailored to address complex web application scenarios, emphasizing security, flexibility, and detailed
request analysis.

### CORS and Preflight Request Handling

In modern web applications, handling Cross-Origin Resource Sharing (CORS) and preflight requests is crucial for ensuring
seamless interaction between different domains. `PhalconKit\Http\Request` provides specialized methods to manage these
scenarios:

- **CORS Request Detection `isCors()`**: This method determines whether a request is a CORS request. It checks for the
  presence of an 'Origin' header and compares it with the request's origin to ascertain if they differ, indicating a
  cross-origin request.

- **Preflight Request Identification `isPreflight()`**: Preflight requests are a critical part of the CORS protocol,
  allowing browsers to check permissions before making actual requests. The `isPreflight` method identifies such
  requests by checking for an OPTIONS method and the presence of the 'Access-Control-Request-Method' header.

- **Same Origin Check `isSameOrigin()`**: This method verifies if the request originates from the same domain as the
  server, an additional check to help limit some types of CSRF (Cross-Site Request Forgery) attacks.

### Comprehensive Request Analysis

The `toArray` method in `PhalconKit\Http\Request` is a comprehensive tool for analyzing and extracting detailed information
from HTTP requests. It converts the entire request into an associative array, encapsulating various aspects:

- Headers, body, and HTTP methods (GET, POST, PUT, etc.).
- Client and server information including IP addresses, server names, and ports.
- Security-related details like user agents, authentication headers, and content types.
- Flags for AJAX requests, secure connections, and more.

By integrating these advanced features, `PhalconKit\Http\Request` not only facilitates the efficient processing of HTTP
requests but also adds layers of security and detailed request analysis, making it a powerful tool for developers
working with Phalcon Kit.

To explore more about Phalcon's base request handling functionalities, refer to
the [Phalcon Request Component documentation](https://docs.phalcon.io/latest/request/){:target="_blank"} and
the [Phalcon HTTP Request API](https://docs.phalcon.io/latest/api/phalcon_http/#httprequest){:target="_blank"}.

## Handling Preflight Requests

Preflight requests are an essential part of modern web applications, especially in scenarios involving CORS (
Cross-Origin Resource Sharing), such as interactions between web applications and mobile apps. Phalcon Kit's `isPreflight()`
method in the `Request` component provides an efficient way to handle these requests. Below is a minimalistic example
demonstrating how to utilize this method to manage preflight requests in your application.

### Creating a Preflight Event Listener

First, we create an event listener that checks for preflight requests. This listener is attached to the dispatch
process:

```php
<?php
namespace App\Events\Dispatcher;

use Phalcon\Http\ResponseInterface;
use PhalconKit\Di\Injectable;

class Preflight extends Injectable
{
    public function beforeExecuteRoute(): void
    {
        // Check if the request is a preflight request
        if ($this->request->isPreflight()) {
        
            // Implement your custom preflight logic here
            // Example: set specific response headers or log the preflight request

            // Send a 204 No Content response and terminate the request lifecycle
            $this->response->setStatusCode(204)->send();
            exit(0);
        }
    }
}
```

### Integrating the Preflight Listener

Next, integrate the Preflight event listener into the application's event management system, and attach it to the
dispatcher:

```php
<?php
$preflight = new \App\Events\Dispatcher\Preflight();
$preflight->setDi($di); // Inject the DI container into the Preflight event listener

$eventsManager = new \Phalcon\Events\Manager();
$eventsManager->attach('dispatch', $preflight); // Attach the Preflight listener to the dispatch event

$dispatcher = new Dispatcher();
$dispatcher->setEventsManager($eventsManager); // Set the events manager for the dispatcher
$dispatcher->setDI($di); // Inject the DI container into the dispatcher

// ...
```

In this example:

- A custom Preflight class is defined, extending PhalconKit\Di\Injectable. Within its beforeExecuteRoute method, it checks
  for preflight requests using isPreflight().
- If a preflight request is detected, the listener executes the necessary business logic, sends a 204 No Content
  response, and terminates the request cycle.
- The Preflight event listener is attached to the Phalcon dispatcher through an event manager, ensuring that preflight
  requests are handled before any route execution.
- This approach ensures that preflight requests are processed efficiently, meeting the necessary CORS protocol
  requirements and enhancing the compatibility.
