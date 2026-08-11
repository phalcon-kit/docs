
Framework HTML tag factory.

This class intentionally keeps Phalcon's tag-factory behavior while giving
applications a PhalconKit-scoped type to register in the DI container. Use it
when a service needs native Phalcon tag helpers but should remain typed to a
framework-owned class.

Applications that need to replace or decorate HTML helpers can extend this
class and keep existing consumers pointed at the same `tag`/tag-factory
service boundary.

***

* Full name: `\PhalconKit\Html\TagFactory`
* Parent class: [`TagFactory`](https://docs.phalcon.io/latest/api/){:target="_blank"}

**See Also:**

* \Phalcon\Html\TagFactory
