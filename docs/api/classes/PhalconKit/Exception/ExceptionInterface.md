
Marker contract for exceptions raised by PhalconKit framework code.

Framework-specific exceptions implement this interface even when they extend
different native PHP exception categories. Consumers can catch this interface
to handle PhalconKit failures without losing the semantic value of native
exception inheritance such as InvalidArgumentException or RuntimeException.

***

* Full name: `\PhalconKit\Exception\ExceptionInterface`
* Parent interfaces:
  `Throwable`
