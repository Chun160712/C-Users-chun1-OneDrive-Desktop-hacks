from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="")

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/goal', methods=["POST", "GET"])
def goal():
  if request.method == "GET":
    return render_template("goal.html")
  else:
    goalsummary = request.form.to_dict()
    goal_list = []
    for keys in goalsummary.values():
        goal_list.append(keys)
    with open('goalsummary.txt', 'w') as f:
        for item in goal_list:
            f.write('%s\n' % item)
    return redirect('/submission')

@app.route('/submission')
def submission():
  return render_template("submission.html")

'''
@app.route("/<usergoal>")
def goalsummary(usergoal):
    return "Submitted!", f"<p>{usergoal}</p>"
'''

@app.route('/goalsummary')
def goal_summary():
    return render_template("goalsummary.html")

@app.route('/task')
def task():
    return render_template("dailytasks.html")

@app.route('/weekly-ratings')
def weekly_rating():
    return render_template("weekly_ratings.html")

if __name__ == '__main__':
  app.run(debug=True)