if __name__ == "__main__":

  from constants import TEAMS as Teams, PLAYERS as Players
  
  
  team1, team2, team3 = Teams.pop(), Teams.pop(), Teams.pop()
  
      
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
    team1_players = []
    team2_players = []
    team3_players = []
    for index, player in enumerate(players, start=1):
      if index % 3 == 0:
        team1_players.append(player)
      elif index % 3 == 2:
        team2_players.append(player)
      else:
        team3_players.append(player)
    return team1_players, team2_players, team3_players
  
  clean_players = clean_data(Players)
  team1_players, team2_players, team3_players = balanced_teams(clean_players)
  
  print("BASKETBALL TEAM STATS TOOL \n")
  print("----MENU---\n")
  print("Here are your choices:\n A) Display Team Stats\n B) Quit")
  
  first_option = input("\nEner an option: ").upper()
  
  if first_option == 'A':
    print("\nA) {} \nB) {} \nC) {}".format(team1, team2, team3))
    second_option = input("\nEnter an option: ").upper()
    if second_option == 'A':
      print("\n Team: {} Stats \n-------------------- \nTotal players: {}".format(team1, len(team1_players)))
      print("Players on team:")
      print(' ' + ', '.join(player["name"] for player in team1_players))
    elif second_option == 'B':
      print("\n Team: {} Stats \n-------------------- \nTotal players: {}".format(team2, len(team2_players)))
      print("Players on team:")
      print(' ' + ', '.join(player["name"] for player in team2_players))
    else:
      print("\n Team: {} Stats \n-------------------- \nTotal players: {}".format(team3, len(team3_players)))
      print("Players on team:")
      print(' ' + ', '.join(player["name"] for player in team3_players))
    
