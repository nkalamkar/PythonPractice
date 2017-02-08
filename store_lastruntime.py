#-------------------------------------------------------------#
#This Script is to get the lastrun time in UTC of the
#Data Replication Task from Informatica Cloud and store
#it in the config table in Oracle database. This time is
#used later by other tasks which are dependent on The data
#brought by this DR so that no data is missed considering the
#timegaps between the $lastruntime variables stored for each
# of the tasks.
#argv[1] : Informatica Task Name , argv[2]: Informatica org
#Name: Nidhi Kalamkar
#Date: 8 FEB 2017
#--------------------------------------------------------------#
import urllib.request as R
import json, cx_oracle, sys, datetime

store_lrt(sys.argv[1], sys.argv[2])

def store_lrt(task_name, org):
    json_response = login(sys.argv[1], sys.argv[2])
    for item in json_response:
        for items in item['entries']:
            # if task name matches and state != 3 (task did not fail with any error)
            if task_name == items['objectName'] and items['state'] != 3:
                print(items['startTimeUtc'])
                start_time_utc = datetime.datetime.strptime(items['startTimeUtc'], '%Y-%m-%d %H:%M:%S.%f')
                conn = cx_oracle.connect('pin/pin@xyz.com/brmdb')
                cur = conn.cursor()
                cur.execute(
                    "update DI_Record_control_t set last_end_time=" + start_time_utc + "where table_name='MASTER_DR")
                cur.close()
                conn.close()
                exit(1)

# Login to Informatica Cloud
def login(task_name, org):
    login__request__url = R.Request('https://app.informaticaondemand.com/ma/api/v2/user/login', data=json.dumps({
        "@type": "login",
        "username": 'nidhi.kalamkar@hughes.com.' + org,
        "password": '*****'
    }).encode('utf-8'), headers={'Content-Type': 'application/json'})
    login__response_str = json.loads((R.urlopen(login__request__url)).read().decode('utf-8'))
    # get the session_id and then get the activity log
    return activity(login__response_str['icSessionId'])


def activity(ic_session_id):
    act__request__url = R.Request('https://app.informaticaondemand.com/saas/api/v2/activity/activityLog?rowLimit=25',
                                  headers={'Accept': 'application/json', 'icSessionId': ic_session_id})
    response_str = json.loads((R.urlopen(act__request__url)).read().decode('utf-8'))
    return response_str


