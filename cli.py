"""
Command-line interface for the application
"""

import click
from rich.console import Console
from rich.table import Table
from utils import add_numbers, multiply_numbers
from config import VERSION

console = Console()

@click.group()
def cli():
    """Team Project CLI"""
    pass

@cli.command()
@click.argument('name')
def greet(name):
    """Greet a person"""
    from utils import greet as greet_func
    click.echo(greet_func(name))

@cli.command()
@click.option('--numbers', '-n', multiple=True, type=int, help='Numbers to add')
def add(numbers):
    """Add numbers"""
    if numbers:
        result = sum(numbers)
        click.echo(f"Sum: {result}")
    else:
        click.echo("No numbers provided")

@cli.command()
def info():
    """Show application info"""
    table = Table(title="Application Info")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="magenta")
    table.add_row("Version", VERSION)
    table.add_row("Python", "3.x")
    console.print(table)

if __name__ == "__main__":
    cli()
