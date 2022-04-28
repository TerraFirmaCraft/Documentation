---
layout: page
title: "Recipes"
permalink: /1.18.x/recipes/
---

<!--
Note to self: consider separating this page out into multiple pages as it might get really long.
One page per recipe type would be decent, all under recipes/
This is generally considering that recipes are more complex than i.e. the types in common-types or data (although the latter also may want to be broken out into their own pages)
 -->

# Recipe Types

Recipes can be configured through [datapacks](https://minecraft.fandom.com/wiki/Recipe). TFC adds a number of recipe types for its custom crafting operations, and they can be used to add, remove, or modify existing recipes. A complete reference of all of TFC's defined recipes, organized into folders depending on their type can be found in the [TFC Github](https://github.com/TerraFirmaCraft/TerraFirmaCraft/tree/1.18.x/src/main/resources/data/tfc/recipes).

TFC adds the following recipe types:

- [Alloy](#alloy)
- [Barrel Instant](#barrel-instant)
- [Barrel Sealed](#barrel-sealed)
- [Bloomery](#bloomery)
- [Casting](#casting)
- [Collapse](#collapse)
- [Knapping](#knapping)
- [Landslide](#landslide)
- [Loom](#loom)
- [Pot](#pot)
- [Quern](#quern)

<hr>

## Alloy

Alloy recipes are used in the creation of alloys in small vessels and crucibles. They contain a list of percentages of each other metal which must be satisfied.

**Note:** Only one alloy recipe should be defined for a given output metal. While this is not *required*, some things may not work correctly.

- Type: `tfc:alloy`
- `result`: A string, representing the registry name of a [Metal](../data/#metals).
- `contents`: An array of objects, each containing the following properties:
  - `metal`: (String) The registry name of the required [Metal](../data/#metals).
  - `min`: The minimum proportion needed in the mixture, in the range [0, 1].
  - `max`: The maximum proportion needed, larger than `min` and in the range [0, 1].

### Example

```json
{
  "type": "tfc:alloy",
  "result": "tfc:bismuth_bronze",
  "contents": [
    {
      "metal": "tfc:copper",
      "min": 0.2,
      "max": 0.3
    },
    {
      "metal": "cool_addon:another_metal",
      "min": 0.5,
      "max": 0.65
    }
  ]
}
```

<hr>

## Barrel Instant

An instant barrel recipe is one which takes effect immediately when putting items in a barrel. It can have fluid or item ingredients, and fluid or item outputs, however if it has both fluid and item ingredients, and a fluid output, then the recipe will only activate if there is enough input items to *fully consume* the input fluid.

Like [Sealed Barrel](#barrel-sealed) recipes, these are declared in their lowest common ratio form, and any multiple of this recipe is able to complete at once.

**Note**: A barrel recipe must have *at least* one of `input_item` or `input_fluid`.

- Type: `tfc:barrel_instant`
- `input_item`: An optional [Item Stack Ingredient](../data/common-types/#item-stack-ingredients), representing the input item. Defaults to empty.
- `input_fluid`: A optional [Fluid Stack Ingredient](../data/common-types/#fluid-stack-ingredients), representing the input fluid. Defaults to empty.
- `output_item`: An optional [Item Stack Provider](../data/common-types/#item-stack-providers), representing the output item. Defaults to empty.
- `output_fluid`: A [Fluid Stack](../data/common-types/#fluid-stack), representing the output fluid. Defaults to empty.
- `sound`: A string, representing the registry name of a sound event, which is played when the recipe finishes. Defaults to `minecraft:block.brewing_stand.brew`.

<hr>

## Barrel Sealed

<hr>

## Bloomery

<hr>

## Casting

<hr>

## Collapse

<hr>

## Knapping

<hr>

## Landslide

<hr>

## Loom

<hr>

## Pot

<hr>

## Quern
