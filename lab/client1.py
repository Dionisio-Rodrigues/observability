import aiohttp
import asyncio
from aiohttp import BasicAuth
import time

async def make_request():
    logins = [('admin@admin.com', 'admin'), ('admin@admin.com', 'admin'), ('admin@admin.com', 'admin'), ('admin@admin.com', 'admin'), ('admin@admin.com', 'admin'), ('admin2@admin.com', 'admin2'),
              ('admin3@admin.com', 'admin3'), ('admin4@admin.com', 'admin4'), ('admin5@admin.com', 'admin5')]

    async with aiohttp.ClientSession() as session:

        while True:
            async_req = []
            for email, password in logins:
                auth = BasicAuth(email, password)
                async_req.append(asyncio.create_task(session.get(
                    'http://localhost:8000/api/companies/', auth=auth)))
                async_req.append(asyncio.create_task(session.post('http://localhost:8000/api/companies/', json={
                    "corporate_name": "string",
                    "fantasy_name": "string",
                    "cnpj": "string",
                    "public_place": "string",
                    "number": "string",
                    "neighbourhood": "string",
                    "city": "string",
                    "cep": "string"
                }, auth=auth)))

            print('requisições enviadas')

            await asyncio.gather(*async_req)


            

asyncio.run(make_request())