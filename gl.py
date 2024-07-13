import numpy as np
from pygltflib import GLTF2
import cv2

def load_gltf(gltf_file_path):
    gltf = GLTF2().load(gltf_file_path)
    return gltf

def read_bin_file(bin_file_path):
    with open(bin_file_path, 'rb') as f:
        bin_data = f.read()
    return bin_data

def interpret_buffer_views(gltf, bin_data):
    for buffer_view in gltf.bufferViews:
        buffer = gltf.buffers[buffer_view.buffer]
        byte_offset = buffer_view.byteOffset
        byte_length = buffer_view.byteLength

        data_segment = bin_data[byte_offset:byte_offset + byte_length]
        print(f"BufferView {buffer_view.buffer}: Offset {byte_offset}, Length {byte_length}")
        print(data_segment[:100])  # Print first 100 bytes for inspection

def interpret_accessors(gltf, bin_data):
    for accessor in gltf.accessors:
        buffer_view = gltf.bufferViews[accessor.bufferView]
        byte_offset = accessor.byteOffset
        component_type = accessor.componentType
        count = accessor.count
        type_str = accessor.type

        data_segment = bin_data[buffer_view.byteOffset + byte_offset:buffer_view.byteOffset + byte_offset + accessor.count * 4]

        print(f"Accessor: Type {type_str}, Component Type {component_type}, Count {count}")
        print(data_segment[:100])  # Print first 100 bytes for inspection

def main():
    gltf_file_path = "D:/python script/wall_wallpaper_cube1 .gltf"
    gltf = load_gltf(gltf_file_path)
    
    # Assuming the .bin file is in the same directory and named accordingly
    bin_file_path = "D:/python script/wall_wallpaper_cube1 .bin"
    bin_data = read_bin_file(bin_file_path)
    
    interpret_buffer_views(gltf, bin_data)
    interpret_accessors(gltf, bin_data)

if __name__ == "__main__":
    main()
