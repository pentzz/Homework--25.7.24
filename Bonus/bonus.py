import random

capital_list: list[str] = [
    'Kabul', 'Tirana', 'Algiers', 'Andorra la Vella', 'Luanda', 'Saint John\'s', 'Buenos Aires', 'Yerevan',
    'Canberra', 'Vienna', 'Baku', 'Nassau', 'Manama', 'Dhaka', 'Bridgetown', 'Minsk', 'Brussels', 'Belmopan',
    'Porto-Novo', 'Thimphu', 'Sucre', 'Sarajevo', 'Gaborone', 'Brasília', 'Bandar Seri Begawan', 'Sofia',
    'Ouagadougou', 'Gitega', 'Praia', 'Phnom Penh', 'Yaoundé', 'Ottawa', 'Bangui', 'N\'Djamena', 'Santiago',
    'Beijing', 'Bogotá', 'Moroni', 'Brazzaville', 'Kinshasa', 'San José', 'Zagreb', 'Havana', 'Nicosia',
    'Prague', 'Copenhagen', 'Djibouti', 'Roseau', 'Santo Domingo', 'Quito', 'Cairo', 'San Salvador', 'Malabo',
    'Asmara', 'Tallinn', 'Mbabane', 'Addis Ababa', 'Palikir', 'Suva', 'Helsinki', 'Paris', 'Libreville',
    'Banjul', 'Tbilisi', 'Berlin', 'Accra', 'Athens', 'Saint George\'s', 'Guatemala City', 'Conakry', 'Bissau',
    'Georgetown', 'Port-au-Prince', 'Tegucigalpa', 'Budapest', 'Reykjavík', 'New Delhi', 'Jakarta',
    'Baghdad', 'Dublin', 'Jerusalem', 'Rome', 'Kingston', 'Tokyo', 'Amman', 'Nur-Sultan', 'Nairobi', 'Tarawa',
    'Pyongyang', 'Seoul', 'Kuwait City', 'Bishkek', 'Vientiane', 'Riga', 'Beirut', 'Maseru', 'Monrovia', 'Tripoli',
    'Vaduz', 'Vilnius', 'Luxembourg', 'Antananarivo', 'Lilongwe', 'Kuala Lumpur', 'Malé', 'Bamako', 'Valletta',
    'Majuro', 'Nouakchott', 'Port Louis', 'Mexico City', 'Palau', 'Chisinau', 'Monaco', 'Ulaanbaatar', 'Podgorica',
    'Rabat', 'Maputo', 'Naypyidaw', 'Windhoek', 'Yaren', 'Kathmandu', 'Amsterdam', 'Wellington', 'Managua',
    'Niamey', 'Abuja', 'Skopje', 'Oslo', 'Muscat', 'Islamabad', 'Ngerulmud', 'Panama City', 'Port Moresby',
    'Asunción', 'Lima', 'Manila', 'Warsaw', 'Lisbon', 'Doha', 'Bucharest', 'Moscow', 'Kigali', 'Basseterre',
    'Castries', 'Kingstown', 'Apia', 'San Marino', 'São Tomé', 'Riyadh', 'Dakar', 'Belgrade', 'Victoria',
    'Freetown', 'Singapore', 'Bratislava', 'Ljubljana', 'Honiara', 'Mogadishu', 'Pretoria', 'Juba', 'Madrid',
    'Colombo', 'Khartoum', 'Paramaribo', 'Stockholm', 'Bern', 'Damascus', 'Taipei', 'Dushanbe', 'Dodoma',
    'Bangkok', 'Lomé', 'Nukuʻalofa', 'Port of Spain', 'Tunis', 'Ankara', 'Ashgabat', 'Funafuti', 'Kampala',
    'Kyiv', 'Abu Dhabi', 'London', 'Washington, D.C.', 'Montevideo', 'Tashkent', 'Port Vila', 'Vatican City',
    'Caracas', 'Hanoi', 'Sanaa', 'Lusaka', 'Harare'
]
print("Welcome to the guessing game!".center(60, "="))

rand: int = random.randint(1, len(capital_list) - 1)
ans: str = capital_list[rand].replace(" ", "-")
temp_ans: list = ["_" if c.isalpha() else c for c in ans]
print(f"The Capital city you need to guess is: ", "".join(temp_ans),f"\n(Try to guess it in less than {int(len(ans) * 1.5)} guesses.)")
user_guesses: list = []
while True:
    user_ans: str = input("Enter a Letter: ").lower()
    if len(user_ans) > 1 or not user_ans.isalpha():
        print("You need to guess with a single letter. Try again..")
        continue
    if user_ans in user_guesses:
        print(f"Youve already guessed the letter {user_ans} in the capital..")
        print("".join(temp_ans))
        continue
    if user_ans in ans.lower():
        temp_ans = [user_ans if ans[i].lower() == user_ans else temp_ans[i] for i in range(len(ans))]
        print(f"You guessed it right! {user_ans} is in the name of the Capital!")
        user_guesses.append(user_ans.lower())
    else:
        print(f"Sorry! the letter: {user_ans} is not in the name of the capital")
        user_guesses.append(user_ans.lower())
    print("".join(temp_ans))
    if not "_" in temp_ans:
        print(f"Congrats! you guessed the capital city name in {len(user_guesses)} guesses.")
        print(f"Great job! You are an expert!" if len(user_guesses) <= len(ans) * 1.5 else "Try harder next time :)")
        break
