def config():
    host = 'host.docker.internal:5000'
    basePath = f'http://{host}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Host': host,
    }


    return {
        'basePath': basePath,
        'headers': headers,
    }
