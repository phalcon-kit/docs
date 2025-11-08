# REST System

The REST System in Phalcon Kit forms the backbone of custom API development. Built upon
[`\PhalconKit\Mvc\Controller\Rest`](/api/classes/PhalconKit/Mvc/Controller/Rest.md), which
itself extends [`\PhalconKit\Mvc\Controller`](/api/classes/PhalconKit/Mvc/Controller.md), this system inherits all functionalities
of the Phalcon Kit Controller base. For an
in-depth understanding of the controller's capabilities, please refer to the Phalcon Kit MVC Controller component
documentation.

Unlike the RESTful System, which focuses on CRUD operations with models, the REST System provides a foundation for APIs
that require custom logic and are not directly tied to specific models.

## Use Cases

The REST System shines in situations that call for tailored solutions. Take authentication, for instance – it's not just
about database interactions; it's also about ensuring secure access, validating user credentials, and maybe even
integrating with third-party services. And that's just one example. Whether you're managing complex user permissions,
processing payment transactions, or syncing data across different platforms, the REST System provides the flexibility
and robustness needed for these diverse tasks. It's designed to adapt to your specific requirements, making it a go-to
choice for unique and sophisticated API functionalities.

!!! note "Note on RESTful System"
    For a more specific use cases requiring direct interaction with model records and advanced query capabilities, consider
    the [RESTful System](restful-system.md).
    This system provides a comprehensive set of tools for intuitive record manipulation and query building, catering to more
    complex data handling needs.

## Key Features

1. **Behavior System**: Integrates events and behaviors based on roles and permissions.
2. **Fractal System**: Transforms objects into structured responses.
3. **Parameter Retrieval**: Efficiently extracts filtered parameters from requests or dispatchers.
4. **Standardized Response**: Ensures consistent, well-structured JSON responses.

### Behavior System

The Behavior System in Phalcon Kit offers a seamless way to integrate custom events and behaviors aligned with your business
rules into your application.

#### Automated Attachment of Behaviors

Behaviors are configured to automatically attach to the controller class, activated during the `beforeExecuteRoute`
phase. This automation ensures that your custom behaviors are always in sync with the controller's lifecycle, enhancing
the reliability and consistency of their execution.

#### ACL Role-Based Configuration

One of the key strengths of this system is its ability to align behaviors with Access Control List (ACL) roles and
permissions. This feature allows you to tailor behaviors to specific user roles, ensuring that each interaction is both
secure and contextually appropriate.

#### Adding Custom Behaviors

To further customize your application, the Behavior System provides methods like `attachBehavior()`
and `attachBehaviors()`. These methods enable you to:

- Integrate custom events into your application workflow.
- Define specific actions to be triggered under certain conditions.
- Enhance the application's functionality with minimal intrusion into the existing codebase.

By leveraging these methods, you can create a dynamic and responsive application that reacts intelligently to various
user interactions and system changes.

### Fractal System

The Fractal system in Phalcon Kit streamlines the process of tailoring data before it becomes part of the final response.
Acting as a high-speed transformer, it offers you complete control over how data is presented and delivered.

#### Transforming Data Efficiently

At the core of the Fractal system is its ability to rapidly and efficiently modify data. This means you can:

- **Customize Data Representation**: Tailor how data is structured in the response, ensuring it meets the specific needs
  of your application or its consumers.
- **Enhance Data Quality**: Apply transformations to improve clarity, add necessary context, or format data for better
  usability.

#### Standardization and Flexibility

Fractal stands out for its balance of standardization and customization. It allows you to establish a consistent data
format across your API responses while giving you the flexibility to address unique data representation needs for
different endpoints or use cases.

By utilizing the Fractal system, you ensure that your API responses are not only consistent and reliable but also
tailored to provide the most value to the end user.

### Parameter Retrieval

With the `REST` System, retrieving filtered data from the `request` or `dispatcher` services is straightforward and
efficient.

#### Automatic Parameter Sanitization

Phalcon Kit seamlessly handles parameter retrieval:

- **Automatic Search**: It first attempts to find and sanitize parameters from the `request`. If not found, it falls
  back to the `dispatcher` service.
- **Request Method Prioritization**: The system prioritizes parameters based on the current request method,
  automatically looking for `query`, `patch`, `put`, and `post` values.

#### Custom Sanitizers

You can define your own [preset sanitizers](https://docs.phalcon.io/latest/request/#preset-sanitizers){:target="_blank"}
using `setParameterFilters()`, and Phalcon Kit will apply them automatically.

```php
<?php
$this->request->setParameterFilters('id', Filter::FILTER_ABSINT, 'get');
$this->request->setParameterFilters('email', Filter::FILTER_EMAIL, 'post');

$params = $this->getParams(); // id and email parameters are sanitized
```

#### Direct Sanitization during Retrieval

For immediate sanitization, use methods like getParam() or getParams() with specified filters:

```php
<?php
// Using `getParam()` for individual parameters
$id = $this->getParam('id', Filter::FILTER_ABSINT, 'get');
$email = $this->getParam('email', Filter::FILTER_EMAIL, 'post');

// Using `getParams()` for multiple parameters
$params = $this->getParams(
    ['name' => 'id', 'filters' => Filter::FILTER_ABSINT, 'scope' => 'get'],
    ['name' => 'email', 'filters' => [Filter::FILTER_EMAIL, Filter::FILTER_TRIM], 'scope' => 'post'],
);
```

 Phalcon kit's parameter retrieval system is designed to make your data handling both safe and efficient, ensuring that you
receive clean and validated data for your application's needs.

### Standardized Response

The response service in Phalcon Kit plays a role in shaping the final output of your API. It ensures that every response sent
back to the client is well-structured, consistent, and aligns with REST standards.

#### Automated Response Structuring

**Automatic Detection and Injection**: When you return a value from your controller, Phalcon Kit intelligently incorporates
this
value into a standardized response object. This process takes place during the `afterExecuteRoute` phase, simplifying
the
response-building process.

**Flexibility in Response Creation**: If you prefer to have complete control over the response, you can bypass Phalcon Kit’s
automation by returning your own `Response` instance. This flexibility allows for customized response handling as
needed.

#### Error and Custom Responses

**Easy Error Handling**: The `setRestErrorResponse()` method is a straightforward way to handle errors. It allows you to
craft
error responses with customized codes, statuses, and body content.

**Prepared Response Utility**: For a more guided approach, use `setRestResponse()`. This method lets Phalcon Kit prepare the
`Response` instance, ensuring that your response adheres to RESTful standards while still catering to your application's
specific needs.

#### Extending and Overriding Responses

**Customization Options**: Both `setRestErrorResponse()` and `setRestResponse()` methods are designed to be overridden,
giving
you the freedom to modify and enhance how responses are handled and structured in your application.

By utilizing Phalcon Kit's response services, you gain the advantage of standardized, clear, and REST-compliant responses,
coupled with the flexibility to adapt and customize as your application requires.
