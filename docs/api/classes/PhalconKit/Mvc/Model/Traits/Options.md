
The Options trait provides methods for managing options using an options manager.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Options`

## Properties

### optionsManager

```php
public ?\PhalconKit\Support\Options\ManagerInterface $optionsManager
```

***

## Methods

### initializeOptions

Initialize the Options Manager for the current instance

```php
public initializeOptions(): void
```

***
### getOptionsManager

Get the Options Manager for the current instance

```php
public getOptionsManager(): \PhalconKit\Support\Options\ManagerInterface
```

**Return Value:**

The Options Manager for the current instance

***
### setOptionsManager

Sets the options manager.

```php
public setOptionsManager(\PhalconKit\Support\Options\ManagerInterface $optionsManager): void
```

**Parameters:**

| Parameter         | Type                                             | Description                    |
|-------------------|--------------------------------------------------|--------------------------------|
| `$optionsManager` | **\PhalconKit\Support\Options\ManagerInterface** | The options manager to be set. |

***
