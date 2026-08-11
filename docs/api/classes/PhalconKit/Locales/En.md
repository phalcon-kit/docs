
Built-in English translation adapter for framework messages.

The adapter ships PhalconKit's default `en_CA.UTF-8` strings and accepts
application-provided NativeArray options so callers can override or extend
the bundled content. It remains a normal Phalcon NativeArray adapter, so it
can be registered anywhere Phalcon expects a translate adapter.

***

* Full name: `\PhalconKit\Locales\En`
* Parent class: [`NativeArray`](https://docs.phalcon.io/latest/api/){:target="_blank"}

**See Also:**

* https://docs.phalcon.io/5.18/translate/

## Methods

### __construct

Create the English locale adapter.

```php
public __construct(\Phalcon\Translate\InterpolatorFactory $interpolator, array<string,mixed> $options = []): mixed
```

The default domain is `phalcon-kit`. On Unix-like systems where
`LC_MESSAGES` exists, it is passed to Phalcon so locale category handling
matches native gettext conventions. User options are merged recursively so
custom content can be layered over the bundled framework strings.

**Parameters:**

| Parameter       | Type                                       | Description                                                                        |
|-----------------|--------------------------------------------|------------------------------------------------------------------------------------|
| `$interpolator` | **\Phalcon\Translate\InterpolatorFactory** | Factory used by Phalcon to
interpolate placeholders.                               |
| `$options`      | **array<string,mixed>**                    | NativeArray options, commonly
`content`, `locale`, `defaultDomain`, or `category`. |

***
