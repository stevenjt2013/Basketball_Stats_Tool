if __name__ == "__main__":

  from constants import TEAMS as Teams, PLAYERS as Players


    
def clean_data(old_list):
    clean_list = []
    for player in old_list:
      clean = {}
      clean["name"] = player["name"]
      clean["guardians"] = player["guardians"]
      if player["experience"] == "YES":
          clean["experience"] = True
      if player["experience"] == "NO":
          clean["experience"] = False
      clean["height"] = int(player["height"][:2])
      clean_list.append(clean)
    return clean_list
    


def balanced_teams(players):
  Panthers = []
  Bandits = []
  Warriors = []
  for index, player in enumerate(players, start=1):
    if index % 3 == 0:
      Panthers.append(player)
    elif index % 3 == 2:
      Bandits.append(player)
    else:
      Warriors.append(player)
  return Panthers, Bandits, Warriors

clean_players = clean_data(Players)
Panthers, Bandits, Warriors = balanced_teams(clean_players)

print("BASKETBALL TEAM STATS TOOL \n")
print("----MENU---\n")
print("Here are your choices:\n A) Display Team Stats\n B) Quit")

first_option = input("\nEner an option: ").upper()

if first_option == 'A':
  print("\nA) Pathers \nB) Bandits \nC) Warriors")
  second_option = input("\nEnter an option: ").upper()
  if second_option == 'A':
    print("\n Team: Panthers Stats \n-------------------- \nTotal players: {}".format(len(Panthers)))
    print("Players on team:")
    print(' ' + ', '.join(player["name"] for player in Panthers))
  elif second_option == 'B':
    print("\n Team: Bandits Stats \n-------------------- \nTotal players: {}".format(len(Bandits)))
    print("Players on team:")
    print(' ' + ', '.join(player["name"] for player in Bandits))
  else:
    print("\n Team: Warriors Stats \n-------------------- \nTotal players: {}".format(len(Warriors)))
    print("Players on team:")
    print(' ' + ', '.join(player["name"] for player in Warriors))
    