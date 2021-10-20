from django.db import models


player_num = (
    ('player 1','player 1'),
    ('player 2','player 2'),
    ('player 3','player 3'),
    ('player 4','player 4'),
)

turn_type = (
    ('blame!','blame!'),
    ('ask!','ask!'),
)

# Create your models here.
class Card_Type (models.Model):
    name = models.CharField(max_length=20)

    def __str__ (self):
        return self.name

class Card (models.Model):
    name = models.CharField(max_length=20)
    type = models.ForeignKey(Card_Type, on_delete=models.PROTECT)
    image = models.ImageField(upload_to = 'cards', null=True, blank=True)

    def __str__ (self):
        return self.name + ' ' + self.type.name


class Player (models.Model):
    name = models.CharField(max_length=20)

    def __str__ (self):
        return self.name 

class Game (models.Model):
    name = models.CharField(max_length=20, null = True, blank = True)
    code = models.CharField(max_length=20)
    dev_card = models.PositiveIntegerField() 
    mod_card = models.PositiveIntegerField() 
    err_card = models.PositiveIntegerField() 

    def __str__ (self):
        return self.name + ' ' + self.code + ' ' + str(self.dev_card) + ' ' + str(self.mod_card) + ' ' + str(self.err_card) + ' '



class Registred (models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    player_number = models.CharField(max_length=20, choices= player_num)

    def __str__ (self):
        return self.player.name + ' ' + self.game.code + ' ' + self.player_number

class Turn (models.Model):
    registred = models.ForeignKey(Registred, on_delete = models.CASCADE) # player registred to game

    dev_card = models.CharField(max_length=20) # select dev card to be asked
    mod_card = models.CharField(max_length=20) # select mod card to be asked
    err_card = models.CharField(max_length=20) # select err card to be asked
    
    cards = models.CharField(max_length=20, null = True, blank = True) # list cards asked
    correct_card = models.PositiveIntegerField(null = True, blank = True) # correct card id, second player   
    
    player_1_reply = models.PositiveIntegerField(null = True, blank = True) # id from current player response 
    player_2_reply = models.PositiveIntegerField(null = True, blank = True) # id from current player response 
    player_3_reply = models.PositiveIntegerField(null = True, blank = True) # id from current player response 
    
    player_request = models.PositiveIntegerField() # id for player request 
    player_asked = models.PositiveIntegerField() # id from current player, player asked
    type = models.CharField(max_length=20, choices= turn_type) # type of turn judge or ask

    def __str__ (self):
        return self.registred.player.name + ' ' + self.dev_card + ' ' + self.mod_card + ' ' + self.err_card + ' '


class Board (models.Model):
    registred = models.ForeignKey(Registred, on_delete=models.PROTECT)    
    # dev cards
    card_d1 = models.CharField(max_length=50, null = True , blank = False)
    card_d2 = models.CharField(max_length=50, null = True , blank = False)
    card_d3 = models.CharField(max_length=50, null = True , blank = False)
    card_d4 = models.CharField(max_length=50, null = True , blank = False)
    card_d5 = models.CharField(max_length=50, null = True , blank = False)
    card_d6 = models.CharField(max_length=50, null = True , blank = False)
    card_d7 = models.CharField(max_length=50, null = True , blank = False)

    # mod cards
    card_m1 = models.CharField(max_length=50, null = True , blank = False)
    card_m2 = models.CharField(max_length=50, null = True , blank = False)
    card_m3 = models.CharField(max_length=50, null = True , blank = False)
    card_m4 = models.CharField(max_length=50, null = True , blank = False)
    card_m5 = models.CharField(max_length=50, null = True , blank = False)
    card_m6 = models.CharField(max_length=50, null = True , blank = False)

    # err cards
    card_e1 = models.CharField(max_length=50, null = True , blank = False)
    card_e2 = models.CharField(max_length=50, null = True , blank = False)
    card_e3 = models.CharField(max_length=50, null = True , blank = False)
    card_e4 = models.CharField(max_length=50, null = True , blank = False)
    card_e5 = models.CharField(max_length=50, null = True , blank = False)
    card_e6 = models.CharField(max_length=50, null = True , blank = False)

    def __str__ (self):
        return self.registred.player.name