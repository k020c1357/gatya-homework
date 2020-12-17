import random
from flask import Flask, render_template

#　関数


def card_conversion(num):
    if num <= 33:
        # card_typeにカードの種類を入れる
        card_type = "N"
    elif num <= 33 + 25:
        card_type = "N+"
    elif num <= 33 + 25 + 20:
        card_type = "R"
    else:
        card_type = "SR+"

    return card_type


# flask インスタンス作成
app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/gatya01')
def gatya01():
    # 1~100の乱数を作って、select_numに入れる
    select_num = random.randint(1, 100)
    card_type = card_conversion(select_num)

    return render_template("gatya01.html", select_num=select_num,
                           card_type=card_type)


@app.route('/gatya11')
def gatya11():
    # list を作って
    select_num_list = {}
    card_type_list = {}
    for i in range(11):
        select_num_list[i] = random.randint(1, 100)
        card_type_list[i] = card_conversion(select_num_list[i])

    return render_template("gatya11.html",
                           select_num_list=select_num_list,
                           card_type_list=card_type_list, time=11)


app.run(debug=True)
