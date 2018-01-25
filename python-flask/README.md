## Templating (Jinja):

### For Loops:

- `app.py`

```python
@app.route('/list/groups')
def list_groups():
	groups = get_groups_function()
	return render_template('show.html', title='My Title', groups=groups)
```

- `templates/show.html`

```html
<html>
  <body>
    <h2> {{ title }} </h2><p>
    <ul>
      {% for item in groups %}
        <li> {{ item }} </li>
      {% endfor %}
    </ul>
  </body>
</html>
```
