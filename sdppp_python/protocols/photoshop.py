import time
async def protocol_call(backend_instance, protocol_name, data):
    start = time.time()
    result = await backend_instance.sdppp.sio.call(protocol_name, data=data, to=backend_instance.sid)
    if not result:
        return None, None
    if 'error' in result:
        raise Exception('sdppp PS side error:' + result['error'])

    return result

class ProtocolPhotoshop:
    sdpppServer = None

    @classmethod
    def set_sdppp_server(cls, sdpppServer):
        cls.sdpppServer = sdpppServer

    @classmethod
    async def get_image(cls, instance_id, document_identify, layer_identify, boundary):
        backend_instance = cls.sdpppServer.backend_instances[instance_id]
        result = await protocol_call(backend_instance, 's_get_image', data={
            'document_identify': document_identify, 
            'layer_identify': layer_identify, 
            'boundary': boundary
        })
        return result
    
    @classmethod
    async def send_images(cls, instance_id, document_identify, layer_identifies, boundaries, image_urls=[], image_blobs=[]):
        backend_instance = cls.sdpppServer.backend_instances[instance_id]
        result = await protocol_call(backend_instance, 's_send_images', data={
            'document_identify': document_identify, 
            'layer_identifies': layer_identifies,
            'boundaries': boundaries,
            'image_urls': image_urls,
            'image_blobs': image_blobs
        })
        return result
    
    @classmethod
    async def get_text(cls, instance_id, document_identify, layer_identify):
        backend_instance = cls.sdpppServer.backend_instances[instance_id]
        result = await protocol_call(backend_instance, 's_get_text', data={
            'document_identify': document_identify, 
            'layer_identify': layer_identify
        })
        return result['text']

    @classmethod
    async def get_selection(cls, instance_id, document_identify, boundary):
        backend_instance = cls.sdpppServer.backend_instances[instance_id]
        result = await protocol_call(backend_instance, 's_get_selection', data={
            'document_identify': document_identify, 
            'boundary': boundary
        })
        return result

    @classmethod    
    async def get_document_info(cls, instance_id, document_identify):
        backend_instance = cls.sdpppServer.backend_instances[instance_id]
        result = await protocol_call(backend_instance, 's_get_document_info', data={
            'document_identify': document_identify
        })
        return result

    @classmethod
    async def get_layer_info(cls, instance_id, document_identify, layer_identify="", layer_name=""):
        backend_instance = cls.sdpppServer.backend_instances[instance_id]
        result = await protocol_call(backend_instance, 's_get_layer_info', data={
            'document_identify': document_identify, 
            'layer_identify': layer_identify,
            'layer_name': layer_name
        })
        return result

    @classmethod
    async def get_layers_in_group(cls, instance_id, document_identify, layer_identifies, select):
        backend_instance = cls.sdpppServer.backend_instances[instance_id]
        result = await protocol_call(backend_instance, 's_get_layers_in_group', data={
            'document_identify': document_identify, 
            'select': select,
            'layer_identifies': layer_identifies
        })
        return result

    @classmethod
    async def get_linked_layers(cls, instance_id, document_identify, layer_identifies, select):
        backend_instance = cls.sdpppServer.backend_instances[instance_id]
        result = await protocol_call(backend_instance, 's_get_linked_layers', data={
            'document_identify': document_identify, 
            'select': select,
            'layer_identifies': layer_identifies
        })
        return result
    