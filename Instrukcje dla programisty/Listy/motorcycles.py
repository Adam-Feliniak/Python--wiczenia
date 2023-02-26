#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles[0] = 'ducati'
#print(motorcycles)

#motorcycles.append('ducati')
#print(motorcycles)

#motorcycles.insert(0, 'ducati')
#print(motorcycles)

#del motorcycles[0]
#print(motorcycles)

#popped_motorcycle = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycle)

#last_owned = motorcycles.pop()
#print(f"Ostatnio zakupiony preze mnie motocykl to {last_owned.title()}.")

#first_owned = motorcycles.pop(0)
#print(f"Mój pierwszy motocykl to {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

#motorcycles.remove('ducati')
#print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n Motocykl {too_expensive.title()} jest zbyt drogi dla mnie.")
