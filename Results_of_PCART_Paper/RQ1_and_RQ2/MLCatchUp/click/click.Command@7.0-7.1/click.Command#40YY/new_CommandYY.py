import click
command = click.Command('my_command', None, None, [click.Option(['--param'], default=42)], help=None, epilog=None, short_help=None, options_metavar='[OPTIONS]', no_args_is_help=False)
