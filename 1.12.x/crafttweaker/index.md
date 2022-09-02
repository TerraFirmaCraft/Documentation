---
layout: page
title: "Craft Tweaker Integration"
permalink: /1.12.x/crafttweaker/
excluded_in_search: true
---

# Craft Tweaker Integration

We provide many Craft Tweaker hooks for all recipes and item capabilities. For information on a specific recipe type, consult the page for that type:

#### [Alloy Recipes](alloys/)

- Used to add alloy recipes.
- Any metal can only have **one** alloy recipe for it.
- Import: `mods.terrafirmacraft.Alloy`

#### [Anvil Recipes](anvil/)

- Used to add anvil working recipes.
- Ingredients **do not need** to be *heatable* - if not, they are treated as "cold forging" recipes.
- Ingredients **do** need to be *forgeable*. Consult [Item Capabilities](items/) for more information.
- Import: `mods.terrafirmacraft.Anvil`

#### [Welding Recipes](welding/)

- Used to add anvil welding recipes.
- Import: `mods.terrafirmacraft.Welding`

#### [Barrel Recipes](barrel/)

- Used to add barrel conversion recipes.
- These can take either items, fluids, or both as input, and return either items, fluids or both.
- Setting a recipe to have a duration of `0` makes it an instant recipe. **Note:** instant recipes are limited by the fluid ingredient. Normal recipes will consume the greatest common multiple of both ingredients.
- Import: `mods.terrafirmacraft.Barrel`

#### [Chisel Recipes](chisel/)

- To add chisel *smoothing* recipes, only.
- In order to add stair or slab recipes, you must add vanilla crafting recipes in the standard stair and slab patterns.
- Import: `mods.terrafirmacraft.Chisel`

#### [Loom Recipes](loom/)

- Used to add loom recipes.
- May require a custom texture to be displayed on the loom
- Import: `mods.terrafirmacraft.Loom`

#### [Item Heating](heating/)

- Used to add heat transformation recipes (e.g. food cooking, metal melting)
- Import: `mods.terrafirmacraft.Heating`

#### [Quern Recipes](quern/)

- Used to add recipes to the Quern
- Import: `mods.terrafirmacraft.Quern`

#### [Knapping Recipes](knapping/)

- Used for simple knapping types (Clay, Fire clay, Leather)
- Addons are able to add their own knapping types, but must handle the GUI and interaction themselves.
- There is a different import based on which knapping type you want:
  - Clay Import: `mods.terrafirmacraft.ClayKnapping`
  - Fire Clay Import: `mods.terrafirmacraft.FireClayKnapping`
  - Leather Import: `mods.terrafirmacraft.LeatherKnapping`

#### [Stone Knapping Recipes](stone-knapping/)

- Used for stone knapping recipes
- These are a bit different as they may produce different results on different rock types, and are used by any subset of all rock types.
- Import: `mods.terrafirmacraft.StoneKnapping`

#### [Item Capabilities](items/)

- Used to add capabilities (Heat, Forgeable, Food, Size, etc.) to external items so they are usable in TFC systems.
- Import: `mods.terrafirmacraft.ItemRegistry`
