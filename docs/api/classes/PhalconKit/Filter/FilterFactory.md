
Factory for filter locators that include PhalconKit sanitizer aliases.

Phalcon's filter factory owns the native sanitizer registry. This subclass
keeps that registry intact and appends PhalconKit's md5, JSON, IPv4, and IPv6
services so framework providers and tests can create equivalent filter
locators without duplicating the alias map.

***

* Full name: `\PhalconKit\Filter\FilterFactory`
* Parent class: [`FilterFactory`](https://docs.phalcon.io/latest/api/){:target="_blank"}

**See Also:**

* https://docs.phalcon.io/5.18/filter/

## Methods

### newInstance

Build a PhalconKit filter locator with native and framework sanitizers.

```php
public newInstance(): \Phalcon\Filter\FilterInterface
```

**Return Value:**

Filter instance suitable for registering as the
DI `filter` service.

***

### getServices

Return the native Phalcon sanitizer map plus PhalconKit aliases.

```php
protected getServices(): array<string,mixed>
```

The returned array is passed directly to `Filter`, where the aliases are
resolved by Phalcon's locator. Applications that need additional filters
should normally register them through the filter provider config instead
of overriding this method.

**Return Value:**

Map of sanitizer aliases to callable or class
service definitions accepted by Phalcon's filter locator.

***
