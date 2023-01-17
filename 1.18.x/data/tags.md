---
layout: page
title: "Tags"
permalink: /1.18.x/data/tags/
---

# Tags

This page details all the tags that TFC adds, and uses for various functions. These have been separated out into [Block Tags](#block-tags), [Fluid Tags](#fluid-tags), and [Item Tags](#item-tags).

## Block Tags

Tag Id | Function
---|---
`tfc:can_trigger_collapse` | Blocks which when mined will search a nearby area for potential blocks that can **start** a collapse.
`tfc:can_start_collapse` | Blocks which can form the epicenter of a collapse. Without a start, a collapse cannot occur.
`tfc:can_collapse` | Blocks which, once a collapse has **started**, can collapse as part of the destruction. Must also have a valid [Collapse Recipe](../recipes/#collapse) defined for this block.
`tfc:can_landslide` | Blocks which can landslide to below or adjacent blocks, and are affected by gravity. Must also have a valid [Landslide Recipe](../recipes/#landslide) defined for this block.
`tfc:supports_landslide` | Blocks which are not full blocks, but count as full blocks when determining if an adjacent block might support a block against landsliding. Blocks cannot landslide when they are supported on at least two sides.
`tfc:toughness_1` | Blocks which are defined to have toughness 1 (Default for blocks without any tag is 0). Falling blocks are able to break non solid blocks with a equal or lesser toughness than the falling block. 
`tfc:toughness_2` | Blocks which are defined to have toughness 2 (Default for blocks without any tag is 0). Falling blocks are able to break non solid blocks with a equal or lesser toughness than the falling block.
`tfc:toughness_3` | Blocks which are defined to have toughness 3 (Default for blocks without any tag is 0). Falling blocks are able to break non solid blocks with a equal or lesser toughness than the falling block.
`tfc:tree_grows_on` | Blocks which a tree is able to spawn on, during world generation.
`tfc:bush_plantable_on` | Blocks which many plants, including bushes, fruit trees, and seasonal plants are able to spawn on, during world generation.
`tfc:single_block_replaceable` | Single blocks which can be replaced during world generation by other features, such as single block plants or grasses.
`tfc:sea_bush_plantable_on` | Blocks which many underwater plants are able to spawn on, during world generation.
`tfc:creeping_plantable_on` | Blocks which creeping plants are able to spawn on, during world generation.
`tfc:thatch_bed_thatch` | Blocks which count as valid `thatch` blocks when trying to make a thatch bed.
`tfc:can_be_snow_piled` | Blocks which can be hidden by snow formation. Can include both single blocks and two-tall plant blocks.
`tfc:can_be_ice_piled` | Blocks which can be hidden by ice formation. Can include both blocks in the ice and immediately above (i.e. lily pads)
`tfc:breaks_when_isolated` | When surrounded on all sides by air blocks, this will pop off as an item upon being updated.
`tfc:lit_by_dropped_torch` | Blocks which, when a torch item entity is dropped on them, might start a fire atop them,
`tfc:charcoal_cover_whitelist` | Blocks that are automatically considered valid cover blocks by a charcoal pit.
`tfc:forge_insulation` | Blocks which serve as the five external insulation blocks of a forge.
`tfc:forge_invisible_whitelist` | Blocks that the forge will treat like air for the purposes of finding their chimney, for example crucibles
`tfc:bloomery_insulation` | Blocks that can be used in the bloomery`s main structure.
`tfc:blast_furnace_insulation` | Blocks that can be used in the blast furnace`s main structure.
`tfc:scraping_surface` | Blocks which can act as a flat surface for a [Scraping Recipe](../recipes/#scraping) to be performed on.
`tfc:can_carve` | Blocks that can be replaced by things like caves and ravines during world generation.
`tfc:logs_that_log` | Log blocks which can be felled as trees, using TFC`s tree chopping functionality.
`tfc:needs_stone_tool` | Blocks that need a stone tool to mine.
`tfc:needs_copper_tool` | Blocks that need a copper tool to mine.
`tfc:needs_bronze_tool` | Blocks that need a bronze tool to mine.
`tfc:needs_wrought_iron_tool` | Blocks that need a wrought iron tool to mine.
`tfc:needs_steel_tool` | Blocks that need a steel tool to mine.
`tfc:needs_black_steel_tool` | Blocks that need a black steel tool to mine.
`tfc:needs_colored_steel_tool` | Blocks that need a red or blue steel tool to mine.
`tfc:prospectable` | Blocks which can be found with the prospectors pick. When found, they will display a message with the translation key `<block translation key>.prospected`.
`tfc:can_be_panned` | Blocks that can be picked up with a pan. Note that this does not necessarily mean that the anything will be dropped upon using the pan.
`tfc:prospectable` | Blocks that can be found with a prospector`s pick
`tfc:converts_to_humus` | Blocks that, when covered in snow and melted in the spring, get replaced with a humus block.
`tfc:wild_crop_grows_on` | Blocks that wild crops can be placed or found on
`tfc:farmland` | Farmland blocks. Used in some checks for block placement.
`tfc:powder_snow_replaceable` | Blocks that can be replaced by patches of powder snow during worldgen.
`tfc:creates_upward_bubbles` | Blocks that create upward bubble columns above them when placed. Note that this tag alone is not enough to cause this functionality, this is only for pre-existing blocks.
`tfc:creates_downward_bubbles` | Blocks that create downward bubble columns.
`tfc:rabbit_raidable` | Blocks that rabbits will attempt to destroy
`tfc:fox_raidable` | Blocks that foxes will attempt to eat berries off of. This only applies to blocks that function like TFC berry bushes.

<hr>

## Fluid Tags

Tag Id | Function
---|---
`tfc:mixable` | Fluids that will mix together if they come in contact in the world.
`tfc:hydrating` | Fluids that hydrate farmland, berry bushes, and other growing things
`tfc:scribing_ink` | Fluids that can be used in the scribing table.
`tfc:usable_in_pot` | Fluids that can be in a firepit's pot
`tfc:usable_in_jug` | Fluids that can be in a jug
`tfc:usable_in_wooden_bucket` | Fluids that can be in a wooden bucket.
`tfc:usable_in_red_steel_bucket` | Fluids that can be in a red steel bucket.
`tfc:usable_in_blue_steel_bucket` | Fluids that can be in a blue steel bucket.
`tfc:usable_in_barrel` | Fluids that can be in a barrel.
`tfc:usable_in_sluice` | Fluids that can flow through a sluice.
`tfc:usable_in_ingot_mold` | Fluids that can be placed in a ingot mold. (In TFC, all molten metals)
`tfc:usable_in_tool_head_mold` | Fluids that can be placed in a tool head mold. (In TFC, only tool metals)

<hr>

## Item Tags

Tag Id | Function
---|---
`tfc:thatch_bed_hides` | Items which when right clicked on two `#tfc:thatch_bed_thatch` blocks, will form a thatch bed.
`tfc:firepit_kindling` | Items which are valid **kindling** for creating a Firepit with a fire starter. More kindling increases the chance of success.
`tfc:firepit_sticks` | Items which are valid **sticks** for creating a Firepit with a fire starter. A firepit requires three sticks to be created.
`tfc:firepit_logs` | Items which are valid **logs** for creating a Firepit with a fire starter. A firepit require one log, which will be immediately inserted as the first [Fuel](../custom/#fuels) item of the Firepit.
`tfc:starts_fires_with_durability` | Items which when right clicked, can start fires at the cost of durability like Flint and Steel. These items can then be used on most light-able TFC devices (firepit, forge, etc.).
`tfc:starts_fires_with_items` | Items which when right clicked, can start fires at the cost of the item itself like Fire Charges. These items can then be used on most light-able TFC devices (firepit, forge, etc.).
`tfc:extinguisher` | Items which can be used on a fire pit to put out the fire.
`tfc:log_pile_logs` | Items which are able to be placed into a log pile.
`tfc:pit_kiln_straw` | Items which are valid for the eight straw layers of a pit kiln.
`tfc:pit_kiln_logs` | Items which are valid for the eight log layers of a pit kiln.
`tfc:can_be_lit_on_torch` | Items which, when right clicked on a lit torch, can be lit into a torch themselves.
`tfc:firepit_fuel` | Items that are valid [Fuels](../custom/#fuels) for the Firepit.
`tfc:forge_fuel` | Items that are valid [Fuels](../custom/#fuels) for the Charcoal Forge.
`tfc:blast_furnace_fuel` | Items that are valid [Fuels](../custom/#fuels) for the Blast Furnace.
`tfc:handstone` | Items that are valid hand stones for a Quern.
`tfc:scrapable` | Items that can be placed flat on a block, with a valid [Scraping Recipe](../recipes/#scraping).
`tfc:knives` | Items that are knives
`tfc:hoes` | Items that are hoes
`tfc:hammers` | Items that are hammers
`tfc:chisels` | Items that are chisels. Required for chiseling functionality.
`tfc:flux` | Items that are usable as the catalyst ingredient for welding.
`tfc:tuyeres` | Items that can go in the Blast Furnace`s tuyere slot.
`tfc:rock_knapping` | Items that can be right clicked to knap, with a valid [Rock Knapping Recipe](../recipes/#rock-knapping).
`tfc:clay_knapping` | Items that can be right clicked to knap, with a valid [Clay Knapping Recipe](../recipes/#knapping).
`tfc:fire_clay_knapping` | Items that can be right clicked to knap, with a valid [Fire Clay Knapping Recipe](../recipes/#knapping).
`tfc:leather_knapping` | Items that can be right clicked to knap, with a valid [Leather Knapping Recipe](../recipes/#knapping).
`tfc:axes_that_log` | Tools that can be used to fell entire trees, via TFC`s tree chopping functionality.
`tfc:bush_cutting_tools` | Tools that can be right-clicked on berry bushes to get cuttings from them.
`tfc:compost_greens` | Items that are considered `green` items by the composter.
`tfc:compost_browns` | Items that are considered `brown` items by the composter.
`tfc:compost_poisons` | Items that poison compost, making it unusable.
`tfc:usable_on_tool_rack` | Tools that can be placed onto a tool rack.
`tfc:usable_in_powder_keg` | Items that are considered gunpowder for purposes of the powderkeg.
`tfc:soup_bowls` | Items that can be transformed into soup. Typically bowls.
`tfc:salad_bowls` | Items that can be clicked to make salad.
`tfc:usable_in_salad` | Items that are allowed in a salad.
`tfc:scribing_ink` | Items that are allowed in the ink slot of a scribing table.
`tfc:sandwich_bread` | Items that are considered bread for the purposes of sandwiches. These items are weighted slightly differently in the bread nutrition calculation and also have a specific place in the bread crafting recipe.
`tfc:small_fishing_bait` | Items that can be used as bait to catch small fish.
`tfc:large_fishing_bait` | Items that can be used as bait to catch large fish.
`tfc:holds_small_fishing_bait` | Fishing rods that can hold only small fishing bait.
`tfc:holds_large_fishing_bait` | Fishing rods that can hold small or large fishing bait.
`tfc:can_be_salted` | Items that can be crafted with salt.
`tfc:pileable_ingots` | Items that can be added to ingot piles. In order to add another item to an ingot pile, it must (1) be in this tag, (2) have a metal defined with the `ingot` field matching said item, and (3) likely needs a properly loaded [metal texture](../custom/#adding-textures).
`tfc:pileable_sheets` | Items that can be added to sheet piles. In order to add another item to an sheet pile, it must (1) be in this tag, (2) have a metal defined with the `sheet` field matching said item, and (3) likely needs a properly loaded [metal texture](../custom/#adding-textures).
`tfc:fox_spawns_with` | Items that a fox has a small chance of spawning with in its mouth.
`tfc:mob_feet_armor` | Armor that monsters can spawn with on their feet.
`tfc:mob_leg_armor` | Armor that monsters can spawn with on their legs.
`tfc:mob_chest_armor` | Armor that monsters can spawn with on their chest.
`tfc:mob_head_armor` | Armor that monsters can spawn with on their head.
`tfc:mob_mainhand_weapons` | Items that monsters can spawn with in their main hand.
`tfc:mob_offhand_weapons` | Items that monsters can spawn with in their off hand.
`tfc:deals_slashing_damage` | Weapons that deal slashing damage.
`tfc:deals_piercing_damage` | Weapons that deal piercing damage.
`tfc:deals_crushing_damage` | Weapons that deal crushing damage.

<hr>

## Entity Tags

Tag Id | Function
---|---
`tfc:turtle_friends` | Entities that turtles do not fear and will follow around curiously.
`tfc:spawns_on_cold_blocks` | Entities that can spawn on snow or ice.
`tfc:destroys_floating_plants` | Entities that destroy floating plants on contact. Essentially, boats.
`tfc:bubble_column_immune` | Entities which TFC bubble columns do not move
`tfc:needs_large_fishing_bait` | Entities that need large fishing bait to catch.
`tfc:hunts_land_prey` | Entities that are feared by land prey. Note that this tag does NOT add hunting functionality to an arbitrary entity.
`tfc:hunted_by_land_predators` | Entities that land predators will attempt to hunt.
`tfc:vanilla_monsters` | Monsters that are prevented from spawning on the surface.
`tfc:deals_slashing_damage` | Entities that deal slashing damage.
`tfc:deals_piercing_damage` | Entities that deal piercing damage.
`tfc:deals_crushing_damage` | Entities that deal crushing damage.
