import json

label_path= "./out/art_painting_labels3.txt"

with open(label_path, "r") as label_file:
    lines= label_file.read().split("\n\n")[1:]

images= []
for instance in lines:
        desc= []
        for line in instance.split("\n")[1:]:
            desc.append(line.split(":")[1])
        title= desc[0]
        descriptions= desc[1:]

        image={
            "image_name" : title,
            "descriptions" : descriptions
        }
        images.append(image)
        #print(image)

js= json.dumps(images, indent=2)
print(js)

with open("json_out.json", "w") as fp:
    fp.writelines(js)

#input("End")