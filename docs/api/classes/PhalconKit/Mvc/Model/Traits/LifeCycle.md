
***

* Full name: `\PhalconKit\Mvc\Model\Traits\LifeCycle`

## Methods

### prepareLifeCycleQuery

Return the query for data retention

```php
public static prepareLifeCycleQuery(\Phalcon\Mvc\Model\Query\BuilderInterface $builder, ?array $parameters = null): void
```

* This method is **static**.
**Parameters:**

| Parameter     | Type                                          | Description |
|---------------|-----------------------------------------------|-------------|
| `$builder`    | **\Phalcon\Mvc\Model\Query\BuilderInterface** |             |
| `$parameters` | **?array**                                    |             |

***
### getLifeCyclePolicy

```php
public static getLifeCyclePolicy(): array
```

* This method is **static**.
***
### getLifeCyclePolicyQuery

```php
public static getLifeCyclePolicyQuery(): ?array
```

* This method is **static**.
***
### getLifeCycleQuery

Return the Query for data retention

```php
public static getLifeCycleQuery(?array $parameters = null, ?\Phalcon\Mvc\Model\Query\BuilderInterface $builder = null): \Phalcon\Mvc\Model\QueryInterface
```

* This method is **static**.
**Parameters:**

| Parameter     | Type                                           | Description |
|---------------|------------------------------------------------|-------------|
| `$parameters` | **?array**                                     |             |
| `$builder`    | **?\Phalcon\Mvc\Model\Query\BuilderInterface** |             |

***
### getBuilder

Return a Query Builder based on parameters

```php
public static getBuilder(?array $parameters = null): \Phalcon\Mvc\Model\Query\BuilderInterface
```

* This method is **static**.
**Parameters:**

| Parameter     | Type       | Description |
|---------------|------------|-------------|
| `$parameters` | **?array** |             |

***
### findLifeCycle

Find records to hard delete for data retention purpose

```php
public static findLifeCycle(?array $parameters = null): mixed
```

* This method is **static**.
**Parameters:**

| Parameter     | Type       | Description |
|---------------|------------|-------------|
| `$parameters` | **?array** |             |

***
