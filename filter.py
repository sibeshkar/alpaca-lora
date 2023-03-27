import json

# define the input and output file paths
input_file = "./alpaca_data_cleaned.json"

# define the number of entries to output
N = 10000

output_file = f"file-{N}.json"

# read the input file
with open(input_file, "r") as f:
    data = json.load(f)


# take the top N entries
top_N = data[:N]

# write the top N entries to the output file
with open(output_file, "w") as f:
    json.dump(top_N, f)
