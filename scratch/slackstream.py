

import json
from slackclient import SlackClient
import os
import time


SLACK_BOT_TOKEN = os.environ['INFOPROL_SLACK_PROLBOT_TOKEN']
BOT_ID = os.environ['INFOPROL_SLACK_PROLBOT_ID']
READ_WS_DELAY = 1 # 1 sec: slack RTM is self-described "event firehose"

    


def parse_evts(msg):
    
    evt = {
        "typ": "slack:api:call",
        "api_call": "chat.postMessage",
        "kwds": {
            "channel": "channel" in msg and msg["channel"] or "write_a_slackbot",
            "text": "text" in msg and msg["text"] or "say something!\n\n```" + json.dumps(msg) + "```",
            "as_user": True
        }
    }
    
    
    json.dumps(msg)
    
    return [evt]  #json.dumps(msg)


def slackstream(slack_client):
    
    if not slack_client.rtm_connect(): return
    
    print('rtm_connect successful!')
    
    while True:
        time.sleep(READ_WS_DELAY)
        
        msgs = slack_client.rtm_read()
        
        print(json.dumps(msgs))
         
        #NOTE that we are allowing for a given msg to parse out to 0,1, or more evts...
        #for evt in [ for evt in [ evts for evts in [ parse_evts(msg) for msg in msgs ] ] ]:
        for evts in [ parse_evts(msg) for msg in msgs ]:
            print('got ' + str(len(evts)) + ' events!')
            for evt in evts:
                yield evt
                
        
        #break
        
        

if __name__ == '__main__':
    
    print('ok, here we go!')
    
    slack_client = SlackClient(SLACK_BOT_TOKEN)
    
    for evt in slackstream(slack_client):
        print('got an event!')
        print(json.dumps(evt))
        
        slack_client.api_call(evt['api_call'], **evt['kwds'])
        print('called ' + evt['api_call'])
        
        
        
        
        
    print("and we're done.")