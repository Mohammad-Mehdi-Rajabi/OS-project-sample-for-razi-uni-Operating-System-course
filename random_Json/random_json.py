import json
import datetime
import random
from pandas import DataFrame





start_id = 32654
_id = start_id
mesg = ' user message'
random_state = ['active', 'inactive']
list_json = list()
list_num = list()
active_list = list()
user_state_dic = {  'UserID': 32654,
                    'state': "active",
                    'ForTime': 120,
                    'logMessage': 'massage'
                }
n = 0
for i in range(10000):
    _id = _id + 1
    n = i 
    user_state_dic['UserID'] = _id
    user_state_dic['state'] = random.choice(random_state)
    user_state_dic['ForTime'] = random.randint(5, 1200)
    user_state_dic['logMessage'] = '{message} date: {D} userID: {user_id}'.format(message = mesg,
                                                     D = datetime.datetime.now(),
                                                     user_id = _id)
    list_num.append(i)
    list_json.append(json.dumps(user_state_dic, indent=4))
    if user_state_dic['state'] == 'active':
        active_list.append(_id)
    
for i in range(0 , len(active_list)):
    ID = random.choice(active_list)
    user_state_dic['UserID'] = ID
    user_state_dic['state'] = 'inactive'
    user_state_dic['ForTime'] = random.randint(5, 1200)
    user_state_dic['logMessage'] = '{message} date: {D} userID: {user_id}'.format(message = mesg,
                                                     D = datetime.datetime.now(),
                                                     user_id = ID)
    
    list_num = n+1
    list_json.append(json.dumps(user_state_dic, indent=4))
random.shuffle(list_json)
df = DataFrame({'num': list_num, 'json': list_json})
df.to_excel('random_json.xlsx', sheet_name='sheet1', index=False)
