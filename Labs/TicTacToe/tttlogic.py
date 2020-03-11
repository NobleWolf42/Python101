__author__ = "Benjamin Carpenter", "Landon Stoner", "Alex VanMannen"

"""
ttt_logic
  This module contains the logic to drive a two-player Tic-Tac-Toe
  game.
"""

'''
---------------------------------------------------------------
  Define any global variables this module may need to maintain the
  state of a Tic-Tac-Toe game.
---------------------------------------------------------------
'''

NW = None
N = None
NE = None
W = None
C = None
E = None
SW = None
S = None
SE = None
player = "X"

def check_status():
    """
    Checks to see if either player has won or if the board is filled.  
    Returns a two-tuple in which the first component is the string
    "X" or the string "O" or the value None; the second component
    of the tuple is one of the following strings that indicates the
    Tic-Tac-Toe board's status:
      "Playing"     No one has won and a move is available
      "Win_NW_NE"   Win across top row
      "Win_W_E"     Win across middle row
      "Win_SW_SE"   Win across bottom row
      "Win_NW_SW"   Win along left column
      "Win_N_S"     Win along center column
      "Win_NE_SE"   Win along right column
      "Win_NW_SE"   Win from left-top corner to right-bottom 
      "Win_NE_SW"   Win from right-top corner to left-bottom 
      "Draw"        All squares filled with no winner
    The first component of the resulting tuple represents the game
    winner, and the second component of the tuple represents the
    winning configuration.  If the status component is "Playing" or
    "Draw", the winner component should be None; for example, the
    tuple ("X", "Win_NE_SE") would be a valid return value, but
    neither ("X", "Draw") nor ("O", "Playing") represents a valid
    result. 
    """
    global NW, N, NE, W, C, E, SW, S, SE, wnr
    if NW == N and N == NE and NW == "X":
        return "X", 'Win_NW_NE'
    elif W == C and C == E and W == "X":
        return "X", "Win_W_E"
    elif SW == S and S == SE and SW == "X":
        return "X", "Win_SW_SE"
    elif NW == W and W == SW and NW == "X":
        return "X", "Win_NW_SW"
    elif N == C and C == S and N == "X":
        return "X", "Win_N_S"
    elif NE == E and E == SE and NE == "X":
        return "X", "Win_NE_SE"
    elif NW == C and C == SE and NW == "X":
        return "X", "Win_NW_SE"
    elif SW == C and C == NE and SW == "X":
        return "X", "Win_NE_SW"
    elif NW == N and N == NE and NW == "O":
        return "O", "Win_NW_NE"
    elif W == C and C == E and W == "O":
        return "O", "Win_W_E"
    elif SW == S and S == SE and SW == "O":
        return "O", "Win_SW_SE"
    elif NW == W and W == SW and NW == "O":
        return "O", "Win_NW_SW"
    elif N == C and C == S and N == "O":
        return "O", "Win_N_S"
    elif NE == E and E == SE and NE == "O":
        return "O", "Win_NE_SE"
    elif NW == C and C == SE and NW == "O":
        return "O", "Win_NW_SE"
    elif SW == C and C == NE and SW == "O":
        return "O", "Win_NE_SW"
    elif NW is not None and N is not None and NE is not None and W is not None and C is not None and E is not None and SW is not None and S is not None and SE is not None:
        return None, "Draw"
    else:
        return None, "Playing"   # Replace with your implementation


