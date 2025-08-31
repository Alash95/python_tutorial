#Input an amount
#check if input is valid
#Input the source currency
#Input the target currency
#Convert the source currency to the target currency 





while True:
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError()
        break
    except ValueError:
        print("Invalid Amount")

currencies = ('USD','EUR', 'CAD')

while True:
    source_currency = input('Source currency (USD/EUR/CAD): ').upper()
    if source_currency not in currencies:
        print('Invalid currency')
    else:
        break

while True:
    target_currency = input('Target currency (USD/EUR/CAD): ').upper()
    if target_currency not in currencies:
        print('Invalid currency')
    else:
        break

rate = {
    'USD': {'EUR': 1.35, 'CAD': 1.25},
    'EUR': {'USD': 1.48, 'CAD': 1.35},
    'CAD': {'USD': 1.58, 'EUR': 1.45}
}

if source_currency == target_currency:
    converted_amount = amount
else:
    converted_amount = amount * rate[source_currency][target_currency]
    print(f'{amount} {source_currency} is equal to {converted_amount:.2f} ')




