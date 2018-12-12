import pygal
from random import randint
class Die():
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
    def roll(self):
        return randint(1,self.num_sides)

die1=Die()
die2=Die()
die3=Die()
results=[]
for roll_num in range(100000):
    result=die1.roll()+die2.roll()+die3.roll()
    results.append(result)
frequencies=[]
max_result=die1.num_sides+die2.num_sides+die3.num_sides
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)
hist=pygal.Bar()
hist.title="Result of rolling a D6 and a D10 dice 1000 times."
hist.x_labels=[num for num in range(3,19)]
hist.x_title="Result"
hist.y_title="Frequency of Result"
hist.add("D6+D6+D6",frequencies)
hist.render_to_file("die_value2.svg")