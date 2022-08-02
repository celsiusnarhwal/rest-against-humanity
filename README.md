This branch of the repository contains the old version of REST Against Humanity before its move from
[DigitalOcean](https://digitalocean.com) to [Vercel](https://vercel.com). The move involved a major refactoring of REST 
Against Humanity's codebase, so I thought it would be a good idea to make a backup. This is the backup.

There's probably nothing of interest to you here. You should go check out [restagainsthumanity.com](https://restagainsthumanity.com) 
instead.

Or you can keep reading, I guess. You do you.
 
# REST Against Humanity

REST Against Humanity is a public API for [Cards Against Humanity](https://cardsagainsthumanity.com/).
You can use it to programatically obtain sets of cards from any of Cards Against Humanity's 71 official packs.

## Usage

REST Against Humanity can be accessed at [restagainsthumanity.com/api](https://restagainsthumanity.com/api).

To obtain a list of all available packs, just shoot a GET request to the root endpoint:

```http request
GET restagainsthumanity.com/api
```

You'll get a list of available packs as the response:
```json
["CAH Base Set", "2012 Holiday Pack", "2013 Holiday Pack", "2014 Holiday Pack", "90s Nostalgia Pack", "..."]
```

To obtain cards from one or more packs, just tack on the `packs` parameter:

```http request
GET restagainsthumanity.com/api?packs=CAH Base Set
```

For multiple packs, separate them with commas:

```http request
GET restagainsthumanity.com/api?packs=CAH Base Set,2012 Holiday Pack,90s Nostalgia Pack
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

REST Against Humanity © celsius narhwal.

Card data is sourced from [JSON Against Humanity](https://crhallberg.com/cah/).

Writing from *Cards Against Humanity* © Cards Against Humanity, LLC. Cards Against Humanity is a trademark of Cards Against Humanity, LLC. This software is in no way affiliated with or endorsed by Cards Against Humanity, LLC.


## License

REST Against Humanity is made available under a [Creative Commons BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).


