
Simple HMVC - allow requests with namespaces and modules
{@inheritdoc}

***

* Full name: `\PhalconKit\Mvc\Application`
* Parent class: [`Application`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Methods

### __construct

HMVC Application
{@inheritdoc}

```php
public __construct(\Phalcon\Di\DiInterface $di): mixed
```

**Parameters:**

| Parameter | Type                        | Description |
|-----------|-----------------------------|-------------|
| `$di`     | **\Phalcon\Di\DiInterface** |             |

***

### request

Requests a location using the specified dispatcher.

```php
public request(array $location = []): string
```

**Parameters:**

| Parameter   | Type      | Description                                                                                                                       |
|-------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| `$location` | **array** | An array containing location information, including namespace, module, controller,
action, and params. Default is an empty array. |

**Return Value:**

The response content of the requested location.

**Throws:**

- [`Exception`](../../Exception.md)

***
