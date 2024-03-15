import streamlit as st
import yaml
import os
import json
# Get chromosome name
list_chr = ["chr21 small", "chr22", "chrX"]
chr_name = st.selectbox('Select chromosome', list_chr)

# Get logging level
logging_name = ['Info', 'Warnings', 'Errors']
log_level = st.selectbox('Select log level', logging_name)

# Dynamically generate paths based on chr_name
bam_path = f"../data/demo/inputs/{chr_name.replace(' ', '.')}.bam"
fai_path = f"../data/demo/inputs/{chr_name.replace(' ', '.')}.fa.fai"
first_name = chr_name.split()[0]
# Create dictionary with selected values
data = {
    "bam": bam_path,
    "fai": fai_path,
    "chr_names": [f"{chr_name.split(".")[0]}"],
    "log_level": log_level
}

# Save to YAML file
output_file = os.path.join('../data/demo', 'config.yaml')
if os.path.exists(output_file):
    os.remove(output_file)
    print('File removed!')

with open(output_file, 'w') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=None, sort_keys=False)
    print("Saved to YAML file")

st.success(f"Selected values saved to {output_file}")
