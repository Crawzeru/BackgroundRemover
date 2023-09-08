from rembg import remove

extension=".png"
image_path=str(input("Write where your image is:(example:C:/Downloads/image.jpg:"))
output_path_name=str(input("Choose a name for your final image:"))
final_name=output_path_name+extension


with open(image_path,'rb') as i:
    with open(final_name,'wb') as o:
        image_file=i.read()
        output_file=remove(image_file)
        o.write(output_file)
        print("Done!")