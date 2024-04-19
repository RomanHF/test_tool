import httpx

entrant_json_path = "app_info.json"
entrant_xml_path = "test.xml"

content_type_headers = {"xml": {"Content-Type": "application/xml"},
                        "json": {"Content-Type": "application/json"}
                        }
while True:
    user_input = input("1-send post request to /EntrantToXml\n"
                       "2-send post request to /EntrantToJson\n"
                       "3-exit\n"
                       "Input:")

    if user_input == "1":
        with open(entrant_json_path, "r", encoding="utf-8") as file:
            content = file.read()
        response = httpx.post("http://127.0.0.1:5000/EntrantToXml",
                              headers=content_type_headers["json"],
                              json=content)
        print(response.text)

    if user_input == "2":
        with open(entrant_xml_path, "r", encoding="utf-8") as file:
            content = file.read()
        response = httpx.post("http://127.0.0.1:5000/EntrantToJson",
                              headers=content_type_headers["xml"],
                              content=content)
        print(response.text)
    if user_input == "3":
        break
