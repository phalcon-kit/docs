
Base checked category for general PhalconKit framework exceptions.

New framework code should prefer the more specific exception classes under
`PhalconKit\Exception` when a native PHP category is useful, such as
`ConfigurationException`, `ServiceException`, `LogicException`, or
`RuntimeException`. This base class remains available for older extension
points and general framework failures that should still implement the common
PhalconKit exception marker.

***

* Full name: `\PhalconKit\Exception`
* Parent class: [`Exception`](https://www.php.net/manual/en/class.exception.php){:target="_blank"}
* This class implements:
  [`\PhalconKit\Exception\ExceptionInterface`](./Exception/ExceptionInterface.md)
