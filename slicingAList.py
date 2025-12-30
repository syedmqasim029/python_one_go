# players = ['BABAR','STARC','de COCK','MILLER','PORAN','KLASSEN','JENSON','PAT CUMMINS']
# print(players[:-2]) # till -2 but in list the last index is exlusive so prints till -2-1 = -3

# for pl in players[:3]:
#     print(pl)


# '''Slicing Task'''
# players = ['BABAR','de COCK','MILLER','PORAN','KLASSEN','JENSON','PAT CUMMINS','STARC']

# for i in players[:4]:
#     print(f"{i} you are in first four players")
# if len(players)%2==0:
#     print(f"{players[(len(players)//2)-1:(len(players)//2)+1]}, you are the middle one")
# else:
#     print(f"{players[len(players)//2]}, you are the middle one")
# for i in players[len(players)//2+1:]:
#     print(f"{i} you the the lower order")