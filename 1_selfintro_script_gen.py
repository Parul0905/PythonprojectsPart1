import datetime

name=input('Enter your name: ').strip()
age=input('Enter your age: ').strip()
city=input('Enter your city: ').strip()
profession=input('Enter your profession: ').strip()
hobby=input('Enter your hobby: ').strip()

intro_message=(f'My name is {name} and I am {age} years old.I live in {city}.My profession is {profession} and I genuinely enjoy {hobby} ')

current_date=datetime.date.today().isoformat()
border="*" * 50
final_output=f"{border}\n {intro_message}\n {border}"
print(final_output)