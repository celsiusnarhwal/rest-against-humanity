---
description: A public API for Cards Against Humanity
---

# REST Against Humanity

REST Against Humanity is a public API for [_Cards Against Humanity_](https://cardsagainsthumanity.com/).
You can use it to programatically obtain cards from any of _Cards Against Humanity_'s 71 official packs.

You should probably read the [rules of _Cards Against Humanity_](https://s3.amazonaws.com/cah/CAH_Rules.pdf) before
using this API.

## Usage

REST Against Humanity can be accessed at [restagainsthumanity.com/api/v1/](https://restagainsthumanity.com/api/v1/).

### Getting a List of Packs

To obtain a list of all available packs, send a GET request to the root endpoint (`/api/v1`).

=== ":fontawesome-brands-python: Python (Requests)"

    ```python
    import requests

    resp = requests.get("https://restagainsthumanity.com/api/v1")

    if resp.status_code == 200:
        print(resp.json())
    ```

=== ":fontawesome-brands-js: JavaScript (Axios)"

    ```javascript
    import axios from "axios";

    const axios = require("axios");

    axios.get("https://restagainsthumanity.com/api/v1").then((resp) => {
      if (resp.status === 200) {
        console.log(resp.data);
      }
    });
    ```

=== ":simple-kotlin: Kotlin (Fuel)"

    ```kotlin
    val (request, response, result) = Fuel.get("https://restagainsthumanity.com/api/v1")
        .responseString()

    if (response.statusCode == 200) {
        println(response.data)
    }
    ```

=== ":fontawesome-brands-java: Java"

    ```java
    var client = HttpClient.newHttpClient();

    var request = HttpRequest.newBuilder()
        .uri(URI.create("https://restagainsthumanity.com/api/v1"))
        .GET()
        .build();

    var response = client.send(request, HttpResponse.BodyHandlers.ofString());

    if (response.statusCode() == 200) {
        System.out.println(response.body());
    }
    ```

=== ":fontawesome-brands-swift: Swift"

    ```swift
    let task = URLSession.shared.dataTask(with: URL(string: "https://restagainsthumanity.com/api/v1")!) { data, response, error in
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

    uri = URI("https://restagainsthumanity.com/api/v1")
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = true
    request = Net::HTTP::Get.new(uri.request_uri)
    response = http.request(request)

    if response.code == "200"
        puts JSON.parse(response.body)
    end
    ```

You'll get a list of available packs as the response:

```json
[
  "CAH Base Set",
  "2012 Holiday Pack",
  "2013 Holiday Pack",
  "2014 Holiday Pack",
  "90s Nostalgia Pack",
  "..."
]
```

### Getting Cards

To obtain cards, specify the packs you want using the `packs` parameter.

=== ":fontawesome-brands-python: Python (Requests)"

    ```python
    import requests

    params = {"packs": "CAH Base Set,CAH: First Expansion"}
    resp = requests.get("https://restagainsthumanity.com/api/v1", params=params)

    if resp.status_code == 200:
        print(resp.json())
    ```

=== ":fontawesome-brands-js: JavaScript (Axios)"

    ```javascript
    import axios from "axios";

    const axios = require("axios");

    axios
      .get("https://restagainsthumanity.com/api/v1", {
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
    val (request, response, result) = Fuel.get("https://restagainsthumanity.com/api/v1")
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
        .uri(URI.create("https://restagainsthumanity.com/api/v1?packs=CAH Base Set,CAH: First Expansion"))
        .GET()
        .build();

    var response = client.send(request, HttpResponse.BodyHandlers.ofString());

    if (response.statusCode() == 200) {
        System.out.println(response.body());
    }
    ```

=== ":fontawesome-brands-swift: Swift"

    ```swift
    let task = URLSession.shared.dataTask(with: URL(string: "https://restagainsthumanity.com/api/v1?packs=CAH Base Set,CAH: First Expansion")!) { data, response, error in
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

    uri = URI("https://restagainsthumanity.com/api/v1?packs=CAH Base Set,CAH: First Expansion")
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = true
    request = Net::HTTP::Get.new(uri.request_uri)
    response = http.request(request)

    if response.code == "200"
        puts JSON.parse(response.body)
    end
    ```

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

The response will come formatted like this:

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

`pick` signifies the number of white cards each player must play. It will always be either `1` or `2`.
