from day15_common import play_game

if __name__ == "__main__":
    input_str = '20,0,1,11,6,3'
    last_turn_num = 30000000

    last_num_spoken = play_game(input_str, last_turn_num)

    print('last_num_spoken', last_num_spoken)