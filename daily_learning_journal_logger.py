import datetime

entry=input('What did you learn today? ').strip()
rating=int(input('What was your productivity? ').strip())

now=datetime.datetime.now()
date_str=now.strftime("%Y-%m-%d-%I:%M:%p")


if rating:
    journal_entry=f'\n I learned {entry} today at {date_str} with Productivity Rating:{rating}\n'
else:
    journal_entry=f'\n I learned {entry} today at {date_str} \n'
journal_entry+='\n'+'-'* 50

with open('learning_journal.txt','a',encoding='utf-8') as f:
    f.write(journal_entry)
print(f'\n Your journal entry has been saved learning_journal.txt')