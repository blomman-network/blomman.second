#!/usr/bin/env python
from PyInquirer import prompt
from subprocess import call
from platform import system

questions = [
    dict(
        type="input",
        name="ip",
        message="What is the IP of the machine your are trying to ping?",
    ),
    dict(type="input", name="pings", message="How many times do you want to ping?"),
]


def ping(address, n=1):
    flag = "-n" if "windows" in system().lower() else "-c"
    command = ["ping", flag, n, address] 
    return call(command) == 0


def clear():
    command = "cls" if "windows" in system().lower() else "clear"
    call(command)


def main():
    clear()
    answers = prompt(questions)
    success = ping(answers["ip"], answers["pings"])
    if not success:
        print(f"Had some issues pinging {answers['ip']}")


if __name__ == "__main__":
    main()
