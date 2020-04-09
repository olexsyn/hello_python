# <a name="top"></a> hello_python

[library](./library)


It's very easy to make some words **bold** and other words *italic* with Markdown. You can even [link to Google!](http://google.com)

# This is an `<h1>` tag

Sometimes it’s useful to have different levels of headings to structure your documents. Start lines with a # to create headings. Multiple ## in a row denote smaller heading sizes.

## Lists


#### Unordered (до 3 уровней)

* Item 1
* Item 2
  * 2nd level
    * 3rd level


#### Ordered 1

1. One
2. Two
3. Three

#### Ordered 2 (только 2 уровня)

```
1. Item 1
1. Item 2
1. Item 3
   1. Item 1a
   1. Item 2b
   1. Item 3a
   1. Item 4b
```

1. Item 1
1. Item 2
1. Item 3
   1. Item 1a
   1. Item 2b
   1. Item 3a
   1. Item 4b

## Task Lists

- [x] @cruad, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

## Emphasis

*This text will be italic*  `*text*`  
_This will also be italic_  `_text_`

**This text will be bold**  `**text**`  
__This will also be bold__  `__text__`

_You **can** combine them_  `_You **can** combine them_`  
*You __can__ combine them*  `*You __can__ combine them*`

[top]: /#top "вверх"

###### This is an `<h6>` tag

[top]

---

> Coffee. The finest organic suspension ever devised... I beat the Borg with it.
> - Captain Janeway

## Code

[top]


```python
digi = 12
stri = 'twelve'

print('digit =', digi, 'string =', stri)

print(f'digit = {digi}, string = {stri}')

print('digit = {}, string = {}'.format(digi, stri))

print('digit = {1}, string = {0}'.format(digi, stri))

print('digit = {digi}, string = {stri}'.format(digi, stri))
```
