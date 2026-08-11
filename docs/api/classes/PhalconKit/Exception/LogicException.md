
Raised when PhalconKit detects an impossible or inconsistent framework state.

Use this exception for violated internal invariants, invalid extension
contracts, or developer-facing integration mistakes that are not caused by a
single bad service lookup. It preserves PHP's native `LogicException`
inheritance so existing catch blocks remain compatible while adding the
PhalconKit exception marker contract.

***

* Full name: `\PhalconKit\Exception\LogicException`
* Parent class: [`LogicException`](https://www.php.net/manual/en/class.logicexception.php){:target="_blank"}
* This class implements:
  [`\PhalconKit\Exception\ExceptionInterface`](./ExceptionInterface.md)
