import copy

class Cube:
    def __init__(self):
        self.faces = {
            'U': [['W'] * 3 for _ in range(3)],
            'D': [['Y'] * 3 for _ in range(3)],
            'L': [['O'] * 3 for _ in range(3)],
            'R': [['R'] * 3 for _ in range(3)],
            'F': [['G'] * 3 for _ in range(3)],
            'B': [['B'] * 3 for _ in range(3)]
        }
        self.move_history = []

    def rotate_face_clockwise(self, face):
        self.faces[face] = [list(row) for row in zip(*self.faces[face][::-1])]

    def rotate_face_counterclockwise(self, face):
        self.faces[face] = [list(row) for row in zip(*self.faces[face])][::-1]

    def apply_move(self, move):
        self.move_history.append(move)
        clockwise = True
        if move.endswith("'"):
            move = move[0]
            clockwise = False
        for _ in range(1 if clockwise else 3):
            self._rotate(move)

    def _rotate(self, move):
        f = self.faces
        if move == 'U':
            self.rotate_face_clockwise('U')
            f['F'][0], f['R'][0], f['B'][0], f['L'][0] = f['R'][0], f['B'][0], f['L'][0], f['F'][0]
        elif move == 'D':
            self.rotate_face_clockwise('D')
            f['F'][2], f['L'][2], f['B'][2], f['R'][2] = f['L'][2], f['B'][2], f['R'][2], f['F'][2]
        elif move == 'L':
            self.rotate_face_clockwise('L')
            for i in range(3):
                f['U'][i][0], f['F'][i][0], f['D'][i][0], f['B'][2 - i][2] = f['F'][i][0], f['D'][i][0], f['B'][2 - i][2], f['U'][i][0]
        elif move == 'R':
            self.rotate_face_clockwise('R')
            for i in range(3):
                f['U'][i][2], f['B'][2 - i][0], f['D'][i][2], f['F'][i][2] = f['B'][2 - i][0], f['D'][i][2], f['F'][i][2], f['U'][i][2]
        elif move == 'F':
            self.rotate_face_clockwise('F')
            for i in range(3):
                f['U'][2][i], f['R'][i][0], f['D'][0][2 - i], f['L'][2 - i][2] = f['L'][2 - i][2], f['U'][2][i], f['R'][i][0], f['D'][0][2 - i]
        elif move == 'B':
            self.rotate_face_clockwise('B')
            for i in range(3):
                f['U'][0][i], f['L'][2 - i][0], f['D'][2][2 - i], f['R'][i][2] = f['R'][i][2], f['U'][0][i], f['L'][2 - i][0], f['D'][2][2 - i]

    def scramble(self, moves):
        for move in moves:
            self.apply_move(move)

    def reset(self):
        self.__init__()

    def get_move_history(self):
        return self.move_history

    def is_solved(self):
        return all(all(cell == row[0] for cell in row) for face in self.faces.values() for row in face)