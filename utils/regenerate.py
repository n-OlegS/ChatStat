"""If your 40 000 message export limit ran out, copy your messages from whatsapp web. If done correctly, each
message should start with a [ symbol, followed by the time, then date, then another ] symbol, and finally the user
and message text. The following is an example of a properly-copied message
[8:42 PM, 12/8/2021] user1: This is a properly-copied message
For the main program to work, however, these messages must be converted to standard whatsapp message
format, as seen below
12/9/21, 7:38 PM - user2: This is a standard exported message
To do so, run this script and enter the path to a file with your copied non-standartized messages. Then, enter a path
to a new blank file. The script will standartize the messages and put them in the second file. After that you can paste
them into your main chat history."""

file = open(str(input()), "r")
new_file = open(str(input()), "w")

for line in file.readlines():
    time = line[1:line.find(",")]
    date = line[(line.find(", ") + 2):line.find("]")]
    line = line[line.find("] "):]
    user = line[(line.find("] ") + 2):line.find(":")]
    message = line[line.find(":") + 2:]

    new_line = date + ", " + time + " - " + user + ": " + message

    new_file.write(new_line)
