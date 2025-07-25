monday_visitors = {"user1", "user2", "user3", "user4", "user5"}
tuesday_visitors = {"user1","user2", "user4", "user6", "user7", "user8"}
wednesday_visitors = {"user1", "user3", "user6", "user9", "user10"}

def unique_visitors_each_day():
    all_unique_visitors = monday_visitors | tuesday_visitors | wednesday_visitors
    print(all_unique_visitors)


def returning_visitors_on_tuesday():
    returning_visitors = monday_visitors & tuesday_visitors
    print(returning_visitors)

def new_visitors_every_day():
    seen_so_far = set()

    monday_new = monday_visitors - seen_so_far
    seen_so_far |= monday_visitors
    print("New visitors on Monday:", monday_new)

    tuesday_new = tuesday_visitors - seen_so_far
    seen_so_far |= tuesday_visitors
    print("New visitors on Tuesday:", tuesday_new)

    wednesday_new = wednesday_visitors - seen_so_far
    seen_so_far |= wednesday_visitors
    print("New visitors on Wednesday:", wednesday_new)

def find_loyal_visiors():
    loyal_visitors=monday_visitors & tuesday_visitors & wednesday_visitors
    for visitor in loyal_visitors:
        print(visitor)

def visitor_overlap_analysis():
    # Daily Visitor Overlap Analysis
    # Compare and print overlaps between each pair of days (e.g., Monday-Tuesday, Tuesday-Wednesday, etc.).
    monday_tuesday = monday_visitors & tuesday_visitors
    tuesday_wednesday = tuesday_visitors & wednesday_visitors
    monday_wednesday = monday_visitors & wednesday_visitors

    print("Visitors on both Monday and Tuesday:", monday_tuesday)
    print("Visitors on both Tuesday and Wednesday:", tuesday_wednesday)
    print("Visitors on both Monday and Wednesday:", monday_wednesday) 
    



if __name__ == "__main__":
    unique_visitors_each_day()
    returning_visitors_on_tuesday()
    new_visitors_every_day()
    find_loyal_visiors()
    visitor_overlap_analysis()