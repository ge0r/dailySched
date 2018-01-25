# dailySched
A daily activies scheduler that tracks time spent for different projects.

### Requirements
- pyqt5
- pyglet
- jsonpickle

Make sure that you pip install them at a virtual environment that uses python 3.

### Running dailySched
`python main.py`

### Using dailySched
- Click an activity to select it.
- Double click an activity to start/end the timer. 
- Once an activity runs out of time an alert sound will play.
- Reset all activity timers using the reset button.

### Creating activities
Create new activities either by editing `data.json`, or delete it and create new activities in `create_activities()` of `activityGUI.py`.
