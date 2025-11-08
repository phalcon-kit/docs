
This file is part of the Phalcon Kit.

Represents a class that extends the Phalcon\Tag class and provides additional functionality.

***

* Full name: `\PhalconKit\Tag`
* Parent class: [`Tag`](https://docs.phalcon.io/latest/api/){:target="_blank"}

**See Also:**

* \Phalcon\Tag

## Properties

### meta

Represents an array that stores meta-information.

```php
protected static array $meta
```

* This property is **static**.

***

### link

Represents an array that stores link information.

```php
protected static array $link
```

* This property is **static**.

***

### attr

Represents an array that stores attributes.

```php
protected static array $attr
```

* This property is **static**.

***

### assetsManager

Represents a service for managing assets.

```php
protected static \PhalconKit\Assets\Manager|null $assetsManager
```

* This property is **static**.

***

## Methods

### getAssetsManager

Retrieves the instance of the Assets Manager.

```php
public static getAssetsManager(): \PhalconKit\Assets\Manager
```

* This method is **static**.
**Return Value:**

The instance of the Assets Manager

***

### setAssetsManager

Sets the assets manager to be used.

```php
public static setAssetsManager(\PhalconKit\Assets\Manager|null $assetsManager): void
```

* This method is **static**.
**Parameters:**

| Parameter        | Type                                 | Description                                                                  |
|------------------|--------------------------------------|------------------------------------------------------------------------------|
| `$assetsManager` | **\PhalconKit\Assets\Manager\|null** | The assets manager to be set. Pass null to unset the current assets manager. |

***

### getEscaper

Retrieves the configured escaper instance.

```php
public static getEscaper(array $params): \Phalcon\Html\Escaper\EscaperInterface|null
```

* This method is **static**.
**Parameters:**

| Parameter | Type      | Description                                                                                                                                  |
|-----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `$params` | **array** | The parameters used to retrieve the escaper instance.
The params should be an associative array with optional keys to configure the escaper. |

**Return Value:**

The configured escaper instance, or null if no escaper is found.

**Throws:**

If the retrieved escaper instance is not an instance of Escaper.
- [`AssertionError`](../AssertionError.md)

**See Also:**

* \Phalcon\Tag::getEscaper()

***

### getEscaperService

Retrieves the escaper service.

```php
public static getEscaperService(): \Phalcon\Html\Escaper\EscaperInterface
```

* This method is **static**.
**Return Value:**

The instance of the escaper service.

**Throws:**

If the retrieved escaper instance is not an instance of Escaper.
- [`AssertionError`](../AssertionError.md)

**See Also:**

* \Phalcon\Tag::getEscaperService()

***

### title

Prints the page title with optional prefixes and suffixes.

```php
public static title(bool $prepend = true, bool $append = true): void
```

* This method is **static**.
**Parameters:**

| Parameter  | Type     | Description                                                                  |
|------------|----------|------------------------------------------------------------------------------|
| `$prepend` | **bool** | [optional] Whether to prepend the page title with a prefix. Default is true. |
| `$append`  | **bool** | [optional] Whether to append the page title with a suffix. Default is true.  |

***

### implodeSprintf

Implode the elements of an array using sprintf and optional glue.

```php
public static implodeSprintf(array $array, string $format = '%s', string|null $glue = null): string
```

Example:
```php
Tag::implodeSprintf(['class' => 'class1 class2', 'id' => 'my-id', 'test' => ['test1', 'test2']], '%%2$s="%%1$s"', ' ');
```

Result:
```HTML
class="class1 class2" id="my-id" test="{['test1', 'test2']}"
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                         |
|-----------|------------------|---------------------------------------------------------------------|
| `$array`  | **array**        | The input array.                                                    |
| `$format` | **string**       | The format string to be used with sprintf. Default is '%s'.         |
| `$glue`   | **string\|null** | The glue string to be used between array elements. Default is null. |

**Return Value:**

The resulting string after implodes. If the input array is empty, an empty string is returned.

***

### escapeParam

Escapes a parameter value based on the attribute.

```php
public static escapeParam(mixed $value = null, string|null $attr = null, string $glue = ' '): array
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                                  |
|-----------|------------------|------------------------------------------------------------------------------|
| `$value`  | **mixed**        | The value to be escaped.                                                     |
| `$attr`   | **string\|null** | The attribute of the parameter. Default is null.                             |
| `$glue`   | **string**       | The delimiter to be used for joining array values. Default is a space (' '). |

**Return Value:**

An array containing the escaped value and the attribute.

***

### get

Retrieves the HTML representation of a specified tag, along with optional parameters and content.

```php
public static get(string $tag, array $params = [], array $html = [], string|null $glue = null): string
```

Example 1:

```php
Tag::get('div', ['class' => 'class1 class2'], ['content1', 'content2']);
```

```HTML
<div class="class1 class2">content1</div>
<div class="class1 class2">content2</div>
```

Example 2:
```php
Tag::get('div', ['class' => 'class1 class2'], ['content1', 'content2'], ' ');
```

```HTML
<div class="class1 class2">content1 content2</div>
```

Example 3:
```php
Tag::get('footer', ['class' => 'my-footer-class'], [
     Tag::get('ul', ['class' => 'my-ul-class'], [
         Tag::get('li', ['class'] => 'my-li-class', ['content1', 'content2']),
         Tag::get('li', ['class'] => 'my-li-class-2', ['content3', 'content4']),
     ],
     Tag::get('ul', ['class' => 'my-ul-class-2'], [
         Tag::get('li', ['class'] => 'my-li-class-3', ['content5', 'content6']),
     ], ''
], ' ');
```

```HTML
<footer class="my-footer-class">
     <ul class="my-ul-class">
         <li class="my-li-class">content1</li>
         <li class="my-li-class">content2</li>
         <li class="my-li-class-2">content3</li>
         <li class="my-li-class-2">content4</li>
     </ul>
     <ul class="my-ul-class-2">
         <li class="my-li-class-3">content5 content6</li>
     </ul>
</div>
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                                                          |
|-----------|------------------|------------------------------------------------------------------------------------------------------|
| `$tag`    | **string**       | The tag name.                                                                                        |
| `$params` | **array**        | The optional parameters for the tag.                                                                 |
| `$html`   | **array**        | The optional HTML content within the tag.                                                            |
| `$glue`   | **string\|null** | The optional string used to join multiple HTML elements. If not provided, the default value is used. |

**Return Value:**

The HTML representation of the tag, including parameters and content.

***

### getTag

Retrieves a formatted string representing a specific tag with the given parameters and HTML attributes.

```php
public static getTag(string $tag, array $params = [], array $html = [], string|null $glue = null): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                       |
|-----------|------------------|-------------------------------------------------------------------|
| `$tag`    | **string**       | The name of the tag to retrieve.                                  |
| `$params` | **array**        | An optional array of parameters to pass as attributes to the tag. |
| `$html`   | **array**        | An optional array of HTML attributes to include in the tag.       |
| `$glue`   | **string\|null** | An optional glue string for joining the HTML attributes.          |

**Return Value:**

The formatted HTML string representing the tag with the provided parameters and attributes.

***

### tag

Prints the HTML code for a given tag, with optional parameters and HTML attributes.

```php
public static tag(string $tag, array $params = [], array $html = [], ?string $glue = null): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type        | Description                                                  |
|-----------|-------------|--------------------------------------------------------------|
| `$tag`    | **string**  | The HTML tag to be printed.                                  |
| `$params` | **array**   | The parameters to be included in the HTML tag attributes.    |
| `$html`   | **array**   | The HTML attributes to be included in the HTML tag.          |
| `$glue`   | **?string** | The optional string used to concatenate the HTML attributes. |

***

### getTagParams

Retrieves the tag parameters based on the given tag name, additional parameters, format string, and glue string.

```php
public static getTagParams(string $tag, array $params = [], string $format = ' %2$s="%1$s"', string|null $glue = null): string
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                                                                                                                                              |
|-----------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$tag`    | **string**       | The name of the tag to retrieve the parameters for.                                                                                                                                      |
| `$params` | **array**        | (Optional) Additional parameters to merge with the tag attributes. The parameters should be provided as an associative array with keys representing the parameter names.                 |
| `$format` | **string**       | (Optional) The format string to use when formatting the tag parameters. The format string should contain two placeholders: %1$s for the parameter value and %2$s for the parameter name. |
| `$glue`   | **string\|null** | (Optional) The glue string to use when joining the formatted tag parameters. If null, the default glue string will be used.                                                              |

**Return Value:**

The formatted tag parameters joined by the glue string.

***

### tagParams

Returns a formatted string containing tag parameters for the specified tag.

```php
public static tagParams(string $tag, array $params = [], string $format = ' %2$s="%1$s"', string|null $glue = null): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                                                                                                                                                                                              |
|-----------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$tag`    | **string**       | The tag to be used.                                                                                                                                                                                                                      |
| `$params` | **array**        | The parameters to be added to the tag. The parameters should be provided as an associative array with keys representing the parameter names and values representing the parameter values.                                                |
| `$format` | **string**       | The format string used to concatenate each parameter. The format string should contain two placeholders ('%1$s' and '%2$s') that will be replaced with the parameter value and name, respectively. The default format is ' %2$s="%1$s"'. |
| `$glue`   | **string\|null** | The glue used to concatenate multiple parameters. If null, the default PHP glue will be used.                                                                                                                                            |

***

### getParams

Will sprintf an array_map of the array and then implode it with a ' ' glue
- Escape attrs and values during the process

```php
public static getParams(array $params = [], string $format = ' %2$s="%1$s"', ?string $glue = null): string
```

Example:
```php
Tag::getParams(['class' => 'class1 class2', 'id' => 'my-id'])
```

Result:
```HTML
class="class1 class2" id="my-id"
```

* This method is **static**.
**Parameters:**

| Parameter | Type        | Description                |
|-----------|-------------|----------------------------|
| `$params` | **array**   | Array to implode & sprintf |
| `$format` | **string**  |                            |
| `$glue`   | **?string** |                            |

**Return Value:**

Return the imploded sprintf "%%2$s="%%1$s" from an array

***

### params

Prints the formatted parameters to the output.

```php
public static params(array $params = [], string $format = ' %2$s="%1$s"', null|string $glue = null): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                                                                                                                                                            |
|-----------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$params` | **array**        | An array containing the parameters to be formatted. The parameters should be provided as an associative array with keys representing the parameter names and values representing the parameter values. |
| `$format` | **string**       | The format string used to format each parameter. The format string should contain two placeholders: %1$s representing the parameter value and %2$s representing the parameter name.                    |
| `$glue`   | **null\|string** | (optional) The string used to glue multiple formatted parameters together. If not provided, the default glue value will be used.                                                                       |

***

### getAttr

Retrieves the attributes of a specific name from the existing list of attributes.

```php
public static getAttr(string $name): array
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description                            |
|-----------|------------|----------------------------------------|
| `$name`   | **string** | The name of the attribute to retrieve. |

**Return Value:**

An array containing the attributes corresponding to the given name. If the attribute does not exist, an empty array is returned.

***

### getAttrs

Retrieves the existing list of attributes.

```php
public static getAttrs(): array
```

* This method is **static**.
**Return Value:**

Returns an array containing the existing list of attributes. The attributes are represented as key-value pairs.

***

### setAttr

Sets attributes for a given name.

```php
public static setAttr(string $name, array $attrs = [], bool $merge = true): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type       | Description                                                                                                                            |
|-----------|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `$name`   | **string** | The name of the attribute.                                                                                                             |
| `$attrs`  | **array**  | The attributes to be set for the given name. The attributes should be an associative array with keys representing the attribute names. |
| `$merge`  | **bool**   | Optional. Specifies whether to merge the new attributes with existing attributes. Default is true.                                     |

***

### setAttrs

Sets attributes for the object.

```php
public static setAttrs(array $attrs = [], bool $merge = false): array
```

* This method is **static**.
**Parameters:**

| Parameter | Type      | Description                                                                                                                                    |
|-----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `$attrs`  | **array** | An array of attributes to be set. Each attribute key represents the name of the attribute and the value represents the value of the attribute. |
| `$merge`  | **bool**  | Optional. Determines whether the existing attributes should be merged with the new attributes. Defaults to false.                              |

**Return Value:**

The updated attributes array after setting the new attributes.

***

### resetAttrs

Reset attributes

```php
public static resetAttrs(): void
```

* This method is **static**.
***

### setMetaCharset

Set the meta charset value
Specifies the character encoding for the HTML document.

```php
public static setMetaCharset(string $charset = 'UTF-8'): void
```

Example:
```php
Tag::setMetaCharset('UTF-8');
Tag::meta('charset', 'UTF-8');
```

Result:
```HTML
<meta charset="UTF-8">
```

Common values:
     UTF-8 - Character encoding for Unicode
     ISO-8859-1 - Character encoding for the Latin alphabet
In theory, any character encoding can be used, but no browser understands all of them. The more widely a character encoding is used, the better the chance that a browser will understand it.

To view all available character encodings, look at IANA character sets.
- @link http://www.iana.org/assignments/character-sets/character-sets.xhtml

For more information about the charset values, please visit this documentation below
- @link https://www.w3schools.com/tags/att_meta_charset.asp

* This method is **static**.
**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$charset` | **string** |             |

***

### setMetaProperty

Sets the value of a meta-property.

```php
public static setMetaProperty(string $property, string|null $content = null): void
```

This method sets the specified meta-property with the given content. If there is
already a meta-property with the same name, it will be removed before adding the new one.

* This method is **static**.
**Parameters:**

| Parameter   | Type             | Description                                                                                       |
|-------------|------------------|---------------------------------------------------------------------------------------------------|
| `$property` | **string**       | The name of the meta-property to set.                                                             |
| `$content`  | **string\|null** | The content to set for the meta-property. It can be null if the property doesn't require content. |

***

### setMetaName

Set the meta-name attribute with the given value.

```php
public static setMetaName(string $name, string|null $content = null): void
```

* This method is **static**.
**Parameters:**

| Parameter  | Type             | Description                                              |
|------------|------------------|----------------------------------------------------------|
| `$name`    | **string**       | The name of the meta-tag.                                |
| `$content` | **string\|null** | The content of the meta-tag. Optional, defaults to null. |

***

### addMeta

Add meta

```php
public static addMeta(string $attr, string $value, string|null $content = null): void
```

* This method is **static**.
**Parameters:**

| Parameter  | Type             | Description                            |
|------------|------------------|----------------------------------------|
| `$attr`    | **string**       | The attribute of the meta-tag          |
| `$value`   | **string**       | The value of the attribute             |
| `$content` | **string\|null** | (optional) The content of the meta-tag |

***

### addRawMeta

Add raw meta

```php
public static addRawMeta(array $meta): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type      | Description               |
|-----------|-----------|---------------------------|
| `$meta`   | **array** | The meta-data to be added |

***

### addLink

Add a new link tag
For more information about the attr, values, and other options please visite the w3schools documentation below
- https://www.w3schools.com/tags/tag_link.asp

```php
public static addLink(string $attr, string $value, array $options = []): void
```

Example:
```php
Tag::addLink('rel', 'alternate', ['type' => 'application/atom+xml', 'title' => 'Phalcon Kit', 'href' => '/blog/news/atom"']);
```

Result:
```HTML
<link rel="alternate" type="application/atom+xml" title="Phalcon Kit News" href="/blog/news/atom">
```

* This method is **static**.
**Parameters:**

| Parameter  | Type       | Description               |
|------------|------------|---------------------------|
| `$attr`    | **string** | Link tag attr             |
| `$value`   | **string** | Link tag attr value       |
| `$options` | **array**  | Link tag attrs and values |

***

### addRawLink

Adds a raw link to the existing list of links.

```php
public static addRawLink(array $link): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type      | Description                                                                                                   |
|-----------|-----------|---------------------------------------------------------------------------------------------------------------|
| `$link`   | **array** | The raw link to be added. The link should be an associative array with keys representing the link attributes. |

***

### removeMeta

Removes meta-tags from the existing list of meta-tags based on the specified attribute, value, and content.

```php
public static removeMeta(string $attr, string|null $value = null, string|null $content = null): void
```

* This method is **static**.
**Parameters:**

| Parameter  | Type             | Description                                                                                                  |
|------------|------------------|--------------------------------------------------------------------------------------------------------------|
| `$attr`    | **string**       | The attribute of the meta-tags to be removed.                                                                |
| `$value`   | **string\|null** | The value of the attribute. If null, all meta-tags with the specified attribute will be removed.             |
| `$content` | **string\|null** | The content of the meta-tags. If null, all meta-tags with the specified attribute and value will be removed. |

***

### getMeta

Retrieves the concatenated string representation of the meta-values.

```php
public static getMeta(string|null $glue = null): string|null
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                                    |
|-----------|------------------|--------------------------------------------------------------------------------|
| `$glue`   | **string\|null** | The optional glue string used to concatenate the meta-values. Default is null. |

**Return Value:**

The concatenated string representation of the meta-values, or null if there are no meta-values.

***

### meta

Prints the meta-information using the specified glue.

```php
public static meta(string|null $glue = null): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                                                             |
|-----------|------------------|---------------------------------------------------------------------------------------------------------|
| `$glue`   | **string\|null** | The glue to be used for concatenating the meta-information. If not provided, the default value is null. |

***

### getLink

Retrieves the links as a concatenated string with an optional glue separator.

```php
public static getLink(string|null $glue = null): string|null
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                                                        |
|-----------|------------------|----------------------------------------------------------------------------------------------------|
| `$glue`   | **string\|null** | The separator used to concatenate the links. If null, no separator is used. Default value is null. |

**Return Value:**

The concatenated string of links, or null if there are no links.

***

### link

Generates and echoes the link string.

```php
public static link(string|null $glue = null): void
```

* This method is **static**.
**Parameters:**

| Parameter | Type             | Description                                                                  |
|-----------|------------------|------------------------------------------------------------------------------|
| `$glue`   | **string\|null** | The glue used to join the link attributes (optional). Default value is null. |

***

### getCss

Retrieves the CSS markup for the specified collection or all collections if no collection is specified.

```php
public static getCss(string|null $collection = null): string|null
```

* This method is **static**.
**Parameters:**

| Parameter     | Type             | Description                                                                                |
|---------------|------------------|--------------------------------------------------------------------------------------------|
| `$collection` | **string\|null** | (optional) The name of the collection. If not specified, all collections will be included. |

**Return Value:**

The CSS markup for the specified collection or all collections. Returns null if no CSS is found.

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### css

Prints the CSS markup for the specified collection or the default collection if no collection is provided.

```php
public static css(string|null $collection = null): void
```

If a collection is provided, it should be a string representing the name of the CSS collection.
If no collection is provided, the default collection will be used.

* This method is **static**.
**Parameters:**

| Parameter     | Type             | Description                                       |
|---------------|------------------|---------------------------------------------------|
| `$collection` | **string\|null** | The name of the CSS collection. Defaults to null. |

***

### getJs

Retrieves JavaScript markup from the given asset collection or from all asset collections if none is specified.

```php
public static getJs(string|null $collection = null): string|null
```

* This method is **static**.
**Parameters:**

| Parameter     | Type             | Description                                                                                                                |
|---------------|------------------|----------------------------------------------------------------------------------------------------------------------------|
| `$collection` | **string\|null** | Optional. The name of the asset collection. If not provided, JavaScript code from all asset collections will be retrieved. |

**Return Value:**

The generated JavaScript code, or null if no JavaScript code is found for the specified collection(s).

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### js

Outputs the JavaScript markup for a specific collection or for all collections if no collection is specified.

```php
public static js(string|null $collection = null): void
```

* This method is **static**.
**Parameters:**

| Parameter     | Type             | Description                                                                                            |
|---------------|------------------|--------------------------------------------------------------------------------------------------------|
| `$collection` | **string\|null** | The name of the collection to retrieve the JavaScript from. If null, all collections will be included. |

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
