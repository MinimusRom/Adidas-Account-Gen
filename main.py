from account import adidas
import colorama, threading
from classes.logger import logger
colorama.init()
log = logger().log

log("--------------------------", "gray")
log("Account Gen", "yellow")
log("Developed by: Euphoria", "yellow")
log("Twitter: @Euph", "yellow")
log("--------------------------", "gray")


def main():
    AD = adidas()
    AD.run()


threads = []
if __name__ == "__main__":
    choice = input("How many?: ")
    for i in range(int(choice)):
        t = threading.Thread(target=main,)
        threads.append(t)
        t.start()
    t.join()
    with open("gen.txt") as f:
        accts = f.read().splitlines()
        print("Accounts Created " + str(len(accts)))