# Loader Component

The loader component serves as an autoloader, adhering to the PSR-4 standard. As with any autoloader,
it performs the task of locating the files your code references, such as classes, based on various
criteria like file names, class names, and namespaces. One notable advantage of
[`\Phalcon\Autoload\Loader`](https://docs.phalcon.io/latest/api/phalcon_autoload/){:target="_blank"}
is its implementation in C, which ensures minimal overhead during the setup process. This inherent
efficiency contributes to a performance boost for your application.

Phalcon Kit Loader extends the native
[`\Phalcon\Autoload\Loader`](https://docs.phalcon.io/latest/api/phalcon_autoload/){:target="_blank"}.
To further optimize speed, Phalcon Kit Loader has disabled the
[file checking callback](https://docs.phalcon.io/latest/autoload/#file-checking-callback){:target="_blank"}
used in Phalcon's native component, ensuring quicker response times.

## Constants

This set of constants facilitate the loading process and form the backbone of the default Phalcon Kit configuration.
These constants can be tailored to suit the specific needs of your project.

| Constant      | Default Value | Description                                                          |
|---------------|---------------|----------------------------------------------------------------------|
| APP_NAMESPACE | App           | Application's main namespace.                                        |
| ROOT_PATH     | \_\_DIR\_\_   | Should be the root directory of your application path on the server. |
| VENDOR_PATH   | ./vendor/     | Vendor folder                                                        |
| APP_PATH      | ./src/        | Application folder                                                   |

## Registration

The loader registration involves setting up the autoloading of various components necessary for your application. This setup includes registering the Composer-generated `autoload.php`, which handles dependencies, and your application's primary namespace.

### Global App Loader

The `loader.php` file serves as a centralized autoloader for your entire application.
This global approach allows for flexibility across different entry points, accommodating various
scenarios such as running migrations, using development tools, or executing commands via the CLI module.

Below is the typical structure for `loader.php`, illustrating how to register the essential components:

```php title="./loader.php"
<?php

use PhalconKit\Autoload\Loader;

// Define the main constants used across the application
const APP_NAMESPACE = 'App';
const ROOT_PATH = __DIR__;
const VENDOR_PATH = ROOT_PATH . '/vendor/';
const APP_PATH = ROOT_PATH . '/app/';

// Initialize the Phalcon Kit Loader
$loader = new Loader();

// Register the Composer autoload file and the application namespace
$loader->registerFiles([VENDOR_PATH . '/autoload.php']);
$loader->registerNamespaces([APP_NAMESPACE => APP_PATH]);

// Activate the loader
$loader->register();

// Return the loader instance for further use
return $loader;
```

This script ensures that all necessary files and namespaces are correctly autoloaded, providing a solid foundation for the application's functionality.

### Global Entry Point

The `./index.php` file acts as the global entry point for your Phalcon Kit application.
It's strategically placed in the root of the project not for direct web server access, 
but as a security measure to safeguard the application's root directory. 
This setup is designed to prevent unauthorized directory listing or exposure 
of sensitive files in case of a security breach.

By directing requests through this entry point, if an attacker gains access to the root
of your project, they encounter the application's standard operational layer, rather 
than raw directory contents or critical infrastructure components.

Here's the typical implementation of the global entry point:

```php title="./index.php"
<?php

use PhalconKit\Bootstrap;

// Load the global autoloader
$loader = require 'loader.php';

// Bootstrap and run the application
echo (new Bootstrap())->run();
```

In this script:

- We include the global loader.php to initialize the autoloading process.
- An instance of PhalconKit\Bootstrap is created and executed, which kickstarts the application. This approach encapsulates 
the initialization and routing in a structured manner, enhancing maintainability and security.

### Public Entry Point

The `./public/index.php` file is designated as the primary entry point for **web server**
interactions with your Phalcon Kit application. This file should reside in the `public` directory
of your project. The purpose of this configuration is to enhance security by restricting web
server access solely to the `public` directory, thereby shielding the rest of your
application's structure and critical files from direct exposure.

```php title="./public/index.php"
<?php

// Delegate to the global entry point
require '../index.php';
```

In this setup:

- The web server is configured to point to the `./public/` directory as the **document root**.
- The `index.php` file within this directory simply requires the global entry point file `../index.php`.
This means that all web requests first go through this file, which then delegates to the main application logic in the root `index.php`.
- This architecture maintains a clear separation between public assets (like images, JavaScript, and CSS files)
and your application's PHP logic, thereby fortifying the security posture of your application.
