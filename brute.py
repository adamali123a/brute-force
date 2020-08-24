import requests
import os
os.system("clear")

j = r"""
 __  __
|  \/  | ___  ___  ___ _____      __
| |\/| |/ _ \/ __|/ __/ _ \ \ /\ / /
| |  | | (_) \__ \ (_| (_) \ V  V /
|_|  |_|\___/|___/\___\___/ \_/\_/
"""
print("\033[0;33m",j)
print("script by Moscow\n")

a = str(input("Enter here target:  ")+"/")
e = ["login.php","login2.html","login3.php","admin/index.php","admin/","admin1/",
     "adminstrartor/","admin3/","administarato/","adminlogin/","webadmin/",
     "websiteadmin/","bb-admin/","adminstratorlogin.php/","admin-area/",
     "admin-area/admin.php","admin/cp.php/","admin/home.php/","bb-admin/login.php",
     "admin/cpanel.php","bb-admin/login.php","admin5/","admin-area/login.php","admin/acount.php",
     "admin/admin.php","admin/controlpanel.php","admin.php","admincp/index.php","admincontrolepanel/index.php",
     "pages/admin/index.php","admin-login.php","admin/admin_login.php","admin-login.php",
     "admin/admin-login.php","admin/index.html","admin/login.html","modelsearch/login.php",
     "moderator/login.php","admin/adminLogin.html","rcjakar/admin/login.php","adminarea/index.html",
     "webadmin.php","webadmin/admin.php","admin/cp.html","adminpanel.php","moderator.html",
     "admin/adminstrator.php","adminstrator/admin.php","adminloginuser.php","user/index.php","adminuselogin/index.php",
     "user/index.php","adminstartologin.php"]
for t in e:
    try:
        e = a + t
        o = requests.get(e)
        if o.ok == True:
            print("\033[0;32m","\n\n\n==>   {}\n\n\n".format(e))
        elif o.ok != True:
            print("\033[0;31m","CPanel Not Found")
    except:
        print("the target error")
