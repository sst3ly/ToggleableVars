#Toggleable Variables

This works by using a class called 't' where you can assign variables to it,
and run .toggle() to toggle it. The value is stored in .v or .value
For example:

```
test = t()
print(test.v)
test.toggle()
print(test.v)
```
This will output:
- False
- True


You can define whether the starting value is True or False like this:
`test = t(default=False)`
or
`test = t(default=True)`
If you leave the default value alone, it will be False.
