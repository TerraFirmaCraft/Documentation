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
The `metal` should be registered Metal types, and the `min` and `max` values should be in the range [0, 1]

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
}`