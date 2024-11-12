from concurrent.futures import thread
import json
from datetime import datetime

current_dateTime = datetime.now()

users = []

for i in range(10000):
    users.append(
        {
            "user_id": str(i),
            "email": "user" + str(i) + "@gmail.com",
            "timestamp": str(current_dateTime),
        }
    )

# create a large number of users
open("users.json", "w").write(json.dumps(users))

with open("users.txt", "w") as file:
    for user in users:
        file.write(user["user_id"] + "," + user["email"] + "\n")

def get_users_by_chunks(chunk_no, batch_size):
    users = len(users) // 10
    start = chunk_no * batch_size
    end = start + batch_size

    users = users[start:end]
    return users


thread.ThreadPoolExecutor(max_workers=10).map(
    get_users_by_chunks, range(10)
)
