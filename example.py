from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
import requests
import rich
import argparse
import sys
import json
import re

baseUrl = 'https://connect.sensium.nz'
baseUrl = 'https://staging.sensiumlabs.com'

def login(token):
	r = requests.post(baseUrl + '/login', json={'token': token})
	if r.status_code == requests.codes.ok:
		return r.json()
	return dict(error=f'HTTP Error {r.status_code}')

def logout(sid):
	r = requests.post(baseUrl + '/logout', headers={'Authorization': 'Bearer ' + sid})
	r.raise_for_status()

def get_client(sid):
	transport = RequestsHTTPTransport(
		url=baseUrl + '/graphql',
		verify=True,
		headers={'Authorization': 'Bearer ' + sid},
	)
	return Client(transport=transport)#, fetch_schema_from_transport=True)


if __name__ == '__main__':
	parser = argparse.ArgumentParser('Sensium Connect API Example')
	parser.add_argument('token', help='Sensium Connect Personal Access Token')
	args = parser.parse_args()

	# Login
	rich.print('Logging in...', end=' ')
	reply = login(args.token)
	if 'error' in reply:
		rich.print(f'[red]FAILED ({reply["error"]})[/red]')
		sys.exit(1)
	sid = reply['sid']
	rich.print(f'[green]Session {sid}[/green]')

	# Run Query
	client = get_client(sid)
	query = '''
	{
		me {
			id
			name
		}
	}
	'''
	rich.print('Executing query', re.sub('\s+', ' ', query))
	result = client.execute(gql(query))
	rich.print('Result')
	rich.print(json.dumps(result, indent=3))

	# Logout
	rich.print('Logging out...', end=' ')
	logout(sid)
	rich.print('[green]OK[/green]')

