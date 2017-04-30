
import os
import json
import twitter



def divine_twit_args():
    api_args = { }
    for an in [ 'consumer_key', 'consumer_secret', 'access_token_key', 'access_token_secret' ]:
        api_args[an] = os.getenv('INFOPROL_TWIT_' + an.upper())
    return api_args




def twApi():
    api = twitter.Api(**divine_twit_args())
    
    #im_legit = api.VerifyCredentials()
    print(im_legit)
    
    return api
    
    
    
    
def keep_going(tweet):
    hh, user = { }, 'human'
    try:
        hh = tweet['entities']['hashtags']    
        user = tweet['user']['screen_name']
    except KeyError:
        pass
        
    hh = [ h['text'] for h in hh if 'text' in h and h['text'] ]
    hh = [ h for h in hh if type(h) is str ]
    hh = [ h.lower() for h in hh ]
    
    if 'sleep' not in hh:
        return (True, None)
        
    return (False, 'will i dream, @' + user + '? [...going to sleep...]')
    
    
    
    
    
    
if __name__ == '__main__':
    print('sucktown 4ever!')
    
    LANGUAGES = ['en']
    USERS = ['@infoprol', '@twitter', '@twitterapi', '@support']
    
    
    twitApi = twitter.Api(**divine_twit_args())
    
    k = 0
    
    with open('output.txt', 'a') as f:
        print('ok, here we go!')
        for ln in twitApi.GetStreamFilter(track=USERS[:1], languages=LANGUAGES):
            print(ln)
            f.write(json.dumps(ln))
            #f.write(type(ln) is str and ln or json.dumps(ln))
            f.write('\n')
            
            do_keep_going, goodbye_msg = keep_going(ln)
            
            if not do_keep_going:
                print('stopping with goodbye:\n' + str(goodbye_msg))
                twitApi.PostUpdate(goodbye_msg)
                break
            
            k += 1
            if k > 1: break
            if k % 1 == 0: print('line ' + str(k))
        
    
    print('yeah yeah that\'s it!')
    