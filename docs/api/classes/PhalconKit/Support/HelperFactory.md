
Helper factory with PhalconKit-specific array/string helpers.

The factory preserves native Phalcon helper services and adds helpers used by
framework exposure, scaffolding, slug, and text-normalization code. The
`@method` annotations document the magic helper surface exposed through both
this factory and `PhalconKit\Support\Helper`.

***

* Full name: `\PhalconKit\Support\HelperFactory`
* Parent class: [`HelperFactory`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### getServices

Return native Phalcon helpers plus PhalconKit helper services.

```php
protected getServices(): array<string,class-string>
```

***
