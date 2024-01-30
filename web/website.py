from flask import Flask,render_template, request, redirect, url_for

app = Flask(__name__)
@app.route("/", methods = ['GET', 'POST'])

def index():
    if request.method == 'POST':
        search_text = request.form['search_text']
        # 在这里执行搜索操作，你可以根据需要添加逻辑
        # 暂时只打印搜索文本
        print("搜索文本:", search_text)
        return redirect(url_for('results', search_text=search_text))
    return render_template('index.html')

@app.route('/results/<search_text>')
def results(search_text):
    # 在这里处理搜索结果，根据需要添加逻辑
    print("result:",search_text)
    law_list = ["民法429", "民法3", "民法87"]
    past_list = ["台北簡易庭 108 年度北簡字第 4247 號民事判決", "桃園簡易庭 108 年度桃小字第 510 號民事判決"]
    return render_template('results.html', search_text=search_text, law_list = law_list, past_list = past_list)

if __name__ == "__main__":
    app.run(debug=True)