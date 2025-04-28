from flask import Flask, request, jsonify
import random
import requests

app = Flask(__name__)

ACCESS_KEY = "bJ2GBuYWPW7md1i9cAI94m7TtejufJAP"

# ردود تحشيشية جاهزة
funny_replies = [
    "هلااااا بالغالييييي 😂 وين الكامرة مالك يلا نصور!",
    "عااش حمودي اليوم نكسر الدنيا بصور خرافية! 📸",
    "لك روح الله عليك فنان، وين سوالفك الزينة؟ 😎",
    "تشرب جاي لو تبدي تشتغل؟ ☕📸",
    "ها ابو التصوير وين؟ جبت العدسات وياك؟ 😂"
]

GOOGLE_TRANSLATE_URL = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=ar&dt=t&q="

@app.route("/", methods=["POST"])
def chat():
    try:
        data = request.json

        if data.get("accessKey") != ACCESS_KEY:
            return jsonify({"error": "Access Denied!"}), 403

        user_message = data.get("query", "").strip()

        if not user_message:
            return jsonify({"text": "احچي وياي لا تسكت يبو 😂"})

        if "فكرة تصوير" in user_message or "فكرة فوتو" in user_message:
            return jsonify({"text": suggest_photo_idea()})

        elif "شورت لست" in user_message:
            return jsonify({"text": suggest_shotlist()})

        elif "نصيحة كاميرا" in user_message:
            return jsonify({"text": camera_tips()})

        elif "كورس تصوير" in user_message:
            return jsonify({"text": suggest_course()})

        elif "فلم فوتو" in user_message:
            return jsonify({"text": suggest_movie()})

        elif "مقولة مصور" in user_message:
            return jsonify({"text": suggest_quote()})

        else:
            reply = random.choice(funny_replies)
            return jsonify({"text": reply})

    except Exception as e:
        return jsonify({"text": f"صار شوية تهريب بس كملنه 😂 ➔ {str(e)}"})

def suggest_photo_idea():
    return """🌟 فكرة تصوير اليوم:
- صور واحد جالس بالشارع ويشرب جاي نظرة عميقة، وخلي الفوكس عالكاسة.
- إعدادات الكاميرا: ISO 200، f/1.8، شتر 1/250
📸 عدسة مقترحة: 50mm f/1.8
رابط عدسة حلوة عالأمازون: https://www.amazon.com/dp/B00007E7JU
"""

def suggest_shotlist():
    return """📋 شورت لست نار:
- لقطة ضحكة طبيعية.
- لقطة عيونه بتركز بالعدسة.
- لقطة مشي بالشمس.
- لقطة قهوة وكتاب على طاولة خشب.
- لقطة انعكاس بالمي.
"""

def camera_tips():
    return """📷 نصيحة اليوم:
- لا ترفع ISO فوق 800 الا اذا مضطر.
- فتحة عدسة f/2.8 مثالية للبورتريه الخفيف.
- خلي دايما عندك Reflector بسيارتك 😂.
"""

def suggest_course():
    return """📚 كورس مجاني عالحلو:
- كورس Street Photography الأساسي (بالعربي والانكليزي).
- رابط الكورس: https://www.udemy.com/course/street-photography/
- نصيحة محمد المصور العالمي: "اصور قبل لا تفكر، مرات اللقطة تجي بلحظة 😂📸"
"""

def suggest_movie():
    return """🎬 فلم فوتوغرافي أسطوري:
- Kodachrome (2017) 🎞️
- قصة مصور يسافر مع ابنه يحقق حلم حياته.
- رابط IMDB: https://www.imdb.com/title/tt1880399/
"""

def suggest_quote():
    return """🧠 مقولة مصور ملهمة:
- "افضل كاميرا هي الكاميرا الي وياك" - Chase Jarvis
- رابط تفاصيل: https://chasejarvis.com/blog/
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
