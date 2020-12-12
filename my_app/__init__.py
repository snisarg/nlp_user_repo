from dataclasses import dataclass

from hydra.core.config_store import ConfigStore

from my_app.optim.adam import AdamConf

cs = ConfigStore.instance()
cs.store(group="task/optim", name="adam", node=AdamConf)
