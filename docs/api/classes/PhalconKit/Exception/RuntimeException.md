
Raised when a PhalconKit operation fails at runtime outside DI resolution.

Prefer `ServiceException` for missing or invalid DI services and
`ConfigurationException` for bad config. Use this class for operational
runtime failures such as query-building failures, unsupported relation
shapes encountered during execution, or wrapped lower-level exceptions that
should remain in the native runtime-exception family.

***

* Full name: `\PhalconKit\Exception\RuntimeException`
* Parent class: [`RuntimeException`](https://www.php.net/manual/en/class.runtimeexception.php){:target="_blank"}
* This class implements:
  [`\PhalconKit\Exception\ExceptionInterface`](./ExceptionInterface.md)
