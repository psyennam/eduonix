from random import choice

class game():
    wins = 0
    lose = 0

    def play(self, gnum, rnum):
        self.guess(gnum, rnum)

    def guess(self,gnum, rnum):
        if(rnum == gnum):
            self.wins += 1
        else:
            self.lose += 1
    
    def result(self):
        return "Total gusess: %s \n Total Lose: %s" % (self.wins, self.lose)


g = game()
numberofgames = input("Number of Games to Play :")

n = [i for i in range(26)]

i = 1
while(i <= numberofgames):
    num = input("Guess Number : ")
    if(num > 0 and num <= 25):
        for _ in range(1):
            rnum = choice(n)
        g.play(num, rnum)
        print("Your guess Number is: %s And Genrated number is: %s" % (num, rnum))
    else:
        print("Enter Guess Number Between 0 to 25")
        pass
    if(numberofgames == i):
        print(g.result())
    i += 1