# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import random
main_num_list = [31,20,11,17,46,28,10,2,35,39,24,38,48,29,25,4,14,42,72,65,59,71,61,66,75,69,57,74,63,70,73,60,68,67,64,58]

mega_num_list = [3,6,12,10,4,14,7,2,5,9,13,21,1,11,22,15,8,20,8,5,16,3,12,21,15,23,13,18,1,17,24,6,25,2,7,4]

main_num_list = list(set(main_num_list))
mega_num_list = list(set(mega_num_list))



final_choice = []
main_choice = []
mega_choice = []
all_time = 0
while all_time < 5:
    times = 0
    while times < 88:
        main_choice = random.choices(population=main_num_list, k=5)
        # print(main_choice)
        
        mega_choice = random.choices(population=mega_num_list, k=1)
        # print(mega_choice)
        
        final_choice = sorted(main_choice) + mega_choice
        
        if len(set(final_choice)) == 6:
            times += 1
    
    all_time += 1
    print(final_choice)






