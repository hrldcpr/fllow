import pprint
import sys

import api
import database


def main(user, path, params):
    db = database.connect()

    with db, db.cursor() as cursor:
        user = database.get_user(cursor, user)

    pprint.pprint(api.get(user, path, **params))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], dict(sys.argv[i].split('=', 1) for i in range(3, len(sys.argv))))
