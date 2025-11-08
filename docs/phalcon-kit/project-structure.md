# Project Structure

#### Standard Phalcon Kit Apps directory structured

One of the key features of Phalcon is that it is loosely coupled. Because of that, you can use any directory structure that is convenient to you. In this example below, we will use a standard directory structure, commonly used in modular MVC applications.

## Standard Modular HMVC Structure

Hierarchical Model-View-Controller (HMVC) is a design pattern that is an extension of the traditional Model-View-Controller (MVC) design pattern. It introduces a hierarchical structure to applications, allowing for increased modularity, reusability, and separation of concerns. Phalcon Kit recommends the HMVC project structure for the following reasons:

1. **Nested Components**: In HMVC, components are structured hierarchically, allowing components to be nested within each other. This makes it possible to create complex pages in a manageable way, as each component can focus on a specific task.
2. **Modularity and Reusability**: HMVC enhances the modularity and reusability seen in MVC. Components in HMVC are self-contained and can be plugged into any part of the application without concern for dependencies. This reduces code redundancy and facilitates code reuse, making the application more maintainable and scalable.
3. **Separation of Concerns**: Like MVC, HMVC maintains a clear separation of concerns among models, views, and controllers. This structure keeps your codebase organized and improves code readability and maintainability.
4. **Parallel Development**: The independent nature of the components in HMVC allows for efficient parallel development. Multiple developers can work on different components simultaneously without affecting each other's work.
5. **Improved Performance**: HMVC can potentially improve the performance of your application. For instance, if a certain module is slow, it won't slow down the entire application, only the specific section where the module is used.
6. **Framework Compatibility**: As HMVC is a well-recognized pattern, many frameworks, libraries, and tools are designed to work with it. Your project can take advantage of a wide range of resources by following the HMVC structure.

By using the HMVC structure in your Phalcon Kit project, you'll be able to build complex applications that remain maintainable, scalable, and efficient.

```text
.
└── my-app/
    ├── app/
    │   ├── bootstrap/
    │   │   ├── Config.php
    │   │   ├── Router.php
    │   │   ├── Services.php
    │   │   └── ...
    │   ├── modules/
    │   │   ├── api/
    │   │   │   ├── controllers/
    │   │   │   │   ├── UserController.php
    │   │   │   │   ├── RoleController.php
    │   │   │   │   └── ...
    │   │   │   ├── models/
    │   │   │   │   ├── User.php
    │   │   │   │   ├── Role.php
    │   │   │   │   └── ...
    │   │   │   ├── views/
    │   │   │   │   ├── error/
    │   │   │   │   │   └── index.phtml
    │   │   │   │   └── index.phtml
    │   │   │   ├── Controller.php
    │   │   │   ├── Model.php
    │   │   │   └── Module.php
    │   │   └── ...
    │   └── Bootstrap.php
    ├── src/
    │   └── (Frontend, Angular, VueJS, React, Svelte, etc.)
    ├── dist/
    │   └── (Frontend Build)
    ├── public/
    │   ├── index.php
    │   └── .htaccess
    ├── vendor/
    │   └── ...
    ├── node_modules/
    │   └── ...
    ├── .env
    ├── .htaccess
    ├── .gitignore
    ├── package.json
    ├── composer.json
    └── ...
```

Each of the listed items refer to different ways of structuring and setting up a Phalcon application to cater to different needs. Here's a brief description of each:

| Structure Pattern (Native Phalcon) | Description |
|---|---|
| micro-factory-default | This is a micro application set up with factory default dependency injection |
| micro-simple-views | This is a micro application with simple views |
| micro | A basic structure for a micro application, without additional features like views |
| multiple-factory-default | This is a standard MVC application with multiple modules, set up with factory default dependency injection |
| multiple-service-layer-model | This is a MVC application with multiple modules, where models are designed to work as service layers |
| multiple-shared-layouts | This is a MVC application with multiple modules, with shared layouts between modules |
| multiple-shared-views | This is a MVC application with multiple modules, with shared views between modules |
| multiple-volt | This is a MVC application with multiple modules, with Volt as the templating engine |
| multiple | A basic structure for a MVC application with multiple modules |
| simple-subcontrollers | A simple MVC application with subcontrollers |
| simple-volt | A simple MVC application using Volt as the templating engine |
| simple-without-application | A simple MVC application without the use of Phalcon\Mvc\Application. This is for more advanced users who want more control over the bootstrap process |
| simple | A basic structure for a simple MVC application |
| single-camelized-dirs | A single module MVC application with camelized directories |
| single-factory-default | A single module MVC application set up with factory default dependency injection |
| single-namespaces | A single module MVC application with namespaces |
| single-service-provider | A single module MVC application where services are provided by a service provider |
| single | A basic structure for a single module MVC application |

Please note that each of these structures cater to different needs and the best one to use depends on the specific requirements of your application.

## External Links

- [Phalcon Project Structure Examples](https://github.com/phalcon/mvc/tree/master){:target="_blank"}
