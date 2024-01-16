#!/usr/bin/env python3

from typing import List
def battle(monsters: List[int]) -> None:
	while(len(monsters) > 1):
	
		minimo = min(monsters)
		maximo = max(monsters)
	
		if(maximo > minimo):
			a = maximo - minimo
			monsters.remove(minimo)
			monsters.remove(maximo)
			monsters.append(a)
		elif(minimo == maximo):
			monsters.remove(minimo)
			monsters.remove(maximo)
	
	if(len(monsters) == 1):
		print("I have won, but at what cost?")
	elif(len(monsters) == 0):
		print("Nobody won!")


			
		
