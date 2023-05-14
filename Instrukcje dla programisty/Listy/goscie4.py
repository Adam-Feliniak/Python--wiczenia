guests_list = ['wojtek', 'babcia', 'sylwia']
print(f"{guests_list[0].title()} chodź coś wszamać!")
print(f"{guests_list[1].title()} ugotujesz mi coś?")
print(f"{guests_list[2].title()} mam coś pysznego dla Ciebie.")

print(f"{guests_list[2].title()} nie przyjdzie.")

guests_list[2] = 'ola'

print(f"{guests_list[0].title()} chodź coś wszamać!")
print(f"{guests_list[1].title()} ugotujesz mi coś?")
print(f"{guests_list[2].title()} mam coś pysznego dla Ciebie.")

print("Znalazłem większy stół")

guests_list.insert(0, 'czarek')
guests_list.insert(2, 'tomek')
guests_list.append('magda')

print(f"{guests_list[0].title()} chodź coś wszamać!")
print(f"{guests_list[1].title()} ugotujesz mi coś?")
print(f"{guests_list[2].title()} mam coś pysznego dla Ciebie.")
print(f"{guests_list[3].title()} zapraszam.")
print(f"{guests_list[4].title()} zapraszam.")
print(f"{guests_list[5].title()} zapraszam.")

removed = guests_list.pop(2)
print(f"{removed.title()}, niestety nie możesz przyjść jednak.")
removed = guests_list.pop(2)
print(f"{removed.title()}, niestety nie możesz przyjść jednak.")
removed = guests_list.pop(2)
print(f"{removed.title()}, niestety nie możesz przyjść jednak.")
removed = guests_list.pop(2)
print(f"{removed.title()}, niestety nie możesz przyjść jednak.")

print(f"{guests_list[0].title()} jednak jesteś zaproszony")
print(f"{guests_list[1].title()} jednak jesteś zaproszony")

print(f"Zaproszono {len(guests_list)} osób")
del guests_list[1]
del guests_list[0]

print(guests_list)
