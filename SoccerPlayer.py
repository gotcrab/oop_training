class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self,sc=1):
        self.goals += sc

    def make_assist(self, ass=1):
        self.assists += ass

    def statistics(self):
        print(f'{self.name} {self.surname} - голы: {self.goals}, передачи: {self.assists}')

leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics()
leo.score()
leo.score(4)
leo.make_assist()
leo.make_assist(15)
leo.statistics()
koko = SoccerPlayer('Shit', 'Happens')
koko.score(0)
koko.make_assist(1)
koko.statistics()
