# Used by:
# Implants named like: Low grade Harvest (5 of 6)
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Frequency Mining Laser",
                                  "maxRange", implant.getModifiedItemAttr("maxRangeBonus"))