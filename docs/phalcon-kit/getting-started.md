# Getting Started

## Information

Our platform enhances the robust capabilities of Phalcon PHP, offering a suite of tools 
to streamline your web development process. For a comprehensive understanding of the foundational 
features, we recommend familiarizing yourself with the
[Official Phalcon PHP Documentation](https://docs.phalcon.io/){:target="_blank"}.

!!! note "PHP Version 8.4+"
    While exploring the Phalcon PHP documentation, keep in mind that some features
    or examples may differ slightly due to our PHP version requirement.
    Zemit is designed to leverage the latest advancements in web technology,
    which is why we support **PHP 8.4 and above**. This approach ensures that you 
    have access to the most recent PHP features, enhancing both **performance** and **security**.

## Install Zemit

Before beginning, ensure you have **PHP** and **Composer** installed on your system, as they are prerequisites for using Zemit.

### Option 1: Creating a New Project with Zemit
To start a fresh project powered by Zemit, use the `composer create-project` command.
This approach sets up a new project with all the essential and recommended files,
along with default configurations to streamline your setup process. Visit the 
[Zemit App](https://github.com/phalcon-kit/app){:target="_blank"} repository for additional details.
Execute the following command in your terminal, replace my-app with your desired project name.

```bash
composer create-project phalcon-kit/app my-app
```
This command creates a new directory with all the necessary Zemit files.

### Option 2: Adding Zemit to an Existing Project
If you already have a project and wish to incorporate Zemit, use the `composer require`
command. This command adds Zemit Core as a dependency to your existing project.
Run the following in your project directory:

```bash
composer require phalcon-kit/core
```

Once installed, you can start using Zemit classes in your project.
Simply include the Composer autoloader, and you're ready to go!

You can initialize your application using the \Zemit\Bootstrap class.
Below is a minimalist example demonstrating how to set up your application
with Zemit, utilizing the [`\Phalcon\Autoload\Loader`](https://docs.phalcon.io/5.6/autoload/).

```php title="./public/index.php"
<?php
use Phalcon\Autoload\Loader;
use Zemit\Bootstrap;

// Initialize the autoloader
$loader = new Loader();

// Specify the Composer autoload file and your application's namespace
$loader->setFiles(['../vendor/autoload.php']);
$loader->setNamespaces(['App' => '../src/']);

// Register the autoloader
$loader->register();

// Bootstrap and run your Zemit application
$bootstrap = new Bootstrap();
echo $bootstrap->run();
```

## Configure your application
Zemit will automatically look for the `.env` from the root of your project. There you can add your own custom variables for your custom application or set the ones that are natively supported by Zemit.
Below you can see an example to configure your database.

```ini title="./.env"
DATABASE_HOST="localhost"
DATABASE_DBNAME="database"
DATABASE_USERNAME="username"
DATABASE_PASSWORD="password"
```


