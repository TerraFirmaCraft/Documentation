---
layout: page
title: "WorldGen Tags"
permalink: /1.21.x/worldgen/tags/
---

This page details all the world generation tags TFC adds. For generic tags, see [Tags](../../tags/).

## Biome Tags

| Tag Id                      | Function                                       |
|-----------------------------|------------------------------------------------|
| `tfc:burrens`               | All variants of burren.                        |
| `tfc:cenotes`               | All variants of cenotes.                       |
| `tfc:dolines`               | All variants of dolines.                       |
| `tfc:has_predictable_winds` | Biomes with trade winds (oceans).              |
| `tfc:is_lake`               | All variants of lakes, including underground.  |
| `tfc:is_ocean`              | All variants of oceans.                        |
| `tfc:is_river`              | All variants of rivers, including underground. |
| `tfc:is_volcanic`           | All volcanic biomes.                           |
| `tfc:karsts`                | All biomes that are of karst type.             |
| `tfc:shilins`               | All variants of shilin.                        |
| `tfc:tower_karsts`          | All biomes that are of tower karst type.       |

## Configured Feature Tags

| Tag Id                      | Function                                                                                                                                                          |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `tfc:dead_forest_trees`     | [Forest Entry Features](../worldgen/features/trees/#forest-entry) spawning in dead forests. Trees added to this feature are automatically added to the world.     |
| `tfc:forest_trees`          | [Forest Entry Features](../worldgen/features/trees/#forest-entry) spawning in regular forests. Trees added to this feature are automatically added to the world.  |
| `tfc:mangrove_forest_trees` | [Forest Entry Features](../worldgen/features/trees/#forest-entry) spawning in mangrove forests. Trees added to this feature are automatically added to the world. |

<hr>
## Placed Feature Tags

| Tag Id                                    | Function                                                                                                               |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| `tfc:feature/berry_bushes`                | All berry bush features.                                                                                               |
| `tfc:feature/boulders`                    | All boulder features.                                                                                                  |
| `tfc:feature/clay_indicators`             | All clay indicator plants.                                                                                             |
| `tfc:feature/corals`                      | All coral features.                                                                                                    |
| `tfc:feature/crops`                       | All crop features.                                                                                                     |
| `tfc:feature/forest_plants`               | Features restricted to forests.                                                                                        |
| `tfc:feature/fruit_trees`                 | All fruit tree features.                                                                                               |
| `tfc:feature/guano_islands`               | Features restricted to guano islands.                                                                                  |
| `tfc:feature/land_plants`                 | Tag holding most plant features.                                                                                       |
| `tfc:feature/ocean_decorations`           | Tag holding non-plant ocean features.                                                                                  |
| `tfc:feature/ocean_plants`                | Tag holding ocean plant features.                                                                                      |
| `tfc:feature/ore_deposits`                | All ore deposits.                                                                                                      |
| `tfc:feature/shield_volcanoes`            | Features that spawn on shield volcanoes.                                                                               |
| `tfc:feature/shore_decorations`           | Features that spawn on shores.                                                                                         |
| `tfc:feature/soil_discs`                  | All soil discs (clay, peat, etc.)                                                                                      |
| `tfc:feature/surface_flood_fill_lakes`    | A tag containing only the floodfill lakes feature.                                                                     |
| `tfc:feature/surface_grasses`             | A tag containing all short grass features.                                                                             |
| `tfc:feature/tide_pool_decorations`       | Tag holding features that spawn in tide pools.                                                                         |
| `tfc:feature/tuyas`                       | Features restricted to tuyas.                                                                                          |
| `tfc:feature/volcanoes`                   | Features restricted to volcanoes.                                                                                      |
| `tfc:in_biome/all_lakes`                  | All lake features, including those in `tfc:in_biome/underground_lakes`.                                                |
| `tfc:in_biome/erosion`                    | A tag which just contains the `tfc:erosion` feature.                                                                   |
| `tfc:in_biome/strongholds`                | Empty.                                                                                                                 |
| `tfc:in_biome/surface_structures`         | Empty.                                                                                                                 |
| `tfc:in_biome/top_layer_modification`     | Features placed in the top layer modification step.                                                                    |
| `tfc:in_biome/underground_decoration`     | Features placed in the underground decoration step.                                                                    |
| `tfc:in_biome/underground_lakes`          | Only underground lake features.                                                                                        |
| `tfc:in_biome/underground_structures`     | Features placed in the underground structures step.                                                                    |
| `tfc:in_biome/veins`                      | Features placed in the ore veins step.                                                                                 |
| `tfc:in_biome/large_features/<biome>`     | Where `<biome>` is the registry name of a TFC biome, the features placed in that biome in the large features step.     |
| `tfc:in_biome/soil_discs/<biome>`         | Where `<biome>` is the registry name of a TFC biome, the features placed in that biome in the soil discs step.         |
| `tfc:in_biome/surface_decoration/<biome>` | Where `<biome>` is the registry name of a TFC biome, the features placed in that biome in the surface decoration step. |
