def checkEmotion(request):
    from flask import redirect

    # リクエストがポストかどうかの判別
    if request.method == 'GET':
        return redirect("https://docs.google.com/forms/d/e/1FAIpQLSdAIMClifUpkJJNGTmhukdPx47LboJZaKOK85tqwAuO3fgDwQ/viewform?usp=sf_link")

    return "Error!"