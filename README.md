[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KQahFieU)

Before running, install the middleware and associated tools (on both machines):
```
sudo dnf install python3-ice ice-compilers
```

Note: The base code is from Example 3.21 of Maarten van Steen's book.

## Extended interface

Three extra operations were added to `Printer.ice` to exercise different RPC data types:

| Operation | Signature | Description |
|-----------|-----------|-------------|
| `sum` | `int sum(int a, int b)` | Returns the sum of two integers |
| `average` | `double average(DoubleSeq values)` | Returns the mean of a sequence of doubles |
| `reverseString` | `string reverseString(string s)` | Returns the input string reversed |

Regenerate the Python stub after editing `Printer.ice`:
```
slice2py Printer.ice
```
