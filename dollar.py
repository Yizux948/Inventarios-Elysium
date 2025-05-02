# from pyDolarVenezuela.pages import AlCambio, BCV, CriptoDolar, ExchangeMonitor, Italcambio
# from pyDolarVenezuela import Monitor
# from pyDolarVenezuela import currency_converter

# monitor = Monitor(CriptoDolar, 'USD')

# information_dolar = monitor.get_value_monitors("enparalelovzla")
# price_in_dolares = currency_converter(
#     type='USD', # VES | USD | EUR
#     value=1, # Bs. 1000
#     monitor=information_dolar # Datos del dolar
# )

# print(price_in_dolares)  # Imprime algo como 28.22466836014677






from pyDolarVenezuela.pages import AlCambio, BCV, CriptoDolar, ExchangeMonitor, Italcambio
from pyDolarVenezuela import Monitor

monitor = Monitor(BCV, 'USD')

# Obtener los valores de todos los monitores
valores_dolar = monitor.get_value_monitors()

# Obtener el valor del dólar en EnParaleloVzla
valor_dolar = monitor.get_value_monitors("enparalelovzla", "price", prettify=True)

print(valor_dolar)