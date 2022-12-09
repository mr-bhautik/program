#installation for linux 
nasm -felf64 code_filename -o output_filename.o
ld output_filename.o -o final_binury_filename
