import random
class game:

    def __init__(self):
        self.board = []
        self.counter = 1
        self.picked = []
        self.win = 1

    def create_board(self):
        for i in range(3):
            row = []       
            for j in range(3):
                row.append('-')
            self.board.append(row)
        return self.board

    def show_board(self):
        for row in self.board:  
            print(' '.join(row))

    def turn(self, num=int):
        if num in self.picked:
            return 'ahhh'
        self.picked.append(num)
        self.check_turn()
        num = num - 1
        if num <= 2 and num > -1:
            self.board[0][num] = self.icon
        elif num <= 5 and num > 2:
            self.board[1][num - 3] = self.icon
        elif num <= 8 and num > 5:
            self.board[2][num - 6] = self.icon
        self.counter += 1
    def win_horizontal(self):
        for row in self.board:
            if row.count('0') == 3:
                print('win for 0')
                self.win -= 1
            elif row.count('x') == 3:
                print('win for x')
                self.win -= 1

    def win_vertical(self):
        s1, s2, s3 = self.board[0], self.board[1], self.board[2]
        vert1, vert2, vert3 = [],[],[]
        vertical_lists = []
        vertical_lists.extend([vert1,vert2,vert3])
        vert1.extend([s1[0],s2[0],s3[0]]) , vert2.extend([s1[1],s2[1],s3[1]]), vert3.extend([s1[2],s2[2],s3[2]])
        for list in vertical_lists:
            if list.count('0') == 3:
                print('win for 0')
                self.win -= 1
            elif list.count('x') == 3:
                print('win for x')
                self.win -= 1
    def win_dia(self):
        s1, s2, s3 = self.board[0], self.board[1], self.board[2]
        vert1, vert2 = [],[]
        vertical_lists = []
        vertical_lists.extend([vert1,vert2,])
        vert1.extend([s1[0],s2[1],s3[2]]) , vert2.extend([s1[2],s2[1],s3[0]])
        for list in vertical_lists:
            if list.count('0') == 3:
                print('win for 0')
                self.win -= 1
            elif list.count('x') == 3:
                print('win for x')
                self.win -= 1
    def draw(self):
        if len(self.picked) == 9:
            print('draw')
            self.win -= 1
    def check_turn(self):
        if self.counter % 2 == 1:
            self.icon = 'x'
        else:
            self.icon = '0'

              
    def run_game(self):
        while self.win == 1:
            self.show_board()
            self.win_horizontal()
            self.win_vertical()
            self.win_dia()
            self.draw()
            self.turn(int(input()))

        
        
samp = game()
samp.create_board()
#samp.show_board()
samp.run_game()
