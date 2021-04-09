import unittest
import oxo_logic
import oxo_ui
from unittest.mock import patch

class TestTicTacTie(unittest.TestCase):
     
     def setUp(self):
          self.game = list(" " * 9)

     def test_checkWinningMoveColumn(self):
          self.game[0] = 'X'
          self.game[3] = 'X'
          self.game[6] = 'X'
          self.assertTrue(oxo_logic._isWinningMove(self.game))

     def test_checkWinningMoveRow(self):
          self.game[0] = 'X'
          self.game[1] = 'X'
          self.game[2] = 'X'
          self.assertTrue(oxo_logic._isWinningMove(self.game))
     
     def test_checkWinningMoveDiagonal1(self):
          self.game[0] = 'X'
          self.game[4] = 'X'
          self.game[8] = 'X'
          self.assertTrue(oxo_logic._isWinningMove(self.game))

     def test_checkWinningMoveDiagonal2(self):
          self.game[2] = 'X'
          self.game[4] = 'X'
          self.game[6] = 'X'
          self.assertTrue(oxo_logic._isWinningMove(self.game))

     def test_duplicateInput(self):
          self.game[0] = 'X'
          self.assertRaises(ValueError,oxo_logic.userMove, self.game,0)

     def test_UserWinner(self):
          self.game[2] = 'X'
          self.game[4] = 'X'
          self.assertEqual(oxo_logic.userMove(self.game,6),'X')
     
     def test_ComputerWinner(self):
          with patch('oxo_logic._generateMove') as mocked_get:
               mocked_get.return_value = 6
               self.game[2] = 'O'
               self.game[4] = 'O'
               win = oxo_logic.computerMove(self.game)
               self.assertEqual(win,'O')
     
     def test_Draw(self):
          self.game = list("X" * 9)
          win = oxo_logic.computerMove(self.game)
          self.assertEqual(win,'D')



          
     




if __name__ == '__main__':
    unittest.main()
 
 