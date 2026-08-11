
Raised when a framework service cannot be resolved or used safely.

Use this exception for missing DI services, wrong service types, invalid
service state, or runtime service contract violations. It extends
RuntimeException because these failures usually depend on the container or
current runtime state rather than a single method argument.

***

* Full name: `\PhalconKit\Exception\ServiceException`
* Parent class: [`RuntimeException`](https://www.php.net/manual/en/class.runtimeexception.php){:target="_blank"}
* This class implements:
  [`\PhalconKit\Exception\ExceptionInterface`](./ExceptionInterface.md)
