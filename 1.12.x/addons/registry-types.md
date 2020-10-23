---
layout: page
title: "Pre-Block Registry Types"
permalink: /1.12.x/addons/registry-types/
---

# Pre-Block Registry Types

TFC does some hackery (read: it fires specific events at the highest priority during `RegistryEvent.Registry<Block>`), in order to collect an amount of type objects (Metals, Rocks, Ores, etc.) in order for TFC to generate every possible permutation and cartesian product of a block or item required.

In this manner, addons can add these types simply by registering one of the pre-block registry types, and then TFC will handle registration of all required blocks and items, and it will just work^(tm).

In order to use this system, an addon must:

- Subscribe to `TFCRegistryEvent.RegisterPreBlock<T>` for the required type (e.g. `Metal`, `Tree`, `Rock`, ...)
- Register objects *to the `tfc` namespace* describing properties of your type.
- Provide the necessary assets (including recipes, models, blockstates, etc.) for all new blocks and items TFC will generate.

In TFC, these types can be found under the `net.dries007.tfc.api.types`. Default TFC registrations can be found under `net.dries007.tfc.types.Default[Foo]s`.

## Metals

The following is an example of using this system to add a metal to TFC. There are several main properties of metals that influence what items and blocks will get registered:

1. Usability
  - If the metal is able to be used to create common components such as dust, sheets, double ingots, anvils, lamps, etc.
  - Example: High Carbon Black Steel is not usable, Black Steel is.
2. Castable
  - If the metal is at most Tier II, it is able to be casted into a mold. This doesn't register any additional items, but it does require additional assets for the mold
  - Example: Bronze is castable, Wrought Iron is not.
3. Tool Metal
  - If the metal is able to be made into tools and armor, including all components for those two.
  - Example: Bronze is a tool metal, Bismuth is not.

