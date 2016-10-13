import click
import requests

from .items import *


@click.command()
@click.option('--postcode', default='3000')
@click.option('--model', default='7+', type=click.Choice(['7', '7+']))
@click.option('--finish', default='Black', type=click.Choice(['JetBlack', 'Black', 'Silver', 'Gold', 'RoseGold']))
@click.option('--storage', default='32', type=click.Choice(['32', '128', '256']))
def main(postcode, model, finish, storage):
    """grannysmith checks stock levels for the specified Apple iPhones
    around a particular Australian postcode."""

    click.echo(click.style('Searching for ', fg='yellow'), nl=False)
    click.echo(click.style('iPhone %s' % model, fg='red'), nl=False)
    click.echo(click.style(' %s' % finish, fg='green'), nl=False)
    click.echo(click.style(' %sGB' % storage, fg='blue'), nl=False)
    click.echo(click.style(
        ' in Apple stores around postcode', fg='yellow'), nl=False)
    click.echo(click.style(' %s' % postcode, fg='cyan'), nl=True)

    products = [item['id']
                for item in items
                if item['model'] == model
                and item['finish'] == finish
                and item['storage'] == storage
                ]
    products_req = "&".join("parts.%s=%s" % (index, item)
                            for index, item in enumerate(products))

    request_url = 'http://www.apple.com/au/shop/retail/pickup-message?location=%s&%s' % (
        postcode, products_req)

    data = requests.get(request_url)
    data = data.json()

    for store in data['body']['stores']:
        for product in products:
            status = store['partsAvailability'][product]['pickupDisplay']
            if status == 'available':
                click.echo(click.style('Available', fg='green'), nl=False)
                click.echo(click.style(' in ', fg='yellow'), nl=False)
                click.echo(click.style(store['storeName'], fg='green'), nl=True)
            else:
                click.echo(click.style('Unavailable', fg='red'), nl=False)
                click.echo(' in %s' % store['storeName'])
