---
layout: page
title: "Custom Data"
permalink: /1.18.x/data/
---

# Custom Data

In addition to recipes, TFC defines and loads a number of completely custom data types. These can also be loaded by datapacks, and all are under the root path `tfc`, meaning that any added data should be located under `/data/<your mod id>/tfc/<subfolder>/...`.

TFC defines the following custom data types:

- [Climate Ranges](#climate-ranges)
- [Drinkables](#drinkables)
- [Fauna](#fauna)
- [Fertilizers](#fertilizers)
- [Food Items](#food-items)
- [Fuels](#fuels)
- [Item Heats](#item-heats)
- [Item Sizes](#item-sizes)
- [Lamp Fuels](#lamp-fuels)
- [Metals](#metals)
- [Supports](#supports)

<hr>

## Climate Ranges

<hr>

## Drinkables

<hr>

## Fauna

<hr>

## Fertilizers

<hr>

## Food Items

<hr>

## Fuels

A fuel defines something that burns, and can be used in a fire pit, forge, or other TFC fuel consuming device. It is a file located under the subfolder `fuels`. It has the following properties:

- `ingredient`: An [Ingredient](./common-types/#ingredients) to which this item size definition applies to.
- `temperature`: A number. The temperature in degrees Celsius that this fuel burns at.
- `duration`: An integer. The duration in ticks that a single item of this fuel burns for.

#### Example

```jsonc
// Reference: data/tfc/tfc/fuels/coal.json
{
    "ingredient": [
        { "item": "minecraft:coal" },
        { "item": "tfc:ore/bituminous_coal" }
    ],
    "duration": 2200,
    "temperature": 1415
}
```

<hr>

## Item Heats

An item heat definition specifies if an item can be heated, and also properties of the heated item. It is a file located under the subfolder `item_heats`. It has the following properties:

- `heat_capacity`: A number which specifies how fast this item heats up relative to others.
- `forging_temperature`: An optional number which specifies the temperature at which this item can be worked, in degrees Celsius. If omitted, this item will not require heat to work.
- `welding_temperature`: An optional number which specifies the temperature at which this item can be worked, in degrees Celsius. If omitted, this item will not require heat to weld.

#### Example

```jsonc
// Reference: data/tfc/tfc/item_heats/metal/bismuth_bronze_ingot.json
{
    "ingredient": {
        "tag": "forge:ingots/bismuth_bronze"
    },
    "heat_capacity": 0.35,
    "forging_temperature": 591.0,
    "welding_temperature": 788.0
}
```

<hr>

## Item Sizes

An item size definition specifies the size and weight of items. Size affects what containers the item can fit in. Weight affects the stack size of the item (and TFC will override the stack size where possible). An Item Size Definition is a file located in under the subfolder `item_sizes`. It has the following properties:

- `ingredient`: An [Ingredient](./common-types/#ingredients) to which this item size definition applies to.
- `size`: An optional string, which must be one of the following sizes: `tiny`, `very_small`, `small`, `normal`, `large`, `very_large`, or `huge`. Defaults to `normal`.
- `weight`: An optional string, which must be one of the following weights: `very_light`, `light`, `medium`, `heavy`, `very_heavy`. Defaults to `medium`.

Note that TFC will attempt to apply defaults for all items that do not have item sizes. It uses the following rules:

1. If the `Item` or `Block` specifies a custom item size implementation.
2. If a item size definition is found matching the item.
3. If the item is a `TieredItem`, it will be Large and Medium.
4. If the item is an `ArmorItem`, it will be Large and Very Heavy.
5. If the item is a `BlockItem`, it will be Small and Light.
6. All other items will be Very Small and Very Light.

#### Example

```jsonc
// Reference: data/tfc/tfc/item_sizes/straw.json
{
    "ingredient": {
        "item": "tfc:straw"
    },
    "size": "small",
    "weight": "very_light"
}
```

<hr>

## Lamp Fuels

<hr>

## Metals

A metal specifies a new metal to be used by TFC. A metal is required in order to melt items into metal fluids, or use metals as ingredients in alloys. Notably, this **does not add new items or blocks** to the game, but only defines a metal to TFC, and how to translate it between fluids and metals. A metal is a file located in under the subfolder `metals`. It has the following properties:

- `tier`: An optional integer, of the tier of the metal. Defaults to `0`.
- `fluid`: The registry name of a fluid which corresponds to this metal.
- `melt_temperature`: A number. The melting temperature of the fluid of this metal.
- `heat_capacity`:  A number which specifies how fast this metal fluid heats up relative to others.

**Note** There must be a **unique** fluid for every metal. Creating multiple metals that reference the same fluid is liable to cause undefined behavior and may introduce bugs!

#### Example

```jsonc
// Reference: data/tfc/tfc/metals/bismuth_bronze.json
{
    "tier": 2,
    "fluid": "tfc:metal/bismuth_bronze",
    "melt_temperature": 985,
    "heat_capacity": 0.35
}
```

<hr>

## Supports
