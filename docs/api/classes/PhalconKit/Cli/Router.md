
CLI router with PhalconKit diagnostic state export.

The class must extend Phalcon's native CLI router because Phalcon CLI
applications and modules expect that concrete runtime behavior. It also
implements PhalconKit's shared router interface for typed DI lookups.

Phalcon 5.16 aligns the native CLI router with `Phalcon\Cli\RouterInterface`,
so this wrapper now satisfies both the native router interface inherited from
the parent and PhalconKit's shared router interface.

***

* Full name: `\PhalconKit\Cli\Router`
* Parent class: [`Router`](https://docs.phalcon.io/latest/api/){:target="_blank"}
* This class implements:
  [`\PhalconKit\Router\RouterInterface`](../Router/RouterInterface.md)

**See Also:**

* https://docs.phalcon.io/latest/application-cli/

## Methods

### toArray

Export the current CLI router match state for diagnostics.

```php
public toArray(): array<string,mixed>
```

**Return Value:**

Current module, task, action, params,
matches, and matched-route metadata.

***
