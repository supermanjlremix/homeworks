purchase_amount = input("Введите сумму покупки: ")

try:
    purchase_amount = float(purchase_amount)
except ValueError as error:
    print(error)
    exit()

if purchase_amount >= 200 and purchase_amount < 300:
    discount = purchase_amount * 0.03
elif purchase_amount >= 300 and purchase_amount < 500:
    discount = purchase_amount * 0.05
elif purchase_amount >= 500:
    discount = purchase_amount * 0.07
else:
    discount = 0

total_amount = purchase_amount - discount

print(f"Сумма к оплате со скидкой: {total_amount:.2f}")
