
PhalconKit validation service type.

The implementation currently delegates to Phalcon's validator stack without
changing behavior. Keeping the wrapper in the framework namespace gives
applications a stable DI type to extend or replace when validation policy
needs to become application-specific.

Use this class anywhere a native `Phalcon\Filter\Validation` instance is
expected. Framework-specific validators under `PhalconKit\Filter\Validation`
are designed to plug into this native validation flow without changing the
message collection or field binding semantics.

***

* Full name: `\PhalconKit\Filter\Validation`
* Parent class: [`Validation`](https://docs.phalcon.io/latest/api/){:target="_blank"}

**See Also:**

* https://docs.phalcon.io/5.18/filter-validation/
