import pprint
import shioaji as sj
import os
from dotenv import load_dotenv #從dotenv模組中匯入load_dotenv這個function

load_dotenv() #讀取設定檔中的內容至環境變數

api = sj.Shioaji(simulation=True)# 初始化時，simulation設為True，代表要使用模擬環境

api.login(api_key=os.getenv('API_Key'),
          secret_key=os.getenv('Secret_Key')
          )
accounts = api.list_accounts()
pprint.pp(accounts)

result = api.activate_ca(
    ca_path=r'E:/桌面/憑證/ekey/551/A127016469/S/Sinopac.pfx',
    ca_passwd="A127016469",
    person_id="A127016469",
)

print(f'Active CA : {result}')