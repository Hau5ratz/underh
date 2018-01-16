class Card:
    CTYPES = {0 : 'Relic',
              1 : 'Money',
              2 : 'Food',
              3 : 'Cultist',
              4 : 'Prisoner',
              5 : 'Suspicion'}
    def __init__(self, ilk, intel=None)
        self.ilk = CTYPES[ilk]
        self.intel = intel

    def __str__(self):
        if hasattr(self, name):
            text = '%s' % self.name
            if self.intel:
                text += " %s"% self.intel
        else:
            text = '%s %s the %s' % (self.firstname, self.lastname, self.ilk)
            if hasattr(self, undead):
                if self.undead:
                    text += " (undead)"
        return text


class Relic(Card):
    '''
    Can replace any other type of resource 
    Important in summoning gods
    '''
    def __init__(self, name, intel=None):
        Card.__init__(self, 0, intel=None)
        self.name = name

class Cultist(Card):
    '''
    Used for undercover events and expeditions.
    Important to have when you have high suspicion.
    '''
    def __init__(self, firstname, lastname, undead=False, intel=None):
        Card.__init__(self, 3, intel=None)
        self.firstname = firstname
        self.lastname = lastname
        self.undead = undead

class Prisoner(Card):
    '''
    Used for sacrifices and food
    '''
    def __init__(self, firstname, lastname, intel=None):
        Card.__init__(self, 4, intel=None)
        self.firstname = firstname
        self.lastname = lastname

class Money(Card):
    '''
    Used to buy other resources and to pay taxes, 
    When Tax Day is in play.
    '''
    def __init__(self, name, intel=None):
        Card.__init__(self, 1, intel=None)
        self.name = name 

class Food(Card):
    '''
    Used for certain events, 
    such as sending people on expeditions and infestations (loss of food, intel=None).
    When there is low food, Red Dreams is added to the deck.
    '''
    def __init__(self, name, firstname=None, lastname=None, intel=None):
        Card.__init__(self, 2, intel=None)
        self.name = name
        self.firstname = firstname
        self.lastname = lastname

class Suspicion(Card):
    '''
    The bad type of resource.
    You don't want more than 4 of these 
    as the police may come for you causing game loss.
    There are events that help you get rid of your suspicion.
    '''
    def __init__(self, name, intel=None):
        Card.__init__(self, 5, intel=None)
        self.name = name
