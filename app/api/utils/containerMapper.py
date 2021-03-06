

def getContainerDetails(container):
    ip = 'N/A'
    if container.state().network != None and container.state().network.get('eth0') != None:
        if len(container.state().network.get('eth0')['addresses']) > 0:
            ip = container.state().network['eth0']['addresses'][0].get('address', 'N/A')

    image = 'N/A'
    if container.config.get('image.os') != None and container.config.get('image.release') != None and container.config.get('image.architecture') != None:
        image = ''.join(container.config.get('image.os') + ' ' + container.config.get('image.release') + ' ' + container.config.get('image.architecture'))

    return {
        'name': container.name,
        'status': container.status,
        'ip': ip,
        'ephemeral': container.ephemeral,
        'image': image,
        'created_at': container.created_at
    }