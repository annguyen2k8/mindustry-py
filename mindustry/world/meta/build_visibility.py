from __future__ import annotations

from mindustry.vars import Vars


from mindustry.content import *
#!                            ^^^^^^

class BuildVisibility:
    hidden:BuildVisibility
    shown:BuildVisibility
    debugOnly:BuildVisibility
    editorOnly:BuildVisibility
    coreZoneOnly:BuildVisibility
    worldProcessorOnly:BuildVisibility
    sandboxOnly:BuildVisibility
    campaignOnly:BuildVisibility
    lightingOnly:BuildVisibility
    ammoOnly:BuildVisibility
    fogOnly:BuildVisibility
    
    
    def __init__(self, visible):
        self.visible = visible

    def is_visible(self):
        return self.visible()

BuildVisibility.hidden = BuildVisibility(lambda: False)
BuildVisibility.shown = BuildVisibility(lambda: True)
BuildVisibility.debugOnly = BuildVisibility(lambda: False)
BuildVisibility.editorOnly = BuildVisibility(lambda: Vars.state.rules.editor)
BuildVisibility.coreZoneOnly = BuildVisibility(lambda: Vars.indexer.isBlockPresent(Blocks.coreZone))
BuildVisibility.worldProcessorOnly = BuildVisibility(lambda: Vars.state.rules.editor or Vars.state.rules.allowEditWorldProcessors)
BuildVisibility.sandboxOnly = BuildVisibility(lambda: Vars.state is None or Vars.state.rules.infiniteResources)
BuildVisibility.campaignOnly = BuildVisibility(lambda: Vars.state is None or Vars.state.isCampaign())
BuildVisibility.lightingOnly = BuildVisibility(lambda: Vars.state is None or Vars.state.rules.lighting or Vars.state.isCampaign())
BuildVisibility.ammoOnly = BuildVisibility(lambda: Vars.state is None or Vars.state.rules.unitAmmo)
BuildVisibility.fogOnly = BuildVisibility(lambda: Vars.state is None or Vars.state.rules.fog or Vars.state.rules.editor)