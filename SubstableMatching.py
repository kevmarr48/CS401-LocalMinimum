"""
Grad Student:
  - Kevin Marroquin (UIN 675558501)
"""

def SubstableMatching(rider_preferences, horse_preferences, rider_unacceptables, horse_unacceptables):
  """
    Returns a substable matching for the given n riders and n horses, if one exists (None otherwise)
    The matching should be a dict with horses as keys, and their matches as values (for any paired horses)

    Args:
      rider_preferences: a dictionary whose keys are riders and whose values are ordered lists 
                         of the rider's preferred horses (from most to least preferred)
      horse_preferences: a dictionary whose keys are horses and whose values are ordered lists 
                         of the horse's preferred riders (from most to least preferred)
      rider_unacceptable: a dictionary whose keys are riders and whose values are unordered sets 
                          of horses that rider deems unacceptable to be matched with 
      horse_unacceptable: a dictionary whose keys are horses and whose values are unordered sets 
                          of the riders that horse deems unaceptable to be matched with                  
  """
  #rank lookup for each horse
  horse_ranking = {}

  for horse in horse_preferences:
    horse_ranking[horse] = {}

    rider_rank = 0

    for rider in horse_preferences[horse]:
      horse_ranking[horse][rider] = rider_rank
      rider_rank += 1


  #making a new clean list where every horse is removed from the riders 
  #preferences unless the rider and the horse find each other acceptable
  rider_list = {}

  for rider in rider_preferences:
    clean_rider_list = []

    for horse in rider_preferences[rider]:
      if horse in rider_unacceptables.get(rider, set()):
        continue
      if rider in horse_unacceptables.get(horse, set()):
        continue
      if rider not in horse_ranking.get(horse, set()):
        continue

      clean_rider_list.append(horse)

    rider_list[rider] = clean_rider_list


  #Gale-Shapley preference setup
  matches = {}

  next_preference = {}

  for rider in rider_list:
    next_preference[rider] = 0

  available_riders = []

  for rider in rider_list:
    available_riders.append(rider)


  #Running Gale-Shapley
  while len(available_riders) > 0:

    rider_suitor = available_riders.pop()

    while next_preference[rider_suitor] < len(rider_list[rider_suitor]):
      horse = rider_list[rider_suitor][next_preference[rider_suitor]]

      next_preference[rider_suitor] += 1

      if horse not in matches:
        matches[horse] = rider_suitor
        break

      # Mr.steal your horse
      current_rider = matches[horse]

      if horse_ranking[horse][rider_suitor] < horse_ranking[horse][current_rider]:
        matches[horse] = rider_suitor

        available_riders.append(current_rider)
        break

  #If there are no matches returns none
  if len(matches) == 0:
    return None


  #Returns horse: rider matches
  return matches

   

if __name__ == "__main__":
  # sample input with 3 riders and 3 horses
  rider_prefs = {1: [1], 2: [2, 1, 3], 3: [1, 3]}
  horse_prefs = {1: [3,2,1], 2: [2, 3], 3: [2, 3]}

  rider_unacceptable = {1: {2, 3}, 2: set(), 3: {2}}
  horse_unacceptable = {1: set(), 2: {1}, 3: {1}}

  # {1: 3, 2: 2} would be a possible substable match for these riders and horses
  # horse 1 + rider 3, horse 2 + rider 2
  matches = SubstableMatching(rider_prefs, horse_prefs, rider_unacceptable, horse_unacceptable)
  # print(matches)