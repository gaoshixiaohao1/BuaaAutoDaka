# coding=utf-8
import requests
import json
from urllib.parse import urlencode
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import logging_loki
from loguru import logger
from config import config


logger.add(logging_loki.LokiHandler(**config["loki_config"]))
logger.add("/log/daka.log")

class CheckBot():
    def __init__(self,username,password,realname,number):
        self.username = username
        self.password = password
        self.realname = realname
        self.number = number
        self.headers = config["user-agent"]
        self.login_data = {
            "username": username, 
            "password": password, 
        }
        identifier={"username":username,"password":password,"realname":realname,"number":number}
        self.submit_data = config["submit_data"]
        self.submit_data["realname"] = self.realname,
        self.submit_data["number"] = self.number
        logger.info("CheckBot init, user is{}".format(str(identifier)))
    
    def check_in(self):
        login_url  = config["login_url"]
        submit_url = config["submit_url"]

        login_r = requests.post(login_url,headers=self.headers,data=self.login_data)
    
        if json.loads(login_r.content.decode())["e"]!=0:
            raise Exception(login_r.content.decode())
        else:
            logger.info("{name} Login success.".format(name=self.realname))
        
        cookies = login_r.cookies.get_dict()
        r = requests.post(submit_url,headers=self.headers,data=self.submit_data,cookies=cookies)

        if r.status_code == 200:
            res_dict = json.loads(r.content.decode())
            if "e" in res_dict:
                if res_dict["e"] == 0:
                    return True
                elif res_dict["m"] == "今天已经填报了":
                    return True
                else:
                    logger.warning(res_dict["m"])
                    return False
        else:
            logger.warning(r.content.decode())
            return False

class BotControl():
    def __init__(self):
        self.bot_list=[]

    def schedule(self):
        for bot in self.bot_list:
            try:
                succ = bot.check_in()
            except:
                logger.error("{} check failed".format(bot.username))
            time.sleep(1)


if __name__ == "__main__":
    logger.info("start")
    bc = BotControl()
    users = config["users"]
    for user_dict in users:
        bc.bot_list.append(CheckBot(**user_dict))
    bc.schedule()
    sched = BlockingScheduler()
    sched.add_job(bc.schedule, "cron", hour="17", minute="10",misfire_grace_time=10)
    sched.start()

    
