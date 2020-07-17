from random import choice
from os import system, getcwd
from time import sleep
import json


class HangMan:
    def __init__(self):
        self.words = json.load(open(getcwd() + '/Projects/HangMan/words.json'))
        self.played_right_letters = []
        self.played_letters = []
        self.gameover = False
        self.errors = 0
        self.hangman = open(getcwd() + '/Projects/HangMan/hangman.txt')
        self.splitted = self.hangman.read().split('"""')
            
   
    def main_menu(self):
        print('Menu')
        print('[ 1 ] Play now\n[ 2 ] Exit')
        select = int(input('Select one: '))
        if select == 1:
            self.play()
        
        else:
            exit()
            
   
    def play(self):
        self.choiced = choice(self.words['words'])       
        self.choiced_by_random = self.choiced['word']   
        self.make_underlines()
        
        while not self.gameover:
            system('clear')
            print(open(getcwd() + '/Projects/HangMan/h_title.txt').read())
            print('--'*24)         
            print(f'{self.splitted[self.errors]}')
            
            print('Letters played: ', end='')
            self.all_letters()          
            print(f'Tip: {self.choiced["description_tip"]}' if self.choiced['tip'] == True else '')                   
            self.letters()            
            self.is_finished(self.played_right_letters)                     
            
            try:
                my_letter = str(input('Letter: ')).lower()[0]                      
                self.make_play(my_letter)    
          
            except:
                print('Type something')
                sleep(2)                            
        
    
    def make_play(self, letter_choiced):
        if letter_choiced in self.played_letters:
            print('You already played this letter')
            sleep(2)
            return
      
        elif letter_choiced == ' ':
            print('Invalid, try again')
            sleep(2)
            return
        
        elif letter_choiced.isdigit():
            print('Only letters')
            sleep(2)
            return
            
        for pos, letter in enumerate(self.choiced_by_random):
            if self.choiced_by_random[pos] == letter_choiced:                
                self.played_right_letters[pos] = letter_choiced                           
                            
        if letter_choiced not in self.choiced_by_random:
            print(f'Oops, dont have "{letter_choiced}"')
            self.errors += 1
            sleep(1.5)
           
            if self.errors == 5:
                tip = str(input('Would you like to get a tip?[Y/N]: ')).upper()[0]
                if tip == 'Y':
                    self.choiced['tip'] = True
                                                                              
        self.played_letters.append(letter_choiced)
        
  
    def make_underlines(self):
        for under in self.choiced_by_random:
            if under == ' ':
                self.played_right_letters.append(' ')
           
            else:
                self.played_right_letters.append('_')
    
           
    def letters(self):
        for under in self.played_right_letters:
            print(f'{under} ', end='')
        
        print()
        
    def all_letters(self):
        for under in self.played_letters:
            print(f'{under} ', end='')
                
        print()
        
    def is_finished(self, actually_game):
       if actually_game.count('_') == 0:              
           print(f'You win, the word was {self.choiced_by_random}'.center(50))                        
           self.gameover = True
           sleep(1)
           self.play_again()
           
       elif self.errors == 6:
           print(f'You lose, maybe next time'.center(50))
           self.gameover = True
           sleep(1)
           self.play_again()
   
    def play_again(self):
        quest = str(input('Play again?[Y/N]: ')).upper()[0]
        if quest == 'Y':
            self.gameover = False
            self.played_right_letters = []
            self.played_letters = []
            self.errors = 0
            system('clear')
            self.play()
       
        self.gameover = False
        self.played_right_letters = []
        self.played_letters = []
        self.errors = 0
        system('clear')
        self.main_menu()
    

HangMan().main_menu()