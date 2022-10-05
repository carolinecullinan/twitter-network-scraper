from random import randint
import time

#-------------------------------------------------------
def load_first_degree_followers(user, f, ego_follows):

    #ids = []
    twint.run.Followers(user)
    # save them in a list
    ids = twint.output.users_list
    
    #ids.extend(followers)
    for i in ids:
        f.write(str(i.followers) + "  " + str(i.username)  + "  " + str(ego_follows) + "  " +  str(c.Username) + "\n")
        time.sleep(randint(5,30))

    print('Done with the 1st degree followers')

    return ids
#-------------------------------------------------------
def load_first_degree_friends(user, f, ego_follows):

    #ids = []
    twint.run.Following(user)
    # save them in a list
    ids2 = twint.output.users_list
        
        
    #ids.extend(followers)
    for i in ids2:
        f.write(str(ego_follows) + "  " + str(c.Username) + "  " + str(i.followers) + "  " + str(i.username) + "\n")
        time.sleep(randint(5,30))

    print('Done with the 1st degree friends')

    return ids2
#---------------------------------------------------------
def load_second_degree_followers(users, f):

    #ids = []
    for user in users:
        try:
            #ids = []
            c = twint.Config()
            c.Username = user.username
            c.Store_object = True
            c.User_full = True
            twint.run.Followers(c)
            ids = twint.output.users_list

            for i in ids:
                f.write(str(i.followers) + "  " + str(i.username) + "  " + str(user.followers) + "  " + str(user.username) +  "\n")
                time.sleep(randint(5,30))
        except Exception:
            pass
            
    print('Done with the 2nd degree followers')

#---------------------------------------------------------
def load_second_degree_friends(users, f):

    #ids = []
    for user in users:
        try:
            c = twint.Config()
            c.Username = user.username
            c.Store_object = True
            c.User_full = True
            twint.run.Following(c)
            ids = twint.output.users_list

            for i in ids:
                f.write(str(user.followers) + "  " + str(user.username) + "  " + str(i.followers) + "  " + str(i.username) + "\n")
                time.sleep(randint(5,30))
        except Exception:
            pass

    print('Done with the 2nd degree friends')
    
    return ids
#---------------------------------------------------------
import twint

c = twint.Config()
c.Username = "username" #Username here
c.Store_object = True
c.User_full = True

#Number of followers of primary source account, # here , no ""
ego_follows = ""


f  = open(c.Username +'-ego-network.txt', 'w')

print('Retrieving user data...')

first_degree_followers = load_first_degree_followers(c, f, ego_follows)

twint.output.users_list = []


first_degree_friends = load_first_degree_friends(c, f, ego_follows)

twint.output.users_list = []


load_second_degree_followers(first_degree_followers, f)

twint.output.users_list = []


load_second_degree_friends(first_degree_friends, f)
       
f.close()
print('Ego network file is ready...')
