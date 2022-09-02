---
layout: page
title: "Fruit Trees"
permalink: /1.12.x/addons/fruit-trees/
excluded_in_search: true
---

# Adding Fruit Trees

The TFC world generator can be made to accept any fruit tree from an implementation `IFruitTree`. The easiest way to do this is to create an enum that copies the methods in `FruitTree`. The only parameter from the `FruitTree` enum that won't work out of the box is `fruit`, which has to be modified to talk with `IFruitTree.getAllDrops` properly.

Declaring your custom fruit tree for generation can be done in that same enum with `static { WorldGenFruitTrees.register(tree) };` where `tree` is your `IFruitTree`.

### Registering your Blocks

There are four blocks fruit trees require, each of which can be registered under your own mod's namespace and only require your `IFruitTree` in the constructor. These are `BlockFruitTreeBranch`, `BlockFruitTreeLeaves`, `BlockFruitTreeSapling`, and `BlockFruitTreeTrunk`. The leaves and sapling should also be registered as an `ItemBlock`.

### Getting your models ready

Make sure to copy and modify as you need the blockstate files from TFC for your branch, leaves, sapling, and trunk blocks. To avoid your leaves being pink and black, there's an extra step. In your subscription to `registerModels` use `setCustomStateMapper` to ignore`BlockFruitTreeLeaves.DECAYABLE` and `BlockFruitTreeLeaves.HARVESTABLE`


Lastly, setup your block color handler for your leaves. TFC uses its own color handler, which you can grab by setting an `IFoliageColor` equal to `GrassColorHandler::computeGrassColor;` in the proper client registry event.

### Adding the tree structure

While you can generate a fruit tree structure the way TFC does with nbtlib, if you only have a few trees it's easier to construct one yourself with a little trickery. Under TFC's assets, copy a fruit tree structure from `tfc/structures/fruit_trees/` and copy it into your own mod's assets folder into the *same exact namespace*. Rename it to what the name of your fruit tree is. Use [NBTExplorer](https://github.com/jaquadro/NBTExplorer/releases) to edit the entries in the `palette` section of the NBT file to match your mod's blocks.
