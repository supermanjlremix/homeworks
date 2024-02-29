usd_amount = input("Введите количество USD: ")

try:
    usd_amount = float(usd_amount)
except ValueError as error:
    print(error)
    exit()
    
target_currency = input("Выберите валюту для конвертации (EUR, UAN, AZN): ")

if target_currency == 'EUR':
    converted_amount = usd_amount * 0.88
    print(f"{usd_amount} USD равно {converted_amount} EUR.")
elif target_currency == 'UAN':
    converted_amount = usd_amount * 27.70
    print(f"{usd_amount} USD равно {converted_amount} UAN.")
elif target_currency == 'AZN':
    converted_amount = usd_amount * 1.70
    print(f"{usd_amount} USD равно {converted_amount} AZN.")
else:
    print("Выбранная валюта недоступна.")
