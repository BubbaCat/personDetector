import hydra
from omegaconf import DictConfig


@hydra.main(config_path='./config', config_name='config_visualize', version_base='1.3.2')
def main(config: DictConfig) -> None:
    analytics = hydra.utils.instantiate(config['base']['example'])
    analytics.run()


if __name__ == '__main__':
    main()
