import argparse
import ConfigParser
import slackclient
import os

def send(auth, dest_user, message, as_user=False):
    sc = slackclient.SlackClient(auth)
    sc.api_call("chat.postMessage", channel=dest_user, text=message, as_user=as_user)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--store", dest="store", help="store defaults", action="store_true")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-u", "--dest-user", dest="user", help="destination slack user")
    group.add_argument("-c", "--dest-channel", dest="channel", help="destination slack channel")
    parser.add_argument("-a", "--auth", dest="auth", help="slack authentication token")
    parser.add_argument("-m", "--message", dest="message")
    parser.add_argument("--as-user", dest="as_user", help="send message as user", action="store_true")
    args = parser.parse_args()
    if args.store:
        Config = ConfigParser.ConfigParser()
        Config.add_section("settings")
        if args.auth:
            Config.set("settings", "auth", args.auth)
        if args.user:
            Config.set("settings", "user", "@"+args.user)
        if args.channel:
            Config.set("settings", "user", args.channel)
        if args.message:
            Config.set("settings", "message", args.message)
        if args.as_user:
            Config.set("settings", "as_user", args.as_user)
        Config.write(open(os.path.expanduser("~/.fastslack"), "w+"))
        print "fastslack defaults stored"
        return

    auth, user, as_user, message = "", "", False, ""
    Config = ConfigParser.ConfigParser()
    Config.read(os.path.expanduser("~/.fastslack"))
    if Config.has_section("settings"):
        if Config.has_option("settings", "auth"):
            auth = Config.get("settings", "auth")
        if Config.has_option("settings", "user"):
            user = Config.get("settings", "user")
        if Config.has_option("settings", "as_user"):
            as_user = Config.get("settings", "as_user")
        if Config.has_option("settings", "message"):
            message = Config.get("settings", "message")

    parser = argparse.ArgumentParser("fastslack")
    group = parser.add_mutually_exclusive_group(required=(not user))
    group.add_argument("-u", "--dest-user", dest="user", help="destination slack user")
    group.add_argument("-c", "--dest-channel", dest="channel", help="destination slack channel")
    parser.add_argument("-a", "--auth", dest="auth", help="slack authentication token", required=(not auth))
    parser.add_argument("-m", "--message", dest="message", required=(not message))
    parser.add_argument("--as-user", dest="as_user", help="send message as user", action="store_true")
    args = parser.parse_args()

    if args.user:
        user = "@"+args.user
    if args.channel:
        user = args.channel
    if args.auth:
        auth = args.auth
    if args.as_user:
        as_user = args.as_user
    if args.message:
        message = args.message
    send(auth, user, message, as_user)

if __name__ == "__main__":
    main()
