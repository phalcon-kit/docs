
This class allows to get the installed version of the core

***

* Full name: `\PhalconKit\Support\Version`
* Parent class: [`Version`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### getVersion

Area where the version number is set. The format is as follows:
ABBCCDE

```php
protected getVersion(): array{: int, : int, : int, : int, : int}
```

A - Major version
B - Med version (two digits)
C - Min version (two digits)
D - Special release: 1 = Alpha, 2 = Beta, 3 = RC, 4 = Stable
E - Special release version i.e. RC1, Beta2 etc.

***
