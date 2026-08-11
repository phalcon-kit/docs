
HTTP response contract used by PhalconKit services.

The interface keeps Phalcon's response contract and makes the reason phrase
accessor explicit for code that needs to inspect final HTTP status metadata
after a controller or service has chosen a status code.

***

* Full name: `\PhalconKit\Http\ResponseInterface`
* Parent interfaces:
  `ResponseInterface`

## Methods

### getReasonPhrase

Return the reason phrase associated with the current status code.

```php
public getReasonPhrase(): string|null
```

Phalcon responses can be created before any explicit status code/reason
phrase has been set, so callers should handle null.

***
