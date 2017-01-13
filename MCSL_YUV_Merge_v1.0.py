
"""
Created by JanWoo Son (superharoldson@gmail.com)
Multimedia Communications and Systems Lab(MCSL)
http://mcsl.gachon.ac.kr
Department of Computer Engineering
Gachon University
"""



import sys


def print_usage():
    print("Usage : \nMCSL_YUV_Cropper [input_file1] [input_file2] [input_file3] [input_file4] [input_resolution] [output_file]")
    print("resolution : WIDTHxHEIGHT")
    print("ex) MCSL_YUV_Merge input1.yuv input2.yuv input3.yuv input4.yuv 1920x1080 output.yuv")
    print("result= output.yuv (3840x2160) \n")
    sys.exit(0)




def input_parameters_check(input_file_path1, input_file_path2, input_file_path3, input_file_path4, input_frame_size, output_file_path):
    try:
        input_file1 = open(input_file_path1, 'rb')
        input_file2 = open(input_file_path2, 'rb')
        input_file3 = open(input_file_path3, 'rb')
        input_file4 = open(input_file_path4, 'rb')
        output_file = open(output_file_path, 'wb')
    except IOError:
        print("file open error!")
        print_usage()

    if input_frame_size.find('x') is -1:
        print_usage()
    else:
        temp = input_frame_size.split('x')
        input_width = int(temp[0])
        input_height = int(temp[1])
        output_width = input_width * 2
        output_height = input_height * 2

    return input_file1, input_file2, input_file3, input_file4, input_width, input_height, output_file



def merge_4_2_0_yuv_data(input_file1, input_file2, input_file3, input_file4, input_width, input_height, output_file):
    while True:
        input_file1_frame = input_file1.read(int(input_width * input_height * 1.5))
        input_file2_frame = input_file2.read(int(input_width * input_height * 1.5))
        input_file3_frame = input_file3.read(int(input_width * input_height * 1.5))
        input_file4_frame = input_file4.read(int(input_width * input_height * 1.5))
        output_frame = ""
        output_width = input_width * 2
        output_height = input_height * 2
        ptr_half_top = 0
        ptr_half_bottom = 0
        if input_file1_frame == '':
            break
        for y in range(input_height):
            output_frame += input_file1_frame[ptr_half_top:ptr_half_top + input_width]
            output_frame += input_file2_frame[ptr_half_top:ptr_half_top + input_width]
            ptr_half_top += input_width
        for y in range(input_height):
            output_frame += input_file3_frame[ptr_half_bottom:ptr_half_bottom + input_width]
            output_frame += input_file4_frame[ptr_half_bottom:ptr_half_bottom + input_width]
            ptr_half_bottom += input_width
        for u in range(input_height / 2):
            output_frame += input_file1_frame[ptr_half_top:ptr_half_top + (input_width / 2)]
            output_frame += input_file2_frame[ptr_half_top:ptr_half_top + (input_width / 2)]
            ptr_half_top += input_width / 2
        for u in range(output_height / 2):
            output_frame += input_file3_frame[ptr_half_bottom:ptr_half_bottom + (input_width / 2)]
            output_frame += input_file4_frame[ptr_half_bottom:ptr_half_bottom + (input_width / 2)]
            ptr_half_bottom += input_width / 2
        for v in range(input_height / 2):
            output_frame += input_file1_frame[ptr_half_top:ptr_half_top + (input_width / 2)]
            output_frame += input_file2_frame[ptr_half_top:ptr_half_top + (input_width / 2)]
            ptr_half_top += input_width / 2
        for v in range(output_height / 2):
            output_frame += input_file3_frame[ptr_half_bottom:ptr_half_bottom + (input_width / 2)]
            output_frame += input_file4_frame[ptr_half_bottom:ptr_half_bottom + (input_width / 2)]
            ptr_half_bottom += input_width / 2
        output_file.write(output_frame)

    input_file1.close()
    input_file2.close()
    input_file3.close()
    input_file4.close()
    output_file.close()



def main():
    if len(sys.argv) is not 7:
        print_usage()

    input_file1, input_file2, input_file3, input_file4, input_width, input_height, output_file = input_parameters_check(
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    merge_4_2_0_yuv_data(input_file1, input_file2, input_file3, input_file4, input_width, input_height, output_file)


if __name__ == "__main__":
    main()

