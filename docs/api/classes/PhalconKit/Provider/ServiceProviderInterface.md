
Interface ServiceProviderInterface

***

* Full name: `\PhalconKit\Provider\ServiceProviderInterface`
* Parent interfaces:
  `ServiceProviderInterface`,
  `InjectionAwareInterface`

## Methods

### register

Register application service.

```php
public register(\Phalcon\Di\DiInterface $di): void
```

**Parameters:**

| Parameter | Type                        | Description |
|-----------|-----------------------------|-------------|
| `$di`     | **\Phalcon\Di\DiInterface** |             |

***

### boot

Package boot method.

```php
public boot(): void
```

***

### configure

Configures the current service provider.

```php
public configure(): void
```

***

### getName

Get the Service name.

```php
public getName(): string
```

***
