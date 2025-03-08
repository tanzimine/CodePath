# def lineup(artists, set_times):
#     final_lst = dict(zip(artists, set_times))
#     return final_lst

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))


# PROBLEM 2
# def get_artist_info(artist, festival_schedule):
#     if artist in festival_schedule:
#         found = festival_schedule[artist]
        
#         return found

#     not_found = {"message": "Artist not found"}
#     return not_found

# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  



# PROBLEM 3
# def total_sales(ticket_sales):
#     total = 0

#     for key in ticket_sales:
#         total+=ticket_sales[key]

#     return total

# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))


# PROBLEM 4
# def identify_conflicts(venue1_schedule, venue2_schedule):

#     conflict = {}

#     for artist in venue1_schedule:
#         if artist in venue2_schedule and venue1_schedule[artist] == venue2_schedule[artist]:
#             conflict[artist] = venue1_schedule[artist]

#     return conflict

# venue1_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "8:00 PM",
#     "HARDY": "7:00 PM",
#     "Bruce Springsteen": "6:00 PM"
# }

# venue2_schedule = {
#     "Stromae": "9:00 PM",
#     "Janelle Monáe": "10:30 PM",
#     "HARDY": "7:00 PM",
#     "Wizkid": "6:00 PM"
# }

# print(identify_conflicts(venue1_schedule, venue2_schedule))


# IMPORTANTTTTT: NEW CONECPT -> COunter()   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # PROBLEM 5
# from collections import Counter
# def best_set(votes):

#     vote_counts = Counter(votes.values())

#     max_votes = max(vote_counts.values())

#     for key, value in vote_counts.items():
#         if value == max_votes:
#             return key
        

# votes1 = {
#     1234: "Yo-Yo Ma", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "Yo-Yo Ma",
#     1239: "SZA"
# }

# votes2 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA"
# }

# print(best_set(votes1))
# print(best_set(votes2))


# PROBLEM 6

# def max_audience_performances(audiences):

#     # max_audience = max(audiences)

#     # count_max = audiences.count(max_audience)

#     # result = max_audience*count_max

#     # return result

#     # ---------------

#     audience_count = {}  
    
#     # Count occurrences of each audience number
#     for audience in audiences:
#         if audience in audience_count:
#             audience_count[audience] += 1
#         else:
#             audience_count[audience] = 1
    
#     max_audience = max(audience_count.keys()) 

#     print(audience_count)
    
    
#     total_audience = max_audience * audience_count[max_audience]  

#     return total_audience

    


# audiences1 = [100, 200, 200, 150, 100, 250]
# audiences2 = [120, 180, 220, 150, 220]

# print(max_audience_performances(audiences1))
# print(max_audience_performances(audiences2))



# PROBLEM 12
# def sort_performers(performer_names, performance_times):

#     combined = list(zip(performance_times, performer_names))

#     combined.sort(reverse=True)

#     result = []
#     for pair in combined:
#         result.append(pair[1])
#     return result


    

# performer_names1 = ["Mary", "John", "Emma"]
# performance_times1 = [180, 165, 170]

# performer_names2 = ["Alice", "Bob", "Bob"]
# performance_times2 = [155, 185, 150]

# print(sort_performers(performer_names1, performance_times1)) 
# print(sort_performers(performer_names2, performance_times2))