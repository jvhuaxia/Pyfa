# Not used by any item
type = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("rechargeRate", module.getModifiedItemAttr("subsystemBonusAmarrCore"),
                           skill="Amarr Core Systems")
