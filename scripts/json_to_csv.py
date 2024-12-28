import json
import csv

source_file = "../data/Streaming_History_Audio_2020_0.json"
dest_file = "../data/output/2020_0.csv"

"""with open(source_file) as json_file:
	jsondata = json.loads(json_file)

data_file = open(dest_file, 'w', newline='')
csv_writer = csv.writer(data_file)

count = 0
for data in jsondata:
	if count == 0:
		header = data.keys()
		csv_writer.writerow(header)
		count += 1
	csv_writer.writerow(data.values())

data_file.close()"""

with open(source_file, "r", encoding="utf-8", newline="") as input_json_file:
    with open(
    dest_file, "w", encoding="utf-8", newline=""
    ) as output_csv_file:

        json_reader = json.loads(input_json_file)
        csv_writer = csv.writer(output_csv_file)

        num_line = 0

        for data in json_reader:

            if num_line == 0:  # Writing column names
                header = data.keys()
                csv_writer.writerow(header)

                num_line += 1

            csv_writer.writerow(data.values())
            num_line += 1
