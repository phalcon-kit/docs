
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\ExportAction`

## Methods

### exportAction

Export the data and end the script execution.

```php
public exportAction(): \Phalcon\Http\ResponseInterface
```

This method retrieves the data by calling the `find` method and then
exposes it using the `exportExpose` method. If the data is successfully
exported using the `export` method, the script execution is ended by
calling `exit` with a status code of 0.

**Throws:**

- [`Exception`](../../../../../../Exception.md)

***