def move(location):
    """
    Places the current player's mark at the given location, if possible.
    The caller must pass one of the following strings specifying
    the location:
      "NorthWest"   Top, left square
      "North"       Top, middle square
      "NorthEast"   Top, right square
      "West"        Left, middle square
      "Center"      Center square
      "East"        Right, middle square
      "SouthWest"   Bottom, left square
      "South"       Bottom, middle square
      "SouthEast"   Bottom, right square

    Returns True if the specified location is available (that is,
    the global variable keeping track of that position is None);
    otherwise the function returns False for an illegal move.
    If the current player makes a valid move, the function ensures
    that control passes to the other player; otherwise, the move
    function does not affect the current player.
    """
    global NW, N, NE, W, C, E, SW, S, SE, player
    if location == "NorthWest" and NW is None:
        NW = player
        change_player()
        return True
    elif location == "North" and N is None:
        N = player
        change_player()
        return True
    elif location == "NorthEast" and NE is None:
        NE = player
        change_player()
        return True
    elif location == "West" and W is None:
        W = player
        change_player()
        return True
    elif location == "Center" and C is None:
        C = player
        change_player()
        return True
    elif location == "East" and E is None:
        E = player
        change_player()
        return True
    elif location == "SouthWest" and SW is None:
        SW = player
        change_player()
        return True
    elif location == "South" and S is None:
        S = player
        change_player()
        return True
    elif location == "SouthEast" and SE is None:
        SE = player
        change_player()
        return True
    else:
        return False


def current_player():
    """
    Returns the player whose turn it is to move.  This allows the
    presentation to report whose turn it is.
    Return value is one of either "X" or "O".
    """
    global player
    return player   # Replace with your implementation


def set_player(new_player):
    """
    Sets the current player.  Useful for games that require the
    player to answer a question correctly before a move.  If the
    player answers incorrectly, the turn moves to the opponent.
    Valid values for new_player are "X" or "O"; any other strings
    will not change the current player.
    """
    global player
    if new_player == "X" or new_player == "O":
        player = new_player
    else:
        pass     # Replace with your implementation


def change_player():
    """
    Alternates turns between players.  X becomes O, and O becomes X.
    """
    global player
    if current_player() == "X":
        player = "O"
    elif current_player() == "O":
        player = "X"
    else:
        pass     # Replace with your implementation


def look(location):
    """
    Returns the mark at the given location.  The caller must pass 
    one of the following strings specifying the location:
      "NorthWest"   Top, left square
      "North"       Top, middle square
      "NorthEast"   Top, right square
      "West"        Left, middle square
      "Center"      Center square
      "East"        Right, middle square
      "SouthWest"   Bottom, left square
      "South"       Bottom, middle square
      "SouthEast"   Bottom, right square

    The function's valid return values are None, "X", or "O".
    Returns None if neither player has marked 
    the given location.  The function also returns None if the
    caller passes any string other than one of the location strings
    listed above.
    This function allows the presentation to draw the contents
    of the Tic-Tac-Toe board.
    """
    if location == "NorthWest":
        if NW == "X":
            return "X"
        elif NW == "O":
            return "O"
        else:
            return None 
    elif location == "North":
        if N == "X":
            return "X"
        elif N == "O":
            return "O"
        else:
            return None 
    elif location == "NorthEast":
        if NE == "X":
            return "X"
        elif NE == "O":
            return "O"
        else:
            return None 
    elif location == "West":
        if W == "X":
            return "X"
        elif W == "O":
            return "O"
        else:
            return None 
    elif location == "Center":
        if C == "X":
            return "X"
        elif C == "O":
            return "O"
        else:
            return None 
    elif location == "East":
        if E == "X":
            return "X"
        elif E == "O":
            return "O"
        else:
            return None 
    elif location == "SouthWest":
        if SW == "X":
            return "X"
        elif SW == "O":
            return "O"
        else:
            return None 
    elif location == "South":
        if S == "X":
            return "X"
        elif S == "O":
            return "O"
        else:
            return None
    elif location == "SouthEast":
        if SE == "X":
            return "X"
        elif SE == "O":
            return "O"
        else:
            return None
    else:
        return None   # Replace with your implementation


def initialize_board():
    """
    Make all the board locations empty and set current player to
    "X" (that is, reset the board to the start of a new game)
    """
    global NW, N, NE, W, C, E, SW, S, SE
    NW = None
    N = None
    NE = None
    W = None
    C = None
    E = None
    SW = None
    S = None
    SE = None
    set_player("X")
    
    
    

if __name__ == "__main__":
    pass   #  This module is not meant to be run as a standalone program

