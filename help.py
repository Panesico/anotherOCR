import csv
import os

for split in ['train', 'eval']:
    csv_path = os.path.join(split, 'labels.csv')
    out_txt_path = f'{split}.txt'
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile, \
         open(out_txt_path, 'w', encoding='utf-8') as txtfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Construct relative image path and get label.
            img_path = os.path.join(split, row['filename'])
            label = row['words']
            txtfile.write(f"{img_path}\t{label}\n")
