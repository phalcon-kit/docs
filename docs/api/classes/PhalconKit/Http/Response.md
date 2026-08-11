
HTTP response implementation used by PhalconKit services.

This wrapper delegates to Phalcon's response object while providing a
framework-scoped type for DI definitions, controller return values, and
service contracts. It does not override serialization, header emission, or
status-code behavior; those remain native Phalcon response responsibilities.

***

* Full name: `\PhalconKit\Http\Response`
* Parent class: [`Response`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  [`\PhalconKit\Http\ResponseInterface`](./ResponseInterface.md)

**See Also:**

* \Phalcon\Http\Response
