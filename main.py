#!/usr/bin/python

#module
import instaloader
import time
from sys import stderr
import sys
import os

#color
Bl='\033[30m'
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'


try:
#LOGO
    os.system("clear")
    os.system("figlet InstagramV1")
    print("")
    print(f"\n              {Wh}[{Gr}!{Wh}] LOGIN YOUR {Re}INSTAGRAM {Wh}ACCOUNT")
    print("")
    US = input(f"\n  {Wh}[{Gr}*{Wh}] USERNAME {Re}INSTAGRAM {Wh}: {Re}")
    PW = input(f"  {Wh}[{Gr}*{Wh}] PASSWORD {Re}INSTAGRAM {Wh}: {Gr}")

    os.system("clear")

    def osintig(US,PW):

        IG_INSTA = instaloader.Instaloader()
        IG_INSTA.login(US, PW)
        if not IG_INSTA.context.is_logged_in:
            IG_INSTA.context.log(f"\n      {Wh}[{Gr}*{Wh}] {Re}Login failed!, you account wrong")
        else:
            IG_INSTA.context.log(f"\n      {Wh}[{Gr}*{Wh}] {Gr}Login Success!")
        time.sleep(3)

        user_input = input(f"\n       {Wh}[{Gr}*{Wh}] INPUT USERNAME TARGET : {Re}")
        profile = instaloader.Profile.from_username(IG_INSTA.context, user_input)

        print(f"\n       {Wh}============================== {Gr}INFORMATION ACCOUNT {Wh}=============================")
        print(f"\n       {Wh}Username              :{Gr} {profile.username}")
        print(f"       {Wh}Full Name             :{Gr} {profile.full_name}")
        print(f"       {Wh}Id                    :{Gr} {profile.userid}")
        print(f"       {Wh}Bio                   :{Gr} {profile.biography}")
        print(f"       {Wh}Url Profile           :{Gr} {profile.external_url}")
        print(f"       {Wh}Account Private       :{Gr} {profile.is_private}")
        print(f"       {Wh}Account Business      :{Gr} {profile.is_business_account}")
        print(f"       {Wh}Account business type :{Gr} {profile.business_category_name}")
        print(f"       {Wh}Followers             :{Gr} {profile.followers}")
        print(f"       {Wh}Following             :{Gr} {profile.followees}")
        print(f"       {Wh}Total Post            :{Gr} {profile.mediacount}")
        time.sleep(0.3)
        print(f"\n       {Wh}[{Gr}*{Wh}]{Wh} Download profile picture : ")
        profile_pic = profile.profile_pic_url
        print(profile_pic)
        print()
        print(f"       {Wh}[{Gr}*{Wh}]{Wh} Download {Gr}target post : ")
        for post in profile.get_posts():
            IG_INSTA.download_post(post, target=profile.username)
        print()
        print(f"       {Wh}[{Gr}*{Wh}]{Wh} Download {Gr}igtv post : ")
        for post in IG_INSTA.get_feed_posts():
            IG_INSTA.download_post(post, target=profile.username)
        print()
        print(f"       {Wh}[{Gr}*{Wh}]{Wh} Download {Gr}highlights post : ")
        for highlight in IG_INSTA.get_highlights(profile):
            for post in highlight.get_items():
                IG_INSTA.download_storyitem(post, target=profile.username)
        print()

        def animasi():
            for i in range(10):
                sys.stdout.write(f'\r       {Wh}LOADING {Gr}|')
                time.sleep(0.1)
                sys.stdout.write(f'\r       {Wh}LOADING {Gr}/')
                time.sleep(0.1)
                sys.stdout.write(f'\r       {Wh}LOADING {Gr}-')
                time.sleep(0.1)
            sys.stdout.write(f'\r       {Wh}LOADING {Gr}\\')
        animasi()
        print(f"\n       {Wh}[{Gr}*{Wh}]{Wh} Show {Gr}target followers : ")
        followers = profile.get_followers()
        for follower in followers:
            print(f"      {Gr}USERNAME : {Wh}{follower.username} {Gr}| ID : {Wh}{follower.userid}")

        def animasi():
            for i in range(10):
                sys.stdout.write(f'\r       {Wh}LOADING {Gr}|')
                time.sleep(0.1)
                sys.stdout.write(f'\r       {Wh}LOADING {Gr}/')
                time.sleep(0.1)
                sys.stdout.write(f'\r       {Wh}LOADING {Gr}-')
                time.sleep(0.1)
            sys.stdout.write(f'\r       {Wh}LOADING {Gr}\\')
        animasi()

        print(f"\n       {Wh}[{Gr}*{Wh}]{Wh} Show {Gr}target followings : ")
        followees = profile.get_followees()
        for followee in followees:
            print(f"      {Gr}USERNAME : {Wh}{followee.username} {Gr}| ID : {Wh}{followee.userid}")
    osintig(US,PW)
except KeyboardInterrupt:
    print(f" {Wh}[ {Ye}! {Wh}] {Ye}PROGRAM STOPPED...")


