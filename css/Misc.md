Misc CSS Notes
==============

Specifying one or more margin values on a single line
-----------------------------------------------------

```CSS
/*      top  right  bottom  left    (clockwise starting with top) */
margin: 10px  5px    15px   20px;

/*      top   L/R   bottom */
margin: 10px  5px    15px;

/*      top/bottom   L/R */
margin: 10px         5px;

/*      all */
margin: 10px;
```

Display
-------

### Block-Level Element ###

- always starts and ends with a newline
- takes up as much width as possible
- Examples:
    - `<p>`
    - `<div>`
