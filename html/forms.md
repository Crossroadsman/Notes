Forms
=====

Basic example
-------------

```html
<form>
  <label for="example_field">Enter some text</label>
  <input id="example_field" type="text" placeholder="Text goes here">
  <input type="submit" value="Submit">
</form>
```
**Notes**:

1. There is no action attribute. Attribute should be omitted (defaults to same page) if the intent is to send the
   form submission to the page that presented the form.
2. There is no method attribute. GET is the default method.
3. the label's `for` attribute matches the input's `id` attribute
4. there are a number of valid input `type`s that are understood by browsers. For more details 
   see: <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input>
5. You can also use the attribute `required` if you want to make the input required but are not using a particular type that enforces 
   completion.
6. an input can have a `value` or a `placeholder` property (strictly, it can have both, but `value` will override `placeholder`)
7. `value` is a default value, if unchanged it will be passed as the value for the specified input when the form is submitted. In
   contrast, `placeholder` will not be submitted with the form, even if the user doesn't replace that text.
   

Radio Buttons
-------------

```html
<form>
  <label for="formfield_cool">Cool</label>
  <input id="formfield_cool" type="radio" name="cool" value="cool">
  <label for="formfield_uncool">Uncool</label>
  <input id="formfield_uncool" type="radio" name="cool" value="uncool">
  ...
</form>
```
**Notes**:

1. Multiple buttons can have the same `name`. If they do, then the radio selection chooses between one of the buttons with that name.
   Otherwise the buttons are totally independent. In the example above, checking button labelled 'Uncool' will uncheck the button labelled 
   'Cool' (if it was checked).
2. Checked buttons will create a query string `<name>=<value>`, unchecked are just `<name>=`

Dropdown
--------

```html
<p>What is your favourite pen brand?</p>
  <select name="pen brand">
    <option value="Nakaya">Nakaya</option>
    <option value="Pilot">Pilot/Namiki</option>
    <option value="Platinum">Pilot/Namiki</option>
    <option value="Sailor">Sailor</option>
    <option value="Other">Something not listed</option>
  </select>
```

**Notes**
