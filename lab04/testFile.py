from Stack import Stack
from lab04 import solveMaze


def test_examlpe1():
    maze1 = [
     ['+', '+', '+', '+', 'G', '+'],
     ['+', ' ', '+', ' ', ' ', '+'],
     ['+', ' ', ' ', ' ', '+', '+'],
     ['+', ' ', '+', '+', ' ', '+'],
     ['+', ' ', ' ', ' ', ' ', '+'],
     ['+', ' ', '+', '+', '+', '+']]

    assert solveMaze(maze1,4,4) == True
    assert maze1 == [
        ['+', '+', '+', '+', 'G', '+'],
        ['+', 8, '+', 11, 12, '+'],
        ['+', 7, 9, 10, '+', '+'],
        ['+', 6, '+', '+', 2, '+'],
        ['+', 5, 4, 3, 1, '+'],
        ['+', ' ', '+', '+', '+', '+']]


def test_examlp2():
    maze2 = [[' ', '+', ' ', '+', ' ', 'G'],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', '+', ' ', ' ', '+', ' '],
            [' ', ' ', ' ', '+', ' ', ' '],
            [' ', '+', ' ', '+', ' ', ' '],
            ['+', ' ', '+', '+', ' ', '+']]
    assert solveMaze(maze2, 4,4) == True
    assert maze2 == [
        [' ', '+', ' ', '+', ' ', 'G'],
        [' ', ' ', ' ', ' ', ' ', 5],
        [' ', '+', ' ', ' ', '+', 4],
        [' ', ' ', ' ', '+', 2, 3],
        [' ', '+', ' ', '+', 1, ' '],
        ['+', ' ', '+', '+', ' ', '+']]


def test_examlp3():
    maze3 = [[' ', '+', ' ', '+', ' ', ' '],
            ['G', ' ', ' ', ' ', ' ', ' '],
            [' ', '+', ' ', ' ', '+', '+'],
            [' ', ' ', '+', ' ', ' ', '+'],
            [' ', '+', ' ', ' ', ' ', ' '],
            [' ', ' ', '+', ' ', ' ', '+']]
    assert solveMaze(maze3, 4,4) == True
    assert maze3 == [
         [' ', '+', 7, '+', ' ', ' '],
         ['G', 8, 6, 5, ' ', ' '],
         [' ', '+', ' ', 4, '+', '+'],
         [' ', ' ', '+', 3, 2, '+'],
         [' ', '+', ' ', ' ', 1, ' '],
         [' ', ' ', '+', ' ', ' ', '+']]


def test_examlp4():
    maze4 = [[' ', '+', ' ', '+', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', '+', ' ', ' ', '+', '+'],
            [' ', '+', '+', '+', ' ', '+'],
            [' ', '+', ' ', '+', ' ', ' '],
            ['G', '+', '+', '+', ' ', '+']]
    assert solveMaze(maze4, 4,4)==  False





        
