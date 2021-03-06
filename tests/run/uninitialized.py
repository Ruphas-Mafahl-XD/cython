# mode: run
# tag: control-flow, uninitialized

def conditional(cond):
    """
    >>> conditional(True)
    []
    >>> conditional(False)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    UnboundLocalError: ...local variable 'a'...
    """
    if cond:
        a = []
    return a

def inside_loop(iter):
    """
    >>> inside_loop([1,2,3])
    3
    >>> inside_loop([])  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    UnboundLocalError: ...local variable 'i'...
    """
    for i in iter:
        pass
    return i

def try_except(cond):
    """
    >>> try_except(True)
    []
    >>> try_except(False)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    UnboundLocalError: ...local variable 'a'...
    """
    try:
        if cond:
            a = []
        raise ValueError
    except ValueError:
        return a

def try_finally(cond):
    """
    >>> try_finally(True)
    []
    >>> try_finally(False)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    UnboundLocalError: ...local variable 'a'...
    """
    try:
        if cond:
            a = []
        raise ValueError
    finally:
        return a

def deleted(cond):
    """
    >>> deleted(False)
    {}
    >>> deleted(True)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    UnboundLocalError: ...local variable 'a'...
    """
    a = {}
    if cond:
        del a
    return a

def test_nested(cond):
    """
    >>> test_nested(True)
    >>> test_nested(False)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    UnboundLocalError: ...local variable 'a'...
    """
    if cond:
        def a():
            pass
    return a()

def test_outer(cond):
    """
    >>> test_outer(True)
    {}
    >>> test_outer(False)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    UnboundLocalError: ...local variable 'a'...
    """
    if cond:
        a = {}
    def inner():
        return a
    return a

def test_inner(cond):
    """
    >>> test_inner(True)
    {}
    >>> test_inner(False)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    NameError: ...free variable 'a' ... in enclosing scope
    """
    if cond:
        a = {}
    def inner():
        return a
    return inner()

def test_class(cond):
    """
    >>> test_class(True)
    1
    >>> test_class(False)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    UnboundLocalError: ...local variable 'A'...
    """
    if cond:
        class A:
            x = 1
    return A.x


def test_try_except_regression(c):
    """
    >>> test_try_except_regression(True)
    (123,)
    >>> test_try_except_regression(False)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    UnboundLocalError: ...local variable 'a'...
    """
    if c:
        a = (123,)
    try:
        return a
    except:
        return a


def test_try_finally_regression(c):
    """
    >>> test_try_finally_regression(True)
    (123,)
    >>> test_try_finally_regression(False)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    UnboundLocalError: ...local variable 'a'...
    """
    if c:
        a = (123,)
    try:
        return a
    finally:
        return a


def test_expression_calculation_order_bug(a):
    """
    >>> test_expression_calculation_order_bug(False)
    []
    >>> test_expression_calculation_order_bug(True)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    UnboundLocalError: ...local variable 'b'...
    """
    if not a:
        b = []
    return (a or b) and (b or a)
