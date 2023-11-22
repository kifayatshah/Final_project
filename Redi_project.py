'''This project is meant to prioritize high speed train over regional train through signaling'''

'''
Object oriented Programming
Error handling 
Testing
'''

from colorama import Fore, Style

class Trains:
    def __init__(self,name, category,speed,gauge):
        self.name= name
        self.category= category
        self.gauge= gauge
        self.speed = speed
        self.weight = None
        self.direction = None

    def high_speed_train(self,weight,direction):
        self.weight= weight
        self.direction = direction

    def regional_train(self, weight, direction):
        self.weight= weight
        self.direction= direction

    def local_Underground_train(self,weight, direction):
        self.weight = weight
        self.direction = direction

    def train_info(self):
        print('\n', 'Name:', self.name, '\n', 'Category:', self.category, '\n', 'Speed:', self.speed, '\n', 'Gauge:',
              self.gauge, '\n', 'Direction:', self.direction)

######################################################################################################

class Signals:
    def __init__(self,*args):
        pass
    def give_signal(self, train, next_train):
        if train.category == 'High-speed' and 360>= train.speed >= 300:
            print(Fore.GREEN+'Green Signal Turned on'+Style.RESET_ALL)
            return 'Green'
        elif train.category== 'Regional' and next_train==None:
            print(Fore.GREEN+'Green Signal Turned on'+Style.RESET_ALL)
            return 'Green'
        elif train.category == 'Regional' and next_train and 360>= next_train.speed>= 300:
            print(Fore.YELLOW+'FIRST:Distant Yellow signal Turned on'+Style.RESET_ALL)
            print(Fore.RED+'NEXT: Turn on Red stop on station. Please take turn to side track'+Style.RESET_ALL)
            return 'Yellow'
        else:
            print(Fore.CYAN+'Caution Signal Turned on. Signal system doesn,t work properly.','\n','Please drive carefully to avoid any emergency.','\n' ,'Reduce speed to 80km/hr'++Style.RESET_ALL)
            return 'Red'



#########################################
# Create an instance of the Trains class
train = Trains('ICE', 'High Speed',350, 11)

# Set the attributes for the high-speed train
train.high_speed_train(850, 'East')
train.train_info()


# Create an instance of the Trains class
train = Trains('Regional Train', 'Normal Speed',22, 11)

# Set the attributes for the high-speed train
train.regional_train(500, 'East')
train.train_info()


# Create an instance of the Trains class
train = Trains('U_Bahn', 'Normal Speed',80, 11)

# Set the attributes for the high-speed train
train.regional_train(500, 'South')
train.train_info()
print('\n')
############################

#Creating instances for regional and high speed trains
t1 = Trains('ICE', 'High-speed', 350, 'Standard')
t2 = Trains('RE', 'Regional', 120, 'Standard')


try:
    signal = Signals()
    signal.give_signal(t2, None)
    signal.give_signal(t1, None)
    signal.give_signal(t1, t2)
    signal.give_signal(t2, t1)
    #signal.give_signal(t2,te)
except NameError as ne:
    print(f'Name Error Occured: {ne}')
except Exception as e:
    print(f'Something went wrong: {e}')


############################################

def test_signals(): #check whether signals work properly as intended
    try:
        signal = Signals()
        signal_1 = signal.give_signal(t2, None)
        signal_2 = signal.give_signal(t1, None)
        signal_3 = signal.give_signal(t1, t2)
        signal_4 = signal.give_signal(t2, t1)
        assert signal_1 == 'Green'
        assert signal_2 == 'Green'
        assert signal_3 == 'Green'
        assert signal_4 == 'Yellow'
    except Exception as er:
        return print(f'Somethings seems wrong in the programme as testing fails.''\n','Reason:',{er})


   #To double check if these works correctly we print the length of the returned signals color, that should be 5 for Green, 3 for red and 6 for yellow respectively

    x = len(signal_1),len(signal_2),len(signal_3),len(signal_4)
    print(x)

test_signals()