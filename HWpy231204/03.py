""" 4. Запросите у пользователя стоимость покупки в $ и размер скидки в %. Посчитайте, какую сумму он должен заплатить на кассе и выведите эту информацию 
в удобном для чтения виде, с двумя знаками после запятой. Используйте оператор подстановки: %"""

try:
    price = float(input('Введите сумму в $: '))
    discount = float(input('Введите размер скидки в %: '))
    
except ValueError:
    print("Введите данные в виде чисел")
    exit()

discounted_price = price - (price / 100 * discount) 
text = "К Оплате: %.2f$"
print(text % discounted_price)