
PhalconKit CLI console wrapper.

The class currently preserves native Phalcon console behavior while giving
applications and providers a PhalconKit namespace type for CLI bootstraps.
CLI modules still rely on native Phalcon console dispatch semantics.

***

* Full name: `\PhalconKit\Cli\Console`
* Parent class: [`Console`](https://docs.phalcon.io/latest/api/){:target="_blank"}

**See Also:**

* https://docs.phalcon.io/latest/application-cli/

## Methods

### __construct

Create the CLI console with an optional DI container.

```php
public __construct(\Phalcon\Di\DiInterface|null $container = null): mixed
```

**Parameters:**

| Parameter    | Type                              | Description                                                                       |
|--------------|-----------------------------------|-----------------------------------------------------------------------------------|
| `$container` | **\Phalcon\Di\DiInterface\|null** | Native or PhalconKit CLI DI container
forwarded to Phalcon's console constructor. |

***
