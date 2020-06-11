### Error handling 


## Try block
The try block lets you test a block of code for errors.

The try block will generate an exception, because x is not defined
```python
try:
  print(x)
except:
  print("An exception occurred")
```
Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an error
## Except block 
The except block lets you handle the error.

```python
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
```
You can use else keyword to define a block of code to be executed if no errors were raised:

```python

``` 

## finally block 
The finally block lets you execute code, regardless of the result of the try- and except blocks.