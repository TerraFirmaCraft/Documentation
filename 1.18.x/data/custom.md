---
layout: page
title: "Custom Data"
permalink: /1.18.x/data/custom/
---

# Custom Data

In addition to recipes, TFC defines and loads a number of completely custom data types. These can also be loaded by datapacks, and all are under the root path `tfc`, meaning that any added data should be located under `/data/<your mod id>/tfc/<subfolder>/...`.

TFC defines the following custom data types:

<!-- Alphabetical Order Please -->

- [Drinkables](#drinkables)
- [Fertilizers](#fertilizers)
- [Food Items](#food-items)
- [Fuels](#fuels)
- [Item Heats](#item-heats)
- [Item Sizes](#item-sizes)
- [Lamp Fuels](#lamp-fuels)
- [Metals](#metals)
- [Supports](#supports)

<hr>

## Drinkables

A drinkable defines that a fluid is directly drinkable. Drinkable fluids can be drank either from an empty hand while right clicking on a source block, or from a container such as the ceramic vessel which allows drinking. The drinkable also defines various effects that the fluid can have on the player when drank. It is located under the subfolder `drinkables`. 

When drinking from a source block, the player consumes 25 mB of the drinkable. Other sources, such as ceramic jugs, consume larger quantities. Note that some drinkable effects are all scaled based on the amount drank.

A drinkable has the following properties:

- `ingredient`: An [Fluid Ingredient](../common-types/#fluid-ingredients), which defines which fluids this drinkable applies to.
- `consume_chance`: An optional number in the range [0, 1] (Default: 0). It represents the chance that, when drank from a source block, the source block is removed.
- `thirst`: An optional integer in the range [0, 100] (Default: 0). It represents an amount of thirst that this drinkable consumes, per 25 mB drank.
- `intoxication`: An optional integer (Default: 0). It represents a number of ticks that the player will be intoxicated for, per 25 mB drank.
- `effects` is a array of custom potion effects that this drinkable can apply. Each entry must be an object with the following properties:
  - `type`: A string, which is the registry ID of a potion effect (i.e. `minecraft:slowness`).
  - `duration`: An optional integer (Default: 20) which is a number of ticks this effect is applied for.
  - `amplifier`: An optional integer (Default: 0) which is the level of the potion effect applied.
  - `chance`: An optional number in the range [0, 1] (Default: 1). This represents the chance that this particular effect will be applied per 25 mB drank.

#### Example:

```jsonc
// Reference: data/tfc/tfc/drinkables/alcohol.json
{
  "ingredient": {
    "tag": "tfc:alcohols"
  },
  "thirst": 10,
  "intoxication": 4000
}
```

<hr>

## Fertilizers

A fertilizer defines an item which can be used on farmland or crops to increase the nutrients in the soil (farmland). Nutrients are used and consumed by crops to increase their yield. It is located under the subfolder `fertilizers`. A fertilizer has the following properties:

- `ingredient`: An [Ingredient](../ingredients/), which defines which items this fertilizer applies to.
- `nitrogen`: A number (Default `0.0`). Defines how much <span style="color:#55FFFF">**Nitrogen**</span> nutrient this fertilizer adds.
- `phosphorus`: A number (Default `0.0`). Defines how much <span style="color:#FFAA00">**Phosphorous**</span> nutrient this fertilizer adds.
- `potassium`: A number (Default `0.0`). Defines how much <span style="color:#FF55FF">**Potassium**</span> nutrient this fertilizer adds.

#### Example

```jsonc
// Reference: data/tfc/tfc/fertilizers/bone_meal.json
{
    "ingredient": {
        "item": "minecraft:bone_meal"
    },
    "potassium": 0.1
}
```

<hr>

## Food Items

A food item definition defines a food, and applies TFC style stats to it including decay, hunger, water, and nutrition. It is a file located under the subfolder `food_items`. It has the following properties:

- `ingredient`: An [Ingredient](../ingredients/) to which this food item definition applies to.
- `hunger`: An integer (Default `4`). Defines how much hunger this food restores. The player's full hunger bar is equal to `20`.
- `saturation`: A number (Default `0.0`). Defines how much saturation this food restores. Measured in the same units as hunger.
- `water`: A number (Default `0.0`). Defines how much water this food restores. The player's full water bar is equal to `100`.
- `decay_modifier`: A number (Default `1.0`). Defines how quickly this item decays. Higher values indicate faster decay, and thus shorter expiration times.
- `grain`: A number (Default `0.0`). Defines how much <span style="color:#FFAA00">**Grain**</span> nutrient this food adds.
- `fruit`: A number (Default `0.0`). Defines how much <span style="color:#55FF55">**Fruit**</span> nutrient this food adds.
- `vegetables`: A number (Default `0.0`). Defines how much <span style="color:#00AA00">**Vegetables**</span> nutrient this food adds.
- `protein`: A number (Default `0.0`). Defines how much <span style="color:#FF5555">**Protein**</span> nutrient this food adds.
- `dairy`: A number (Default `0.0`). Defines how much <span style="color:#AA00AA">**Dairy**</span> nutrient this food adds. 

**Note:** Typical values for nutrients are 0-2 for small items (fruits, vegetables), and 1-4 for larger items (breads, meats), and higher for meals. Note that nutrients should also scale with hunger: A 2 nutrient/4 hunger food is the same (nutritionally) as a 4 nutrient/8 hunger food.

<hr>

## Fuels

A fuel defines something that burns, and can be used in a fire pit, forge, or other TFC fuel consuming device. It is a file located under the subfolder `fuels`. It has the following properties:

- `ingredient`: An [Ingredient](../ingredients/) to which this item size definition applies to.
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

- `ingredient`: An [Ingredient](../ingredients/) to which this item size definition applies to.
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

A lamp fuel is a fluid which an be used in a lamp. It will burn over time, consuming mB per tick in order to keep the lamp lit. It has the following properties:

- `fluid`: A [Fluid Ingredient](../common-types/#fluid-ingredients) which determines which fluids this lamp fuel applies to.
- `valid_lamps`: A [Block Ingredient](../common-types#block-ingredients) which determines what (lamp) blocks are valid for this fuel to be added to.
- `burn_rate` An integer, representing how fast this lamp consumes fuel, in ticks per mB.

#### Example

```jsonc
// Reference: data/tfc/tfc/lamp_fuels/olive_oil.json
{
    "fluid": "tfc:olive_oil",
    "valid_lamps": {
        "type": "tfc:tag",
        "tag": "tfc:lamps"
    },
    "burn_rate": 8000
}
```

<hr>

## Metals

A metal specifies a new metal to be used by TFC. A metal is required in order to melt items into metal fluids, or use metals as ingredients in alloys. Notably, this **does not add new items or blocks** to the game, but only defines a metal to TFC, and how to translate it between fluids and metals. A metal is a file located in under the subfolder `metals`. It has the following properties:

- `tier`: An optional integer, of the tier of the metal. Defaults to `0`.
- `fluid`: The registry name of a fluid which corresponds to this metal.
- `melt_temperature`: A number. The melting temperature of the fluid of this metal.
- `heat_capacity`:  A number which specifies how fast this metal fluid heats up relative to others.
- `ingots`: An [Ingredient](../ingredients/) which defines ingot items that are of this metal. This is used in order to allow other mod ingots to be placed in ingot piles.
- `sheets`: An [Ingredient](../ingredients/) which defines sheet items that are of this metal. This is used in order to allow other mod sheets to be placed in sheet piles.

**Note** There must be a **unique** fluid for every metal. Creating multiple metals that reference the same fluid is liable to cause undefined behavior and may introduce bugs!

##### Adding Textures

Each metal references a hardcoded texture location, by the name `tfc:block/metal/full/<the metal name>`. For example, `bismuth_bronze` references the texture at `tfc/textures/block/metal/full/bismuth_bronze.png`. This texture is then used to render both ingot piles and sheet piles. When providing an external texture (i.e. via a resource pack), if the ingot and/or sheet pile is showing up as a missing texture, it is likely because it isn't added to the atlas used to draw the texture. In order to do this automatically, in the `tfc-client-config.toml` file, add the texture as entry to this list (In `tfc:block/metal/full/<the metal name>` format).

#### Example

```jsonc
// Reference: data/tfc/tfc/metals/bismuth_bronze.json
{
    "tier": 2,
    "fluid": "tfc:metal/bismuth_bronze",
    "melt_temperature": 985,
    "heat_capacity": 0.35,
    "ingots": {
        "tag": "forge:ingots/bismuth_bronze"
    },
    "sheets": {
        "tag": "forge:sheets/bismuth_bronze"
    }
}
```

<hr>

## Supports

Supports define blocks which prevent collapses from **starting** within a specific radius. They do not prevent collapses that started outside the support radius from causing blocks to collapse within the supported area. A support is a file located in under the subfolder `supports`. It has the following properties:

- `ingredient`: A [Block Ingredient](../common-types/#block-ingredients) which defines what blocks this support applies to.
- `support_up`: Integer (Default `0`). The number of blocks upwards that this block supports.
- `support_down`: Integer (Default `0`). The number of blocks downwards that this block supports.
- `support_horizontal`: Integer (Default `0`). The number of blocks horizontally that this block supports.

#### Example

```jsonc
// Reference: data/tfc/tfc/supports/ash.json
{
    "ingredient": "tfc:wood/horizontal_support/ash",
    "support_up": 1,
    "support_down": 1,
    "support_horizontal": 4
}
```
