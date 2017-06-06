import argparse
import slackclient


def send(auth, dest_user, message, as_user=False):
    sc = slackclient.SlackClient(auth)
    sc.api_call('chat.postMessage', channel=dest_user, text=message, as_user=as_user)


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--dest-user", dest='user', help='destination slack user')
    group.add_argument("-c", "--dest-channel", dest='channel', help='destination slack channel')
    parser.add_argument("-a", "--auth", dest='auth', help='slack authentication token', required=True)
    parser.add_argument("-m", "--message", dest='message', required=True)
    parser.add_argument("--as-user", dest='as_user', help='send message as user', action='store_true')
    args = parser.parse_args()
    if args.user:
        user = '@'+args.user
    else:
        user = args.channel
    send(args.auth, user, args.message, args.as_user)

if __name__ == '__main__':
    main()
