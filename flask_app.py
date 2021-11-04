import os

from dotenv import load_dotenv
from flask import Flask, render_template, jsonify

from Timer import Timer


load_dotenv()


app = Flask(__name__)

b_countdown = 30
c_countdown = 20
d_countdown = 10

b_timer = Timer(duration=b_countdown,
                name='b',
                predictions_url='https://api-v3.mbta.com/predictions/'
                                '?filter[stop]=place-chill'
                                '&filter[route]=Green-B'
                                '&filter[direction_id]=1',
                schedule_url='https://api-v3.mbta.com/schedules/'
                             '?filter[stop]=place-chill'
                             '&filter[route]=Green-B'
                             '&filter[direction_id]=1')
c_timer = Timer(duration=c_countdown,
                name='c',
                predictions_url='https://api-v3.mbta.com/predictions/'
                                '?filter[stop]=place-clmnl'
                                '&filter[route]=Green-C'
                                '&filter[direction_id]=1',
                schedule_url='https://api-v3.mbta.com/schedules/'
                             '?filter[stop]=place-clmnl'
                             '&filter[route]=Green-C'
                             '&filter[direction_id]=1')
d_timer = Timer(duration=d_countdown,
                name='d',
                predictions_url='https://api-v3.mbta.com/predictions/'
                                '?filter[stop]=place-rsmnl'
                                '&filter[route]=Green-D'
                                '&filter[direction_id]=1',
                schedule_url='https://api-v3.mbta.com/schedules/'
                             '?filter[stop]=place-rsmnl'
                             '&filter[route]=Green-D'
                             '&filter[direction_id]=1')

timers = {'b_timer': b_timer, 'c_timer': c_timer, 'd_timer': d_timer}

@app.route("/", methods=["GET"])
def index():
    global b_timer
    b_timer.reset_prediction()
    global c_timer
    c_timer.reset_prediction()
    global d_timer
    d_timer.reset_prediction()
    return render_template("index.html")


@app.route("/_update_timer/<tmr>", methods=["GET", "POST"])
def timer(tmr):
    timers[tmr].decrement()
    seconds_remaining = timers[tmr].duration
    display = timers[tmr].set_display()
    return jsonify({f'{timers[tmr].name}_display': display,
                    f'{timers[tmr].name}_seconds_remaining': f'{seconds_remaining} seconds'})


if __name__ == "__main__":
    app.run()