TFC will register the models for any items added automatically via this system. As such, if you expect to fit with TFC, you should provide the following resource files. In this case, `[metal]` should be replaced with the registry path name of the metal in question. (Note: the contents, textures, and organization can be changed if needed. This is just one way to provide all necessary resources. I have included recipes in with the resources, as in order for the metal to function identical to other TFC metals, they are necessary, however they aren't strictly necessary in order for the models to all resolve properly.)

All JSON files can be modified from ones found [here](https://github.com/TerraFirmaCraft/TerraFirmaCraft/tree/1.12.x/src/main/resources/assets). Ther're for 1.12, and if you're looking for other minecraft versions, switch to other branches.

### Required for ALL metals

```
tfc\blockstates\fluid\[metal].json
tfc\models\item\metal\ingot\[metal].json
tfc\textures\blocks\metal\[metal].png
```

### Required for CASTABLE metals

```
tfc\models\item\ceramics\fired\mold\ingot\[metal].json
tfc\textures\items\ceramics\fired\mold\ingot\[metal].png
tfc\textures\items\metal\ingot\[metal].png
```

### Required for USABLE metals

```
tfc\blockstates\sheet\[metal].json
tfc\models\item\ceramics\fired\mold\ingot\[metal].json
tfc\models\item\metal\double_ingot\[metal].json
tfc\models\item\metal\double_sheet\[metal].json
tfc\models\item\metal\dust\[metal].json
tfc\models\item\metal\lamp\[metal].json
tfc\models\item\metal\nugget\[metal].json
tfc\models\item\metal\scrap\[metal].json
tfc\models\item\metal\sheet\[metal].json
tfc\textures\items\ceramics\fired\mold\ingot\[metal].png
tfc\textures\items\metal\double_ingot\[metal].png
tfc\textures\items\metal\double_sheet\[metal].png
tfc\textures\items\metal\dust\[metal].png
tfc\textures\items\metal\ingot\[metal].png
tfc\textures\items\metal\lamp\[metal].png
tfc\textures\items\metal\nugget\[metal].png
tfc\textures\items\metal\scrap\[metal].png
tfc\textures\items\metal\sheet\[metal].png
```

### Required for TOOL metals

```
tfc\blockstates\anvil\[metal].json
tfc\models\item\metal\anvil\[metal].json
tfc\models\item\metal\axe\[metal].json
tfc\models\item\metal\axe_head\[metal].json
tfc\models\item\metal\boots\[metal].json
tfc\models\item\metal\chestplate\[metal].json
tfc\models\item\metal\chisel\[metal].json
tfc\models\item\metal\chisel_head\[metal].json
tfc\models\item\metal\greaves\[metal].json
tfc\models\item\metal\hammer\[metal].json
tfc\models\item\metal\hammer_head\[metal].json
tfc\models\item\metal\helmet\[metal].json
tfc\models\item\metal\hoe\[metal].json
tfc\models\item\metal\hoe_head\[metal].json
tfc\models\item\metal\javelin\[metal].json
tfc\models\item\metal\javelin_head\[metal].json
tfc\models\item\metal\knife\[metal].json
tfc\models\item\metal\knife_blade\[metal].json
tfc\models\item\metal\mace\[metal].json
tfc\models\item\metal\mace_head\[metal].json
tfc\models\item\metal\pick\[metal].json
tfc\models\item\metal\pick_head\[metal].json
tfc\models\item\metal\propick\[metal].json
tfc\models\item\metal\propick_head\[metal].json
tfc\models\item\metal\saw\[metal].json
tfc\models\item\metal\saw_blade\[metal].json
tfc\models\item\metal\scythe\[metal].json
tfc\models\item\metal\scythe_blade\[metal].json
tfc\models\item\metal\shears\[metal].json
tfc\models\item\metal\shield\[metal].json
tfc\models\item\metal\shield\[metal]_blocking.json
tfc\models\item\metal\shovel\[metal].json
tfc\models\item\metal\shovel_head\[metal].json
tfc\models\item\metal\sword\[metal].json
tfc\models\item\metal\sword_blade\[metal].json
tfc\models\item\metal\tuyere\[metal].json
tfc\models\item\metal\unfinished_boots\[metal].json
tfc\models\item\metal\unfinished_chestplate\[metal].json
tfc\models\item\metal\unfinished_greaves\[metal].json
tfc\models\item\metal\unfinished_helmet\[metal].json
tfc\recipes\metal\[metal]\[metal]_anvil.json
tfc\recipes\metal\[metal]\[metal]_axe.json
tfc\recipes\metal\[metal]\[metal]_chisel.json
tfc\recipes\metal\[metal]\[metal]_hammer.json
tfc\recipes\metal\[metal]\[metal]_hoe.json
tfc\recipes\metal\[metal]\[metal]_javelin.json
tfc\recipes\metal\[metal]\[metal]_knife.json
tfc\recipes\metal\[metal]\[metal]_mace.json
tfc\recipes\metal\[metal]\[metal]_pick.json
tfc\recipes\metal\[metal]\[metal]_propick.json
tfc\recipes\metal\[metal]\[metal]_saw.json
tfc\recipes\metal\[metal]\[metal]_scythe.json
tfc\recipes\metal\[metal]\[metal]_shovel.json
tfc\recipes\metal\[metal]\[metal]_sword.json
tfc\textures\items\metal\anvil\[metal].png
tfc\textures\items\metal\axe\[metal].png
tfc\textures\items\metal\axe_head\[metal].png
tfc\textures\items\metal\boots\[metal].png
tfc\textures\items\metal\chestplate\[metal].png
tfc\textures\items\metal\chisel\[metal].png
tfc\textures\items\metal\chisel_head\[metal].png
tfc\textures\items\metal\greaves\[metal].png
tfc\textures\items\metal\hammer\[metal].png
tfc\textures\items\metal\hammer_head\[metal].png
tfc\textures\items\metal\helmet\[metal].png
tfc\textures\items\metal\hoe\[metal].png
tfc\textures\items\metal\hoe_head\[metal].png
tfc\textures\items\metal\javelin\[metal].png
tfc\textures\items\metal\javelin_head\[metal].png
tfc\textures\items\metal\knife\[metal].png
tfc\textures\items\metal\knife_blade\[metal].png
tfc\textures\items\metal\mace\[metal].png
tfc\textures\items\metal\mace_head\[metal].png
tfc\textures\items\metal\pick\[metal].png
tfc\textures\items\metal\pick_head\[metal].png
tfc\textures\items\metal\propick\[metal].png
tfc\textures\items\metal\propick_head\[metal].png
tfc\textures\items\metal\saw\[metal].png
tfc\textures\items\metal\saw_blade\[metal].png
tfc\textures\items\metal\scythe\[metal].png
tfc\textures\items\metal\scythe_blade\[metal].png
tfc\textures\items\metal\shears\[metal].png
tfc\textures\items\metal\shield\[metal].png
tfc\textures\items\metal\shovel\[metal].png
tfc\textures\items\metal\shovel_head\[metal].png
tfc\textures\items\metal\sword\[metal].png
tfc\textures\items\metal\sword_blade\[metal].png
tfc\textures\items\metal\tuyere\[metal].png
tfc\textures\models\armor\[metal]_layer_1.png
tfc\textures\models\armor\[metal]_layer_2.png
```

### Required for TOOL AND CASTABLE metals

```
tfc\models\item\ceramics\fired\mold\axe_head\[metal].json
tfc\models\item\ceramics\fired\mold\chisel_head\[metal].json
tfc\models\item\ceramics\fired\mold\hammer_head\[metal].json
tfc\models\item\ceramics\fired\mold\hoe_head\[metal].json
tfc\models\item\ceramics\fired\mold\javelin_head\[metal].json
tfc\models\item\ceramics\fired\mold\knife_blade\[metal].json
tfc\models\item\ceramics\fired\mold\mace_head\[metal].json
tfc\models\item\ceramics\fired\mold\pick_head\[metal].json
tfc\models\item\ceramics\fired\mold\propick_head\[metal].json
tfc\models\item\ceramics\fired\mold\saw_blade\[metal].json
tfc\models\item\ceramics\fired\mold\scythe_blade\[metal].json
tfc\models\item\ceramics\fired\mold\shovel_head\[metal].json
tfc\models\item\ceramics\fired\mold\sword_blade\[metal].json
tfc\textures\items\ceramics\fired\mold\axe_head\[metal].png
tfc\textures\items\ceramics\fired\mold\chisel_head\[metal].png
tfc\textures\items\ceramics\fired\mold\hammer_head\[metal].png
tfc\textures\items\ceramics\fired\mold\hoe_head\[metal].png
tfc\textures\items\ceramics\fired\mold\javelin_head\[metal].png
tfc\textures\items\ceramics\fired\mold\knife_blade\[metal].png
tfc\textures\items\ceramics\fired\mold\mace_head\[metal].png
tfc\textures\items\ceramics\fired\mold\pick_head\[metal].png
tfc\textures\items\ceramics\fired\mold\propick_head\[metal].png
tfc\textures\items\ceramics\fired\mold\saw_blade\[metal].png
tfc\textures\items\ceramics\fired\mold\scythe_blade\[metal].png
tfc\textures\items\ceramics\fired\mold\shovel_head\[metal].png
tfc\textures\items\ceramics\fired\mold\sword_blade\[metal].png
```
