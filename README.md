## Ejercicio - CreditCard class en Python

Crear una clase `CreditCard` que tenga como datos `name`, `number`, `expiration`, `cvc` y `status`. El status es una lista de 5 saldos enteros.Posteriormente crea la clase `Portfolio` que podrá recibir un portafolio de n tarjetas de crédito.

Restricciones:

- La clase `CreditCard` podrá sumar los saldos del `status` de la tarjeta de crédito.

- La clase `Portfolio` tendrá los siguientes comportamientos: agregar otra tarjeta de crédito al portafolio, sumar el total de saldos (status) de las tarjetas que conforman el portafolio, borrar tarjetas de crédito del portafolio y entregar el total de tarjetas en el portafolio.


Desarrolla el código basado en las pruebas `specs` correspondientes. 


```python
"""Clase CreditCard"""

...


"""Clase Portfolio"""

...

```
```python
"""Cinco instancias de CreditCard"""

...

"""Portafolio con cinco objetos de tarjetas de crédito"""

...

```

```python
"""Ejemplo de entrada con un objeto tarjeta y salida"""

#creditcard1
amex = CreditCard("Amex", "2345673444", "12/15", "2345", [234, 567, 456, 567, 344])


#portafolio con un objeto de tarjeta de crédito
portfolio = [amex]

#suma de saldos y número de tarjetas en portafolio
portfolio_1 = Portfolio(portfolio)
print(portfolio_1.sum_portfolio())
#>> 2168
print(portfolio_1.how_many_cards())
#>> 1

```

```python
#Test Driven Development - TDD
$ test_credit_card.py
```
