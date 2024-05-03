def set_difficulty():
    difficulty = 0
    while difficulty == 0:
      difficulty = int(input(f'Please choose the difficulty:\n1 - Easy\n2 - Medium\n'))
      if difficulty == 1:
        print ('Difficulty set as Easy.')
      elif difficulty == 2:
        print ('Difficulty set as Medium.')
      #IMPLEMENT DIFFICULTY   --   3 - Hard\n
      #if difficulty == 3:
        #print ('Difficulty set as Hard.')
      else:
        difficulty = 0
        print ('Please choose a valid option.')
    return difficulty

def make_word_list():
    full_word_list = []
    with open("/content/beginnerwords.txt", "r") as beginner_words:
      for a in beginner_words:
        b = a.replace('\n', '')
        full_word_list.append(b)
    return full_word_list



class Player:
    """Basic player Class."""
    def __init__(self, name):
      self.name = name
      self.rowcol_moves = {}
      self.plays_list = []
      self.word_list = []
      self.board = None
      self.mask = None
      self.score = 0
      self.turn_score = []

    def set_board(self):
      board_len = 0
      while board_len == 0:
        match_board = new_board()
        self.board, board_len = match_board[0], match_board[1]
        #print (f"this is board{self.board}, of {board_len} length")
        if self.mask is None:
          self.mask = p1.board.copy()
      return self.board, self.mask, board_len

    

class NPC():
    """Basic NPC Class."""
    def __init__(self, difficulty):
      self.name = 'The Enemy Intelligence'
      self.difficulty = difficulty
      self.rowcol_moves = {}
      self.plays_list = []
      self.word_list = []
      self.board = p1.board.copy()
      self.mask = self.board.copy()
      self.score = 0
      self.turn_score = []