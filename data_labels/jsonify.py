import json

label_path= "image_descriptions.txt"

with open(label_path, "r") as label_file:
    lines= label_file.read().split("\n\n")

images= []
titles= []
for instance in lines:
        desc= []
        for line in instance.split("\n")[1:]:
            desc.append(line.split(":")[1].strip())
        title= desc[0]
        descriptions= desc[1:]

        image={
            "image_name" : title,
            "descriptions" : descriptions
        }
        images.append(image)
        titles.append(title)
        #print(image)

js= json.dumps(images, indent=2)

with open("image_descriptions.json", "w") as fp:
    fp.writelines(js)

js= {
    "train" : titles,
    "val" : [],
    "test": []
}
js= json.dumps(js, indent=2)
with open("image_splits.json", "w") as fp:
    fp.writelines(js)

#input("End")