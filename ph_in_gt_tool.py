import phonenumbers
from phonenumbers.geocoder import description_for_number
from phonenumbers.carrier import name_for_number
from phonenumbers.timezone import time_zones_for_number
import shortcut as st
import time

st.author()
st.tool_starting()

def initial():
    hash = "#"
    for i in range (1):
        print("initializing.........")
        time.sleep(1)
        for j in range (10):
            print(hash,(j+1)*10,"%")
            hash = hash + "#"
            time.sleep(0)

while True:
    print("Enter the Target number with code ")
    target_n = input(">")
    if target_n == "--exit" or target_n == "-E" or target_n == "":
        break
    try:
        parse_n = phonenumbers.parse(target_n)
        host_name = name_for_number(parse_n,"en")
        country_name = description_for_number(parse_n,"en")
        time_zone = time_zones_for_number(parse_n)
        try :
            print(" ")
            print(" ")
            print("Enter <--exit> or <-E> or <>  |  for exiting the tool any time")
            print("Enter <--host> or <-HT>       |  for host name")
            print("Enter <--country_n> or <-CN>  |  for country name")
            print("Enter <--time-z> or <-TZ>     |  for time zone")
            print("Enter <--all> or <-A>         |  for all the above")
            print("Enter <--info>                |  for tool information")
            print("Enter <--help> or <-H>        |  help for using tool")
            print(" ")
            print(" ")
            choice = input(">")
            if choice == "--host" or choice == "-HT":
                print(" ")
                initial()
                print(" ")
                print("Host name :- ",host_name)
                print(" ")
            elif choice == "--country_n" or choice == "-CN" :
                print(" ")
                initial()
                print(" ")
                print("Country name :- ",country_name)
                print(" ")
            elif choice == "--time_z" or choice == "-TZ" :
                print(" ")
                initial()
                print(" ")
                print("Time zone :- ",time_zone)
                prinnt(" ")
            elif choice == "--all" or choice == "-A" :
                hash = "#"
                for i in range (1):
                    print("initilizating.........")
                    time.sleep(4)
                    for j in range (10):
                         print(" ")
                         print(hash,(j+1)*10,"%")
                         hash = hash + "#"
                         time.sleep(1)
                print(" ")
                print("Host name    :- ",host_name)
                print("Country name :- ",country_name)
                print("Time zone    :- ",time_zone)
                print(" ")
            elif choice == "--exit" or choice == "-E" or choice == "":
                break
            print("If you want to continue enter <--conti> or <-C> and to exit <--exit> or <-E>")
            user_choice = input(">")
            if user_choice == "--conti" or user_choice == "-C" :
                continue
            elif user_choice == "--exit" or user_choice == "-E" or user_choice == "":
                break
            else:
                break
            #elif choice == "--info" :
            #    info()
            #elif choice == "help" or "-H":
            #    help()
        except Exception as e :
            print(e,"Parsing error")
        continue
    except Exception as e :
        print("The syntax was invalid :- ",e)
        print("If you want to continue press <--conti> or <-C> and to exit press <--exit> or <-E>")
        user_choice = input(">")
        if user_choice == "--conti" or user_choice == "-C" :
            continue
        elif user_choice == "--exit" or user_choice == "-E" or user_choice == "":
            break
        else:
            break
