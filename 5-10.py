current_users = ['admin', '1234', 'user', 'username', 'potato']
new_users = ['tomato', '1234', 'pass', 'chilli', 'potato']
for i in new_users:
    if i.lower() in current_users:
        print ('You may proceed')
    else:
        print ('Enter a new username!')
