# simple test of click from: https://click.palletsprojects.com/en/8.0.x/

import click

@click.command()
@click.option('--count', default=10, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()