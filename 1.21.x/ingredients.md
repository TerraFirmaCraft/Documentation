---
layout: page
title: "Ingredients"
permalink: /1.21.x/ingredients/
---

# Ingredients

An ingredient represents an input to a recipe or other piece of data. All vanilla and modded recipes should support ingredients and can use any of the following ingredients. It must be a JSON object with one of the following keys:

1. An `item` key with the registry name of an item.
2. A `tag` key with the registry name of an item tag.
3. A `type` key with the name of a custom ingredient type.

In addition to the two ingredients added by Minecraft, TFC adds a number of custom ingredients which can be used anywhere an `Ingredient` is required, even by other mod's recipes. TFC adds the following ingredient types:

<!--linky_begin_sort_alphabetical-->

- [And](#and)
- [Fluid Content](#fluid-content)
- [Has Trait](#has-trait)
- [Heat](#heat)
- [Lacks Trait](#lacks-trait)
- [Not Rotten](#not-rotten)
- [Rotten](#rotten)
- [Sized](#sized-ingredient)

<!--linky_end_sort_alphabetical-->
<hr>
<!--linky_begin_sort_categories-->

## And

An ingredient which combines multiple ingredients together using AND logic. The item must match **all** child ingredients to be accepted. This is used to combine an item or tag with modifier ingredients like [Heat](#heat), [Not Rotten](#not-rotten), or [Has Trait](#has-trait).

- `type`: `tfc:and`
- `children`: A list of [Ingredients](../ingredients/) that must all match.

#### Example

```jsonc
// An ingredient which only accepts non-rotten minecraft:steak
{
    "type": "tfc:and",
    "children": [
        { "item": "minecraft:steak" },
        { "type": "tfc:not_rotten" }
    ]
}
```

```jsonc
// An ingredient which only accepts minecraft:iron_ingots if they are heated above 300 C
{
    "type": "tfc:and",
    "children": [
        { "item": "minecraft:iron_ingot" },
        { "type": "tfc:heat", "min": 300 }
    ]
}
```

<hr>

## Fluid Content

An ingredient which expects an item to contain a fluid (such as a bucket). It has the following fields:

- `type`: `tfc:fluid_content`
- `fluid`: A [Sized Fluid Ingredient](../common-types/#fluid-stack-ingredients), which must match the fluid contained in the item.

#### Example

```jsonc
// An ingredient which accepts any item containing at least 100 mB of water
{
    "type": "tfc:fluid_content",
    "fluid": {
        "amount": 100,
        "ingredient": { "fluid": "minecraft:water" }
    }
}
```

<hr>

## Has Trait

This is an ingredient which only accepts food items if they have a specific trait. It has the following fields:

- `type`: `tfc:has_trait`
- `trait`: String. The registry name of a [Food Trait](../common-types/#food-traits) which must be present.

#### Example

```jsonc
// An ingredient which only accepts any brined food item
{
    "type": "tfc:has_trait",
    "trait": "tfc:brined"
}
```

```jsonc
// An ingredient which only accepts a brined tfc:food/apple (using tfc:and)
{
    "type": "tfc:and",
    "children": [
        { "item": "tfc:food/apple" },
        { "type": "tfc:has_trait", "trait": "tfc:brined" }
    ]
}
```

<hr>

## Heat

This is an ingredient which only accepts items if they are currently within a certain temperature range. At least one of `min` or `max` must be specified. It has the following fields:

- `type`: `tfc:heat`
- `min`: Optional number. The minimum temperature this item must have, in degrees Celsius. Defaults to no minimum.
- `max`: Optional number. The maximum temperature this item must have, in degrees Celsius. Defaults to no maximum.

#### Example

```jsonc
// An ingredient which only accepts any item heated above 500 C
{
    "type": "tfc:heat",
    "min": 500
}
```

<hr>

## Lacks Trait

This ingredient is the same as [Has Trait](#has-trait) but is inverted. It tests if a food lacks a specified trait.

- `type`: `tfc:lacks_trait`
- `trait`: String. The registry name of a [Food Trait](../common-types/#food-traits) which must not be present.

#### Example

```jsonc
// An ingredient which only accepts food items that have not been brined
{
    "type": "tfc:lacks_trait",
    "trait": "tfc:brined"
}
```

<hr>

## Not Rotten

This is an ingredient which only accepts food items if they are not rotten. It has no additional fields.

- `type`: `tfc:not_rotten`

#### Example

```jsonc
// An ingredient which only accepts non-rotten minecraft:steak (using tfc:and)
{
    "type": "tfc:and",
    "children": [
        { "item": "minecraft:steak" },
        { "type": "tfc:not_rotten" }
    ]
}
```

<hr>

## Rotten

This is an ingredient which only accepts food items if they are rotten. It has no additional fields.

- `type`: `tfc:rotten`

#### Example

```jsonc
// An ingredient which accepts any rotten food
{
    "type": "tfc:rotten"
}
```

<hr>

## Sized

This ingredient lacks a type, and is added by NeoForge. To use it, simply add a `count` to the ingredient.

- `count`: A positive Integer specifying how much of the item is needed.

#### Example

```jsonc
// An ingredient used in the clay knapping type
{
    "count": 5,
    "tag": "tfc:clay_knapping"
}
```

<hr>

<!--linky_end_sort_categories-->