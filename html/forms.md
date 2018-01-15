Forms
=====

Basic example:

```html
<form>
  <label for="example_field">Enter some text</label>
  <input id="example_field" type="text" placeholder="Text goes here">
  <input type="submit" value="Submit">
</form>
```
Notes:

1. There is no action attribute. Attribute should be omitted (defaults to same page) if the intent is to send the
   form submission to the page that presented the form.
2. There is no method attribute. GET is the default method.
3. the label's `for` attribute matches the input's `id` attribute
4. there are a number of valid input `type`s that are understood by browsers. For more details 
   see: <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input>
5. an input can have a `value` or a `placeholder` property (strictly, it can have both, but `value` will override `placeholder`)
6. `value` is a default value, if unchanged it will be passed as the value for the specified input when the form is submitted. In
   contrast, `placeholder` will not be submitted with the form, even if the user doesn't replace that text.
   
