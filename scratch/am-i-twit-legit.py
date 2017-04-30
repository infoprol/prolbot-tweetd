
import os
import twitter



def divine_twit_args():
    api_args = { }
    for an in [ 'consumer_key', 'consumer_secret', 'access_token_key', 'access_token_secret' ]:
        api_args[an] = os.getenv('INFOPROL_TWIT_' + an.upper())
    return api_args




def twApi():
    api = twitter.Api(**divine_twit_args())
    
    im_legit = api.VerifyCredentials()
    print(im_legit)
    
    
    
    
if __name__ == '__main__':
    print('sucktown 4ever!')
    
    twapi = twApi()
    
    
    print('yeah yeah that\'s it!')
    