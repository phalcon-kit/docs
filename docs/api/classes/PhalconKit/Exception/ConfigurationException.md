
Raised when framework configuration is present but invalid.

Use this exception for bad class names, unsupported config values, invalid
option shapes, or incompatible configured services. It extends
InvalidArgumentException so callers can distinguish configuration mistakes
from runtime service failures.

***

* Full name: `\PhalconKit\Exception\ConfigurationException`
* Parent class: [`InvalidArgumentException`](https://www.php.net/manual/en/class.invalidargumentexception.php){:target="_blank"}
* This class implements:
  [`\PhalconKit\Exception\ExceptionInterface`](./ExceptionInterface.md)
