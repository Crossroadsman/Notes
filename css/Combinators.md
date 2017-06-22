CSS Combinators
===============

There are four CSS combinators:

- descendant (space)
- child (>)
- adjacent sibling (+)
- general sibling (~)

Descendant
----------

```CSS
div span {
   keyword: value
}
```

The above will select any `span` that is somewhere inside a `div`, as in the following example:

```HTML
<div>
    <p>
        <span>This is a span</span
    </p>
</div>
```

Child
-----

```CSS
div > ul {
    keyword: value
}
```

Will select only `ul`'s that is the immediate child of a `div`, so in the following example:

```HTML
<div>
    <ul id="first ul">
        <li><ul id="second ul">
                <li></li>
    </ul>
    <ul id="third ul">
    </ul>
</div>
```

`#first ul` and `#third ul` will be selected, but `#second ul` will not.

Adjacent Sibling
----------------

```CSS
img + span {
    keyword: value
}
```

Like a **child** will only select a sibling (=same **parent** [cf ancestor]) that is adjacent (i.e., immediately next to).

General Sibling
---------------

```CSS
img ~ span {
    keyword: value
}

Will select any `span` that follows `img` and has the same parent.
