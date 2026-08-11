
Phalcon autoloader optimized for framework bootstrap usage.

PhalconKit disables the native file-existence callback after construction so
autoloading does not perform redundant file checks in production. Namespace
registration remains native Phalcon behavior; only the file checking
callback is changed.

***

* Full name: `\PhalconKit\Autoload\Loader`
* Parent class: [`Loader`](https://docs.phalcon.io/latest/api/){:target="_blank"}

**See Also:**

* https://docs.phalcon.io/5.18/autoload/

## Methods

### __construct

Create the loader and disable native file checking.

```php
public __construct(bool $isDebug = false): mixed
```

The callback is disabled after native construction so the object is still
initialized exactly as Phalcon expects, then tuned for PhalconKit's
bootstrap path.

**Parameters:**

| Parameter  | Type     | Description                                         |
|------------|----------|-----------------------------------------------------|
| `$isDebug` | **bool** | Forwarded to the native Phalcon loader constructor. |

**Throws:**

When native Phalcon loader initialization fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
