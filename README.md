# monster_battle
Python script that defines a function called battle that simulates a battle between monsters. The goal is to keep eliminating monsters until only one or none are left. This project was made for my System Programming for Engineers class.

IMPORTING LIST FROM TYPING: This import statement is used to specify the type of the monsters parameter in the function. It indicates that monsters should be a list of integers.

DEFINITION OF THE BATTLE FUNCTION: This function takes a list of integers representing the strengths of monsters as its parameter.

WHILE LOOP TO SIMULATE THE BATTLE: The loop continues as long as there are more than one monster in the list.

FINDING THE MINIMUM AND MAXIMUM STRENGHT MONSTERS: These lines find the minimum and maximum strength monsters in the list.

ELIMINATING MONSTERS AND UPDATING THE LIST: If the maximum strength monster is greater than the minimum strength monster, the difference is calculated (a) and a new monster with strength a is added to the list. If the minimum and maximum strength monsters are equal, both are removed from the list.

After the while loop, it checks if there is one monster left or none, and prints the corresponding message.

