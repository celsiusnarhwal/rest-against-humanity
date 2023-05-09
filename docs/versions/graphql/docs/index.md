---
title: Docs
description: A public API for Cards Against Humanity
---

# REST Against Humanity

REST Against Humanity is a public API for Cards Against Humanity. You can use it to programatically obtain sets of
cards from any of _Cards Against Humanity_'s 71 official packs.

You should probably read the [rules of Cards Against Humanity](https://s3.amazonaws.com/cah/CAH_Rules.pdf) before using
this API.

REST Against Humanity is accessible at `https://restagainsthumanity.com/api/graphql`.

!!! graphql "This is a GraphQL API"

    This version of REST Against Humanity uses GraphQL. You should familiarize yourself with the [GraphQL language](https://graphql.org/learn/) before using it.

## Introspection

You can explore the API's schema and build queries from the comfort of your browser with
GraphiQL.

[:simple-graphql: Open GraphiQL :fontawesome-sharp-regular-arrow-up-right-from-square:](/api/graphql){ .md-button .md-button--gql }

## Query Fields

### packs <small markdown>[PackType](#packtype)</small>

List _Cards Against Humanity_ packs.

| **Argument** | **Type**                    | **Description**                                 | **Required?** |
| ------------ | --------------------------- | ----------------------------------------------- | ------------- |
| `where`      | [`PackFilter!`](#packinput) | Criteria by which to filter the packs returned. | No            |

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

| **Argument** | **Type**                              | **Description**                                 | **Required?** |
| ------------ | ------------------------------------- | ----------------------------------------------- | ------------- |
| `where`      | [`BlackCardFilter!`](#blackcardinput) | Criteria by which to filter the cards returned. | No            |

For the `white` field:

| **Argument** | **Type**                              | **Description**                                 | **Required?** |
| ------------ | ------------------------------------- | ----------------------------------------------- | ------------- |
| `where`      | [`WhiteCardFilter!`](#whitecardinput) | Criteria by which to filter the cards returned. | No            |

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

### PackFilter

Criteria by which to filter packs.

| **Field** | **Type** | **Description**       | **Required?** |
| --------- | -------- | --------------------- | ------------- |
| `name`    | `String` | The name of the pack. | No            |
| `id`      | `Int`    | The ID of the pack.   | No            |

### BlackCardFilter

Criteria by which to filter black cards.

| **Field** | **Type** | **Description**                          | **Required?** |
| --------- | -------- | ---------------------------------------- | ------------- |
| `text`    | `String` | The text of the card.                    | No            |
| `pick`    | `Int`    | The number of blank spaces the card has. | No            |

### WhiteCardFilter

Criteria by which to filter white cards.

| **Field** | **Type** | **Description**       | **Required?** |
| --------- | -------- | --------------------- | ------------- |
| `text`    | `String` | The text of the card. | No            |

## Examples

### Listing all pack names

```graphql
query {
  packs {
    name
  }
}
```

### Listing all packs and cards

```graphql
query {
  packs {
    name
    black {
      text
      pick
    }
    white {
      text
    }
  }
}
```

### Listing all black cards with a `pick` of 2

```graphql
query {
  packs {
    name
    black(where: { pick: 2 }) {
      text
      pick
    }
  }
}
```

### Listing all packs with the word "expansion" in their name

```graphql
query {
  packs(where: { name: "expansion" }) {
    name
  }
}
```
