import hydra
from hydra.core.config_store import ConfigStore
from omegaconf import OmegaConf

from nlp_tasks import Config
from fairseq.dataclass.initialize import hydra_init

import my_app


hydra_init()

@hydra.main(config_path="conf", config_name="nlp_tasks/config")
def my_app(cfg: Config) -> None:
    cs = ConfigStore.instance()
    print(cs.repo)
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
