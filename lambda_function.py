def lambda_handler(event, context):

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud Cafe Menu</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
            }

            .container {
                max-width: 800px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px gray;
            }

            h1 {
                color: #ff6600;
                text-align: center;
            }

            table {
                width: 100%;
                border-collapse: collapse;
            }

            th, td {
                border: 1px solid #ddd;
                padding: 10px;
                text-align: left;
            }

            th {
                background-color: #ff6600;
                color: white;
            }

            .special {
                background-color: #fff3cd;
                padding: 10px;
                border-radius: 5px;
                margin-bottom: 15px;
            }
        </style>
    </head>
    <body>

        <div class="container">

            <h1>Cloud Cafe</h1>

            <p><strong>Rating:</strong> 4.7 / 5</p>
            <p><strong>Status:</strong> Open</p>
            <p><strong>Delivery Time:</strong> 25 Minutes</p>

            <div class="special">
                <h3>Today's Special</h3>
                <p>Margherita Pizza - ₹299</p>
            </div>

            <h2>Menu</h2>

            <table>
                <tr>
                    <th>Food Item</th>
                    <th>Price</th>
                </tr>
                <tr>
                    <td>Margherita Pizza</td>
                    <td>₹299</td>
                </tr>
                <tr>
                    <td>Veg Burger</td>
                    <td>₹149</td>
                </tr>
                <tr>
                    <td>White Sauce Pasta</td>
                    <td>₹249</td>
                </tr>
                <tr>
                    <td>Paneer Momos</td>
                    <td>₹129</td>
                </tr>
                <tr>
                    <td>Cold Coffee</td>
                    <td>₹99</td>
                </tr>
            </table>

            <br>

            <h3>Special Offer</h3>
            <p>20% OFF on orders above ₹500</p>

        </div>

    </body>
    </html>
    """

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": html
    }