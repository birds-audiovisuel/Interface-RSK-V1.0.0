from flask import Flask, render_template, request, jsonify


import os

import rsk
import math

app = Flask(__name__)

client = rsk.Client('')  

@app.route('/')
def index():
    # Render the index page with the drawing and referee data
    
    referee_data = {
        'game_is_running': client.referee['game_is_running'],
        'game_paused': client.referee['game_paused'],
        'halftime_is_running': client.referee['halftime_is_running'],  # Correct key name
        'teams_blue_score': client.referee['teams']['blue']['score'],
        'teams_green_score': client.referee['teams']['green']['score'],
        'teams_blue_x_positive': client.referee['teams']['blue']['x_positive'],
        'teams_green_x_positive': client.referee['teams']['green']['x_positive'],

    }
    return render_template('index.html', referee_data=referee_data)

@app.route('/outils/maths/update_field', methods=['GET'])
def update_field():
    app.logger.info('update_field endpoint called')
    # Fetch the latest positions of the robots and the ball
    data = {
        'ball': list(client.ball),
        'robot': {
            'green': {
                1: {'pose': list(client.robots['green'][1].pose), 'penalized': client.referee['teams']['green']['robots']['1']['penalized'], 'penalized reason': client.referee['teams']['green']['robots']['1']['penalized_reason'], 'penalized remaining': client.referee['teams']['green']['robots']['1']['penalized_remaining'], },
                2: {'pose': list(client.robots['green'][2].pose), 'penalized': client.referee['teams']['green']['robots']['2']['penalized'], 'penalized reason': client.referee['teams']['green']['robots']['2']['penalized_reason'], 'penalized remaining': client.referee['teams']['green']['robots']['2']['penalized_remaining'],}
            },
            'blue': {
                1: {'pose': list(client.robots['blue'][1].pose), 'penalized': client.referee['teams']['blue']['robots']['1']['penalized'], 'penalized reason': client.referee['teams']['blue']['robots']['1']['penalized_reason'], 'penalized remaining': client.referee['teams']['blue']['robots']['1']['penalized_remaining'], },
                2: {'pose': list(client.robots['blue'][2].pose), 'penalized': client.referee['teams']['blue']['robots']['2']['penalized'], 'penalized reason': client.referee['teams']['blue']['robots']['2']['penalized_reason'], 'penalized remaining': client.referee['teams']['blue']['robots']['2']['penalized_remaining'], }
            }
        }
    }
    return jsonify(data)


@app.route('/outils/maths/teleport_ball', methods=['POST'])
def teleport_ball():
    data = request.get_json()
    x, y = data['x'], data['y']
    client.teleport_ball(x, y)  # Teleport ball to (x, y)
    return jsonify(success=True)

@app.route('/outils/maths/move_robot', methods=['POST'])
def move_robot():
    data = request.get_json()
    color, id = data['color'], data['id']
    x, y, alpha = data['x'], data['y'], data['alpha']
    client.robots[color][id].goto((x, y, alpha), wait=True)  # Move robot to (x, y, alpha)
    return jsonify(success=True)

@app.route('/outils/maths/reset_robots', methods=['POST'])
def reset_robots():
    positions = {
        'green': {1: [0.46, 0, 180], 2: [0.92, 0, 180]},
        'blue': {1: [-0.46, 0, 0], 2: [-0.92, 0, 0]}
    }
    for color, robots in positions.items():
        for id, (x, y, alpha) in robots.items():
            client.robots[color][id].goto((x, y, math.radians(alpha)), wait=True)
            client.teleport_ball(0, 0)
    return jsonify(success=True)





