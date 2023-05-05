---
icon: simple/graphql
description: A public GraphQL API for Cards Against Humanity
hide:
  - footer
---

# GraphQL Against Humanity

GraphQL Against Humanity is REST Against Humanity's GraphQL API. You can use it to programatically obtain sets of
cards from any of _Cards Against Humanity_'s 71 official packs.

You should probably read the [rules of Cards Against Humanity](https://s3.amazonaws.com/cah/CAH_Rules.pdf) before using
this API.

GraphQL Against Humanity is accessible at `https://restagainsthumanity.com/api/graphql`.

## Introspection

You can explore the API's schema and build queries from the comfort of your browser with
GraphiQL.

[:simple-graphql: Open GraphiQL :fontawesome-sharp-regular-arrow-up-right-from-square:](/api/graphql){ .md-button .md-button--gql }

## Query Fields

### packs <small markdown>[PackType](#packtype)</small>

List _Cards Against Humanity_ packs.

| **Argument** | **Type**                   | **Description**                                 | **Required?** |
| ------------ | -------------------------- | ----------------------------------------------- | ------------- |
| `where`      | [`PackInput!`](#packinput) | Criteria by which to filter the packs returned. | No            |

## Objects

### PackType

A _Cards Against Humanity_ pack.

| **Field** | **Type**                              | **Description**         |
| --------- | ------------------------------------- | ----------------------- |
| `name`    | `String!`                             | The name of the pack.   |
| `id`      | `Int!`                                | The ID of the pack.     |
| `black`   | [`[BlackCardType!]!`](#blackcardtype) | The pack's black cards. |
| `white`   | [`[WhiteCardType!]!`](#whitecardtype) | The pack's white cards. |

For the `black` field:

| **Argument** | **Type**                             | **Description**                                 | **Required?** |
| ------------ | ------------------------------------ | ----------------------------------------------- | ------------- |
| `where`      | [`BlackCardInput!`](#blackcardinput) | Criteria by which to filter the cards returned. | No            |

For the `white` field:

| **Argument** | **Type**                             | **Description**                                 | **Required?** |
| ------------ | ------------------------------------ | ----------------------------------------------- | ------------- |
| `where`      | [`WhiteCardInput!`](#whitecardinput) | Criteria by which to filter the cards returned. | No            |

### BlackCardType

A _Cards Against Humanity_ black card.

| **Field** | **Type**                 | **Description**                          |
| --------- | ------------------------ | ---------------------------------------- |
| `text`    | `String!`                | The text of the card.                    |
| `pick`    | `Int!`                   | The number of blank spaces the card has. |
| `pack`    | [`PackType!`](#packtype) | The pack the card belongs to.            |

### WhiteCardType

A _Cards Against Humanity_ white card.

| **Field** | **Type**                 | **Description**               |
| --------- | ------------------------ | ----------------------------- |
| `text`    | `String!`                | The text of the card.         |
| `pack`    | [`PackType!`](#packtype) | The pack the card belongs to. |

## Inputs

### PackInput

Criteria by which to filter packs.

| **Field** | **Type** | **Description**       | **Required?** |
| --------- | -------- | --------------------- | ------------- |
| `name`    | `String` | The name of the pack. | No            |
| `id`      | `Int`    | The ID of the pack.   | No            |

### BlackCardInput

Criteria by which to filter black cards.

| **Field** | **Type** | **Description**                          | **Required?** |
| --------- | -------- | ---------------------------------------- | ------------- |
| `text`    | `String` | The text of the card.                    | No            |
| `pick`    | `Int`    | The number of blank spaces the card has. | No            |

### WhiteCardInput

Criteria by which to filter white cards.

| **Field** | **Type** | **Description**       | **Required?** |
| --------- | -------- | --------------------- | ------------- |
| `text`    | `String` | The text of the card. | No            |
