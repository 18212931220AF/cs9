from lab03 import *


def test_multiply():
    assert multiply(7,5) == 35
    assert multiply(3,8) == 24
    assert multiply(12,8) == 96
    assert multiply(13,14) == 182


def test_collectMultiples():
    assert collectMultiples([2,4,6,8,10], 4) == [4,8]
    assert collectMultiples([5,7,10,12,16,20], 5) == [5,10,20]
    assert collectMultiples([1,6,9,14], 3) == [6,9]
    assert collectMultiples([1,2,3,4,5,6], 2) == [2,4,6]


def test_countVowels():
    assert countVowels("good morning") == 4
    assert countVowels("nice to meet you") == 7
    assert countVowels("i love python") == 4
    assert countVowels("i love you") == 5



def test_reverseVowels():
    assert reverseVowels("Iiaolu") == "uoaiI"
    assert reverseVowels("Ouelsv") == "euO"
    assert reverseVowels("ehjlois") == "ioe"
    assert reverseVowels("paeiqnu") == "uiea"



    
    
