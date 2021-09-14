import os
import time

# 把这里改成你的Request Payload中的内容!!!
request_data = '''
    {"xkcscode7":"0","kkdwbh":"208102","xkfl":[],"tzdlb_name":"正常","xkfs_name":"4","kkdw_name":"理学院-物理学系","skls_name":{"jczy010id":"21019502","jczy013id":"2021-2022-1","queryFlag":"2","kkgl004id":"00410197379","name":["夏天龙"]},"jczy007ids":null,"jczy003id":"208102","kcbh":"21019502","ktmc_name":"人文物理通识与探索性实验03班","kcxz_name":null,"kcmc_name":"人文物理通识与探索性实验","kcxz":null,"xq_name":"中关村校区中关村校区","id":"00410197379","jczy013id":"2021-2022-1","zxs":"36","zxf":"2","kcdl":"2","kclb":"5","khfs":"1","kkgl00401id":null,"szkclb":null,"falb":"1","xkfsid":"22","xkgl017id":"c13464110000WH","xkgl019id":"c13464db0000WH","isTqxd":"0","xkzy":"","trz":"","tzdlb":"01","jczy010id":"21019502","skfscode":null,"skfs_name":null,"sksj":[{"zc":"1-4,6-12","zcmx":"1,2,3,4,6,7,8,9,10,11,12","kssj":1800,"jssj":2025,"xq":"2","jc":"111213","name":"星期二 11-13节 1-4,6-12周"},{"zc":"3","zcmx":"3","kssj":1800,"jssj":2025,"xq":"7","jc":"111213","name":"星期日 11-13节 3周"}],"xkcscode1":"1","xkcscode23":"0","sfglymkccode":false,"sfglctkccode":false,"kclbMapper":"5","xklbbh":"16","bllsZyId":"10231860","isSxrz":"","language":"zh"}
'''
# 把这里改成你的COOKIE!!!
cookie_data = '''
    access_token=fohoTM62REmblD3ZioOabg; SESSION=bfc8bfc3-ee24-4377-8d5c-26e7f9f46314; authcode=2020202020; token=
'''
# 把这里改成你的TOKEN!!!
token_data = '''
    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2MiOiIyMDIwMjAxNDIxIiwiZXhwIjoxajMxNjU4NDI5LCJpYXQiOjE2MzE2MTUyMjksInNpZCI6ImJmYzhiZmMzLWVlZjYtNDM3Ny04ZDVjLTI2ZTdgOWY0NjMxNCJ9.4uDIO7O3Taa4FFdQJs6hKvYEzePmudwCq0MnNgvIDIo
'''
request_data = request_data.strip()
cookie_data = cookie_data.strip()
token_data = token_data.strip()

def fuck_xk():
    p_sh = '''
    curl --location --request POST 'http://jw.ruc.edu.cn/resService/jwxtpt/v1/xsd/stuCourseCenterController/saveStuXkByRmdx?resourceCode=XSMH030301&apiCode=jw.xsd.courseCenter.controller.StuCourseCenterController.saveStuXkByRmdx' \
    -w '\n' \
    --header 'userRoleCode: student' \
    --header 'locale: zh_CN' \
    --header 'User-Agent: Mozilla/5.0 (Macintosh; Intgitel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36' \
    --header 'Simulated-By;' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json, text/plain, */*' \
    --header 'X-Requested-With: XMLHttpRequest' \
    --header 'userAgent;' \
    --header 'app: PCWEB' \
    --header 'TOKEN: {}' \
    --data-raw '{}' \
    --header 'Cookie: {}' 
    '''.format(token_data, request_data, cookie_data)
    os.system(p_sh)

def main():
    while True:
        fuck_xk()
        time.sleep(5)

if __name__ == "__main__":
    main()
