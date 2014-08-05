pyfuncrun
=========

Run a python function in a module from command line

##Install

```bash
$ pip install pyfuncrun
```

##Usage

```bash
$ pyfuncrun <path.to.func> <func arguments> <arguments for func to parse in sys.argv>
```


##Example

func.py:

```python
def print_sys_argv():
    print sys.argv


def func_with_args(a, b):
    print ((a + b), sys.argv)


def func_with_kwargs(a, b, c=1):
    print ((a + b + c), sys.argv)
```

Run:

```bash
$ pyfuncrun func.print_sys_argv 1 2
[1, 2]

$ pyfuncrun func.func_with_args 1 2
(3, [])

$ pyfuncrun func.func_with_kwargs 1 2 3 4
(6, [4])
```
