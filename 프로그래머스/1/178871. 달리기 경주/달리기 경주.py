def solution(players, callings):
    index_dict = {player: idx for idx, player in enumerate(players)}

    for name in callings:
        current_idx = index_dict[name]
        
        if current_idx > 0:
            previous_player = players[current_idx - 1]
            players[current_idx], players[current_idx - 1] = players[current_idx - 1], players[current_idx]
            
            index_dict[name] -= 1
            index_dict[previous_player] += 1

    return players
