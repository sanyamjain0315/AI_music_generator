from flask import Flask, render_template, request
from bardapi import Bard
import re, datetime, time

from prompt_to_lyrics import promt_to_lyrics
from lyrics_to_vocal import vocal_production
from lyrics_to_freestyle import freestyle
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")
    # temp = "1685844724"

    # return render_template('result.html', vocal_loc="../../1685844724-freestyle.mp3")



# @app.route('/process-form', methods=['POST'])
# def process_form():
#     print("Submit Button Clicked")
#     user_input = request.form.get('user_input')
#     dropdown_menu = request.form.get('dropdown_menu')
#     print(type(user_input))
#     # Call your Python function with user input and dropdown value
#     result_json = promt_to_lyrics(user_input)
#     vocal_production(lyrics = result_json["lyrics"][:125], uuid=dropdown_menu, bpm=result_json["bpm"])

#     # Pass the result to the render_template
#     return render_template('result.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    print("Submit Button Clicked")
    user_input = request.form.get('user_input')
    dropdown_menu = request.form.get('dropdown_menu')

    print(user_input)
    print(dropdown_menu)
    unique = str(int(datetime.datetime.now().timestamp()))
    # Call your Python function with user input and dropdown value
    if type(user_input) is str and type(dropdown_menu) is str:
        result_json = promt_to_lyrics(user_input)
        vocal_url = vocal_production(lyrics = result_json["lyrics"][0], uuid=dropdown_menu, bpm=result_json["bpm"], unique_identifier=unique)
        freestyle_url = freestyle(lyr=result_json["lyrics"][0], bpm=result_json["bpm"], unique_identifier=unique)
        # Pass the result to the render_template
        return render_template('result.html', vocal_loc= vocal_url, free_loc=freestyle_url, lyrics = result_json["lyrics"][0], bpm=result_json["bpm"],bars= result_json["bars"])
    else:
        return "Failed"
    



if __name__ == '__main__':
    app.debug=True
    app.run()