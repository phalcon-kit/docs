
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\ExportAction`

## Methods

### exportAction

Export records matching the prepared REST query.

```php
public exportAction(): \Phalcon\Http\ResponseInterface
```

The action finds the result set, applies the export exposure rules, and
delegates response generation to the export trait. Content negotiation and
supported export formats are owned by `export()`.

**Throws:**

When the requested export content type is not
supported.
- [`HttpException`](../../../../../Exception/HttpException.md)
When CSV generation fails.
- [`Exception`](https://csv.thephpleague.com/){:target="_blank"}

***
