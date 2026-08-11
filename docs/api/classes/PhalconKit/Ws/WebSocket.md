
Console runtime used for WebSocket task dispatching.

The class extends Phalcon's CLI console because WebSocket entrypoints route
to task/action pairs, while the surrounding provider/bootstrap layer owns
the actual server lifecycle.

***

* Full name: `\PhalconKit\Ws\WebSocket`
* Parent class: [`Console`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### __construct

Create the WebSocket console with an optional DI container.

```php
public __construct(?\Phalcon\Di\DiInterface $container = null): mixed
```

**Parameters:**

| Parameter    | Type                         | Description |
|--------------|------------------------------|-------------|
| `$container` | **?\Phalcon\Di\DiInterface** |             |

***
