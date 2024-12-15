import datetime

#----------------------------------------
#sub function
#----------------------------------------
#for debug
def dbgprint(message):
    # date time string
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # print message
    print(f"[{timestamp}] {message}")

