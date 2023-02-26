guests_list = ['wojtek', 'babcia', 'sylwia']
print(f"{guests_list[0].title()} chodź coś wszamać!")
print(f"{guests_list[1].title()} ugotujesz mi coś?")
print(f"{guests_list[2].title()} mam coś pysznego dla Ciebie.")

print(f"{guests_list[2].title()} nie przyjdzie.")

guests_list[2] = 'ola'

print(f"{guests_list[0].title()} chodź coś wszamać!")
print(f"{guests_list[1].title()} ugotujesz mi coś?")
print(f"{guests_list[2].title()} mam coś pysznego dla Ciebie.")