
***

* Full name: `\PhalconKit\Mvc\Model\Traits\Abstracts\AbstractMetaData`

## Methods

### getModelsMetaData

```php
public getModelsMetaData(): \Phalcon\Mvc\Model\MetaDataInterface
```

* This method is **abstract**.
***
### requireMetaDataModel

Require the trait host to satisfy Phalcon's model metadata contract.

```php
protected requireMetaDataModel(): \Phalcon\Mvc\ModelInterface
```

Metadata helpers call native model-manager APIs that expect a model
instance. This explicit check keeps accidental composition into a
non-model class from falling through to PHP assertions or late method
errors.

**Throws:**

When the trait host is not a Phalcon model.
- [`LogicException`](../../../../Exception/LogicException.md)

***
### requireMetaDataEntity

Require the trait host to expose Phalcon's entity attribute API.

```php
protected requireMetaDataEntity(): \Phalcon\Mvc\EntityInterface
```

Primary-key value and attribute helpers read and write raw model
attributes. This helper gives extension authors a deterministic framework
exception when that entity API is unavailable.

**Throws:**

When the trait host is not a Phalcon entity.
- [`LogicException`](../../../../Exception/LogicException.md)

***
