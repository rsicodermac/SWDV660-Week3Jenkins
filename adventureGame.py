from random import *

### This class is set both enemy and player ###
### Initiates the health and damage done ###
class Character:
    '''constructor'''
    def __init__(self):
        self.name = ""
        self.health = 1
        self.health_max = 1
    def attackDamage(self, enemy):
        #randomize damage inflicted
        damage = min((max(randint(0, self.health) , randint(0, enemy.health))), enemy.health)
        enemy.health = enemy.health - damage
        if damage == 0:
            print( '{} dodged {}\'s punch, mocking him with an evil laugh'.format (enemy.name, self.name)) 
        else:
            damagedEnemy = '{}\'s attack lands smoothly, damaging {}'.format (self.name, enemy.name)
            print(damagedEnemy)
        return enemy.health <= 0
### Initializing the Enemies using the Character constructor within ###
### Created a list to randomize enemy encounters ###
class Enemy(Character):
    def __init__(self, player):
        Character.__init__(self)
        enemyList = ['White Walkers','Unsullied','Cercei Lannister']
        #print(randint(enemyList))
        self.health = randint(1, player.health)
        #self.name = ''
        if self.health < 8:
            self.name = enemyList[0]
        elif self.health > 5:
            self.name = enemyList[1]
        else:
            self.name = enemyList[2]
        
        print(self.name + ' health = ' + str(self.health))

class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.state = 'normal'
        self.health = 10
        self.health_max = 10
    #exit the game
    def quit(self):
        print( '{} admitted defeat and brought shame to his house name!!!'.format(self.name))
        self.health = 0
    #print list of commands
    def help(self):
        #key values from dictionary
        print (Commands.keys())
    #method for checking player's current health and inventory
    def status(self):
        print( '{} current health: {} / {}'.format(self.name, self.health, self.health_max))
    def tired(self):
        print( '{} is gassed.'.format(self.name))
        print ("%s feels tired." % self.name)
        #decreases health 
        self.health = max(1, self.health - 1)
    def rest(self):
        if self.state != 'normal':
            print('{} can\'t stop right now, life is on the line.'.format(self.name))
            self.enemy_attacks()
        else:
            print( '{} rests.'.format(self.name))
            if randint(0, 1):
                self.enemy = Enemy(self)
                print('{} frightened by {}'.format(self.name, self.enemy.name))
                self.state = 'fight'
                self.enemy_attacks()
            else:
                #increase health if its lower than max, but lower if resting too long
                if self.health < self.health_max:
                    self.health = self.health + 1
                else:
                    print('{} rests too long, hears voices, and gets paranoid'.format(self.name))
                    self.health = self.health - 1
    def explore(self):
        if self.state != 'normal':
            print ('{} spots too many enemies to move from hiding'.format(self.name))
            self.enemy_attacks()
        else:
            print('{} creeps beyond the walls.'.format(self.name))
            if randint(0, 1):
                self.enemy = Enemy(self)
                print('{} stares down {}, will there be a showdown?'.format(self.name, self.enemy.name))
                self.state = 'fight'
            else:
                if randint(0, 1):
                    self.tired()
    def flee(self):
        if self.state != 'fight':
            print('{} determined to save Jon Snow, runs for dear life.'.format(self.name))
            self.tired()
        else:
            if randint(1, self.health + 5) > randint(1, self.enemy.health):
                print('{} hides from {}'.format(self.name, self.enemy.name))
                self.enemy = None
                self.state = 'normal'
            else:
                print('{} corners {} eliminating an escape route'.format(self.enemy.name,self.name))
                self.enemy_attacks()
    def attack(self):
        if self.state != 'fight':
            print('{} dodged {}\'s punch, mocking him with an evil laugh'.format (enemy.name, self.name))
            self.tired()
        else:
            if self.attackDamage(self.enemy):
                print('{} beheads {}'.format(self.name, self.enemy.name))
                self.enemy = None
                self.state = 'normal'
                if randint(0, self.health) < 10:
                    self.health = self.health + 1
                    self.health_max = self.health_max + 1
                    print('{} gained confidence'.format(self.name))
            else:
                self.enemy_attacks()
    def enemy_attacks(self):
        if self.enemy.attackDamage(self):
            print('{} was captured by {} and fed to the hounds.'.format(self.name, self.enemy.name))

Commands = {
    'explore': Player.explore,
    'attack': Player.attack,
    'flee': Player.flee,
    'status': Player.status,
    'rest': Player.rest,
    'quit': Player.quit,
    'help': Player.help,
  }
def main():
    
    moves = 10
    dragonglass = 25
    mainCharacter = Player()
    mainCharacter.name = input("What is your character's name? ")
    print ("- For command list enter 'help' - ")
    print ('{} know\'s the dangers surrounding the Iron Throne, and Winter is coming. Dragon Glass is needed.'.format(mainCharacter.name))

    for i in range(moves):
        if moves <= 10:
            while(mainCharacter.health > 0):
              line = input("> ")
              args = line.split()
              if len(args) > 0:
                commandFound = False
                for c in Commands.keys():
                  if args[0] == c[:len(args[0])]:
                    Commands[c](mainCharacter)
                    commandFound = True
                    break
            if not commandFound:
                print ("{} questions your command, please enter a valid command".format(mainCharacter.name))
        else:
            dragonglass = dragonglass*randint(5,25)
            print('The war was won, you collected ' + dragonglass + ' pieces of dragonglass and saved humanity itself')
main()

