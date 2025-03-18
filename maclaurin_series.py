from sympy import diff, symbols, factorial, pprint, cos, series, ln

def maclaurin_series(func, n):
    series = 0
    for k in range(n):

        diff_func_series = diff(func, x, k)

        diff_func_at_0 = diff_func_series.subs(x, 0)

        series += (diff_func_at_0 / factorial(k)) * x**k

    return series

x = symbols('x')
func = ln((1 + x) / (1 - x))
result = maclaurin_series(func, 6)
result_sumpy = series(func, x, 0, 6).removeO()
assert result.equals(result_sumpy), "Результаты не совпадают!" # Проверка ручного алгоритма со встроенным в SymPy.
pprint(result)
