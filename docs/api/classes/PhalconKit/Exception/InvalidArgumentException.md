
Raised when a caller passes an invalid argument to PhalconKit code.

Use this exception for method arguments, payload fragments, or helper input
that is structurally invalid but not specifically an application
configuration problem. It extends PHP's native `InvalidArgumentException` so
existing consumers that catch the native category keep working, while the
`ExceptionInterface` marker lets applications handle all PhalconKit-origin
failures through one framework contract.

***

* Full name: `\PhalconKit\Exception\InvalidArgumentException`
* Parent class: [`InvalidArgumentException`](https://www.php.net/manual/en/class.invalidargumentexception.php){:target="_blank"}
* This class implements:
  [`\PhalconKit\Exception\ExceptionInterface`](./ExceptionInterface.md)
