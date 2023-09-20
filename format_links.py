import csv

with open('raw_links.txt') as file:
    csv_reader = csv.reader(file)
    print('[list]')
    for link in csv_reader:
        l = link[0]

        # the BBcode link needs the wranglertjforum domain prefix
        addr = l.replace('https://', '')

        # hygiene the human readable link
        s = l.replace('https://wranglertjforum.com/threads/', '')
        s = s.replace('-', ' ')
        s = s[:s.rfind('.')]

        print(f'[*][url="{addr}"]{s}[/url]')

    print('[/list]')
