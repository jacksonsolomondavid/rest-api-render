from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    try:
        data = request.get_json()

        arr = data.get("data", [])

        # Fixed user details (replace with your own values)
        user_id = "Jackson_Solomon_David_15102003"
        email = "jdavidsolomoncheruvathur@gmail.com"
        roll_number = "22BCE1716"

        # Output arrays
        evens, odds, alphabets, specials = [], [], [], []
        total_sum = 0

        for item in arr:
            if isinstance(item, str) and item.isdigit():   # numeric string
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    evens.append(item)
                else:
                    odds.append(item)
            elif isinstance(item, int):   # direct integer
                total_sum += item
                if item % 2 == 0:
                    evens.append(str(item))
                else:
                    odds.append(str(item))
            elif isinstance(item, str) and item.isalpha():  # alphabet
                alphabets.append(item.upper())
            elif isinstance(item, str):   # special character
                specials.append(item)

        # Build concat string → reverse + alternating caps
        concat = "".join(alphabets[::-1])
        alt_caps = "".join(
            c.upper() if i % 2 == 0 else c.lower()
            for i, c in enumerate(concat)
        )

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odds,
            "even_numbers": evens,
            "alphabets": alphabets,
            "special_characters": specials,
            "sum": str(total_sum),
            "concat_string": alt_caps
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
