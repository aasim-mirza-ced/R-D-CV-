import struct

def read_buffer_view(data, offset, length):
    return data[offset:offset + length]

def interpret_accessor_data(data, component_type, count, type):
    if component_type == 5126:  # FLOAT
        format_char = 'f'
    elif component_type == 5123:  # UNSIGNED_SHORT
        format_char = 'H'
    else:
        raise ValueError(f"Unsupported component type: {component_type}")

    component_size = struct.calcsize(format_char)

    if type == "VEC2":
        num_components = 2
    elif type == "VEC3":
        num_components = 3
    elif type == "SCALAR":
        num_components = 1
    else:
        raise ValueError(f"Unsupported type: {type}")

    accessor_data = []
    for i in range(count):
        start = i * component_size * num_components
        end = start + component_size * num_components
        component_values = struct.unpack(f'<{num_components}{format_char}', data[start:end])
        accessor_data.append(component_values)

    return accessor_data

def main():
    bin_file_path = "D:/KMP_gltf/trialth/trialtheme.bin"

    with open(bin_file_path, "rb") as f:
        buffer_data = f.read()

    # Example of reading buffer views (replace these offsets and lengths with actual values)
    buffer_views = [
        {"byteOffset": 0, "byteLength": 288},
        {"byteOffset": 288, "byteLength": 288},
        {"byteOffset": 576, "byteLength": 192},
        {"byteOffset": 768, "byteLength": 192},
        {"byteOffset": 960, "byteLength": 72}
    ]

    for i, buffer_view in enumerate(buffer_views):
        offset = buffer_view["byteOffset"]
        length = buffer_view["byteLength"]
        buffer_view_data = read_buffer_view(buffer_data, offset, length)
        print(f"BufferView {i}: Offset {offset}, Length {length}")
        print(buffer_view_data)

    # Example of interpreting accessor data (replace these with actual values)
    accessors = [
        {"type": "VEC3", "componentType": 5126, "count": 24},
        {"type": "VEC3", "componentType": 5126, "count": 24},
        {"type": "VEC2", "componentType": 5126, "count": 24},
        {"type": "VEC2", "componentType": 5126, "count": 24},
        {"type": "SCALAR", "componentType": 5123, "count": 36}
    ]

    for i, accessor in enumerate(accessors):
        accessor_type = accessor["type"]
        component_type = accessor["componentType"]
        count = accessor["count"]
        offset = buffer_views[i]["byteOffset"]
        length = buffer_views[i]["byteLength"]
        
        accessor_data = read_buffer_view(buffer_data, offset, length)
        interpreted_data = interpret_accessor_data(accessor_data, component_type, count, accessor_type)
        
        print(f"Accessor {i}: Type {accessor_type}, Component Type {component_type}, Count {count}")
        for item in interpreted_data:
            print(item)

if __name__ == "__main__":
    main()
