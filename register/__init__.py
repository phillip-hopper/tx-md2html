from __future__ import print_function, unicode_literals
import requests


def register():
    # post_url = 'https://api.door43.org/tx/module'
    post_url = 'https://n51h54n74j.execute-api.us-west-2.amazonaws.com/tx/module'
    post_data = {'name': 'md2html',
                 'version': '1',
                 'type': 'conversion',
                 'resource_types': ['obs'],
                 'input_format': ['md'],
                 'output_format': ['html'],
                 'options': ['language', 'css'],
                 'private_links': [],
                 'public_links': []}

    response = requests.post(post_url, json=post_data)

    if response.ok:
        print('Registered successfully.')


if __name__ == '__main__':
    register()
