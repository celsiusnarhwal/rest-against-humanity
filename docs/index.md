---
icon: fontawesome/solid/webhook
description: A public REST API for Cards Against Humanity
hide:
  - footer
---

# REST Against Humanity

REST Against Humanity is a public API for [_Cards Against Humanity_](https://cardsagainsthumanity.com/).
You can use it to programatically obtain sets of cards from any of _Cards Against Humanity_'s 71 official packs.

You should probably read the [rules of _Cards Against Humanity_](https://s3.amazonaws.com/cah/CAH_Rules.pdf) before
using this API.

## Endpoints

### Packs

`https://restagainsthumanity.com/api/v2/packs`

Names of _Cards Against Humanity_ packs available through REST Against Humanity.

#### Parameters

None.

#### Example Response

```json
["CAH Base Set", "2012 Holiday Pack", "2014 Holiday Pack", ...]
```

#### Code Examples

=== ":fontawesome-brands-python: Python (Requests)"

    ```python
    import requests

    resp = requests.get("https://restagainsthumanity.com/api/v2/packs")

    if resp.status_code == 200:
        print(resp.json())
    ```

=== ":fontawesome-brands-js: JavaScript (Axios)"

    ```javascript
    import axios from "axios";

    const axios = require("axios");

    axios.get("https://restagainsthumanity.com/api/v2/packs").then((resp) => {
      if (resp.status === 200) {
        console.log(resp.data);
      }
    });
    ```

=== ":simple-kotlin: Kotlin (Fuel)"

    ```kotlin
    val (request, response, result) = Fuel.get("https://restagainsthumanity.com/api/v2/packs")
        .responseString()

    if (response.statusCode == 200) {
        println(response.data)
    }
    ```

=== ":fontawesome-brands-java: Java"

    ```java
    var client = HttpClient.newHttpClient();

    var request = HttpRequest.newBuilder()
        .uri(URI.create("https://restagainsthumanity.com/api/v2/packs"))
        .GET()
        .build();

    var response = client.send(request, HttpResponse.BodyHandlers.ofString());

    if (response.statusCode() == 200) {
        System.out.println(response.body());
    }
    ```

=== ":fontawesome-brands-swift: Swift"

    ```swift
    let task = URLSession.shared.dataTask(with: URL(string: "https://restagainsthumanity.com/api/v2/packs")!) { data, response, error in
        if let data = data, let response = response as? HTTPURLResponse, response.statusCode == 200 {
            print(String(data: data, encoding: .utf8)!)
        }
    }

    task.resume()
    ```

=== ":simple-ruby: Ruby"

    ```ruby
    require "net/http"
    require "json"

    uri = URI("https://restagainsthumanity.com/api/v2/packs")
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = true
    request = Net::HTTP::Get.new(uri.request_uri)
    response = http.request(request)

    if response.code == "200"
        puts JSON.parse(response.body)
    end
    ```

### Cards

_Cards Against Humanity_ cards.

`https://restagainsthumanity.com/api/v2/cards`

#### Parameters

| **Name**         | **Type** | **Description**                                                                                                                                                            | **Required?** | **Default** |
| ---------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------- |
| packs            | string   | A comma-separated, case-sensitive, list of packs to limit the response to.                                                                                                 | No            | All packs   |
| color            | string   | Limit the response to either black or white cards. Must be one of either "black" or "white".                                                                               | No            | N/A         |
| pick             | integer  | The pick that black cards in the response should be limited to. (A black card's pick is the number of blank spaces it has for white cards to fill.) Must be either 1 or 2. | No            | N/A         |
| includePackNames | boolean  | Whether to include the name of each card's originating pack in the response.                                                                                               | No            | True        |

!!! danger

    It's important that you separate pack names with **commas only** — _not_ commas and spaces.

    For example, this is fine:

    ```
    CAH Base Set,2012 Holiday Pack,90s Nostalgia Pack
    ```

    But this is not:

    ```
    CAH Base Set, 2012 Holiday Pack, 90s Nostalgia Pack
    ```

    Unexpected whitespace will cause an HTTP 400 error.

#### Example Response

```json
{
  "black": [
    {
      "text": "_ + _ = Hipsters",
      "pick": 2,
      "pack": "CAH Base Set"
    },
    {
      "text": "_ is a sure sign of mankind's decline.",
      "pick": 1,
      "pack": "CAH Base Set"
    },
    {
      "text": "_ would only happen in my worst nightmares.",
      "pick": 1,
      "pack": "CAH Base Set"
    }
  ],
  "white": [
    {
      "text": "A balanced breakfast.",
      "pack": "CAH Base Set"
    },
    {
      "text": "A big hoopla about nothing.",
      "pack": "CAH Base Set"
    },
    {
      "text": "A cat with... hands.",
      "pack": "CAH Base Set"
    }
  ]
}
```

#### Code Examples

=== ":fontawesome-brands-python: Python (Requests)"

    ```python
    import requests

    params = {"packs": "CAH Base Set,CAH: First Expansion"}
    resp = requests.get("https://restagainsthumanity.com/api/v2/cards", params=params)

    if resp.status_code == 200:
        print(resp.json())
    ```

=== ":fontawesome-brands-js: JavaScript (Axios)"

    ```javascript
    import axios from "axios";

    const axios = require("axios");

    axios
      .get("https://restagainsthumanity.com/api/v2/cards", {
        params: {
          packs: "CAH Base Set,CAH: First Expansion",
        },
      })
      .then((resp) => {
        if (resp.status === 200) {
          console.log(resp.data);
        }
      });
    ```

=== ":simple-kotlin: Kotlin (Fuel)"

    ```kotlin
    val (request, response, result) = Fuel.get("https://restagainsthumanity.com/api/v2/cards")
        .parameter("packs", "CAH Base Set,CAH: First Expansion")
        .responseString()

    if (response.statusCode == 200) {
        println(response.data)
    }
    ```

=== ":fontawesome-brands-java: Java"

    ```java
    var client = HttpClient.newHttpClient();

    var request = HttpRequest.newBuilder()
        .uri(URI.create("https://restagainsthumanity.com/api/v2/cards?packs=CAH Base Set,CAH: First Expansion"))
        .GET()
        .build();

    var response = client.send(request, HttpResponse.BodyHandlers.ofString());

    if (response.statusCode() == 200) {
        System.out.println(response.body());
    }
    ```

=== ":fontawesome-brands-swift: Swift"

    ```swift
    let task = URLSession.shared.dataTask(with: URL(string: "https://restagainsthumanity.com/api/v2/cards?packs=CAH Base Set,CAH: First Expansion")!) { data, response, error in
        if let data = data, let response = response as? HTTPURLResponse, response.statusCode == 200 {
            print(String(data: data, encoding: .utf8)!)
        }
    }

    task.resume()
    ```

=== ":simple-ruby: Ruby"

    ```ruby
    require "net/http"
    require "json"

    uri = URI("https://restagainsthumanity.com/api/v2/cards?packs=CAH Base Set,CAH: First Expansion")
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = true
    request = Net::HTTP::Get.new(uri.request_uri)
    response = http.request(request)

    if response.code == "200"
        puts JSON.parse(response.body)
    end
    ```
