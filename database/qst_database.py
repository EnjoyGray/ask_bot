import json
from random import randint


def qst_inv200():
    with open(r"database\I_never.json", "r", encoding='utf-8') as json_file:
        i_nvn = json.load(json_file)

    num = str(randint(1, 200))
    invn = i_nvn.get(num)
    return invn


def qst500():
    with open(r"database\qst.json", "r", encoding='utf-8') as js_file:
        qsr = json.load(js_file)

    nm = str(randint(1, 500))
    qst = qsr.get(nm)
    return qst


if __name__ == "__main__":
    qst_inv200()
    qst500()
