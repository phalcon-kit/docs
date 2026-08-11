
Exposes the installed PhalconKit core version through Phalcon's version API.

Keeping this wrapper aligned with `\Phalcon\Support\Version` lets consumers
use the same version-format helpers they already know from Phalcon while
reporting the framework package version.

***

* Full name: `\PhalconKit\Support\Version`
* Parent class: [`Version`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### getVersion

Return the internal version tuple consumed by Phalcon's formatter.

```php
protected getVersion(): array{int, int, int, int, int}
```

The tuple format is:
ABBCCDE

A - Major version
B - Med version (two digits)
C - Min version (two digits)
D - Special release: 1 = Alpha, 2 = Beta, 3 = RC, 4 = Stable
E - Special release version i.e. RC1, Beta2 etc.

**Return Value:**

Major, medium, minor, stability,
and stability-version tuple.

***
