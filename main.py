import os
import click
import yaml
import sys


def load_config(config_name):
    config_filepath = './assets/' + config_name + '.yaml'
    if os.path.exists(config_filepath):
        print(f'cli: Configuration from {config_filepath}')
    else:
        sys.exit(f'cli: ERROR! Configuration file '
                 f'{config_filepath} is missing!!')

    with open(config_filepath, 'r') as f:
        cfg = yaml.safe_load(f)
    return cfg


def update_config(cfg, key1: str, key2: str, val):
    cfg[key1][key2] = val
    return cfg


def print_config(cfg):
    os.system("")
    print('\033[36m' + yaml.dump(cfg, indent=4, width=120, sort_keys=False) +
          '\033[0m')
    return


@click.group()
def cli():
    """
    pretrain
    """


@cli.command()
@click.option('--device', '-d', required=False, default='GPU',
              help="device specification (options: GPU, TPU). "
                   "Default is GPU")
@click.option('--config_name', '-c', required=False, default='config')
def pretrain(config_name, device):
    """ execute pretraining process

    ex) python main.py pretrain gpu
    """
    from pretrain import Pretrainer

    config = load_config(config_name)
    print_config(config)
    trainer = Pretrainer(config=config)
    trainer.pretrain()


if __name__ == '__main__':
    cli()
    pass
