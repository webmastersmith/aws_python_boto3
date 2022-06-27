def whoWins(S):
    #write your Logic here:
    turn = 'lilly'
    lily_score = 0
    carl_score = 0
    was_skipped = False
    
    def change_str(w, i):
        str_arr = list(w)
        str_arr[i] = 'X'
        # return string with changed char.
        return ''.join(str_arr)

    def is_palindrome(w):
        return True if w == w[::-1] else False

    #check if can be a palindrome
    def can_be_palindrome(w):
        # iterate to find if changing O to X will make a palindrome
        for i, c in enumerate(w):
            if c == 'O':
                new_str = change_str(w, i)
                if is_palindrome(new_str):
                    return i
        return -1

    def toggle_turn():
        return 'carl' if turn == 'lilly' else 'lilly'
    
    def every(w):
        for i in w:
            if not i == 'X':
                return False
        return True

    # start iteration. while not 1 and not x
    while not every(S): 
        # skip
        if not is_palindrome(S) and not was_skipped:
            turn = toggle_turn()
            was_skipped = True
            continue
        
        # can't skip
        idx = can_be_palindrome(S)
        # string can become a palindrome
        if idx > -1:
            S = change_str(S, idx)
            was_skipped = False
            if turn == 'carl':
                carl_score += 1
            else:
                lily_score += 1
            turn = toggle_turn()
            continue
        # string cannot become palindrome
        else:
            for i, c in enumerate(S):
                if c == 'O':
                    S = change_str(S, i)
                    was_skipped = False
                    if turn == 'carl':
                        carl_score += 1
                    else:
                        lily_score += 1
                    turn = toggle_turn()
                    break

    # are all chars 'X'
    if lily_score == carl_score:
        return 'TIE'
    else:
        return 'LILY' if carl_score > lily_score else 'CARL'




print(whoWins('OXXOOXXO'))
print(whoWins('OOOOOOOO'))
# Expected Output
# CARL
# CARL
print('-----------------------------')


# 2nd try
# Input

# 10
print(whoWins('OOOXXOOXXOOO'))
print(whoWins('XXOOXXXXOOXX'))
print(whoWins('XOXXOXXOXXOX'))
print(whoWins('OXXXOXOXOXXXO'))
print(whoWins('XOXOXXOXXOXOX'))
print(whoWins('XOOOXXXXOOOX'))
print(whoWins('XOOXXOOXXOOX'))
print(whoWins('OXOOXOOXOOXO'))
print(whoWins('OXXOXOOXOXXO'))
print(whoWins('OOXXOXOXOXXOO'))
# CARL
# CARL
# CARL
# LILY
# LILY
# CARL
# CARL
# CARL
# CARL
# LILY


# 3rd try
# OOXOO
# OXOXO


# Expected Output

# CARL
# LILY





# def ifExists(n,a,b):
    
#     a = ''.join(sorted(list(a)))
#     b = ''.join(sorted(list(b)))
#     print(a)
#     print(b)

#     set_arr = set()
#     for i in range(n):
#         anum = ord(a[i]) - 96
#         bnum = ord(b[i]) - 96
#         set_arr.add(abs(anum - bnum))
#     return "YES" if len(set_arr) == 1 else "NO"




# print(ifExists(3, "afp", 'hrc'))
# # YES
# print(ifExists(9, 'ghodrkvcj', 'ijqftmxel'))
# # YES



# 3
# 9
# ghodrkvcj
# ijqftmxel
# 9
# rdbbeesil
# tfddggekn
# 9
# puiltnkvf
# rwknvpmxh

# YES
# NO
# YES

















# Array Eater
# def eater(N,K,P,A):
#     A.sort()
#     parr = [A.pop() for i in range(P)]
#     karr = [A.pop() for i in range(K)]
       
#     return sum(parr) + sum(A)

# def makeArr(A):
#     return list(map(lambda x: int(x), A.split(' ')))

# # A  = []
# eater(12, 3, 7, makeArr('3 6 0 6 12 16 11 8 7 9 2 10'))
# eater(8, 7, 0, makeArr('15 13 15 6 12 9 1 2'))
# eater(5, 2, 1, makeArr('2 6 4 9 3'))


# String Riddle
    # a = ''.join(sorted(list(a)))
    # b = ''.join(sorted(list(b)))
    # num_set = set()
    # for i in range(n):
    #     a_num = ord(a[i]) - 96
    #     b_num = ord(b[i]) - 96
    #     num_set.add(abs(a_num - b_num))
    # return 'YES' if len(num_set) == 1 else 'NO'
