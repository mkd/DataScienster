# Chatper 1.1: Finding key connectors

"""
List of users, each represented by a
dict that contains for each user his or her id (which is a number) and name
"""
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]


"""
the “friendship” data, represented as a list of pairs of IDs:
"""
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# adding a list of friends to each user
for user in users:
    user["friends"] = []

# populate the list of friends for each user
for i, j in friendships:
    """
    this works because a friendship is a reciprocal relationship, so users[i]
    should be added to users[j]'s friends list, and viceversa, users[j]
    should be added to users[i]'s friends list.
    """
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


# now we can ask questions to the data
# For example: total number of connections of a person
def getNumberOfFriends(user):
    return(len(user["friends"]))

totalConnections = sum(getNumberOfFriends(user) for user in users)

totalUsers = len(users)
avgConnections = totalConnections / totalUsers


"""
It’s also easy to find the most connected people—they’re the people who have the
largest number of friends. Since there aren’t very many users, we can sort them
from “most friends” to “least friends”:
"""
# create a list (user_id, number_of_friends)
numFriendsById = [(user["id"], getNumberOfFriends(user)) for user in users]
sortedList= sorted(numFriendsById, key=lambda user_tuple : user_tuple[1], reverse=True)
for user in sortedList:
    print(f'{users[user[0]]["name"]}, {user[1]}')
