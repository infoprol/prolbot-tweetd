
import sys
import os
import json
from slackclient import SlackClient



BOT_NAME = 'prolbot'




def divine_slack_args():
    toke = os.environ.get('INFOPROL_SLACK_PROLBOT_TOKEN')
    return [toke]
    
    
    
    
    
def get_id_from_name(name, slack_client=SlackClient(*divine_slack_args())):
    list_users = slack_client.api_call('users.list')
    #print(json.dumps(list_users))
    if not list_users.get('ok'):
        return Exception('users.list NOT ok!')
        
    users = list_users.get('members')
    for user in users:
        print('name: ' + user['name'])
        print('id: ' + user['id'])
        if 'name' in user and user['name'] == name:
            return 'id' in user and user['id'] or None
            
    return None
    
    
    
if __name__ == '__main__':
    slack_args = divine_slack_args()
    slack_client = SlackClient(*slack_args)
    
    bot_id = get_id_from_name(BOT_NAME, slack_client)
    
    
    print('bot_id: ' + str(bot_id))
    
