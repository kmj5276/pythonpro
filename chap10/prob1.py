print("                Death of an Alien\n")
class Player:
	def blast(self, enemy):
		print("The player blasts an enemy.")
		enemy.die()

class Alien:
	def die(self):
		print("The alien gasps and syas, 'Oh this is it. This is the big one.")
		print("Yes, it's getting dark now. Tell my 1.6 million larvae that I loved them...")
		print("Good-bye, cruel universe.'")

hero = Player()
invader = Alien()
hero.blast(invader)

print("\n\nPress the enter key to exit.")
