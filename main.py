def checkEmotion(request):
    from flask import render_template

    # リクエストがポストかどうかの判別
    if request.method == 'GET':
        return render_template("inputEmotion.html")
    elif request.method == 'POST':
        return render_template("result.html")

    return "Error!"