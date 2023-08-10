# Chinese Character Pronunciations App

## Getting a pronunciation from a specific dialect
You can use the html interface provided by "doc.html", simply run "app.py"
then paste http://127.0.0.1:5001/ or http://192.168.0.102:5001 into your browser. Choose the desired dialect from the dropdown menu,
then enter the desired character into the box. Then all you have to do is click,
"Submit". The interface will return a simple table containing the character, its
English gloss, and its pronunciation in the chosen dialect of Chinese. For example:
```
Character: 上
Gloss: top; superior, highest; go up, send up
Pronunciation: shàng(shang4)
```
The API can be called directly without the UI, using a POST request.
The endpoint is `http://localhost:5001/get_dialect`.
The POST request must contain a JSON body with the `"character" and "dialect"` keys, for example
```json
{"character": "上", "dialect": "Mandarin"}
```
A complete `curl` command looks like this:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"character": "上", "dialect": "Mandarin"}' http://localhost:5001/get_dialect
```
This is the expected output for the above curl command:
```json
{"character": "上", "gloss": "top; superior, highest; go up, send up", "pronunciation": "shàng(shang4)"}
```