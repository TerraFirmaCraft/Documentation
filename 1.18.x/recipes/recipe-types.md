---
layout: page
title: "Recipe Types"
permalink: /1.18.x/recipes/recipe-types/
---

# Recipe Types

These are the recipe types TFC adds:

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

### Alloy

Alloy recipes define certain ratios of metals that can be formed into another metal.

- Type: `tfc:alloy`
- Fields:
  - `result`: A Metal.
  - `contents`: An array of objects, each containing the following properties:
    - `metal`: A Metal constituent of the recipe
    - `min`: The minimum proportion needed in the mixture, in the range [0, 1].
	- `max`: The maximum proportion needed, larger than `min` and in the range [0, 1]

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
}```
