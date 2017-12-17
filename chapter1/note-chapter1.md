## Chapter1: The Python Data Model

1.  特殊方法是由python解释器调用而不是使用者去调用。

2.  built-in complex type can be used to represent two-dimensional vectors.

    ```python
    In [3]: acom=complex(1,2)

    In [4]: acom
    Out[4]: (1+2j)
    ```

3.   The string returned by **\_\_repr\_\_** should be unambiguous and, if possible, match the source code necessary to re-create the object being represented.

    That is why our chosen represenetaion looks calling the constructor of the class.(e.g., Vector(3, 4))

    **\_\_str\_\_** should return a string suitable for display to end users

    if you only implement one of these special methods, choose **\_\_repr\_\_**, because when no custom **\_\_str\_\_** is available, python will call **\_\_repr\_\_** as a fallback.

    ​


