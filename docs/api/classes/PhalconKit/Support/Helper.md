
Static facade for native Phalcon and PhalconKit helper services.

Calls are forwarded to the configured `helper` DI service when one exists,
otherwise a new `HelperFactory` is created. The facade keeps lightweight
helper calls available in static contexts such as config construction and
legacy helper usage.

Native methods

***

* Full name: `\PhalconKit\Support\Helper`

## Properties

### helperFactory

Helper factory used by the static facade.

```php
public static ?\PhalconKit\Support\HelperFactory $helperFactory
```

* This property is **static**.

***

## Methods

### getHelperFactory

Return the helper factory used by static helper calls.

```php
public static getHelperFactory(): \PhalconKit\Support\HelperFactory
```

The default DI `helper` service is preferred so applications can override
or extend helper registration globally. When no DI service is available,
the facade falls back to a local `HelperFactory`.

* This method is **static**.
***

### __callStatic

Forward static helper calls to the active helper factory.

```php
public static __callStatic(string $name, array<int,mixed> $arguments): mixed
```

* This method is **static**.
**Parameters:**

| Parameter    | Type                 | Description          |
|--------------|----------------------|----------------------|
| `$name`      | **string**           | Helper service name. |
| `$arguments` | **array<int,mixed>** | Helper arguments.    |

***
