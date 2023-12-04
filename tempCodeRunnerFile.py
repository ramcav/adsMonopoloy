  # Roll the dice
                self.roll_dice(player, board)
                if player.has_lost():
                    party.players_lost.append(player)
                    print(f"{player.name} lost!")
                    if len(party.players_lost) == party.nb_of_player - 1:
                        winner = ne