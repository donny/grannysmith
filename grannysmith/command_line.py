import grannysmith
import click

@click.command()
def main():
    click.echo(grannysmith.joke())
