import argparse
from client.manager import TelemostManager
from client.config import BASE_URL, CLIENT_ID, CLIENT_SECRET, OAUTH_TOKEN
from client.shemas import AccessLevel

tm = TelemostManager(
    url=BASE_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    oauth=OAUTH_TOKEN,
)


def create_conference(cohosts):
    if cohosts:
        # фильтруем только те, что содержат домен
        cohosts = [email for email in cohosts if '@' in email]
        response = tm.create_conference(
            waiting_room_level=AccessLevel.PUBLIC,
            cohosts=cohosts
        )
    else:
        response = tm.create_conference(
            waiting_room_level=AccessLevel.PUBLIC
        )
    print(response)


def get_conference_info(conference_id):
    response = tm.get_conference_info(conference_id=conference_id)
    print(response)


def get_conference_cohosts(conference_id):
    response = tm.get_conference_cohosts(conference_id=conference_id)
    print(response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="telemost", description="CLI для Yandex Telemost API")
    subparsers = parser.add_subparsers(dest="command")

    # команда create
    create_parser = subparsers.add_parser("create", help="Создать конференцию")
    create_parser.add_argument("--add", nargs="*", help="Email-адреса соведущих (cohosts)")

    # команда info
    info_parser = subparsers.add_parser("info", help="Получить информацию о конференции")
    info_parser.add_argument("--id", required=True, help="ID конференции")

    # команда cohosts
    cohosts_parser = subparsers.add_parser("cohosts", help="Получить информацию об организаторах встречи")
    cohosts_parser.add_argument("--id", required=True, help="ID конференции")

    args = parser.parse_args()

    if args.command == "create":
        create_conference(args.add)
    elif args.command == "info":
        get_conference_info(args.id)
    elif args.command == "cohosts":
        get_conference_cohosts(args.id)
    else:
        parser.print_help()
