import re # type: ignore
def extract_number(text):
    pattern=r'\b\d{1,2} \d{10}\b'
    match=re.search(pattern,text)
    if match:
        return match.group()
    else:
        return False
def extract_time(text):
    pattern=r'\b\d{1,2}:\d{2}\b'
    match=re.search(pattern,text)
    if match:
        return match.group()
    else:
        return False
print('Welcom to Dialer bot (to exit say  "Exit")')
while True:
    usrinp=input('Enter the number to dial ')
    if 'exit' in usrinp.lower():
        print('See you again :)')
        break
    dial=extract_number(usrinp)
    if dial:
        while True:
            usrinp2=input('Enter the time to be dialed at in 24 hrs system (ex: "20:24")')
            time=extract_time(usrinp2)
            if 'exit' in usrinp2.lower():
                print('See you again :)')
                exit=True
                break
            if time:
                print(f'Ok dialing {dial} at {time} ...')
                break
            else:
                print("Error in time")
    else:
        print('Error in number')
    if exit==True:
        break
