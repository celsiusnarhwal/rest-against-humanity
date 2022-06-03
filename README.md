# REST Against Humanity

REST Against Humanity is a public API for [Cards Against Humanity](https://cardsagainsthumanity.com/).
You can use it to programatically obtain sets of cards from any of Cards Against Humanity's 71 official packs.

## Usage

REST Against Humanity can be accessed at [rest-against-humanity-rlpdt.ondigitalocean.app](https://rest-against-humanity-rlpdt.ondigitalocean.app) (Sorry about the URL - I'll have a proper domain name soon.)

To obtain a list of all available packs, just shoot a GET request to the root URL:

```http request
GET rest-against-humanity-rlpdt.ondigitalocean.app

# [ "CAH Base Set", "2012 Holiday Pack", "2013 Holiday Pack", "2014 Holiday Pack", "90s Nostalgia Pack", ...]
```

To obtain cards from one or more packs, just tack on the `packs` parameter:

```http request
GET rest-against-humanity-rlpdt.ondigitalocean.app?packs=CAH Base Set
```

For multiple packs, separate them with commas:

```http request
GET rest-against-humanity-rlpdt.ondigitalocean.app?packs=CAH Base Set,2012 Holiday Pack,90s Nostalgia Pack
```

The response will come formatted like this:

```json
{
  "white": [
    "A balanced breakfast.",
    "A big hoopla about nothing.",
    "A cat with... hands."
  ],
  "black": [
    {
      "text": "_ + _ = Hipsters",
      "pick": 2
    },
    {
      "text": "_ is a sure sign of mankind's decline.",
      "pick": 1
    },
    {
      "text": "_ would only happen in my worst nightmares.",
      "pick": 1
    }
  ]
}
```
`pick` signifies the number of white cards each player must play. It will always be either `1` or `2`.

It may do you well to learn the [rules of Cards Against Humanity](https://s3.amazonaws.com/cah/CAH_Rules.pdf) before using this API.

## Attributions

Card data is sourced from [JSON Against Humanity](https://crhallberg.com/cah/).

## License

REST Against Humanity is made available under a [Creative Commons BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).


