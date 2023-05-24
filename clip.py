import click
import pyperclip


@click.group()
def cli():
    """Clipboard Manager"""
    pass

@cli.command()
def show():
    """Show clipboard content"""
    click.echo("Clipboard content:")
    click.echo(pyperclip.paste())

@cli.command()
def clear():
    """Clear clipboard"""
    pyperclip.copy('')
    click.echo("Clipboard cleared.")

@cli.command()
@click.option('--preview', is_flag=True, help='Preview clipboard content')
def append(preview):
    """Append current selection to clipboard"""
    click.echo("Enter the selection:")
    selection = click.prompt('', prompt_suffix='')

    if preview:
        click.echo("Clipboard content preview:")
        current_content = pyperclip.paste()
        click.echo(current_content + selection)

    pyperclip.copy(current_content + selection)
    click.echo("Selection appended to clipboard.")

if __name__ == '__main__':
    cli()
