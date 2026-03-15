import datetime
from datetime import date
#Function for length conversion 
def len_converter():
    print("The length converter is active")
    print("1.meter to feet")
    print("2.feet to kilometer")
    print("3.kilometer to miles")
    print("4.miles to meter")
    choice = int(input("Enter your choice from above(1/2/3/4) : "))
    if choice == 1:
        meter = float(input("Enter the length in meter : "))
        feet = meter * 3.28084
        print(f"{meter} mtrs is equal to {feet} feet")
    elif choice == 2:
        feet = float(input("Enter the length in feet : "))
        kilometer = feet * 0.0003048
        print(f"{feet} ft is equal to {kilometer} km") 
    elif choice == 3:
        km = float(input("enter the length in kilometer : "))
        miles = km * 0.621
        print(f"{km} km is equal to {miles} miles")
    elif choice == 4:
        miles = float(input("enter the length in miles : "))
        meter = miles * 1609.34
        print(f"{miles} miles is equal to {meter} mtrs")
    else:
        print("👌")

#Function for weight conversion
def weight_converter():
    print("The weight converter is for kg to pounds and gm to pounds : ")
    print("1.kg to pounds")
    print("2.grams to pounds")
    choice = int(input("Enter your choice from above(1/2) : "))
    if choice == 1:
        kg = float(input("Enter the weight in kg : "))
        pounds = kg * 2.20462
        print(f"{kg} kg is equal to {pounds} pds")
    elif choice == 2:
        grams = float(input("Enter the weight in grams : "))
        pounds = grams * 0.00220462
        print(f"{grams} gms is equal to {pounds} pds")
    else:
        print("😠😠😠😠😠😠😠")

# Function for temperature conversion deg. C TO F and kelvin
def tem_converter():
    print("1.Celsius to Fahrenheit")
    print("2.Celsius to kelvin")
    choice = int(input("Enter your choice from above(1/2) : "))
    if choice == 1:
        cel =  float(input("Enter the temperature in Celsius : "))
        f = (cel * 9/5) + 32
        print(f"{cel} °C is equal to {f} °F")
    elif choice == 2:
        cel = float(input("Enter the temperature in Celsius : "))
        K = cel + 273.15
        print(f"{cel} °C is equal to {K} K")
    else:
        print('😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️')

# Function for time conversion
def time_converter():
    print("1.hour to minute")
    print("2.minute to second")
    print("3.second to hour")
    choice = int(input("Enter your choice from above(1/2/3) : "))

    if choice == 1:
        hr = float(input("Enter the time in hour : "))
        min = hr * 60
        print(f"{hr} hr is equal to {min} min")
    elif choice == 2:
        min = float(input("Enter the time in minute : "))
        sec = min * 60
        print(f"{min} min is equal to {sec} sec")
    elif choice == 3:
        sec = float(input("Enter the time in second : "))
        hr = sec / 3600
        print(f"{sec} sec is equal to {hr} hr")
    else:
        print("😐😐😐😐😐😐")

# function for Age conversion 

def age_conversion():
    birth_year = int(input("Enter your birth year : "))
    current_year = date.today().year
    age_now = current_year - birth_year
    print(f"Your current age is {age_now} years")

#Function for currency conversion
def currency_converter_in_usd():
    print("1.Indian rupee")
    print("2.Japanese yen")
    print("3.euro")
    print("4.Russia ruble")
    choice = int(input("Enter your choice from above(1/2/3/4) : "))
    if choice == 1:
        inr = float(input("Enter the amount in Indian rupee : "))
        print(f"{inr} INR is equal to {inr * 0.012} USD")
    elif choice == 2:
        yen = float(input("Enter the amount in Japanese yen : "))
        print(f"{yen} JPY is equal to {yen * 0.0074} USD")
    elif choice == 3:
        euro = float(input("Enter the amount in euro : "))
        print(f"{euro} EUR is equal to {euro * 1.18} USD")  
    elif choice == 4:
        ruble = float(input("Enter the amount in Russia ruble : "))
        print(f"{ruble} RUB is equal to {ruble * 0.013} USD")   
    else:
        print("🤑🤑🤑🤑🤑🤑🤑🤑")
    
#Main function 
print("Welcome to the unit converter")
print("1.Length converter")
print("2.Weight converter")
print("3.Temperature converter")
print("4.Time converter")
print("5.Age converter")
print("6.Currency converter in USD")
print("7.Exit")

choose = int(input("Enter your choice from above(1/2/3/4/5/6/7) : "))

if choose == 1:
    result = len_converter()
elif choose == 2:
    result = weight_converter()
elif choose == 3:
    result = tem_converter()
elif choose == 4:
    result = time_converter()
elif choose == 5:
    result = age_conversion()
elif choose == 6:
    result = currency_converter_in_usd()
elif choose == 7:
    print("Thank you for using the unit converter")
else:
    print("bhaggggggggggg")